<#
.SYNOPSIS
  Obsidian Markdown 위키의 끊어진 내부 링크와 선택적 메타데이터 누락을 읽기 전용으로 검사한다.

.DESCRIPTION
  .git, .claude, .obsidian과 Codex 검토보고서 폴더는 검사 대상에서 제외한다.
  기본 실행은 콘솔에 결과만 표시하며, -ReportPath를 지정했을 때만 Markdown 보고서를 작성한다.
#>
[CmdletBinding()]
param(
    [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path,
    [switch]$CheckMetadata,
    [string]$ReportPath,
    [ValidateRange(1, 10000)]
    [int]$MaxIssues = 30
)

$ErrorActionPreference = 'Stop'
$excludedSegments = @('\.git\', '\.claude\', '\.obsidian\', '\Codex워크스페이스\검토보고서\')
$markdownFiles = Get-ChildItem -LiteralPath $Root -Filter '*.md' -File -Recurse |
    Where-Object {
        $candidate = $_.FullName
        -not ($excludedSegments | Where-Object { $candidate -like "*$_*" })
    }

$targets = New-Object 'System.Collections.Generic.HashSet[string]' ([System.StringComparer]::OrdinalIgnoreCase)
$documents = @()

function Add-Target {
    param([string]$Name)

    if (-not [string]::IsNullOrWhiteSpace($Name)) {
        [void]$targets.Add($Name.Trim())
    }
}

foreach ($file in $markdownFiles) {
    $relativePath = $file.FullName.Substring($Root.Length).TrimStart('\', '/')
    $relativeWithoutExtension = [System.IO.Path]::ChangeExtension($relativePath, $null).Replace('\', '/')
    $content = Get-Content -LiteralPath $file.FullName -Raw
    if ($null -eq $content) {
        $content = ''
    }

    Add-Target $relativeWithoutExtension
    Add-Target $file.BaseName

    $heading = [regex]::Match($content, '(?m)^#\s+(.+?)\s*$')
    if ($heading.Success) {
        Add-Target $heading.Groups[1].Value
    }

    $inlineAliases = [regex]::Match($content, '(?m)^aliases:\s*\[(.+?)\]\s*$')
    if ($inlineAliases.Success) {
        foreach ($alias in $inlineAliases.Groups[1].Value -split ',') {
            Add-Target ($alias.Trim().Trim('"', "'"))
        }
    }

    $documents += [pscustomobject]@{
        File = $file
        RelativePath = $relativePath.Replace('\', '/')
        Content = $content
    }
}

$brokenLinks = @()
$metadataIssues = @()
foreach ($document in $documents) {
    $matches = [regex]::Matches($document.Content, '\[\[([^\]]+)\]\]')
    foreach ($match in $matches) {
        $target = $match.Groups[1].Value -replace '\|.*$', '' -replace '#.*$', ''
        $target = $target.Trim().Trim('"', "'") -replace '\.md$', ''
        if ([string]::IsNullOrWhiteSpace($target)) {
            continue
        }

        $normalizedTarget = $target.Replace('\', '/')
        if (-not $targets.Contains($normalizedTarget) -and -not $targets.Contains([System.IO.Path]::GetFileName($normalizedTarget))) {
            $line = ($document.Content.Substring(0, $match.Index) -split "`r?`n").Count
            $brokenLinks += [pscustomobject]@{
                File = $document.RelativePath
                Line = $line
                Target = $target
            }
        }
    }

    if ($CheckMetadata -and $document.RelativePath -like '튜터워크스페이스/과목별/*') {
        $frontmatter = [regex]::Match($document.Content, '\A---\s*\r?\n([\s\S]*?)\r?\n---')
        if (-not $frontmatter.Success) {
            $metadataIssues += [pscustomobject]@{ File = $document.RelativePath; Issue = 'frontmatter 없음' }
            continue
        }

        foreach ($field in @('subject', 'chapter', 'moc')) {
            if ($frontmatter.Groups[1].Value -notmatch "(?m)^$field\s*:") {
                $metadataIssues += [pscustomobject]@{ File = $document.RelativePath; Issue = "'$field' 필드 없음" }
            }
        }
    }
}

$summary = @(
    "# 위키 무결성 검사",
    '',
    "- 검사 시각: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')",
    "- 대상 Markdown: $($documents.Count)개",
    "- 끊어진 위키링크: $($brokenLinks.Count)개",
    "- 메타데이터 이슈: $($metadataIssues.Count)개"
)

if ($brokenLinks.Count -gt 0) {
    $summary += '', '## 끊어진 위키링크'
    foreach ($issue in ($brokenLinks | Select-Object -First $MaxIssues)) {
        $summary += "- ``$($issue.File):$($issue.Line)`` → ``[[$($issue.Target)]]``"
    }
    if ($brokenLinks.Count -gt $MaxIssues) {
        $summary += "- … 추가 $($brokenLinks.Count - $MaxIssues)건 (모두 보려면 ``-MaxIssues 10000``으로 실행)"
    }
}

if ($CheckMetadata -and $metadataIssues.Count -gt 0) {
    $summary += '', '## 메타데이터 점검'
    foreach ($issue in ($metadataIssues | Select-Object -First $MaxIssues)) {
        $summary += "- ``$($issue.File)``: $($issue.Issue)"
    }
    if ($metadataIssues.Count -gt $MaxIssues) {
        $summary += "- … 추가 $($metadataIssues.Count - $MaxIssues)건 (모두 보려면 ``-MaxIssues 10000``으로 실행)"
    }
}

if ($brokenLinks.Count -eq 0 -and $metadataIssues.Count -eq 0) {
    $summary += '', '## 결과', '', '발견된 이슈가 없습니다.'
}

$summary -join [Environment]::NewLine | Write-Output

if (-not [string]::IsNullOrWhiteSpace($ReportPath)) {
    $resolvedReportPath = [System.IO.Path]::GetFullPath($ReportPath, $Root)
    $reportDirectory = Split-Path -Path $resolvedReportPath -Parent
    New-Item -ItemType Directory -Path $reportDirectory -Force | Out-Null
    Set-Content -LiteralPath $resolvedReportPath -Value ($summary -join [Environment]::NewLine) -Encoding utf8
    Write-Output "보고서 저장: $resolvedReportPath"
}

if ($brokenLinks.Count -gt 0 -or $metadataIssues.Count -gt 0) {
    exit 1
}
