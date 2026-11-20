# CLAUDE.md — ADP_statistic

이 파일은 연결용 지시서다. 규칙 본문은 아래 문서에 있으며 여기에 복사하지 않는다.

## 세션 시작 시
1. 학습 세션(과목·챕터·개념 공부)이면 `00_Hub_Orchestrator_Brief.md`를 먼저 읽고 그 워크플로를 따른다.
2. 역할이 정해지면 해당 브리프를 읽는다.
   - 튜터: `튜터워크스페이스/01_tutor_brief_v1.md`
   - 채점관: `채점워크스페이스/02_grader_brief_v1.md`
3. 보조 에이전트(Grok Bot)와의 경계는 `AGENTS.md`를 따른다. 학습 콘텐츠·채점·정리노트 운영은 Claude 담당이다.

## Rprojects 연동
- 함께 연결된 `Rprojects` 저장소(로컬: `../Rprojects`)의 `CLAUDE.md` §6–7(LLM Wiki, AI 역할 분담)을 따른다.
- 교훈 받은편지함은 `Rprojects/_meta/lessons.md` 하나뿐이다. 이 저장소에 `lessons.md`를 만들지 않는다.

## 환경 메모
- 교재 PDF(`튜터워크스페이스/*.pdf`)는 `.gitignore` 대상이라 클라우드 세션에는 없다. 원문 확인·번역이 필요하면 사용자에게 알린다.
