# MD / HTML 사용 지침

작성 2026-11-15, 같은 날 외부 검토(12개 결함)를 반영해 보완했다. 이전 판은 `md-html-guidelines.v1.md`.
한국어·영어·일본어·중국어 자료, 원 논쟁(Thariq Shihipar의 X 원문과 반응, HN 토론, Simon Willison, Daniel Miessler, Karpathy), Claude 공식 문서, 논문 40여 편, 직접 측정을 바탕으로 정리했다.
논문마다 확인 수준이 다르다. **본문 확인**(arXiv·공개 저장소 본문), **Liner 풀 텍스트**(Liner Scholar가 보여 준 본문), **초록만**, **검색 요약만**으로 나눠 7절과 출처에 적었다. 측정의 원자료는 `measurement/NOTES.md`에 있다.

## 한 줄 요약

**형식은 "얼마나 자주, 누가 다시 읽는가"로 고른다. 매번 로드되는 파일과 사람이 고치는 원본은 MD, 사람이 한 번 보고 판단하는 화면은 원본에서 만든 HTML, 사람이 값을 고르는 일은 export 버튼이 달린 HTML.**
사람이 빨리 읽게 만드는 건 형식보다 구조(요약 먼저, 섹션마다 요약, 상세는 그 아래)이고, AI가 잘 읽게 만드는 것도 형식 문법보다 구조(제목 경로, 잘리지 않은 표, 구역 구분)다. 검토 화면은 보기 좋게보다 **사람이 판단하게** 만든다.

## 1. 판단 순서

위에서부터 묻고, 답이 정해지면 그 자리에서 끝낸다.

1. **얼마나 자주 다시 읽히는가**: 매 세션·매 작업마다 컨텍스트에 들어가면 **즉시 MD로 확정하고 끝낸다.** 한 번 쓰고 끝나는 산출물이면 2단계로.
2. **누가 고치는가**: 사람이 직접 고치거나 git diff로 검토하면 **원본은 MD로 확정한다.** 사람에게 보여 줄 화면이 따로 필요할 때만 3단계로.
3. **누가 읽고 무엇을 해야 하는가**:
   - 에이전트가 읽으면 MD. 원본 MD가 있으면 원본을 넘긴다. HTML밖에 없으면 2절 "에이전트에게 HTML을 넘길 때"를 따른다.
   - 사람이 읽고 끝이면 MD로 충분하다.
   - 사람이 여러 안을 비교하거나 구조를 한눈에 봐야 하면 원본에서 만든 HTML 뷰.
   - 사람이 값을 고르거나 순서를 정해야 하면 인터랙티브 HTML(3절의 export 루프를 지킨다).
4. **어디로 공유하는가**:
   - GitHub·Notion처럼 표준 MD를 렌더링하는 곳이면 MD.
   - Slack 메시지는 표준 MD가 아니다. 공식 서식 안내에는 굵게·기울임·밑줄·취소선·코드·인용·목록만 있고 제목(`#`)·표·Mermaid는 없다. 요약을 메시지로 쓰고, 긴 문서는 MD가 렌더링되는 곳이나 HTML 뷰의 링크로 붙인다.
   - 개발 도구가 없는 사람에게는 HTML을 링크로 보낸다(접근 제한이 있는 곳에). HTML 파일을 첨부로 보내면 잘 열어 보지 않는다.

## 2. 상황별 지침

