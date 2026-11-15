# MD / HTML 사용 지침

작성 2026-11-15. 한국어·영어·일본어·중국어 자료, 원 논쟁(Thariq Shihipar의 X 원문과 반응, HN 토론, Simon Willison, Daniel Miessler, Karpathy), Claude 공식 문서, 논문 40여 편, 직접 측정을 바탕으로 정리했다. 논문은 arXiv·공개 저장소 본문이나 Liner Scholar 풀 텍스트로 확인했고, 초록까지만 본 것은 따로 표시했다.

## 한 줄 요약

**형식은 "얼마나 자주, 누가 다시 읽는가"로 고른다. 매번 로드되는 파일과 사람이 고치는 원본은 MD, 사람이 한 번 보고 판단하는 화면은 원본에서 만든 HTML, 사람이 값을 고르는 일은 export 버튼이 달린 HTML.**
사람이 빨리 읽게 만드는 건 형식보다 구조(요약 먼저, 섹션마다 요약, 상세는 그 아래)이고, AI가 잘 읽게 만드는 것도 형식 문법보다 구조(제목 경로, 잘리지 않은 표, 구역 구분)다. 검토 화면은 보기 좋게보다 **사람이 판단하게** 만든다.

## 1. 판단 순서

1. **얼마나 자주 다시 읽히는가**: 매 세션·매 작업마다 컨텍스트에 들어가면 MD. 한 번 넘기고 끝나는 계획이나 참고 자료면 HTML이어도 된다(4절 비용 참고).
2. **누가 고치는가**: 사람이 직접 고치거나 git에서 diff로 검토하면 MD.
3. **사람이 무엇을 해야 하는가**: 읽고 끝이면 MD로 충분하다. 여러 안을 비교하거나 구조를 한눈에 봐야 하면 HTML 뷰. 값을 고르거나 순서를 정해야 하면 인터랙티브 HTML.
4. **어디로 공유하는가**: GitHub·Notion·Slack처럼 MD를 렌더링하는 곳이면 MD. 개발 도구가 없는 사람에게 보내야 하면 HTML을 링크로(접근 제한이 있는 곳에). HTML 파일을 첨부로 보내면 잘 열어 보지 않는다.

## 2. 상황별 지침

