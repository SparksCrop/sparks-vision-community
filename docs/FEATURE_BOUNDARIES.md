# Proposed public and commercial boundaries

This is a planning document, not a statement that every listed feature is already available. Only publicly reviewed, sanitized code may be migrated from the private product.

| Capability | Public community | Commercial product |
| --- | --- | --- |
| Documentation and tutorials | Public | Supported customer guides |
| Example MCP integrations and schemas | Public, using mock data | Private service integrations and authenticated production backend |
| Extension/plugin examples | Public under MIT | Managed premium integrations, support and updates |
| User interface proposals and accessibility patterns | Public designs/examples | Customer dashboard, supported desktop release |
| Testing | Synthetic fixtures and interoperability samples | Release signing, private system tests and device pairing validation |
| Local Windows engine | Interface docs and safe demonstration fixtures only | Production Windows broker, permissions, full product implementation |
| Secure remote ChatGPT connectivity | Public integration concepts/documentation | Authenticated managed connection, account and device entitlements |
| Team/community workflow | GitHub issues, PRs, discussions, published roadmap | Private owner approvals, production CI/CD, restricted secrets |
| Subscription billing and premium support | Pricing information only when approved | Secure billing service, metering, support, account portal |

## Rules

1. Public code must have an explicit compatible license and pass a confidential-data review before release.
2. Sensitive Windows captures, customer data, access credentials, internal infrastructure and proprietary engine modules must remain private.
3. Security/privacy principles can be public; secrecy is not a substitute for secure authentication and authorization.
4. Public issues and pull requests must never grant remote machine permissions or direct access to production environments.
5. Contributors to this repository retain rights provided by the MIT license; no automatic employment, compensation, or access to the private core is implied.
6. Commercial terms, prices, trials and production availability must be marked *planned* until operationally ready and approved.