| 상황 | 형식 | 이유 |
|---|---|---|
| `CLAUDE.md`, `AGENTS.md`, 스킬, 메모리, 인계 노트 | MD (제목 + 글머리표) | 매번 컨텍스트에 들어가므로 토큰이 누적된다. Claude Code 문서는 제목·글머리표로 묶고 파일당 200줄 이하, 코드에서 알 수 없는 것만 적으라고 한다. 여러 단계 절차는 스킬로 뺀다 |
| 에이전트가 실행할 스펙·계획 | 원본은 MD. 사람이 검토할 탐색·계획 자료는 원본에서 HTML 뷰를 따로 만들어도 된다. 에이전트에게는 MD 원본을 넘긴다 | 원본은 하나여야 하고 사람이 고칠 수 있어야 한다. HTML 계획을 넘겼을 때 구현·검증이 나아진다는 측정은 없다 |
| 프롬프트 안에 지시·맥락·자료를 함께 넣을 때 | 구역을 XML 태그로 나눔 (`<instructions>`, `<context>`, `<document>`) | Claude 공식 권장. 섞인 내용을 오해 없이 구분하게 한다. 태그 이름은 일관되게, 계층이 있으면 중첩한다 |
| 2만 토큰 이상의 긴 자료를 줄 때 | 자료를 위에, 질문·지시는 맨 끝에. 여러 문서는 `<document>` + `<source>` | Claude 공식 문서: 질문을 끝에 두면 응답 품질이 최대 30% 좋아졌다. 관련 부분을 먼저 인용하게 하면 잡음을 줄인다 |
| AI에게 넘기는 문서 파일 (통째로 읽힐 때) | MD나 일반 텍스트. 제목 계층을 살리고 표는 자르지 않는다 | 같은 내용을 TXT·MD·JSON·CSV로 넣은 실험에서 MD·TXT가 가장 안정적이었고 CSV는 판단이 크게 흔들렸다(Zhang 외 2026) |
| RAG 색인용 조각 | 조각마다 제목 경로를 붙이고 표 행은 자르지 않는다. 원본이 HTML이면 정리한 HTML 조각도 후보 | MD가 PDF보다 나았던 이유는 문법이 아니라 제목 경로와 온전한 표 행이었다(Kumar 2026). CSS·JS·주석·긴 속성을 지운 HTML이 일반 텍스트보다 나았다(HtmlRAG). 통째로 읽히는 문서 입력과는 별개의 전처리다 |
| AI에게 주는 사실 데이터(표) — 단순 2차원 표 | MD 파이프 표 | 파이프 표가 문장·JSON·지식 그래프보다 효율과 정확도의 균형이 가장 좋았다(Claude 3.5 Sonnet 포함 8개 모델). HTML 표와 MD 표의 차이는 대부분 작았다 |
| AI에게 주는 사실 데이터(표) — 셀 병합(`rowspan`/`colspan`)·다단 헤더 | 구조를 잃지 않는 형식: 정리한 HTML `<table>`(`style`·`class` 등 표시용 속성 제거)이나 JSON. 정확도가 중요하면 쓰는 모델로 직접 비교 | MD 파이프 표 문법에는 병합 셀과 다단 헤더 표기가 없어, 펼치면 값이 중복되거나 헤더 관계가 사라진다. 다만 정확도 근거는 아니다. 병합 셀 탐지 과제에서 HTML은 MD보다 낫지 않았다(Sui 외: GPT-4 MD 82.64% 대 HTML 81.28%, GPT-3.5 78.00% 대 76.67%). 표 전반에서는 HTML이 대체로 가장 견고한 텍스트 형식이었다(TABVERSE, 초록 기준) |
| AI에게 주는 사실 데이터 — 계층이 깊을 때 | JSON | 표로 펴면 계층이 사라진다 |
| 작업 상태 기록 | 구조화된 상태는 JSON, 진행 메모는 자유 텍스트, 이력은 git | Claude 공식 권장 |
| 사람이 쓰고 고치는 설계 문서, 결정 기록, 계약서 | MD (+ Mermaid) | diff, 공동 편집, 리뷰가 쉽다. 흐름도·시퀀스 같은 단순한 다이어그램은 Mermaid로 충분하다 |
| PR 설명 | MD | GitHub가 렌더링한다. 크거나 낯선 PR만 HTML 설명 페이지를 따로 붙인다(3절을 지킨다) |
| 여러 안 비교, 아키텍처 설명, 리서치 보고서, 코드 흐름 설명 | 원본(MD)에서 만든 HTML 뷰 | 나란히 비교, SVG 다이어그램, 색으로 구분한 diff는 MD로 흉내 내기 어렵다. 다만 그림이냐 글이냐보다 **어떤 수준의 정보를 보여주느냐**가 이해를 좌우했다 |
| 티켓 정렬, 파라미터 조정, 데이터 라벨링, 프롬프트 튜닝 | export 버튼이 달린 인터랙티브 HTML | 글로 설명하기 어려운 선택을 사람이 직접 하게 한다. HTML이 가장 확실하게 나은 경우다 |
| 이메일 본문 | MD나 일반 텍스트(필요하면 제한된 HTML로 변환) | 이메일 클라이언트는 CSS를 대부분 지운다 |
| 짧은 메모, TODO, 일일 로그 | MD | HTML로 만들 이유가 없다 |

### 에이전트에게 HTML을 넘길 때 (웹 페이지 포함)

우선순위: **① 원본 MD가 있으면 MD를 넘긴다. ② HTML밖에 없으면 정제한 뒤 용도에 맞게 넘긴다. ③ 사람용 HTML 뷰를 에이전트 입력으로 되돌리지 않는다.** 5절의 보안 규칙도 이 절차를 따른다.

1. **먼저 코드로 정제한다.** `script`·`style`·주석을 지우고, 숨김 요소(`display:none`, `visibility:hidden`, `aria-hidden`, 크기 0, 화면 밖 배치)를 지운다. 숨긴 텍스트에 지시문이 들어 있을 수 있다(Greshake 외 2023). 잡음은 프롬프트보다 코드로 거른다.
2. **사람이 펼쳐 볼 수 있는 접힌 내용은 버리지 않는다.** `<details>`, 탭, 아코디언 안의 내용은 정상 정보다. 출처(어느 섹션에서 접혀 있었는지)와 함께 따로 둔다.
3. **용도별로 넘긴다.**

| 용도 | 넘기는 형태 | 이유 |
|---|---|---|
| 내용 추출(요약, 질의응답) | 보이는 텍스트를 MD로 | 원본 HTML은 약 97%가 마크업이고, 잘라 넣으면 접힌 정보가 통째로 빠진다 |
| 브라우저 조작(강한 모델) | 정제한 HTML DOM | 강한 모델은 레이아웃 정보를 버튼 위치 판단에 써서 압축 표현보다 최대 17.5%p 나았다. 약한 모델은 반대였다(Read More, Think More) |
| 구조 보존 RAG | 정제한 HTML(CSS·JS·주석·긴 속성 제거, 빈 태그·단일 중첩 정리) | HtmlRAG가 이렇게 정리한 HTML이 일반 텍스트보다 나았다 |

정제는 인젝션을 줄일 뿐 막지 못한다. 보이는 텍스트에도 지시문이 있을 수 있으므로 넘긴 내용은 데이터로만 다루게 한다.

## 3. 검토 화면(HTML 뷰)을 만들 때 지킬 것