| 상황 | 형식 | 이유 |
|---|---|---|
| `CLAUDE.md`, `AGENTS.md`, 스킬, 메모리, 인계 노트 | MD (제목 + 글머리표) | 매번 컨텍스트에 들어가므로 토큰이 누적된다. Claude Code 문서는 제목·글머리표로 묶고 파일당 200줄 이하, 코드에서 알 수 없는 것만 적으라고 한다. 여러 단계 절차는 스킬로 뺀다 |
| 에이전트가 실행할 스펙·계획 | 원본은 MD. 한 번 넘기는 탐색·계획 자료는 HTML도 가능 | 원본은 하나여야 하고 사람이 고칠 수 있어야 한다. HTML 계획을 넘겼을 때 구현·검증이 나아진다는 측정은 없다 |
| 프롬프트 안에 지시·맥락·자료를 함께 넣을 때 | 구역을 XML 태그로 나눔 (`<instructions>`, `<context>`, `<document>`) | Claude 공식 권장. 섞인 내용을 오해 없이 구분하게 한다. 태그 이름은 일관되게, 계층이 있으면 중첩한다 |
| 2만 토큰 이상의 긴 자료를 줄 때 | 자료를 위에, 질문·지시는 맨 끝에. 여러 문서는 `<document>` + `<source>` | Claude 공식 문서: 질문을 끝에 두면 응답 품질이 최대 30% 좋아졌다. 관련 부분을 먼저 인용하게 하면 잡음을 줄인다 |
| AI에게 넘기는 문서 파일 | MD나 일반 텍스트. 섹션 경로(제목 계층)를 함께 넘기고 표는 자르지 않는다 | 같은 내용을 TXT·MD·JSON·CSV로 넣은 실험에서 MD·TXT가 가장 안정적이었고 CSV는 판단이 크게 흔들렸다. RAG에서 MD가 나았던 이유도 문법이 아니라 제목 경로와 온전한 표 행이었다 |
| AI에게 주는 사실 데이터(표) | MD 파이프 표가 기본. 계층이 깊으면 JSON | 파이프 표가 문장·JSON·지식 그래프보다 효율과 정확도의 균형이 가장 좋았다(Claude 3.5 Sonnet 포함 8개 모델). HTML 표와 MD 표의 차이는 대부분 작았다 |
| 작업 상태 기록 | 구조화된 상태는 JSON, 진행 메모는 자유 텍스트, 이력은 git | Claude 공식 권장 |
| AI에게 주는 웹 페이지 — 내용을 뽑을 때 | 보이는 텍스트를 MD로. 접힌 섹션은 출처와 함께 따로 | 원본 HTML은 약 97%가 마크업이고, 잘라 넣으면 접힌 정보가 통째로 빠진다. 잡음은 프롬프트보다 코드로 거른다 |
| AI에게 주는 웹 페이지 — 강한 모델이 페이지를 조작할 때 | HTML 유지 | 강한 모델은 레이아웃 정보를 버튼 위치 판단에 써서 압축 표현보다 최대 17.5%p 나았다. 약한 모델은 반대였다 |
| 사람이 쓰고 고치는 설계 문서, 결정 기록, 계약서 | MD (+ Mermaid) | diff, 공동 편집, 리뷰가 쉽다. 흐름도·시퀀스 같은 단순한 다이어그램은 Mermaid로 충분하다 |
| PR 설명 | MD | GitHub가 렌더링한다. 크거나 낯선 PR만 HTML 설명 페이지를 따로 붙인다(3절을 지킨다) |
| 여러 안 비교, 아키텍처 설명, 리서치 보고서, 코드 흐름 설명 | 원본(MD)에서 만든 HTML 뷰 | 나란히 비교, SVG 다이어그램, 색으로 구분한 diff는 MD로 흉내 내기 어렵다. 다만 그림이냐 글이냐보다 **어떤 수준의 정보를 보여주느냐**가 이해를 좌우했다 |
| 티켓 정렬, 파라미터 조정, 데이터 라벨링, 프롬프트 튜닝 | export 버튼이 달린 인터랙티브 HTML | 글로 설명하기 어려운 선택을 사람이 직접 하게 한다. HTML이 가장 확실하게 나은 경우다 |
| 이메일 본문 | MD나 일반 텍스트(필요하면 제한된 HTML로 변환) | 이메일 클라이언트는 CSS를 대부분 지운다 |
| 짧은 메모, TODO, 일일 로그 | MD | HTML로 만들 이유가 없다 |

## 3. 검토 화면(HTML 뷰)을 만들 때 지킬 것

**원본과 구조**
- **원본이 아니라 뷰다.** 뷰와 원본이 다르면 원본이 맞다. 뷰를 직접 고치지 말고 원본을 고친 뒤 다시 만든다. 뷰에 원본 파일과 날짜(또는 커밋)를 적는다.
- **맨 위에는 AI의 결론이 아니라 사람이 할 일을 둔다.** 결정해야 할 항목, 확인된 것과 확인되지 않은 것, 이 화면이 다루지 않은 것을 먼저 보여준다. 소제목은 그 섹션 내용을 요약하게 쓴다. MD에도 똑같이 적용된다.
- **짧게.** 상위 요약이 긴 상세 자료보다 이해를 도왔고, 과도한 문서는 오히려 이해를 방해했다.

**사람이 판단하게 만들기**
- **AI 계획에는 "이 계획의 가정" 섹션을 두고 사람이 하나씩 확인하게 한다.** AI가 만든 계획을 검토할 때 가정을 찾게 하자 과신이 가장 많이 줄었고 부담은 늘지 않았다.
- **가능하면 AI 추천보다 사람의 판단을 먼저 받는다.** 억지로 생각하게 만드는 설계가 단순 설명보다 과신을 크게 줄였다. 대신 가장 인기가 없었으니 중요한 결정에만 쓴다.
- **고른 결과는 export한다.** JSON·MD·프롬프트로 복사해 에이전트에게 돌려준다.

