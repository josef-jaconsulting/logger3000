# Context System — How This Folder Works

This folder gives every agent session (and every human operator) a shared,
persistent understanding of the project that survives across sessions and
across agents. It complements, not replaces, what you already have:

| File / Folder          | Answers                          | Scope              | Update frequency |
|-------------------------|-----------------------------------|---------------------|-------------------|
| `AGENTS.md`             | "How should any agent behave here?" | Static rules        | Rarely |
| `AI.md`                 | "What's the task right now?"      | Current sprint/task | Every task |
| `context/SOUL.md`       | "Who is this agent, in character/tone terms?" | Agent identity | Rarely |
| `operator.md`           | "Who is the human, and how do they like to work?" | Per-human | Occasionally |
| `context/MEMORY.md`     | Index — where to find everything below | Pointer file | When structure changes |
| `context/memory/activeContext.md` | "What's being worked on, and what should the next session know first?" | Rolling | Every session |
| `context/memory/progress.md` | "What milestones are done / in progress / blocked?" | Project-wide | Weekly / per milestone |
| `context/memory/system_patterns.md` | "What architectural decisions and conventions exist, and why?" | Project-wide | On decision |
| `context/memory/tech_context.md` | "What's the stack, setup, constraints?" | Project-wide | On change |
| `context/memory/faq.md` | "What do people keep asking?" | Project-wide | As questions recur |
| `context/memory/learnings.md` | "What did we try that didn't work, and what did we learn?" | Project-wide | As learned |
| `context/handover_template.md`  | Template used at the end of a session to brief the next one | Per session | Every session end |

## Golden rule
**Every agent session starts by reading `context/MEMORY.md`** (which points to
everything else) **and ends by updating `context/memory/activeContext.md`**
using the `handover_template.md` template. This is the two habits that make the whole
system work — everything else is detail.

## Ownership & review
- Any agent may *propose* edits to `memory/*.md` files as part of normal work.
- Changes to `SOUL.md` or an operator profile should be flagged to the human
  operator explicitly before being saved (identity/preference files are
  sensitive — silent edits erode trust).
- A human should skim `progress.md` and `learnings.md` roughly weekly, the
  same way you'd skim a team's Slack digest.
- Treat this whole folder as version-controlled documentation: commit it,
  diff it, review it in PRs like code.

## Format convention: frontmatter + line caps
Every file in `context/memory/` starts with a small YAML block:

```yaml
---
description: "One line — what's in this file, for scanning without opening it."
updated: 2026-07-12
max_lines: 200
---
```

The point is to let an agent decide relevance by reading ~5 lines instead
of the whole file. `MEMORY.md` tells the agent to scan frontmatter before
loading a body. `faq.md` and `learnings.md` extend the same idea to
individual entries via a `tags:`/`Tags:` line, since those files are
append-only logs with many small entries rather than one document.

`max_lines` is a soft ceiling, not an editor-enforced limit — a file
crossing it is a signal to prune, archive, or split, not something to
ignore. We chose markdown + YAML frontmatter over a format like TOML for
this: the bulk of these files is prose (rationale, explanations), which
markdown handles more compactly and more reliably than a config format —
see the format-choice discussion in memory if you want the reasoning.

## Why split it this way
- **Identity vs. preferences vs. memory are different things.** `SOUL.md` is
  who the agent is (stable). Operator profiles are who the human is and how
  they like to work (stable-ish). `memory/` is what's been learned and
  decided (constantly growing). Mixing these makes all three harder to
  maintain.
- **`activeContext.md` is intentionally short-lived and gets rewritten
  often** — it's the "sticky note," not the archive. `progress.md` and
  `learnings.md` are the archive.