**원본과 구조**
- **원본이 아니라 뷰다.** 뷰와 원본이 다르면 원본이 맞다. 뷰를 직접 고치지 말고 원본을 고친 뒤 다시 만든다. 뷰에 원본 파일과 날짜(또는 커밋)를 적는다.
- **맨 위에는 AI의 결론이 아니라 사람이 할 일을 둔다.** 결정해야 할 항목, 확인된 것과 확인되지 않은 것, 이 화면이 다루지 않은 것을 먼저 보여준다. 소제목은 그 섹션 내용을 요약하게 쓴다. MD에도 똑같이 적용된다.
- **짧게.** 상위 요약이 긴 상세 자료보다 이해를 도왔고, 과도한 문서는 오히려 이해를 방해했다.

**사람이 판단하게 만들기**
- **AI 계획에는 "이 계획의 가정" 섹션을 두고 사람이 하나씩 확인하게 한다.** AI가 만든 계획을 검토할 때 가정을 찾게 하자 과신이 가장 많이 줄었고 부담은 늘지 않았다(Ghosh 외 2026, 글쓰기 과제).
- **가능하면 사람이 먼저 판단하게 한다.** 예: 사람이 먼저 결정한 뒤 AI 제안을 보여 주기, 요청할 때만 제안을 보여 주기. 이런 인지 강제 설계 3종(먼저 결정, 요청 시 표시, 30초 대기)을 묶은 조건이 단순 설명 조건보다 과신을 줄였다. 다만 줄어든 것은 두 지표 중 하나(탄수화물이 가장 많은 재료 고르기)에서만 유의했고, 세 설계 사이에는 유의한 차이가 없었다. 과신이 가장 많이 준 설계일수록 주관 평가가 낮았으니 중요한 결정에만 쓴다(Buçinca 외 2021, 영양 과제, N=199).
- **고른 결과는 export해서 원본에 반영한다.** 인터랙티브 HTML에서 고른 값은 JSON·MD·프롬프트로 export해 에이전트에게 돌려주고, 에이전트가 원본(MD/JSON)에 반영하게 한다. 그 뒤 화면은 원본에서 다시 만든다.
- **자주 다시 만드는 뷰는 고정 템플릿으로 기계 변환한다.** 매번 에이전트에게 HTML 전체를 새로 쓰게 하면 직접 측정에서 평균 75.7초가 들었다. 원본 데이터를 읽어 HTML을 찍어 내는 템플릿·스크립트를 한 번 만들어 두면, 같은 MD를 꾸밈 없는 HTML로 기계 변환한 크기는 1.2배였고 생성에 모델이 들지 않는다(4절). 템플릿의 CSS는 결과 파일 크기에만 더해진다.

**설명과 표시 방식**
- **설명을 더 붙이는 것으로 검토가 나아지지 않는다.** AI 설명은 AI가 맞든 틀리든 제안을 받아들일 확률만 높였고, AI 신뢰도만 보여 준 조건보다 팀 성과가 낫지 않았다(Bansal 외 2021, 3개 과제, 1,626명). 설명이 과신을 줄인 건 설명이 검증 비용을 충분히 낮출 때였다(Vasconcelos 외 2023, 미로 과제, 5개 연구 N=731). 주장마다 근거(코드 줄, 출처 링크)로 바로 가서 하나씩 확인할 수 있게 한다.
- **AI가 만든 부분과 사람이 확인한 부분을 나눠 표시한다.** 주장마다 "검증됨/미검증"이나 신뢰도를 붙이고, 해결되지 않은 불확실성을 드러낸다. 항목마다 신뢰도를 갱신해 보여 주면 적절한 의존이 늘었고(Goddard 외 2012), AI 신뢰도만 보여 준 조건은 설명을 붙인 조건만큼 팀 성과를 냈다(Bansal 외 2021).
- **AI의 조언을 가장 눈에 띄게 두지 않는다.** 눈에 띄게 보여준 조언은 틀려도 더 따랐고, 세부 정보가 지나치게 많으면 덜 신중해졌다. "이렇게 하라"는 권고보다 판단에 필요한 정보를 보여준다(Goddard 외 2012).
- **보기 좋은 것과 맞는 것을 구분한다.** 깔끔한 화면, 정돈된 PR 설명은 품질 신호가 아니다. 도구가 템플릿으로 찍어 내는 경우가 많다.

**누락**
- **"이 화면이 다루지 않은 것"을 꼭 적는다.** AI가 짚어 준 곳만 보게 되기 쉽고, AI가 놓친 것은 숙련자도 그대로 따라갔다. 중요한 변경은 원본 diff로 직접 확인한다.

**만들 때**
- **필요할 때만 만든다.** HTML은 생성 시간과 토큰이 더 든다. 사람이 실제로 보고 판단할 산출물에만 쓴다.
- **CSS는 작업할 때 공용으로, 내보낼 때 인라인으로.** 예제 HTML 토큰의 약 45%(44~47%)가 CSS다(4절). 로컬이나 정적 호스팅에서 여러 뷰를 만들 때는 미리 정한 공용 CSS(또는 고정 클래스 규격)를 참조하게 하고, 에이전트에게 그 클래스 목록을 함께 준다. 목록 없이 클래스를 쓰게 하면 없는 클래스를 지어낼 수 있다. 아티팩트, 첨부, 단일 링크처럼 파일 하나로 내보낼 때는 외부 CSS 경로가 따라가지 않으므로 빌드 단계에서 공용 CSS를 `<style>`로 인라인한다. 이 인라인은 스크립트가 하므로 생성 토큰이 들지 않는다.
- **오픈 모델이면 내용을 먼저 쓰게 한다.** 오픈 모델은 형식 지시만으로 추론이 떨어졌고, 내용과 서식을 나누면 대부분 회복됐다. 최신 비공개 모델(Claude 등)에서는 이 손실이 거의 없었다.