**설명과 표시 방식**
- **설명을 더 붙이는 것으로 검토가 나아지지 않는다.** AI 설명은 맞든 틀리든 수용만 늘렸다. 설명이 과신을 줄인 건 검증 비용을 낮출 때뿐이었다. 주장마다 근거(코드 줄, 출처 링크)로 바로 가서 하나씩 확인할 수 있게 한다.
- **AI가 만든 부분과 사람이 확인한 부분을 나눠 표시한다.** 주장마다 "검증됨/미검증"이나 신뢰도를 붙이고, 해결되지 않은 불확실성을 드러낸다. 항목별 신뢰도 표시는 적절한 의존을 늘렸다.
- **AI의 조언을 가장 눈에 띄게 두지 않는다.** 눈에 띄게 보여준 조언은 틀려도 더 따랐고, 세부 정보가 지나치게 많으면 덜 신중해졌다. "이렇게 하라"는 권고보다 판단에 필요한 정보를 보여준다.
- **보기 좋은 것과 맞는 것을 구분한다.** 깔끔한 화면, 정돈된 PR 설명은 품질 신호가 아니다. 도구가 템플릿으로 찍어 내는 경우가 많다.

**누락**
- **"이 화면이 다루지 않은 것"을 꼭 적는다.** AI가 짚어 준 곳만 보게 되기 쉽고, AI가 놓친 것은 숙련자도 그대로 따라갔다. 중요한 변경은 원본 diff로 직접 확인한다.

**만들 때**
- **필요할 때만 만든다.** HTML은 생성 시간과 토큰이 더 든다. 사람이 실제로 보고 판단할 산출물에만 쓴다.
- **여러 뷰를 만들면 CSS를 공용 파일로 뺀다.** HTML 토큰의 절반 가까이가 CSS다.
- **오픈 모델이면 내용을 먼저 쓰게 한다.** 오픈 모델은 형식 지시만으로 추론이 떨어졌고, 내용과 서식을 나누면 대부분 회복됐다. 최신 비공개 모델(Claude 등)에서는 이 손실이 거의 없었다.

## 4. 비용

두 가지로 직접 쟀다. (1) Thariq가 공개한 Claude Code 생성 예제 HTML 31개를 o200k 토크나이저로 셌다(Claude 토크나이저는 비공개라 근사). (2) 같은 원본(지침 3절, 약 800토큰)을 주고 Opus 5.5 하위 에이전트에게 "MD 문서로"와 "독립형 HTML 파일로"를 각각 3번씩 쓰게 해 걸린 시간과 사용량 기록의 토큰을 비교했다(2026-11-15).

| 비교 | 결과 |
|---|---|
| 문서형 HTML(보고서, 계획, 설명, PR 정리) 대 같은 내용의 MD 근사치 (예제 31개) | 약 4~7배 |
| HTML 토큰 구성 (예제 31개) | CSS 44~47%, JS 12~13%, SVG 2~8%, 화면에 보이는 글 11~14% |
| 생성 시간 (직접 생성 3회씩) | MD 평균 21.8초, HTML 평균 75.7초, 약 3.5배 |
| Claude 사용 토큰 차이 (직접 생성 3회씩) | HTML이 문서 하나당 약 7,300토큰 더 |
| 결과 파일 크기 (직접 생성, o200k) | HTML이 MD의 약 4.1~5.2배 |
| 에이전트가 만든 HTML에서 CSS·JS를 뺀 것 | 여전히 MD의 약 2.1~2.8배 |
| 같은 MD를 꾸밈 없는 HTML로 기계 변환 | 1.2배 |

- 비용의 절반 가까이는 CSS·JS다. 에이전트에게 HTML을 넘겨야 하면 `<style>`·`<script>`를 빼고 넘긴다. 그래도 에이전트가 만든 HTML은 카드·라벨·클래스 같은 구조가 붙어 MD의 2~3배가 남는다. 원본 MD가 있으면 MD를 넘긴다.
- 생성 시간은 Thariq가 말한 "2~4배"의 위쪽이었다. 두 조건 모두 에이전트 시작 같은 고정 시간이 들어 있어 순수 생성 배율은 이보다 크다.
- 문서 하나가 4천~8천 토큰이라 한 번 넘기는 비용은 작다. 매번 로드되는 파일에서는 4~7배가 그대로 쌓인다.
- MD도 일반 텍스트보다 약 26% 더 든다(Eliav 2026).
- 직접 생성 측정의 한계: 조건마다 3회, 내용 하나(한국어), 모델 하나. 6개를 동시에 돌려 서버 부하가 시간에 섞였을 수 있다. 사용량 기록은 입력·출력을 나누지 않아 출력 토큰은 차이로 추정했다.

