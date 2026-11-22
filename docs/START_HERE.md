# Start contributing to Sparks Vision

**Welcome.** This is the public open-source contribution area for Sparks Vision. It is not the private Windows control engine and does not provide access to any person's computer.

**Fastest path:** Pick one of the tasks below, comment on the issue with what you plan to do, fork this repository, and submit a small pull request. A maintainer reviews contributions before they are merged. No invitation, paid account, team membership, or access token is required to open a public pull request.

## Choose your first task

| Task | Good fit for | Deliverable |
| --- | --- | --- |
| [#1: Review website navigation accessibility](https://github.com/SparksCrop/sparks-vision-community/issues/1) | Designers, accessibility testers | Reproducible desktop/mobile checklist using public-only content |
| [#2: Improve the contributor quickstart](https://github.com/SparksCrop/sparks-vision-community/issues/2) | First-time contributors, technical writers | Improve this guide with clear, verified first-PR instructions |
| [#3: Propose a mock MCP integration](https://github.com/SparksCrop/sparks-vision-community/issues/3) | AI/integration developers | A test-only tool contract with synthetic inputs and outputs |
| [#4: Propose public plugin and UI ideas](https://github.com/SparksCrop/sparks-vision-community/issues/4) | Developers, product designers | A scoped public-safe proposal without private product code |

These issues are **proposals**, not a promise of assignment or acceptance. Discuss larger work with a maintainer before implementing it.

## Your first pull request

1. Sign in to GitHub and read [CONTRIBUTING.md](../CONTRIBUTING.md), [SECURITY.md](../SECURITY.md), and the [public/commercial feature boundaries](FEATURE_BOUNDARIES.md).
2. Find an [open issue](https://github.com/SparksCrop/sparks-vision-community/issues). Leave a short comment with your proposed deliverable and how you will test it. You do **not** need permission to fork.
3. Select **Fork** on the repository page. Clone your own fork locally, or edit a Markdown file directly through GitHub.
4. Create a short branch, such as docs/clarify-quickstart. Work only with public files, invented examples, and synthetic test data.
5. Check local documentation links with python3 scripts/check_docs.py when that script is present on your branch. If it is not present, verify every edited link manually.
6. Commit and push to your fork. Open a pull request against SparksCrop/sparks-vision-community → main, linking the issue.
7. Fill in the pull request template: responsible human, use of AI tools, tests performed, license/attribution, risks, and rollback. Respond to maintainer review.

**If this is your first GitHub PR:** You can also click the pencil icon on a public Markdown file in your fork to make a small proposed docs change, then follow GitHub's prompt to create a pull request.

## Safety and scope

- Never upload real credentials, API keys, browser profiles, customer information, personal desktop captures, or private Sparks Vision code.
- Do not test live devices, accounts, or real AI-chat connectors as part of public exercises. Use fixtures and mocked data only.
- Do not claim ChatGPT, Claude, Codex, Manus, billing, or device control is production-ready without verified compatibility evidence.
- AI-assisted contributions are welcome, but a human must review the output and disclose what was actually checked.
- Public submissions are subject to this repository's [MIT license](../LICENSE). Trademarks and private commercial code remain separate.
- Report security concerns privately using [SECURITY.md](../SECURITY.md), **not** public issues.

## How work gets reviewed

Maintainers review relevance, license, security, privacy, tests, accessibility, and whether work belongs in the public repository. A draft or submitted PR is not automatically approved. Contributions may need changes before merge.

For the proposed workflow and development environments, see the [team development guide](TEAM_DEVELOPMENT_GUIDE.md). For the product's planned public roadmap, see [ROADMAP.md](ROADMAP.md).