## 4. 비용

두 가지로 직접 쟀다(2026-11-15). 원자료와 스크립트는 `measurement/`에 있다.

- **측정 1, 예제 HTML 31개**: Thariq의 GitHub 저장소 `thariqs/html-effectiveness`의 `main` HEAD(2026-11-15에 받음)에서 `index.html` 2개를 뺀 31개(본 예제 20개 + `unknowns/` 11개)를 o200k_base 토크나이저(tiktoken)로 셌다. Claude 토크나이저는 비공개라 근사다. "MD 근사치"는 Python 표준 라이브러리 `html.parser.HTMLParser`를 상속한 자체 휴리스틱 변환기(`measure.py`의 `Split`)로 만들었다. `script`·`style`·`svg` 안의 텍스트를 버리고 `h1~h6`→`#`, `li`→`- `, `td/th`→` | `, `code`→백틱으로 바꾼다. 사람이 쓴 MD가 아니다. 받을 때 해시는 기록하지 않았다. 커밋 이력상 2026-07-03의 `1787245`(Merge branch 'add-project-docs') 뒤로 커밋이 없고, `unknowns/` 예제 11개는 그 직전 `e5787a4`에서 추가됐으므로 측정 대상은 `1787245`로 본다.
- **측정 2, 직접 생성**: 지침 3절(당시 판)을 잘라 낸 원본(o200k 814토큰)을 프롬프트에 직접 넣고, Claude Code 하위 에이전트(general-purpose, 상위 세션을 상속한 Opus 5.5) 6개를 동시에 돌렸다. MD 3회, HTML 3회. 프롬프트 원문은 이 절 끝에 있다. 토큰과 시간은 완료 알림의 `subagent_tokens`, `duration_ms`다. effort는 하위 에이전트마다 기록하지 않았다. 상위 세션의 effort는 high였고, 하위 에이전트가 이를 그대로 받았는지는 확인하지 못했다.

| 비교 | 결과 |
|---|---|
| 문서형 HTML(보고서, 계획, 설명, PR 정리) 대 MD 근사치 (측정 1) | 약 4~7배. 전체 중앙값은 본 예제 20개 9.51배(4.06~65.17), unknowns 11개 7.31배(3.55~62.55). 인터랙티브 예제는 내용이 JS 데이터 안에 있어 배율이 과장된다 |
| HTML 토큰 구성 (측정 1) | 본 예제 20개: CSS 44%, JS 12%, SVG 8%, 보이는 글 11%, 나머지 태그·속성·클래스 등 25%. unknowns 11개: CSS 47%, JS 13%, SVG 2%, 보이는 글 14%, 나머지 24% |
| CSS·JS 합산 비중 | 예제(측정 1) 56~60%. 직접 생성 HTML 3개(측정 2) 43~50%, 그중 CSS만 31~39% |
| 생성 시간 (측정 2) | MD 평균 21.8초(20.9~23.2), HTML 평균 75.7초(66.2~82.7). 평균 비 약 3.5배, 회차 조합에 따라 2.9~3.9배 |
| Claude 사용량 합계 (측정 2) | MD 평균 69,314(69,276~69,365), HTML 평균 76,600(75,085~77,687). 차이 약 7,300. 입력(시스템 프롬프트 포함)·출력·사고·도구 호출을 나누지 않은 합계다 |
| 결과 파일 크기 (측정 2, o200k) | MD 1,198~1,223, HTML 4,931~6,282. HTML이 MD의 약 4.0~5.2배, 평균 차이 약 4,500 |
| 직접 생성 HTML에서 `<style>`·`<script>`를 뺀 것 | 여전히 MD의 약 2.1~2.8배 |
| 같은 MD를 꾸밈 없는 HTML로 기계 변환 | 1.2배 (지침 파일 당시 판, python-markdown + `tables` 확장, 4,379 → 5,274토큰) |

- 예제 HTML에서는 CSS·JS가 토큰의 절반을 넘는다(56~60%). 에이전트에게 HTML을 넘겨야 하면 2절 절차대로 `<style>`·`<script>`를 빼고 넘긴다. 그래도 에이전트가 만든 HTML은 카드·라벨·클래스 같은 구조가 붙어 MD의 2~3배가 남는다. 원본 MD가 있으면 MD를 넘긴다.
- 사용량 차이(약 7,300)는 결과 파일의 o200k 차이(약 4,500)보다 크다. 나머지 약 2,800은 토크나이저 차이와 사고·도구 호출 토큰으로 보이지만 나눠 잴 수 없었다. "HTML 출력이 7,300토큰 더"라고 읽지 않는다.
- 생성 시간은 Thariq가 말한 "2~4배"의 위쪽이었다. 다만 아래 한계 ①처럼 과대 추정일 수 있고, 반대로 에이전트 시작 같은 고정 시간은 배율을 줄이는 쪽으로 섞여 있다. 두 효과의 크기는 따로 재지 않았다.
- 문서 하나가 수천 토큰이라 한 번 넘기는 비용은 작다. 매번 로드되는 파일에서는 배율이 그대로 쌓인다.
- MD도 일반 텍스트보다 약 26% 더 든다(Eliav 2026).