## 5. 공유와 보안

- 내부 정보나 개인정보가 든 HTML은 공개 호스팅(GitHub Pages, 공개 S3 등)에 올리지 않는다. 접근 제한이 있는 곳(비공개 아티팩트 링크 등)을 쓴다.
- 남이 만든 HTML은 JS가 실행되므로 코드처럼 다룬다.
- 에이전트에게 HTML을 읽힐 때는 숨긴 텍스트에 지시문이 들어 있을 수 있다. 텍스트나 MD로 바꾼 뒤 넘긴다.
- MD도 채팅 화면에서 렌더링되면 이미지 링크로 데이터가 새어 나갈 수 있다. 출처를 모르는 MD를 그대로 렌더링하지 않는다.

## 6. 양쪽 주장 검토

### HTML 쪽 주장 (Thariq 원문 기준)

| 주장 | 판정 | 근거 |
|---|---|---|
| 100줄 넘는 MD는 읽기 어렵다 | 부분적으로 맞다. 원인은 형식보다 길이와 구조다 | 사람은 웹 페이지 단어의 20~28%만 읽는다(Nielsen 2008). 레이아웃을 개선해도 읽기 속도와 이해도는 그대로였고 만족도와 피로감만 나아졌다(Chaparro 외 2005). 엔지니어 744명은 모두 "맨 앞 요약 + 섹션 요약 아래 상세"를 골랐고 그 순서로 읽었다(Silyn-Roberts 2002). 이 구조는 MD로도 된다 |
| 정보 밀도가 높다 | 맞다. 다이어그램, 나란히 비교, 색 구분 diff에서 | 단순한 다이어그램은 Mermaid로도 된다. 프로그램 이해 실험에서 글이냐 그림이냐는 차이가 없었고 정보의 수준이 차이를 만들었다(Shneiderman 외 1982, 학생 51·32명) |
| 공유가 쉽다 | 호스팅한 링크일 때만, 받는 사람에 따라 다르다 | Thariq 본인도 Slack으로 HTML 파일을 보내면 클릭률이 "끔찍하다"고 했다. 공개 호스팅에 올렸다가 고객 데이터가 노출된 사례가 HN에서 보고됐다 |
| HTML을 쓰면 루프 안에 있다고 느낀다 | 느낌은 측정이 아니다. 판단을 요구하는 인터랙션이 있을 때만 근거가 있다 | AI 설명은 맞든 틀리든 수용만 늘렸다(Bansal 외, CHI 2021). 질 낮은 설명은 정확도를 떨어뜨리면서 확신은 높였다(Kaufman 2026). 리뷰어는 LLM이 가리킨 곳에 집중했다(Tufano 외). 반대로 사람이 먼저 판단하거나 가정을 찾게 하면 과신이 줄었다(Buçinca 외, CSCW 2021; 2601.18033) |
| 직접 편집을 안 하니 MD의 편집 장점은 덜 중요하다 | 틀렸다 | 원본을 사람이 못 고치면 공동 작성이 끊긴다(HN, Miessler) |
| 1M 컨텍스트에서는 늘어난 토큰이 체감되지 않는다 | 한 번 넘기는 자료에만 맞다 | 직접 측정에서 문서형 HTML은 MD의 약 4~7배였다. 매번 로드되는 파일은 세션 수만큼 쌓인다 |
| 생성이 2~4배 오래 걸려도 그만한 가치가 있다 | 사람이 보는 일회성 산출물에서만 맞다 | 직접 측정에서 HTML 생성은 MD의 약 3.5배 걸렸고 문서 하나당 Claude 토큰이 약 7,300개 더 들었다. 버전 관리가 가장 큰 단점이라는 것도 본인이 인정했다 |

### MD 쪽 주장

