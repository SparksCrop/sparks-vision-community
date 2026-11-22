# Maintainer triage and release checklist

**Status:** Proposed operating procedure. This document is not a substitute for GitHub-enforced branch rules or required CI checks.

## New contributor response

For each new public issue or PR:

1. Confirm it belongs to the public repo. Move any request for private product code, credentials, device access, customer data, or commercial backend changes to a private owner-managed process without copying sensitive content into GitHub.
2. Categorize: docs, design/accessibility, mock integration, testing, or other. Mark whether a first-time contributor can safely work on it.
3. Ask for one deliverable, acceptance criteria, a test plan, and public-only fixtures.
4. Record a responsible human maintainer and planned reviewer. Do not grant direct Write access simply to accept a contribution.
5. Direct the contributor to [START_HERE.md](START_HERE.md) and [CONTRIBUTING.md](../CONTRIBUTING.md).
6. For PRs, review security, dependency licenses, attribution, clear AI disclosures, tests, and rollback. Enforced branch protection must be verified separately.
7. After human review and passing checks, an authorized maintainer merges; update linked issue and public release notes as appropriate.

## Proposed labels (create in repository settings)

- good first issue — small, well-scoped public task
- documentation — how-to material, onboarding, translations
- accessibility — keyboard, screen reader, contrast, reduced motion
- integration-mock — synthetic protocol or plugin examples
- design — public UI proposals and review
- needs-triage — awaiting maintainer scope review
- ready — accepted scope, safe to start
- in-review — pull request requires review
- blocked — cannot proceed; reason recorded
- security — only non-sensitive security process work; never public vulnerability details

These are **proposed**, not confirmed as created.

## Project board plan (not yet created)

Use one GitHub Project with Backlog → Ready → In Progress → Review → QA → Done. Track issue/PR link, owner, priority, component, acceptance criteria, and evidence. Keep the project public-safe; private commercial milestones belong in a restricted board.

**Until a GitHub Project actually exists:** Use the public [Issues](https://github.com/SparksCrop/sparks-vision-community/issues) and [Pull Requests](https://github.com/SparksCrop/sparks-vision-community/pulls) lists as the source of truth. Do not call the planned board live.

## Release gates

- Public contributions never receive production secrets or Windows device access.
- CI checks provide feedback, not a security guarantee.
- Required approvals and status checks are only enforced when repository rules are actually configured and tested.
- Never automatically deploy the commercial engine or trigger billing from a public PR.
- A public release must be explicitly reviewed for licenses, proprietary content, personal information, and unverified product claims.