**측정의 한계**
- ① **베이스라인 비대칭.** 입력 원본이 이미 MD였다. MD 조건은 거의 다시 정리만 하면 됐고 HTML 조건은 레이아웃·CSS를 새로 설계해야 했다. 내용을 처음부터 쓰는 상황보다 시간 배율(3.5배)과 토큰 차이를 과대 추정했을 수 있다.
- ② **토크나이저와 사용량의 성격.** 파일 크기는 o200k 근사이고, 사용량은 Claude의 실제 집계다. 두 수치는 단위가 다르다. 사용량에는 사고 토큰과 도구 호출 토큰이 섞여 있다.
- ③ **역변환의 정보 손실.** 측정 1의 MD 근사치는 HTML에서 뽑은 것이라 SVG, 레이아웃, 나란히 비교, JS 안의 데이터 같은 시각·구조 정보가 빠진다. 2절에서 "MD로 흉내 내기 어렵다"고 한 바로 그 정보다. 따라서 "같은 정보를 담은 MD"와의 비교가 아니라 "글 부분만 남긴 것"과의 비교이고, 시각 정보가 많은 예제일수록 배율이 커진다. 문서형(글 위주) 예제의 4~7배만 일반화한다.
- ④ **표본.** 측정 2는 조건마다 3회, 내용 하나(한국어, 814토큰), 모델 하나다. 짧은 원본이라 CSS 같은 고정 비용의 비중이 크다. 긴 문서에서 배율이 어떻게 바뀌는지는 재지 않았다.
- ⑤ **동시 실행.** 6개를 동시에 돌려 서버 부하가 시간에 섞였을 수 있다.

**측정 2 프롬프트 원문** (두 조건 모두 영어 지시문 + 원본 전문. 차이는 과제 문장과 저장 경로뿐)
- MD 조건: "Turn the SOURCE below into a well-structured Markdown document — a reference page a team would read. Keep all content in Korean and keep every point; you may reorganize and add structure (headings, lists, tables) where useful."
- HTML 조건: "Turn the SOURCE below into a single self-contained HTML file — a well-designed reference page a team would read in a browser (inline CSS, optional inline JS, no external resources). Keep all content in Korean and keep every point; you may reorganize and add structure, visual hierarchy, and interactivity where useful."
- 공통: "Use exactly ONE Write call to save the result to: <경로>", "Do not read any files, search, or use any other tool.", "After writing, reply with only the word DONE."

## 5. 공유와 보안

- 내부 정보나 개인정보가 든 HTML은 공개 호스팅(GitHub Pages, 공개 S3 등)에 올리지 않는다. 접근 제한이 있는 곳(비공개 아티팩트 링크 등)을 쓴다.
- 남이 만든 HTML은 JS가 실행되므로 코드처럼 다룬다.
- 에이전트에게 HTML을 읽힐 때는 2절 "에이전트에게 HTML을 넘길 때"의 정제를 먼저 한다. 숨김 요소를 코드로 지운 뒤, 내용만 필요하면 MD로, 브라우저 조작이나 구조 보존 RAG면 정제한 HTML만 넘긴다. 원본 HTML을 그대로 넘기지 않는다.
- MD도 채팅 화면에서 렌더링되면 이미지 링크로 데이터가 새어 나갈 수 있다. 출처를 모르는 MD를 그대로 렌더링하지 않는다.

## 6. 양쪽 주장 검토

### HTML 쪽 주장 (Thariq 원문 기준)

| 주장 | 판정 | 근거 |
|---|---|---|
| 100줄 넘는 MD는 읽기 어렵다 | 부분적으로 맞다. 원인은 형식보다 길이와 구조다 | 사람은 웹 페이지 단어의 20~28%만 읽는다(Nielsen 2008). 레이아웃을 개선해도 읽기 속도와 이해도는 그대로였고 만족도와 피로감만 나아졌다(Chaparro 외 2005). 엔지니어 744명은 모두 "맨 앞 요약 + 섹션 요약 아래 상세"를 골랐고 그 순서로 읽었다(Silyn-Roberts 2002). 이 구조는 MD로도 된다 |
| 정보 밀도가 높다 | 맞다. 다이어그램, 나란히 비교, 색 구분 diff에서 | 단순한 다이어그램은 Mermaid로도 된다. 프로그램 이해 실험에서 글이냐 그림이냐는 차이가 없었고 정보의 수준이 차이를 만들었다(Shneiderman 외 1982, 학생 51·32명) |
| 공유가 쉽다 | 호스팅한 링크일 때만, 받는 사람에 따라 다르다 | Thariq 본인도 Slack으로 HTML 파일을 보내면 클릭률이 "끔찍하다"고 했다. 공개 호스팅에 올렸다가 고객 데이터가 노출된 사례가 HN에서 보고됐다 |
| HTML을 쓰면 루프 안에 있다고 느낀다 | 느낌은 측정이 아니다. 판단을 요구하는 인터랙션이 있을 때만 근거가 있다 | AI 설명은 AI가 맞든 틀리든 수용만 늘렸다(Bansal 외, CHI 2021). 질 낮은 설명은 정확도를 떨어뜨리면서 확신은 높였다(Kaufman 2026). 리뷰어는 LLM이 가리킨 곳에 집중했다(Tufano 외 2024). 반대로 사람이 먼저 판단하는 등 인지 강제 설계를 넣거나 가정을 찾게 하면 과신이 줄었다(Buçinca 외, CSCW 2021; Ghosh 외 2026) |
| 직접 편집을 안 하니 MD의 편집 장점은 덜 중요하다 | 틀렸다 | 원본을 사람이 못 고치면 공동 작성이 끊긴다(HN, Miessler) |
| 1M 컨텍스트에서는 늘어난 토큰이 체감되지 않는다 | 한 번 넘기는 자료에만 맞다 | 직접 측정에서 문서형 HTML은 MD 근사치의 약 4~7배였다. 매번 로드되는 파일은 세션 수만큼 쌓인다 |
| 생성이 2~4배 오래 걸려도 그만한 가치가 있다 | 사람이 보는 일회성 산출물에서만 맞다 | 직접 측정에서 HTML 생성은 MD의 약 3.5배 걸렸고(원본이 MD라 과대 추정 가능, 4절 한계 ①) 사용량이 문서 하나당 약 7,300 더 들었다(사고·도구 호출 포함). 버전 관리가 가장 큰 단점이라는 것도 본인이 인정했다 |

