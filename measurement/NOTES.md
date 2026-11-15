# 측정 기록 (2026-11-15, 지침 4절의 근거)

지침 작성 세션에서 실제로 한 일을 그대로 적은 기록이다. 여기 없는 세부 정보는 지어내지 않는다.

## 환경

- Python 3.15.0, 임시 가상환경에 `tiktoken`(o200k_base 인코딩)과 `markdown`(python-markdown) 설치
- Claude 토크나이저는 공개되지 않아 o200k_base로 근사했다

## 측정 1: Thariq 예제 HTML 31개

- 출처: GitHub `thariqs/html-effectiveness` 저장소의 HEAD(2026-11-15 받음, 커밋 해시는 기록하지 않음). 받은 HTML 33개 중 `index.html` 2개를 빼고 31개(본 예제 20개 + `unknowns/` 11개)
- 스크립트: `scripts/fetch.py`(받기), `scripts/measure.py`(측정)
- 파서: Python 표준 라이브러리 `html.parser.HTMLParser`를 상속한 자체 휴리스틱 변환기(`measure.py`의 `Split` 클래스). `script`·`style`·`svg` 안의 텍스트를 버리고, `h1~h6`→`#`, `li`→`- `, `td/th`→` | `, `code`→백틱으로 바꿔 "MD 근사치"를 만든다. 실제 MD 작성본이 아니라 근사치다
- 인터랙티브 도구 예제(18·19·20, unknowns 06)는 내용이 JS 데이터 안에 있어 텍스트 추출에 덜 잡혀 배율이 과장된다
- 결과(o200k): 본 예제 20개 HTML/MD근사 중앙값 9.51(최소 4.06, 최대 65.17), unknowns 11개 중앙값 7.31(3.55~62.55). 문서형 예제는 약 4~7배
- 토큰 구성 합계(본 예제 20개): style 44%, script 12%, svg 8%, 보이는 텍스트 11% → 나머지 약 25%는 태그·속성·클래스 등. unknowns 11개: style 47%, script 13%, svg 2%, 텍스트 14% → 나머지 약 24%
  - 위 네 범주는 정규식으로 `<style>`·`<script>`·`<svg>` 블록 전체를 각각 셌으므로, 블록 사이 겹침은 없다고 가정했다
- 지침 파일 자체(당시 버전)를 python-markdown(`tables` 확장)으로 꾸밈 없는 HTML로 변환: MD 4,379 → HTML 5,274토큰, 1.20배

## 측정 2: 하위 에이전트 직접 생성 (MD 3회, HTML 3회)

- 원본: 지침 3절을 그대로 잘라 낸 `generated/source.md`(o200k 814토큰)
- 방식: Claude Code 하위 에이전트(general-purpose, 모델은 상위 세션을 상속한 Opus 5.5) 6개를 백그라운드로 **동시에** 실행
- 프롬프트: 두 조건 모두 영어 지시문 + 원본 전문을 프롬프트에 직접 넣음(파일 읽기 없음). 차이는 과제 문장과 저장 경로뿐
  - MD 조건 과제: "Turn the SOURCE below into a well-structured Markdown document — a reference page a team would read. Keep all content in Korean and keep every point; you may reorganize and add structure (headings, lists, tables) where useful."
  - HTML 조건 과제: "Turn the SOURCE below into a single self-contained HTML file — a well-designed reference page a team would read in a browser (inline CSS, optional inline JS, no external resources). Keep all content in Korean and keep every point; you may reorganize and add structure, visual hierarchy, and interactivity where useful."
  - 공통 규칙: "Use exactly ONE Write call to save the result to: <경로>", "Do not read any files, search, or use any other tool.", "After writing, reply with only the word DONE."
- 토큰과 시간은 하위 에이전트 완료 알림의 `subagent_tokens`, `duration_ms` 값이다. 이 값은 입력(시스템 프롬프트 포함)·출력·사고(thinking)·도구 호출을 나누지 않은 합계다

| 실행 | subagent_tokens | duration_ms | 결과 파일 o200k |
|---|---|---|---|
| md_1 | 69,365 | 23,161 | 1,198 |
| md_2 | 69,300 | 20,949 | 1,223 |
| md_3 | 69,276 | 21,230 | 1,213 |
| html_1 | 77,687 | 82,664 | 5,943 (style 1,845, script 708, 둘을 뺀 나머지 3,390) |
| html_2 | 75,085 | 66,178 | 4,931 (style 1,568, script 776, 나머지 2,587) |
| html_3 | 77,027 | 78,374 | 6,282 (style 2,451, script 669, 나머지 3,162) |

- 평균: MD 69,314토큰·21.8초, HTML 76,600토큰·75.7초 → 차이 약 7,286토큰, 시간 약 3.5배
- 측정 스크립트: `scripts/gen_measure.py`. 생성된 파일: `generated/`
- 알려진 한계: 조건마다 3회, 내용 하나(한국어), 모델 하나, 동시 실행, 입력 원본이 이미 MD라 MD 조건이 변환할 것이 적었을 수 있음(베이스라인 비대칭), 사용량 값에 사고 토큰이 섞였을 수 있음

## 초록까지만 본 논문의 확인된 위치

- Duggan & Payne 2009: https://researchportal.bath.ac.uk/en/publications/text-skimming-the-process-and-effectiveness-of-foraging-through-t/ (PDF는 403으로 받지 못함), DOI 10.1037/a0016995
- DeStefano & LeFevre 2007: DOI 10.1016/j.chb.2005.08.012 (Computers in Human Behavior 23(3))
- Kücking 외 2026: DOI 10.1016/j.ijmedinf.2025.106223 (International Journal of Medical Informatics 207)
- Narvekar 외, Silyn-Roberts 1999, Parasuraman & Riley 1997, Lee & See 2004: 이 세션에서 URL·DOI를 확인하지 않았다
- Bansal 외 2021(arXiv 2006.14779), Buçinca 외 2021(arXiv 2102.09692), Vasconcelos 외 2023(arXiv 2212.06823): 본문이 arXiv에 무료 공개돼 있다. 이 세션에서는 초록만 읽었다(유료라서가 아님)
