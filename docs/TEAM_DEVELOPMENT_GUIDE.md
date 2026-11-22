# Sparks Vision Community — developer workflow and environments

**Status:** Proposed. This guide describes how collaboration should work; it does not imply that the board, previews, CI, or customer deployment are already active.

## One shared headquarters
- **GitHub Issues:** Every change starts with one public, scoped issue and acceptance criteria.
- **GitHub Projects (planned):** One board with Backlog → Ready → In Progress → Review → QA → Done. Track owner, priority, component, preview, check status, and blocker.
- **GitHub Discussions:** Asynchronous proposals, design reviews, announcements, and contributor questions. Do not post personal data or security disclosures.
- **Discord (optional):** Fast community chat. Decisions, requirements, and accepted designs must be summarized back in GitHub so they are searchable.
- **VS Code (optional):** An individual code editor, not the shared project dashboard. Other editors are welcome.

## Standard workflow — humans with or without AI
1. Find or open an issue; agree on scope, owner, acceptance criteria, and public-safe test data.
2. Fork the public repository and create `feature/`, `fix/`, or `docs/` branch.
3. Make a small, focused change using local fixtures; never request remote access to another contributor's PC.
4. Run the documented checks relevant to the change and collect synthetic/public-only evidence.
5. Open a PR referencing the issue, with the responsible human, AI-use disclosure, tests, screenshots (if safe), risk, and rollback.
6. Maintainers review license compatibility, privacy, security, quality, accessibility, and public/commercial boundaries.
7. Merge only after checks and required review. Mark the task Done and document visible behavior changes.
8. If the work needs private code, stop and ask maintainers for a sanitized public interface or mock; do not move proprietary code into this repository.

## Visual development and testing
| Environment | Use | Permitted data |
| --- | --- | --- |
| Contributor local machine | Editor, live-reload samples, unit tests | Synthetic data only |
| Public PR checks (planned) | Lint, format, link and fixture validation | No device credentials or real desktop control |
| Website PR preview (planned) | Responsive visual and accessibility review | Static/demo content only |
| Private product staging | Owner-managed cross-component integration | Authorized test accounts, separate from public community |
| Production | Released customer website/app | Release owner approval and rollback plan |

A browser preview cannot validate native Windows control or a real ChatGPT host. Those need separate permissioned tests in the private product.

## Minimum maintainer checklist before accepting outside contributions
- Enable and verify repository rules: prohibit unreviewed direct pushes and require status checks on the default branch, where the account and GitHub plan support this.
- Verify what protections are actually enforced; `CODEOWNERS` and PR templates alone are not enforcement.
- Create public Project board and labels; publish a new-contributor starting issue and a list of maintainers.
- Configure safe CI with least-privilege tokens; don't expose secrets to forks or run untrusted PR code with production credentials.
- Add a public example plugin/fixture with documented tests and no PC or personal-account access.
- Keep billing, product engine, device pairing, production customer data, and release credentials out of this repository.
- For any real security issue, follow `SECURITY.md`, not a public issue.

## Release and update flow
Contributor PR → reviewed public component → versioned release note → private compatibility evaluation (if adopted) → gated staging → owner-approved product release.

**Ownership:** Volunteer contributions do not grant admin access, payment, employment, or rights to private code. Public repository contributions follow this repository's MIT license; trademarks remain separately controlled.

**Next owner decisions:** Set up Project board; confirm contributor reviewers; select a website preview provider after costs/access controls are reviewed.
