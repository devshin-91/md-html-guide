# 기여자

누가 무엇을 했는지 나눠 적었다. 진행 순서는 `HISTORY.md`에 있다.

## 사람

| 기여자 | 역할 |
|---|---|
| devshin-91 (Chansu Shin) | 주제 제기(블로그 글 두 편), 조사 범위와 방향 결정, 반영 시점 결정(CLAUDE.md에는 아직 넣지 않기로 함), Liner Scholar 확장 직접 설치, 외부 검토 3차례 진행과 결과 전달, 남은 선택 사항 결정 |

## AI 작성자

| 기여자 | 환경 | 역할 |
|---|---|---|
| Claude (Claude Opus 5.5, effort high) | Claude Code 데스크톱 앱, 세션 1 "yooncarrot 기사 검토" | 블로그 글 검토, 다국어 자료·논문 조사, 지침 초안과 v1 작성, X 원문·arXiv 대조, 토큰·시간 측정 설계와 집계, 측정 기록(`measurement/NOTES.md`) |
| Claude (Claude Opus 5.5, effort high) | Claude Code 데스크톱 앱, 세션 2 "MD/HTML 지침 검토 반영" | 결함 12개 반영(v2), 검토자 값의 원전 대조, 서지 보완, 최종본, 이력·기여자·참고 자료 정리 |
| Claude 하위 에이전트 (general-purpose, 6개) | 세션 1에서 실행 | 측정 2의 MD·HTML 생성(`measurement/generated/`) |
| Claude 하위 에이전트 (web-fetch) | 세션 1·2에서 실행 | 웹 페이지·Crossref·arXiv·Zenodo 조회 |

## 외부 검토자

| 기여자 | 환경 | 역할 |
|---|---|---|
| Claude Opus (High) | 웹 claude.ai, 시크릿 모드 | 1차 검토. 통합 리포트의 "도구 1: Claude Max(집행관 A·B)", 64점. 계량·실험 설계, 에이전트 워크플로, 실현 가능성 |
| Gemini Pro (Argon High) | 웹 Gemini, 시크릿 모드 | 1차 검토. 통합 리포트의 "도구 2: Google AI Pro(집행관 C)", 30점. 문헌 팩트체크, 인용 정합성, 절 사이 논리 충돌 |
| Gemini 4 Argon High | Antigravity | 1차 검토 통합("사령관", 49점, 결함 12개 확정), 수정 지시문 작성, 2차(빈칸 값 제공), 3차(99점, 최종 승인) |

검토자 표기는 사용자가 알려 준 이름 그대로다.

## 도구와 데이터

| 이름 | 쓰인 곳 |
|---|---|
| Liner Scholar (사용자 계정) | 논문 탐색 스레드, 풀 텍스트 요약 12편(5편 본문, 7편 초록) |
| Liner Scholar: Full Papers via Library (Chrome 확장) | 풀 텍스트 모드. 사용자가 직접 설치 |
| Claude Code 내장 브라우저, Claude in Chrome | X 원문·arXiv·Liner 열람 |
| tiktoken (`o200k_base`) | 토큰 근사 측정 |
| python-markdown (`tables` 확장) | MD → 꾸밈 없는 HTML 변환 측정 |
| Python 표준 라이브러리 `html.parser` | HTML → MD 근사 변환기(`measurement/scripts/measure.py`) |
| Crossref API, arXiv API, Zenodo API, GitHub API | 서지·커밋 이력 확인 |
| `thariqs/html-effectiveness` (Thariq Shihipar) | 측정 1의 예제 HTML 31개. 이 저장소에는 포함하지 않았다 |