### MD 쪽 주장

| 주장 | 판정 | 근거 |
|---|---|---|
| AI는 MD를 가장 잘 이해한다 | 근거 없다. 다만 문서 입력에서는 MD·텍스트가 안정적이었다 | 통제 실험에서 MD가 일반 텍스트보다 안정적으로 낫지 않았다(Eliav 2026). 형식에 따라 GPT-3.5-turbo 점수가 최대 40% 달라졌고 GPT-4는 더 견고했다(He 외 2024). 의미 없는 서식 차이로 LLaMA-2-13B에서 최대 76점 벌어졌고, 모델 크기를 키우거나 지시 튜닝을 해도 민감도가 남았다(Sclar 외, ICLR 2024). 문서 파일 실험에서는 MD·TXT가 JSON·CSV보다 안정적이었다(Zhang 외 2026) |
| `#` 계층이 어텐션 가중치로 Lost in the Middle을 줄인다 | 근거 없다 | 이런 메커니즘을 보인 연구를 찾지 못했다. 효과가 있었던 건 RAG 조각마다 제목 경로를 붙이는 것이었다(Kumar 2026) |
| HTML은 AI에게 나쁘다 | 틀렸다 | 정리한 HTML이 RAG에서 일반 텍스트보다 나았다(HtmlRAG, WWW 2025). 표에서는 HTML이 대체로 가장 견고했다(TABVERSE, 초록 기준). 강한 모델은 페이지를 조작할 때 HTML이 나았다(Read More, Think More). 원본 HTML을 정리 없이 넣는 게 나쁘다 |
| 토큰 효율이 좋다 | 맞다 | 직접 측정에서 문서형 HTML의 약 1/4~1/7. 차이의 절반 이상이 CSS·JS다 |
| diff와 버전 관리가 깔끔하다 | 맞다 | 양쪽 모두 인정한다 |
| 학습 데이터에 MD가 많다 | 확인할 수 없다 | 웹 HTML도 학습 데이터에 매우 많다 |

### 양쪽이 다 놓친 것

- **형식보다 구조.** 사람에게는 요약 먼저·섹션 요약·상세 순서가, AI에게는 제목 경로·온전한 표·구역 구분이 효과를 냈다. 둘 다 형식과 상관없이 된다.
- **설명보다 판단.** 검토 품질을 올린 건 더 많은 설명이 아니라 사람이 가정을 확인하고 먼저 판단하게 만드는 장치였다.
- **문장 자체를 읽기 쉽게.** Karpathy는 ASD-STE100(항공 정비 문서용 통제 언어)에 가깝게 쓰게 하면 읽기 쉬워진다고 했다.
- **정답 형식은 모델과 흐름마다 다르다.** 정확도가 중요한 파이프라인이면 쓰는 모델로 직접 비교한다.

## 7. 확인하지 못한 것

**측정**
- 4절 "측정의 한계" ①~⑤가 그대로 남아 있다. 특히 직접 생성 측정은 원본이 MD여서 HTML 쪽에 불리했고, 조건마다 3회뿐이다.
- 예제 저장소의 커밋 해시는 받을 때 기록하지 않아 커밋 이력으로 `1787245`를 추정했다. 하위 에이전트의 effort는 기록하지 않았다(상위 세션은 high).
- HTML 계획을 에이전트에게 넘겼을 때 구현·검증 품질이 달라지는지 측정한 연구를 찾지 못했다.

**문헌의 확인 수준**
- 본문 일부를 보완 때(2026-11-15) arXiv PDF로 직접 확인: Buçinca 외 2021(1~12쪽: 조건 설계, 결과 표 1~3), Bansal 외 2021(1~3쪽: 초록, 서론, 기여 요약), Vasconcelos 외 2023(1~2쪽: 초록, 서론). 세 편 모두 arXiv에 무료로 공개돼 있다. 첫 작성 때는 초록만 읽었고, 3절의 세부 조건은 이번에 본문과 대조해 고쳤다.
- 초록만 확인: Narvekar 외 2025, Duggan & Payne 2009, DeStefano & LeFevre 2007, Silyn-Roberts 1998(첫 작성 때 1999로 잘못 적음), Kücking 외 2026, Parasuraman & Riley 1997, Lee & See 2004, TABVERSE. 이 중 TABVERSE(2절 표 행)를 빼면 본문에서 이름을 들어 인용하지 않았다.
- Liner 풀 텍스트로 확인: Why HTML-to-LLM Scraping Fails, Dratsch 외 2023, Lu 2026, Rahman 외 2026.
- 검색 요약으로만 확인: InfoQ Japan, ifanr, 数位时代 기사.

