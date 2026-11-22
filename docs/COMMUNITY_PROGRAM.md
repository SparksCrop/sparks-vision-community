# Sparks Vision — Open Contributor Program

**Status:** Community participation is open for proposals and reviewed public contributions. This program does **not** give volunteers access to the commercial Windows engine, production systems, customer accounts, or payment systems.

## Who may participate
Anyone may submit a public GitHub issue, propose an improvement, review documentation, test a synthetic demo, or fork this repository to submit a pull request. Developers, designers, testers, technical writers, accessibility reviewers, translators, and AI-assisted contributors are all welcome.

No employment, compensation, early product access, or maintainer status is implied. Contributors must have permission to submit all material and comply with the [MIT license](../LICENSE), [Code of Conduct](../CODE_OF_CONDUCT.md), [security policy](../SECURITY.md), and [contribution guide](../CONTRIBUTING.md).

## Contribution tracks
| Track | Appropriate first work | Not permitted in public submissions |
| --- | --- | --- |
| Docs and localization | Installation concepts, FAQs, glossaries, safe tutorials, translations | Customer logs and private product text |
| UI and accessibility | Mock screens, keyboard/screen-reader checks, responsive design examples | Customer captures or proprietary assets |
| Integrations | MCP contract examples, client setup walkthroughs, compatibility reports | Real device endpoints, secrets, access tokens |
| Testing | Synthetic fixtures, tests, reproduction steps on mock data | Personal files, credentials, real desktop recordings |
| Research and product | Clearly sourced feature proposals and platform limitations | Promises of unsupported commercial features |

**Need private implementation details?** First open an issue asking for a safe mock interface. Do not copy or expose private code.

## Step-by-step process
1. Start with an [existing issue](https://github.com/SparksCrop/sparks-vision-community/issues) or open a proposal. State the user problem, intended change, risks, and acceptance checks.
2. A maintainer marks a task ready before substantial implementation. Volunteer ideas may be discussed even if they are not accepted.
3. Fork the public repository and work in a small branch. Use test-only accounts and synthetic data.
4. Test the proposed change. For AI-assisted work, identify the tools used and describe what a human actually reviewed or verified.
5. Open a pull request using the template and link the issue. A responsible human must review the generated or hand-written change.
6. A maintainer checks code quality, licenses, privacy, safety, accessibility, and applicability to the public scope; requested changes are normal.
7. Only an authorized maintainer merges. Contributors do not require direct write permissions to participate.

## Contribution review and ownership
- Every public change requires maintainer review; do not treat review checkboxes or CODEOWNERS as enforced branch protection.
- The maintainer may reject, postpone, or request rework of a submission.
- Public code is licensed under MIT as stated in this repository. The Sparks Vision trademark, private engine, deployment credentials, and production services are not included.
- Use GitHub Discussions for broad questions once enabled; until then, use issues. Important decisions made in chat should be recorded in the relevant issue.
- Never post vulnerability details to public issues; use [SECURITY.md](../SECURITY.md).

## Maintainer launch checklist (not yet all complete)
- [x] Public repo, license, contribution guide, issue template, and starter issues.
- [ ] Verify enforced default-branch review and status-check rules before granting any outside collaborator Write access.
- [ ] Create a GitHub Project board: Backlog, Ready, In Progress, Review, QA, Done.
- [ ] Configure required CI for public examples with least-privilege GitHub Actions permissions.
- [ ] Enable or verify Discussions, announce participation rules, and assign volunteer-triage owners.
- [ ] Publish one tested, safe MCP mock example and a compatibility matrix based on actual host tests.
- [ ] Link the approved community area from the public website after website review.

*Open to contribution does not mean open access to the owner's PC or commercial backend.*
