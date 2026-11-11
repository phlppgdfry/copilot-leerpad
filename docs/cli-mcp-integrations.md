# Lesson 8 — GitHub CLI, MCP & Secure Integrations

## 1. Environment

- IDE: Visual Studio Code
- AI assistant: GitHub Copilot Student / Fusion
- Repository: `phlppgdfry/copilot-leerpad`
- Operating system: macOS
- Focus: GitHub CLI, MCP integration, least-privilege access and agent security

## 2. GitHub CLI

The GitHub CLI provides terminal-based access to GitHub repositories, issues and pull requests.

| Command | Purpose | Read-only |
|---|---|---|
| `gh --version` | Display installed CLI version | Yes |
| `gh auth status` | Inspect authentication status | Yes |
| `gh repo view` | Inspect repository details | Yes |
| `gh issue list` | List open issues | Yes |
| `gh pr list` | List open pull requests | Yes |
| `gh issue view 8` | Inspect a specific issue | Yes |

**Observation:** The CLI was used during earlier lessons to create issues, manage branches and prepare pull requests.

**Verification:** Exact CLI outputs from this lesson should be recorded separately if needed.

## 3. CLI and AI Integration

GitHub CLI output can provide structured context for AI analysis.

Potential use cases:

- Summarizing GitHub issues.
- Understanding pull request status.
- Identifying unfinished development tasks.
- Preparing implementation plans.
- Comparing repository changes.

**Lesson learned:** Structured CLI output, especially JSON, can reduce ambiguity when providing data to an AI assistant.

**Experiment status:** The supplied Copilot transcript does not establish the exact results of the separate CLI-output comparison exercise.

## 4. MCP Inventory

Copilot inspected the local configuration at:

`~/.copilot/mcp-config.json`

The configuration reportedly exposes an existing GitHub bridge using:

`"tools": ["*"]`

This indicates broad tool exposure rather than an explicit read-only tool allowlist.

| Server | Purpose | Access |
|---|---|---|
| Existing GitHub MCP bridge | GitHub integration | Wildcard tool configuration observed |
| Proposed read-only GitHub gateway | Restricted repository analysis | Design only; not installed |

**Important:** The actual GitHub token permissions and server-side restrictions were not verified. Wildcard tool exposure does not automatically prove unrestricted GitHub write access.

## 5. MCP Experiment

### Inspection performed

- Local MCP configuration examined by Copilot.
- Repository README inspected.
- Previous model and agent evaluation notes inspected.
- Existing GitHub bridge identified.
- Read-only alternative designed.

### Limitations

- No MCP server was installed.
- No MCP configuration was changed.
- No live read-only gateway was tested.
- Actual authentication scopes were not verified.
- Enforcement of proposed security controls remains untested.

## 6. Proposed Secure MCP Architecture

### Architecture

`Copilot → Read-only MCP Policy Gateway → GitHub API → Approved Repository`

### Proposed server

`copilot-leerpad-github-readonly`

Repository allowlist:

`phlppgdfry/copilot-leerpad`

The gateway should restrict access to one approved repository and expose only approved read operations.

### Allowed tools

- `repository_metadata_read`
- `issue_list_read`
- `issue_read`
- `pull_request_list_read`
- `pull_request_read`
- `repository_file_read`
- `repository_search_read`
- Optional: `commit_list_read`
- Optional: `task_context_summarize`

These are proposed interface names, not confirmed tools already installed.

### Minimum GitHub permissions

Prefer a GitHub App restricted to the approved repository with:

- Metadata: read
- Contents: read
- Issues: read
- Pull requests: read

Additional permissions should only be granted when required and justified.

### Authentication

Use short-lived GitHub App installation tokens generated server-side.

Credentials must never appear in prompts, tool responses or logs.

A fine-grained, single-repository read-only token could be considered as a fallback.

### Forbidden operations

The read-only gateway must not permit:

- File modifications or deletion
- Issue or pull request modifications
- Branch creation or deletion
- Pushing commits
- Automatic merges
- Running deployments
- Executing GitHub Actions workflows
- Accessing repository secrets
- Changing repository administration settings

Any future write capability should use a separate authorization boundary and require explicit human approval.

## 7. Security Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Excessive tool exposure | Explicit read-only tool allowlist |
| Unauthorized repository access | Server-side repository allowlist |
| Prompt injection | Treat GitHub content as untrusted data |
| Credential leakage | Server-side credentials and redacted logs |
| Unauthorized writes | No write operations exposed |
| Data exfiltration | No arbitrary external URL fetching |
| Excessive data retrieval | Pagination and response-size limits |
| Rate-limit exhaustion | Quotas, caching and rate-limit handling |
| Malformed tool responses | Schema validation and fail-closed behavior |

## 8. Verification Plan

Before implementing or trusting the proposed gateway:

1. Verify access is restricted to `phlppgdfry/copilot-leerpad`.
2. Verify that only approved read tools are advertised.
3. Confirm issues, pull requests and repository files can be read.
4. Confirm write operations are denied.
5. Confirm credentials never appear in outputs or logs.
6. Test resistance to malicious instructions in issues and Markdown.
7. Test path restrictions and unauthorized repositories.
8. Test malformed responses and API failures.
9. Verify audit logging without exposing secrets.

**Current status:** Architecture designed; implementation and verification not performed.

## 9. Lessons Learned

1. GitHub CLI provides an effective interface for inspecting repository state and development tasks.
2. MCP allows AI agents to access external systems, but introduces additional permission and security considerations.
3. Tool availability and actual authorization are different concepts.
4. A dedicated read-only gateway is a safer design for repository analysis than relying solely on broad tool exposure.
5. Agent-generated architecture proposals require independent verification before implementation.

## 10. Conclusion

**GitHub CLI:** Useful for explicit, repeatable repository operations controlled by the developer.

**MCP:** Useful when an AI agent needs structured access to external tools or repository information.

**Security recommendation:** Start with read-only access, apply least privilege, verify tool permissions and require explicit human authorization for sensitive actions.

**Final result:** A secure MCP architecture has been designed for the learning project. No server or configuration changes have been implemented.