| 주장 | 판정 | 근거 |
|---|---|---|
| AI는 MD를 가장 잘 이해한다 | 근거 없다. 다만 문서 입력에서는 MD·텍스트가 안정적이었다 | 통제 실험에서 MD가 일반 텍스트보다 안정적으로 낫지 않았다(Eliav 2026). 형식에 따라 GPT-3.5 점수가 최대 40% 달라졌다(He 외 2024). 의미 없는 서식 차이로 최대 76%p 벌어졌고 형식별 성능은 모델 사이에 거의 상관이 없었다(Sclar 외, ICLR 2024). 문서 파일 실험에서는 MD·TXT가 JSON·CSV보다 안정적이었다(Not as Sweet, 2026) |
| `#` 계층이 어텐션 가중치로 Lost in the Middle을 줄인다 | 근거 없다 | 이런 메커니즘을 보인 연구를 찾지 못했다. 효과가 있었던 건 조각마다 제목 경로를 붙이는 것이었다(MD 대 PDF RAG) |
| HTML은 AI에게 나쁘다 | 틀렸다 | 정리한 HTML이 RAG에서 일반 텍스트보다 나았다(HtmlRAG, WWW 2025). 표에서는 HTML이 대체로 가장 견고했다(TABVERSE). 강한 모델은 페이지를 조작할 때 HTML이 나았다(Read More, Think More). 원본 HTML을 정리 없이 넣는 게 나쁘다 |
| 토큰 효율이 좋다 | 맞다 | 직접 측정에서 문서형 HTML의 약 1/4~1/7. 차이의 대부분은 CSS·JS다 |
| diff와 버전 관리가 깔끔하다 | 맞다 | 양쪽 모두 인정한다 |
| 학습 데이터에 MD가 많다 | 확인할 수 없다 | 웹 HTML도 학습 데이터에 매우 많다 |

### 양쪽이 다 놓친 것

- **형식보다 구조.** 사람에게는 요약 먼저·섹션 요약·상세 순서가, AI에게는 제목 경로·온전한 표·구역 구분이 효과를 냈다. 둘 다 형식과 상관없이 된다.
- **설명보다 판단.** 검토 품질을 올린 건 더 많은 설명이 아니라 사람이 가정을 확인하고 먼저 판단하게 만드는 장치였다.
- **문장 자체를 읽기 쉽게.** Karpathy는 ASD-STE100(항공 정비 문서용 통제 언어)에 가깝게 쓰게 하면 읽기 쉬워진다고 했다.
- **정답 형식은 모델과 흐름마다 다르다.** 정확도가 중요한 파이프라인이면 쓰는 모델로 직접 비교한다.

## 7. 확인하지 못한 것

- 예제 HTML 토큰 측정은 o200k 근사이고, MD 근사치는 HTML에서 변환해 만들었다. 직접 생성 측정은 조건마다 3회뿐이다(4절).
- HTML 계획을 에이전트에게 넘겼을 때 구현·검증 품질이 달라지는지 측정한 연구를 찾지 못했다.
- 초록까지만 본 논문: Narvekar 외(JSON·YAML·텍스트), Duggan & Payne 2009, DeStefano & LeFevre 2007, Silyn-Roberts 1999, Kücking 외 2026, Parasuraman & Riley 1997, Lee & See 2004, Buçinca 외 2021, Bansal 외 2021, Vasconcelos 외 2023. 유료이거나 본문을 열지 못했다.
- 인지 강제 실험(2601.18033)은 글쓰기 과제다. 코딩 계획 검토에도 같은지는 모른다.
- 표 형식 연구(Sui 외)는 GPT-3.5·GPT-4 시절 결과다.

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