**적용 범위**
- 모델 세대: 형식 민감도·표 형식 연구는 2023~2024년 모델 결과다. Sui 외는 GPT-3.5·GPT-4, He 외는 GPT-3.5-turbo·GPT-4(GPT-4가 더 견고), Sclar 외는 LLaMA-2-13B 등 오픈 모델이다. 최신 모델에서 편차 크기는 확인하지 못했다. 크기가 클수록 줄어든다는 결과(He 외)와 크기·지시 튜닝으로도 남는다는 결과(Sclar 외)가 함께 있다. TABVERSE(2026)는 초록에 평가 모델 이름이 없어 세대를 확인하지 못했다.
- 인지 강제 실험 중 Ghosh 외 2026은 글쓰기 과제, Buçinca 외 2021은 영양(저탄수화물 대체) 과제다. 코딩 계획 검토에도 같은지는 모른다.
- Slack 서식은 Slack 도움말의 메시지 서식 안내 기준이다. 캔버스·앱 메시지의 렌더링은 확인하지 않았다.

## 출처

### 원 논쟁과 반응
- Thariq Shihipar, [Using Claude Code: The Unreasonable Effectiveness of HTML](https://x.com/trq212/status/2052809885763747935) (X, 2026-05-09). 예제: [thariqs.github.io/html-effectiveness](https://thariqs.github.io/html-effectiveness), [저장소](https://github.com/thariqs/html-effectiveness)
- Andrej Karpathy, [HTML 출력 권장과 형식 발전 단계](https://x.com/karpathy/status/2053872850101285137) (2026-05-12), [LLM 출력 이해 팁](https://x.com/karpathy/status/2105819303471976479) (2026-10-02)
- Angie Jones, [출력은 HTML, 입력은 MD](https://x.com/trq212/status/2052809885763747935/quotes) (인용 글)
- Simon Willison, [링크 글](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/) (2026-05-08)
- Daniel Miessler, [Text is Thought, and Thought is Holy](https://danielmiessler.com/blog/text-is-thought-holy)
- 박재홍, [LLM 시대, 마크다운 대신 HTML을 쓰라고?](https://wikidocs.net/blog/@jaehong/13111/) (HN 토론 정리)
- Carrot Yoon, [md와 html 형식에 대한 생각](https://yooncarrot.com/article/69)
- AX Engineer Lukas, [AG 시대 MD 보다 HTML](https://brunch.co.kr/@lukas08/208)
- InfoQ Japan, [Anthropic リード: HTML が有効に](https://www.infoq.com/jp/news/2026/07/anthropic-html-markdown-agent/), ifanr, [Markdown 已死，HTML 当立？](https://www.ifanr.com/1665516), 数位时代, [Markdown過時了?](https://www.bnext.com.tw/article/90893/) (검색 요약으로만 확인)
- Cloudflare, [에이전트를 위한 Markdown 소개](https://blog.cloudflare.com/ko-kr/markdown-for-agents/)

### 공식 문서
- Claude, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) (XML 태그, 긴 자료 배치, 출력 형식, 상태 기록)
- Claude Code, [How Claude remembers your project](https://code.claude.com/docs/en/claude-md) (CLAUDE.md 작성법)
- Slack, [Format your messages in Slack](https://slack.com/help/articles/202288908-Format-your-messages) (메시지 서식)

### LLM 쪽 연구
- He 외, [Does Prompt Formatting Have Any Impact on LLM Performance?](https://arxiv.org/abs/2411.10541) (2024)
- Sclar 외, [Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design](https://arxiv.org/abs/2310.11324) (ICLR 2024)
- Voronov 외, [Mind Your Format](https://arxiv.org/abs/2401.06766) (ACL 2024 Findings)
- Eliav, [Prompt Design at Scale](https://arxiv.org/abs/2607.19257) (2026, 동료 심사 전)
- Lee 외, [The Format Tax](https://arxiv.org/abs/2604.03616) (2026)
- Zhang 외, [Not as Sweet by Another Name: An Empirical Study of Format Robustness in LLM Document Workflows](https://arxiv.org/abs/2607.27648) (ASE 2026)
- Narvekar, Mukherjee, Tanuwijaya, Evaluating the Impact of Input Format on LLM Performance: JSON vs. YAML vs. Text (IEEE FMLDS 2025, pp. 572–577), [doi:10.1109/FMLDS67896.2025.00072](https://doi.org/10.1109/fmlds67896.2025.00072) (초록만)
- Tan 외, [HtmlRAG](https://arxiv.org/abs/2411.02959) (WWW 2025)
- Kumar, [Is Markdown Better Than PDF for Retrieval-Augmented Generation? A Controlled Paired-Format Benchmark](https://zenodo.org/records/21829016) (2026, Zenodo 프리프린트, doi:10.5281/zenodo.21829016)
- Why HTML-to-LLM Scraping Fails: A Production Analysis (2026, Liner 풀 텍스트로 확인, 원문 URL 미기록)
- Sui 외, [Table Meets LLM](https://arxiv.org/abs/2305.13062) (WSDM 2024)
- Ahsan 외, [TABVERSE](https://arxiv.org/abs/2606.09578) (2026, 심사 중, 초록만)
- Oh 외, [Talking with Tables](https://arxiv.org/abs/2412.17189) (2024)
- Enomoto 외, [Read More, Think More](https://arxiv.org/abs/2604.01535) (2026)
- Greshake 외, [Not what you've signed up for: indirect prompt injection](https://arxiv.org/abs/2302.12173) (2023)

### 사람 쪽 연구
- Nielsen, [How Little Do Users Read?](https://www.nngroup.com/articles/how-little-do-users-read/) (2008)
- Pernice, [The Layer-Cake Pattern of Scanning Content on the Web](https://www.nngroup.com/articles/layer-cake-pattern-scanning/) (NN/g 2019)
- Silyn-Roberts, [Document Structure and Its Effect on Engineers' Reading Strategies](https://ascelibrary.com/doi/10.1061/%28ASCE%291052-3928%282002%29128%3A3%28115%29) (2002)
- Silyn-Roberts, [Using Engineers' Characteristics to Improve Report Writing Instruction](https://doi.org/10.1061/%28ASCE%291052-3928%281998%29124%3A1%2812%29) (Journal of Professional Issues in Engineering Education and Practice 124(1), 1998, pp. 12–16) (초록만)
- Chaparro, Shaikh, Baker, [Reading Online Text With a Poor Layout: Is Performance Worse?](https://portfolio.erau.edu/en/publications/reading-online-text-with-a-poor-layout-is-performance-worse/) (Usability News 2005)
- Duggan & Payne, [Text skimming: The process and effectiveness of foraging through text under time pressure](https://doi.org/10.1037/a0016995) (Journal of Experimental Psychology: Applied 15(3), 2009, pp. 228–242; [저장소 페이지](https://researchportal.bath.ac.uk/en/publications/text-skimming-the-process-and-effectiveness-of-foraging-through-t/)) (초록만)
- DeStefano & LeFevre, [Cognitive load in hypertext reading: A review](https://doi.org/10.1016/j.chb.2005.08.012) (Computers in Human Behavior 23(3), 2007, pp. 1616–1641) (초록만)
- Shneiderman 외, [Control Flow and Data Structure Documentation: Two Experiments](https://www.cs.umd.edu/users/ben/papers/Shneiderman1982Control.pdf) (CACM 1982)
- Dyson, [How physical text layout affects reading from screen](https://doi.org/10.1080/01449290410001715714) (Behaviour & Information Technology 23(6), 2004, pp. 377–393)
- Fogg 외, Stanford Web Credibility Project ([요약](https://en.wikipedia.org/wiki/Stanford_Web_Credibility_Project))

### 자동화 편향과 AI 검토 연구
- Parasuraman & Riley, [Humans and Automation: Use, Misuse, Disuse, Abuse](https://doi.org/10.1518/001872097778543886) (Human Factors 39(2), 1997, pp. 230–253) (초록만)
- Lee & See, [Trust in Automation: Designing for Appropriate Reliance](https://doi.org/10.1518/hfes.46.1.50_30392) (Human Factors 46(1), 2004, pp. 50–80) (초록만)
- Goddard 외, [Automation bias: a systematic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/) (JAMIA 2012)
- Dratsch 외, [Automation Bias in Mammography: The Impact of Artificial Intelligence BI-RADS Suggestions on Reader Performance](https://doi.org/10.1148/radiol.222176) (Radiology 307(4), 2023, Liner 풀 텍스트로 확인)
- Kücking 외, [Impact of AI recommendation correctness on diagnostic accuracy in clinical decision-making](https://doi.org/10.1016/j.ijmedinf.2025.106223) (International Journal of Medical Informatics 207, 2026) (초록만)
- Perry 외, [Do Users Write More Insecure Code with AI Assistants?](https://arxiv.org/abs/2211.03622) (CCS 2023)
- Kaufman, [Programmers Are Poor and Overconfident Judges of LLM-Generated Assertions](https://arxiv.org/abs/2607.08885) (2026)
- Tufano 외, [Deep Learning-based Code Reviews: A Paradigm Shift or a Double-Edged Sword?](https://arxiv.org/abs/2411.11401) (2024)
- Lu, [A study of AI usage in GitHub pull requests](https://hdl.handle.net/1828/24150) (UVic Master's Project 2026, Liner 풀 텍스트로 확인)
- Rahman 외, [Plausible Is Not Enough: Trust and Evidence in AI-Authored Pull Request Review](https://arxiv.org/abs/2610.21144) (2026, Liner 풀 텍스트로 확인)
- Bansal 외, [Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance](https://arxiv.org/abs/2006.14779) (CHI 2021, 본문 일부 확인)
- Buçinca, Malaya, Gajos, [To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making](https://arxiv.org/abs/2102.09692) (CSCW 2021, 본문 일부 확인)
- Vasconcelos 외, [Explanations Can Reduce Overreliance on AI Systems During Decision-Making](https://arxiv.org/abs/2212.06823) (CSCW 2023, 본문 일부 확인)
- Ghosh, Sarkar, Lindley, Poelitz, [An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing](https://arxiv.org/abs/2601.18033) (2026)
- 논문 탐색에 쓴 Liner Scholar 스레드: https://scholar.liner.com/ko/threads/01a1dcb3-809e-76e0-990d-e07d2f2cdd4e
