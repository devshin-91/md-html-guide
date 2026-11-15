# MD / HTML 사용 지침

AI 에이전트와 일할 때 Markdown과 HTML을 언제 쓸지 정리한 지침이다. 다국어 자료, 원 논쟁(Thariq Shihipar의 X 글과 반응), Claude 공식 문서, 논문 40여 편, 직접 측정을 근거로 썼다. 외부 AI 검토를 세 차례 받았다(49점 → 99점).

**한 줄 요약**: 매번 로드되는 파일과 사람이 고치는 원본은 MD, 사람이 한 번 보고 판단하는 화면은 원본에서 만든 HTML, 사람이 값을 고르는 일은 export 버튼이 달린 HTML.

## 파일

| 파일 | 내용 |
|---|---|
| [`md-html-guidelines.md`](md-html-guidelines.md) | 지침 최종본 |
| [`md-html-guidelines.v1.md`](md-html-guidelines.v1.md) | 외부 검토 전 판 |
| [`HISTORY.md`](HISTORY.md) | 작업 이력: 조사, 측정, 검토 3차례, 반영 |
| [`CONTRIBUTORS.md`](CONTRIBUTORS.md) | 사람, AI 작성자, 외부 검토자, 도구별 역할 |
| [`REFERENCES.md`](REFERENCES.md) | 참고 자료 전체와 확인 수준 |
| [`review-checklist.md`](review-checklist.md) | 결함 12개(C-1~m-3)를 어디서 어떻게 고쳤는지 |
| [`skill/md-html-format/`](skill/md-html-format/SKILL.md) | 지침을 Claude Code 스킬로 줄인 것 |
| [`measurement/`](measurement/) | 4절 측정 기록(`NOTES.md`), 스크립트, 생성 파일 |

## 스킬로 쓰기

`skill/md-html-format/SKILL.md`는 지침의 1~3절과 5절을 Claude Code 스킬로 줄인 것이다. 평소에는 스킬 목록의 설명 한 줄만 컨텍스트에 들어가고, 형식을 고르거나 HTML 보고서·검토 화면을 만들거나 에이전트에게 문서를 넘길 때 본문이 불린다. 근거가 필요하면 스킬이 `~/md-html-guide/md-html-guidelines.md`를 읽는다.

설치는 폴더를 개인 스킬 폴더로 복사한다.

```bash
cp -r skill/md-html-format ~/.claude/skills/
```

지침을 고치면 스킬의 요약 부분도 함께 고친다.

## 측정 재현

`measurement/NOTES.md`에 환경, 프롬프트 원문, 회차별 수치가 있다. Thariq의 예제 HTML은 이 저장소에 넣지 않았다. `measurement/scripts/fetch.py`로 [원 저장소](https://github.com/thariqs/html-effectiveness)에서 받는다. 측정 당시 대상은 커밋 `1787245`로 본다.

```bash
python measurement/scripts/fetch.py <받을 폴더>
python measurement/scripts/measure.py <받을 폴더> md-html-guidelines.v1.md
python measurement/scripts/gen_measure.py measurement/generated
```

필요한 패키지: `tiktoken`, `markdown`. `measure.py`의 두 번째 인자는 측정 당시 지침 파일이다. 당시 판은 v1 직전 판이라 기계 변환 수치(4,379 → 5,274토큰)는 v1로 재현하면 조금 다르게 나온다.

## 라이선스

이 저장소의 모든 내용(문서, 측정 스크립트, 생성 파일)은 [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)을 따른다. 전문은 [`LICENSE`](LICENSE)에 있다. 쓸 때는 출처(저작자 devshin-91, 이 저장소)를 표시한다.

인용한 논문·글·예제의 권리는 각 저작자에게 있다.
