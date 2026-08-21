# -*- coding: utf-8 -*-
"""
김충락 회귀분석 PDF를 챕터별로 분할하고 OCR 레이어를 추가하는 스크립트.

사용법 (Anaconda Prompt 또는 PowerShell에서):
    pip install pypdf ocrmypdf
    # ocrmypdf는 tesseract-ocr 시스템 설치도 필요. Windows: https://github.com/UB-Mannheim/tesseract/wiki
    # 한국어 학습데이터(kor.traineddata)를 tesseract tessdata 폴더에 추가해야 함.

    python split_by_chapter.py --split-only           # 1단계: 분할만
    python split_by_chapter.py --ocr                  # 2단계: OCR 레이어 추가
    python split_by_chapter.py                        # 둘 다 (분할 + OCR)
"""

from __future__ import annotations
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

# ====== 경로 설정 ======
# 2026-08-21 수정(무결성 검토 F-07): 원본 PDF 위치가 세 곳에서 서로 달라
#   (스크립트 ROOT / 주석의 ...\ADP\ / mapping json 의 _source_pdf)
#   지금 실행하면 "원본 PDF 없음"으로 멈췄다. → 후보 경로를 순서대로 탐색하고
#   --source 로 직접 지정할 수 있게 바꿨다.
SCRIPT_DIR = Path(__file__).resolve().parent   # <볼트>/튜터워크스페이스/regression_김충락/
VAULT_ROOT = SCRIPT_DIR.parent.parent          # <볼트>/  (예: ...\문서\회귀분석\)
MAPPING_JSON = SCRIPT_DIR / "chapter_page_mapping.json"
OUT_DIR = SCRIPT_DIR / "회귀분석_chapters"
RAW_DIR = OUT_DIR / "_raw_split"  # OCR 전 임시 분할본

PDF_NAMES = ["회귀분석_김충락.pdf", "Regression Analysis_note (I).pdf"]


def find_source_pdf(explicit: str | None, mapping: dict) -> Path | None:
    """--source > 스크립트 폴더 > 볼트 루트 > mapping의 _source_pdf 순으로 탐색."""
    if explicit:
        p = Path(explicit).expanduser()
        return p if p.exists() else None
    candidates = [d / n for d in (SCRIPT_DIR, VAULT_ROOT) for n in PDF_NAMES]
    hinted = mapping.get("_source_pdf")
    if hinted:
        candidates.append(Path(hinted))
    for c in candidates:
        if c.exists():
            return c
    return None


# ====== 챕터별 분할 ======
def split_pdf(source: Path, mapping: dict, raw_dir: Path) -> list[Path]:
    """원본 PDF를 챕터별로 분할 (이미지 그대로 보존)."""
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError:
        print("[ERROR] pypdf가 설치되어 있지 않습니다. `pip install pypdf` 실행 필요.")
        sys.exit(1)

    raw_dir.mkdir(parents=True, exist_ok=True)
    print(f"원본 PDF 로딩: {source}")
    reader = PdfReader(str(source))
    total = len(reader.pages)
    print(f"총 페이지: {total}")

    if total != mapping["_total_pdf_pages"]:
        print(f"[WARN] 매핑 기대값 {mapping['_total_pdf_pages']} != 실제 {total}. 매핑 확인 필요.")

    outputs = []
    for ch in mapping["chapters"]:
        out = raw_dir / f"{ch['id']}_{ch['title'].replace(' ', '_')}.pdf"
        writer = PdfWriter()
        for p in range(ch["pdf_start"] - 1, ch["pdf_end"]):  # 1-indexed → 0-indexed
            writer.add_page(reader.pages[p])
        with open(out, "wb") as f:
            writer.write(f)
        size_mb = out.stat().st_size / (1024 * 1024)
        print(f"  {ch['id']}: {ch['n_pages']}p, {size_mb:.1f} MB -> {out.name}")
        outputs.append(out)
    return outputs


# ====== OCR 레이어 추가 ======
def ocr_chapter(raw_pdf: Path, out_pdf: Path, lang: str = "kor+eng") -> bool:
    """ocrmypdf로 검색 가능한 PDF 생성."""
    if shutil.which("ocrmypdf") is None:
        print("[ERROR] ocrmypdf가 PATH에 없습니다. `pip install ocrmypdf` 후 tesseract도 설치 필요.")
        return False

    cmd = [
        "ocrmypdf",
        "-l", lang,
        "--skip-text",                # 이미 텍스트 있는 페이지는 그대로
        "--optimize", "1",            # 약간의 압축
        "--jobs", "2",
        str(raw_pdf), str(out_pdf),
    ]
    print(f"  OCR: {raw_pdf.name} -> {out_pdf.name}")
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [FAIL] {raw_pdf.name}: returncode={e.returncode}")
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--split-only", action="store_true", help="분할만 수행 (OCR 생략)")
    ap.add_argument("--ocr", action="store_true", help="OCR만 수행 (이미 분할된 _raw_split 사용)")
    ap.add_argument("--lang", default="kor+eng", help="OCR 언어 (기본: kor+eng)")
    ap.add_argument("--source", default=None, help="원본 PDF 경로 (미지정 시 자동 탐색)")
    args = ap.parse_args()

    if not MAPPING_JSON.exists():
        print(f"[ERROR] 매핑 파일 없음: {MAPPING_JSON}")
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    mapping = json.loads(MAPPING_JSON.read_text(encoding="utf-8"))

    source_pdf = find_source_pdf(args.source, mapping)
    if source_pdf is None and not args.ocr:
        print("[ERROR] 원본 PDF를 찾지 못했습니다. 탐색한 곳:")
        for d in (SCRIPT_DIR, VAULT_ROOT):
            for n in PDF_NAMES:
                print(f"   - {d / n}")
        if mapping.get("_source_pdf"):
            print(f"   - {mapping['_source_pdf']}  (mapping의 _source_pdf)")
        print("   → --source <경로> 로 직접 지정할 수 있습니다.")
        sys.exit(1)

    # 1단계: 분할
    if not args.ocr:
        print("\n=== 1단계: 챕터별 분할 ===")
        split_pdf(source_pdf, mapping, RAW_DIR)

    if args.split_only:
        print("\n분할만 완료. --ocr 옵션으로 OCR 레이어를 추가할 수 있습니다.")
        return

    # 2단계: OCR
    print("\n=== 2단계: OCR 레이어 추가 ===")
    raw_files = sorted(RAW_DIR.glob("*.pdf"))
    if not raw_files:
        print(f"[ERROR] 분할된 파일이 없습니다: {RAW_DIR}")
        sys.exit(1)

    success = 0
    for raw in raw_files:
        out = OUT_DIR / raw.name
        if ocr_chapter(raw, out, lang=args.lang):
            success += 1

    print(f"\n완료: {success}/{len(raw_files)} 챕터 OCR 성공.")
    print(f"출력 폴더: {OUT_DIR}")


if __name__ == "__main__":
    main()
