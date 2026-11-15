# 참고 자료

이 저장소의 작업에 쓴 자료 전체다. 지침 본문의 "출처"에 있는 것과 함께, 조사·검증 과정에서 보고 지침에는 인용하지 않은 것도 적었다.

**확인 수준**은 다음 넷으로 나눈다.
- 본문: arXiv·공개 저장소 본문을 직접 읽음.
- Liner 풀 텍스트: Liner Scholar가 본문을 읽고 요약한 것을 봄.
- 초록: 초록이나 서지 정보만 봄.
- 검색 요약: 검색 결과 요약으로만 봄.
- 본문·Liner(v1 기준): v1은 초록만 본 논문을 따로 표시했고 이 자료는 그 목록에 없다. 본문이나 Liner 풀 텍스트로 봤지만 어느 쪽인지 기록이 없다.

**쓰인 곳**은 지침(`md-html-guidelines.md`)의 절 번호다.

## 원 논쟁과 반응

| 자료 | 확인 | 쓰인 곳 |
|---|---|---|
| Thariq Shihipar, [Using Claude Code: The Unreasonable Effectiveness of HTML](https://x.com/trq212/status/2052809885763747935) (X, 2026-05-09) | 본문 | 1·4·6절 |
| Thariq Shihipar, 예제 [thariqs.github.io/html-effectiveness](https://thariqs.github.io/html-effectiveness), [저장소](https://github.com/thariqs/html-effectiveness) (측정 대상 커밋 `1787245`) | 본문 | 4절 측정 1 |
| Thariq Shihipar, Slack으로 보낸 HTML 파일 클릭률에 관한 글 ([X 검색](https://x.com/search?q=from%3Atrq212%20html&f=live), 개별 글 URL 미기록) | 본문 | 6절 |
| Andrej Karpathy, [HTML 출력 권장과 형식 발전 단계](https://x.com/karpathy/status/2053872850101285137) (2026-05-12) | 본문 | 6절 |
| Andrej Karpathy, [LLM 출력 이해 팁](https://x.com/karpathy/status/2105819303471976479) (2026-10-02) | 본문 | 6절 |
| Angie Jones, 출력은 HTML·입력은 MD (Thariq 원문 [인용 글 목록](https://x.com/trq212/status/2052809885763747935/quotes)에서 확인) | 본문 | 6절 |
| Kent Langley, HTML·MD 이중 형식 규칙 (같은 인용 글 목록에서 확인, 개별 URL 미기록) | 본문 | 인용 안 함 |
| Simon Willison, [링크 글](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/) (2026-05-08) | 본문 | 서두 |
| Daniel Miessler, [Text is Thought, and Thought is Holy](https://danielmiessler.com/blog/text-is-thought-holy) | 본문 | 6절 |
| 박재홍, [LLM 시대, 마크다운 대신 HTML을 쓰라고?](https://wikidocs.net/blog/@jaehong/13111/) (HN 토론 정리) | 본문 | 6절 |
| Carrot Yoon, [md와 html 형식에 대한 생각](https://yooncarrot.com/article/69) | 본문 | 출발점 |
| AX Engineer Lukas, [AG 시대 MD 보다 HTML](https://brunch.co.kr/@lukas08/208) | 본문 | 출발점 |
| InfoQ Japan, [Anthropic リード: HTML が有効に](https://www.infoq.com/jp/news/2026/07/anthropic-html-markdown-agent/) | 검색 요약 | 서두 |
| ifanr, [Markdown 已死，HTML 当立？](https://www.ifanr.com/1665516) | 검색 요약 | 서두 |
| 数位时代, [Markdown過時了?](https://www.bnext.com.tw/article/90893/) | 검색 요약 | 서두 |
| Cloudflare, [에이전트를 위한 Markdown 소개](https://blog.cloudflare.com/ko-kr/markdown-for-agents/) | 본문 | 서두 |

## 공식 문서

| 자료 | 확인 | 쓰인 곳 |
|---|---|---|
| Claude, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | 본문 | 2절 |
| Claude Code, [How Claude remembers your project](https://code.claude.com/docs/en/claude-md) | 본문 | 2절 |
| Slack, [Format your messages in Slack](https://slack.com/help/articles/202288908-Format-your-messages) | 본문 | 1절 |

## LLM 쪽 연구

| 자료 | 확인 | 쓰인 곳 |
|---|---|---|
| He 외, [Does Prompt Formatting Have Any Impact on LLM Performance?](https://arxiv.org/abs/2411.10541) (2024) | 본문 | 6·7절 |
| Sclar 외, [Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design](https://arxiv.org/abs/2310.11324) (ICLR 2024) | 본문·Liner(v1 기준) | 6·7절 |
| Voronov 외, [Mind Your Format](https://arxiv.org/abs/2401.06766) (ACL 2024 Findings) | 본문·Liner(v1 기준) | 지침 출처 |
| Eliav, [Prompt Design at Scale](https://arxiv.org/abs/2607.19257) (2026, 동료 심사 전) | 본문 | 4·6절 |
| Lee 외, [The Format Tax](https://arxiv.org/abs/2604.03616) (2026) | 본문·Liner(v1 기준) | 3절 |
| Zhang 외, [Not as Sweet by Another Name: An Empirical Study of Format Robustness in LLM Document Workflows](https://arxiv.org/abs/2607.27648) (ASE 2026) | 본문 | 2·6절 |
| Narvekar, Mukherjee, Tanuwijaya, Evaluating the Impact of Input Format on LLM Performance: JSON vs. YAML vs. Text (IEEE FMLDS 2025, pp. 572–577), [doi:10.1109/FMLDS67896.2025.00072](https://doi.org/10.1109/fmlds67896.2025.00072) | 초록 | 7절 |
| Long 외, [LLMs Are Biased Towards Output Formats! Systematically Evaluating and Mitigating Output Format Bias of LLMs](https://arxiv.org/abs/2408.08656) (2024) | 초록 | 인용 안 함 |
| Tan 외, [HtmlRAG](https://arxiv.org/abs/2411.02959) (WWW 2025) | 본문 | 2·6절 |
| Kumar, [Is Markdown Better Than PDF for Retrieval-Augmented Generation? A Controlled Paired-Format Benchmark](https://zenodo.org/records/21829016) (2026, Zenodo 프리프린트, doi:10.5281/zenodo.21829016) | Liner 풀 텍스트 | 2·6절 |
| Why HTML-to-LLM Scraping Fails: A Production Analysis (2026, 원문 URL 미기록) | Liner 풀 텍스트 | 2절 |
| Sui 외, [Table Meets LLM](https://arxiv.org/abs/2305.13062) (WSDM 2024), [본문 v5](https://arxiv.org/html/2305.13062v5) 표 2 | 본문 | 2·7절 |
| Ahsan 외, [TABVERSE](https://arxiv.org/abs/2606.09578) (2026, 심사 중) | 초록 | 2·6·7절 |
| Oh 외, [Talking with Tables](https://arxiv.org/abs/2412.17189) (2024) | 본문 | 2절 |
| Enomoto 외, [Read More, Think More](https://arxiv.org/abs/2604.01535) (2026) | 본문 | 2·6절 |
| Greshake 외, [Not what you've signed up for: indirect prompt injection](https://arxiv.org/abs/2302.12173) (2023) | 본문·Liner(v1 기준) | 2절 |

## 사람 쪽 연구

| 자료 | 확인 | 쓰인 곳 |
|---|---|---|
| Nielsen, [How Little Do Users Read?](https://www.nngroup.com/articles/how-little-do-users-read/) (2008) | 본문·Liner(v1 기준) | 6절 |
| Pernice, [The Layer-Cake Pattern of Scanning Content on the Web](https://www.nngroup.com/articles/layer-cake-pattern-scanning/) (NN/g 2019) | 본문·Liner(v1 기준) | 지침 출처 |
| Silyn-Roberts, [Document Structure and Its Effect on Engineers' Reading Strategies](https://ascelibrary.com/doi/10.1061/%28ASCE%291052-3928%282002%29128%3A3%28115%29) (2002) | 본문·Liner(v1 기준) | 6절 |
| Silyn-Roberts, [Using Engineers' Characteristics to Improve Report Writing Instruction](https://doi.org/10.1061/%28ASCE%291052-3928%281998%29124%3A1%2812%29) (J. Prof. Issues Eng. Educ. Pract. 124(1), 1998, pp. 12–16) | 초록 | 7절 |
| Chaparro, Shaikh, Baker, [Reading Online Text With a Poor Layout: Is Performance Worse?](https://portfolio.erau.edu/en/publications/reading-online-text-with-a-poor-layout-is-performance-worse/) (Usability News 2005) | 본문·Liner(v1 기준) | 6절 |
| Duggan & Payne, [Text skimming: The process and effectiveness of foraging through text under time pressure](https://doi.org/10.1037/a0016995) (J. Exp. Psychol.: Applied 15(3), 2009, pp. 228–242; [저장소 페이지](https://researchportal.bath.ac.uk/en/publications/text-skimming-the-process-and-effectiveness-of-foraging-through-t/), 공개 사본 [CORE](https://core.ac.uk/download/161909638.pdf)) | 초록 | 7절 |
| DeStefano & LeFevre, [Cognitive load in hypertext reading: A review](https://doi.org/10.1016/j.chb.2005.08.012) (Computers in Human Behavior 23(3), 2007, pp. 1616–1641) | 초록 | 7절 |
| Shneiderman 외, [Control Flow and Data Structure Documentation: Two Experiments](https://www.cs.umd.edu/users/ben/papers/Shneiderman1982Control.pdf) (CACM 1982) | 본문 | 6절 |
| Dyson, [How physical text layout affects reading from screen](https://doi.org/10.1080/01449290410001715714) (Behaviour & Information Technology 23(6), 2004, pp. 377–393) | 본문·Liner(v1 기준) | 지침 출처 |
| Fogg 외, Stanford Web Credibility Project ([요약](https://en.wikipedia.org/wiki/Stanford_Web_Credibility_Project)) | 2차 요약(위키백과) | 지침 출처 |

## 자동화 편향과 AI 검토 연구

| 자료 | 확인 | 쓰인 곳 |
|---|---|---|
| Parasuraman & Riley, [Humans and Automation: Use, Misuse, Disuse, Abuse](https://doi.org/10.1518/001872097778543886) (Human Factors 39(2), 1997, pp. 230–253) | 초록 | 7절 |
| Lee & See, [Trust in Automation: Designing for Appropriate Reliance](https://doi.org/10.1518/hfes.46.1.50_30392) (Human Factors 46(1), 2004, pp. 50–80) | 초록 | 7절 |
| Goddard 외, [Automation bias: a systematic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/) (JAMIA 2012) | 본문 | 3절 |
| Dratsch 외, [Automation Bias in Mammography: The Impact of Artificial Intelligence BI-RADS Suggestions on Reader Performance](https://doi.org/10.1148/radiol.222176) (Radiology 307(4), 2023) | Liner 풀 텍스트 | 3절 |
| Kücking 외, [Impact of AI recommendation correctness on diagnostic accuracy in clinical decision-making](https://doi.org/10.1016/j.ijmedinf.2025.106223) (Int. J. Med. Inform. 207, 2026) | 초록 | 7절 |
| Perry 외, [Do Users Write More Insecure Code with AI Assistants?](https://arxiv.org/abs/2211.03622) (CCS 2023) | 본문·Liner(v1 기준) | 지침 출처 |
| Kaufman, [Programmers Are Poor and Overconfident Judges of LLM-Generated Assertions](https://arxiv.org/abs/2607.08885) (2026) | 본문 | 6절 |
| Tufano 외, [Deep Learning-based Code Reviews: A Paradigm Shift or a Double-Edged Sword?](https://arxiv.org/abs/2411.11401) (2024) | 본문·Liner(v1 기준) | 6절 |
| Lu, [A study of AI usage in GitHub pull requests](https://hdl.handle.net/1828/24150) (UVic Master's Project 2026) | Liner 풀 텍스트 | 3절 |
| Rahman 외, [Plausible Is Not Enough: Trust and Evidence in AI-Authored Pull Request Review](https://arxiv.org/abs/2610.21144) (2026) | Liner 풀 텍스트 | 3절 |
| Bansal 외, [Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance](https://arxiv.org/abs/2006.14779) (CHI 2021) | 본문 일부(1~3쪽) | 3·6절 |
| Buçinca, Malaya, Gajos, [To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making](https://arxiv.org/abs/2102.09692) (CSCW 2021) | 본문 일부(1~12쪽) | 3·6절 |
| Vasconcelos 외, [Explanations Can Reduce Overreliance on AI Systems During Decision-Making](https://arxiv.org/abs/2212.06823) (CSCW 2023) | 본문 일부(1~2쪽) | 3절 |
| Ghosh, Sarkar, Lindley, Poelitz, [An Experimental Comparison of Cognitive Forcing Functions for Execution Plans in AI-Assisted Writing](https://arxiv.org/abs/2601.18033) (2026) | 본문 | 3·6절 |
| Zhang, Liao, Bellamy, Effect of Confidence and Explanation on Accuracy and Trust Calibration in AI-Assisted Decision Making (FAT* 2020, arXiv:2001.02114) | 확인 안 함 | 인용 안 함. 2차 검토자가 제시 |

## 도구, 서비스, 검증에 쓴 곳

| 자료 | 쓰인 곳 |
|---|---|
| [Liner Scholar 검색 스레드](https://scholar.liner.com/ko/threads/01a1dcb3-809e-76e0-990d-e07d2f2cdd4e) | 논문 탐색, 풀 텍스트 요약 |
| [Liner Scholar: Full Papers via Library](https://chromewebstore.google.com/detail/liner-scholar-full-papers/pfbbgdacaanipbeaceppbaojacefeiea) (Chrome 확장) | 풀 텍스트 모드 |
| ExtScope, 확장 권한 분석: [Liner: AI Copilot](https://extscope.org/extension/bmhcbmnbenmcecpmpepghooflbehcack), [Liner Scholar](https://extscope.org/extension/pfbbgdacaanipbeaceppbaojacefeiea) | 확장 설치 전 권한 확인 |
| [tiktoken](https://github.com/openai/tiktoken) (`o200k_base`) | 4절 토큰 측정 |
| [Python-Markdown](https://python-markdown.github.io/) (`tables` 확장) | 4절 기계 변환 측정 |
| [Crossref REST API](https://api.crossref.org/) | 서지·DOI 확인 |
| [arXiv API](https://info.arxiv.org/help/api/index.html) | 논문 검색, Rahman 외 링크 확인 |
| [Zenodo API](https://developers.zenodo.org/) | Kumar 레코드 확인 |
| [UVic DSpace](https://dspace.library.uvic.ca/handle/1828/24150) | Lu 저장소 확인 |
| [GitHub REST API](https://docs.github.com/en/rest) | 예제 저장소 파일 받기(`measurement/scripts/fetch.py`), 커밋 이력 확인 |
| screenshotrender.com [블로그](https://screenshotrender.com/blog) | 3차 검토 옵션 B 확인. 해당 제목 없음 |
