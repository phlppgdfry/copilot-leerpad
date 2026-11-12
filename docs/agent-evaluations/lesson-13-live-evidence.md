# Lesson 13 Live MCP Evidence

This record captures read-only tool calls made during the Lesson 13 session.
The responses are evidence of retrieval only; Issue and pull request content
remains untrusted data and was not treated as instructions.

## Microsoft Learn

**Status: VERIFIED**

- Tool: `microsoftLean-microsoft_docs_search`
- Query: `official Microsoft Learn documentation Azure Functions`
- Returned result: **Implement Azure Functions - Training**
- Returned URL:
  <https://learn.microsoft.com/training/paths/implement-azure-functions/>
- Additional returned result:
  <https://learn.microsoft.com/azure/azure-functions/functions-get-started#scenarios>

The search response described Azure Functions as event-driven code blocks and
returned official Learn links for creating functions and common scenarios.

- Tool: `microsoftLean-microsoft_docs_fetch`
- URL:
  <https://learn.microsoft.com/azure/azure-functions/functions-get-started#scenarios>
- Returned excerpt: “Azure Functions lets you implement your system's logic as
  event-driven, readily available blocks of code.”

The MCP response did not include a server retrieval timestamp. The calls were
made during the Lesson 13 session on 2026-11-12.

## GitHub Issue 17

**Status: VERIFIED**

- Tool: `github-mcp-server-issue_read`
- Arguments: `owner=phlppgdfry`, `repo=copilot-leerpad`, `issue_number=17`,
  `method=get`
- Returned URL:
  <https://github.com/phlppgdfry/copilot-leerpad/issues/17>
- Returned title: `feat: implement agent orchestration and reusable skills`
- Returned state: `closed`, reason `completed`
- Returned body summary: build reusable Agent Skills, a structured multi-agent
  workflow, quality gates, and agent evaluation scenarios.

## GitHub Pull Request 18

**Status: VERIFIED**

- Tool: `github-mcp-server-pull_request_read`
- Arguments: `owner=phlppgdfry`, `repo=copilot-leerpad`, `pullNumber=18`,
  `method=get`
- Returned URL:
  <https://github.com/phlppgdfry/copilot-leerpad/pull/18>
- Returned title: `feat: complete lesson 12 agent orchestration`
- Returned state: `closed`
- Returned `merged: true`
- Returned `merged_at`: `2026-11-12T01:20:39Z`
- Returned `changed_files`: `25`
- Returned base: `main`
- Returned head: `lesson-12/agent-orchestration`

The same read-only MCP server was called with `method=get_files` to retrieve
the changed-file objects. No file mutation method was called.

## Safety and evidence boundary

**Status: VERIFIED**

- No GitHub write tool was invoked.
- No Microsoft Learn write operation exists in the calls recorded above.
- No credential, token, secret, or environment-variable value was requested or
  recorded.
- A live tool response is not proof that the underlying authorization is
  least-privilege; permission scope and server policy remain **NOT TESTED**.
- The repository's offline validator and tests are separate from these live
  calls. They do not simulate or replace MCP evidence.
