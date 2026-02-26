# Project TODOs

## MCP Readiness
Next steps to enable this API for full Model Context Protocol (MCP) tool usage:

- [ ] **Dependency Installation:** Add `@modelcontextprotocol/sdk` to `apps/api/package.json`.
- [ ] **MCP Server Implementation:** Create a dedicated MCP server entry point (e.g., `apps/api/src/mcp-server.ts`) that:
    - Parses `openapi.yaml`.
    - Maps `operationId` to MCP tools.
    - Preserves and passes the refined `description` metadata to the AI client.
- [ ] **Secure Credentials:** Configure a mechanism (e.g., `.env` or system environment variables) to provide the `X-API-TOKEN` or OAuth2 credentials to the MCP runtime.
- [ ] **Client Configuration:** Create an MCP configuration file (`mcp-config.json` or equivalent for your AI client) that:
    - Specifies the `node` runtime command.
    - Points to the compiled `dist/mcp-server.js`.
    - Sets the required environment variables.
- [ ] **Transport Layer:** Decide on the primary transport (default to `stdio` for local desktop clients; consider `SSE` for remote hosting).
- [ ] **Verification:** Test the AI's ability to:
    - List cars and navigate pagination.
    - Follow the "fetch car detail before logTrip" instruction.
    - Correctly handle RFC 7807 "Problem" error responses.

## Copilot Extension Readiness
Next steps to enable GitHub Copilot Chat (via @mention) to access and manage the car fleet:

- [ ] **GitHub App Registration:** Create a new GitHub App in your account/org settings.
    - [ ] Enable **Copilot** capabilities for the app.
    - [ ] Configure a **Callback URL** pointing to your agent's `/agent` endpoint (use `ngrok` for local dev).
- [ ] **Copilot Agent Implementation:** Develop a new service (or endpoint in `apps/api`) that:
    - [ ] Implements the Copilot Chat agent protocol (receiving `POST` requests from GitHub).
    - [ ] Uses the `openapi.yaml` to map user intent (natural language) to API functions.
    - [ ] Formats data into **rich Markdown/UI components** (e.g., tables for trip logs, buttons for actions).
- [ ] **Identity Mapping:** Implement logic to securely map a GitHub user's OAuth token to your API's `X-API-TOKEN` or internal user ID.
- [ ] **System Prompt Integration:** Ensure the `AI_INSTRUCTIONS.md` (e.g., the "odometer continuity" rule) is part of the agent's LLM system prompt.
- [ ] **Safety & Confirmation:** Implement "Confirmation Cards" for destructive actions like soft-deleting vehicles via `PATCH`.
- [ ] **Development Tunneling:** Set up `ngrok` or GitHub Codespaces to expose your local API to GitHub's cloud for end-to-end testing.