### Claude 공식 문서
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) (XML 태그, 긴 자료 배치, 출력 형식, 상태 기록)
- [How Claude remembers your project](https://code.claude.com/docs/en/claude-md) (CLAUDE.md 작성법)

### LLM 쪽 연구
- He 외, [Does Prompt Formatting Have Any Impact on LLM Performance?](https://arxiv.org/abs/2411.10541) (2024)
- Sclar 외, [Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design](https://arxiv.org/abs/2310.11324) (ICLR 2024)
- Voronov 외, [Mind Your Format](https://arxiv.org/abs/2401.06766) (ACL 2024 Findings)
- Eliav, [Prompt Design at Scale](https://arxiv.org/abs/2607.19257) (2026, 동료 심사 전)
- Lee 외, [The Format Tax](https://arxiv.org/abs/2604.03616) (2026)
- [Not as Sweet by Another Name: Format Robustness in LLM Document Workflows](https://arxiv.org/abs/2607.27648) (2026, ACM)
- Tan 외, [HtmlRAG](https://arxiv.org/abs/2411.02959) (WWW 2025)
- Kumar, [Is Markdown Better Than PDF for RAG?](https://zenodo.org/search?q=%22Is%20Markdown%20Better%20Than%20PDF%22) (2026, Zenodo 프리프린트)
- Why HTML-to-LLM Scraping Fails: A Production Analysis (2026, Liner 풀 텍스트로 확인)
- Sui 외, [Table Meets LLM](https://arxiv.org/abs/2305.13062) (WSDM 2024)
- Ahsan 외, [TABVERSE](https://arxiv.org/abs/2606.09578) (2026, 심사 중)
- Oh 외, [Talking with Tables](https://arxiv.org/abs/2412.17189) (2024)
- Enomoto 외, [Read More, Think More](https://arxiv.org/abs/2604.01535) (2026)
- Greshake 외, [Not what you've signed up for: indirect prompt injection](https://arxiv.org/abs/2302.12173) (2023)

### 사람 쪽 연구
- Nielsen, [How Little Do Users Read?](https://www.nngroup.com/articles/how-little-do-users-read/) (2008)
- Pernice, [The Layer-Cake Pattern of Scanning Content on the Web](https://www.nngroup.com/articles/layer-cake-pattern-scanning/) (NN/g 2019)
- Silyn-Roberts, [Document Structure and Its Effect on Engineers' Reading Strategies](https://ascelibrary.com/doi/10.1061/%28ASCE%291052-3928%282002%29128%3A3%28115%29) (2002)
- Chaparro, Shaikh, Baker, [Reading Online Text With a Poor Layout: Is Performance Worse?](https://portfolio.erau.edu/en/publications/reading-online-text-with-a-poor-layout-is-performance-worse/) (Usability News 2005)
- Shneiderman 외, [Control Flow and Data Structure Documentation: Two Experiments](https://www.cs.umd.edu/users/ben/papers/Shneiderman1982Control.pdf) (CACM 1982)
- Dyson, How physical text layout affects reading from screen (Behaviour & IT 2004)
- Fogg 외, Stanford Web Credibility Project ([요약](https://en.wikipedia.org/wiki/Stanford_Web_Credibility_Project))

### 자동화 편향과 AI 검토 연구
- Goddard 외, [Automation bias: a systematic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/) (JAMIA 2012)
- Dratsch 외, Automation Bias in Mammography (Radiology 2023, Liner 풀 텍스트로 확인)
- Perry 외, [Do Users Write More Insecure Code with AI Assistants?](https://arxiv.org/abs/2211.03622) (CCS 2023)
- Kaufman, [Programmers Are Poor and Overconfident Judges of LLM-Generated Assertions](https://arxiv.org/abs/2607.08885) (2026)
- Tufano 외, [Deep Learning-based Code Reviews](https://arxiv.org/abs/2411.11401) (2024)
- Lu, A study of AI usage in GitHub pull requests (UVic 석사 논문 2026, Liner 풀 텍스트로 확인)
- Rahman 외, Plausible Is Not Enough: Trust and Evidence in AI-Authored Pull Request Review (2026, arXiv판을 Liner 풀 텍스트로 확인)
- Bansal 외, [Does the Whole Exceed its Parts?](https://arxiv.org/abs/2006.14779) (CHI 2021)
- Buçinca 외, [To Trust or to Think](https://arxiv.org/abs/2102.09692) (CSCW 2021)
- Vasconcelos 외, [Explanations Can Reduce Overreliance on AI Systems During Decision-Making](https://arxiv.org/abs/2212.06823) (CSCW 2023)
- [An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing](https://arxiv.org/abs/2601.18033) (2026)
- 논문 탐색에 쓴 Liner Scholar 스레드: https://scholar.liner.com/ko/threads/01a1dcb3-809e-76e0-990d-e07d2f2cdd4e
