# Memory Index

Read this file first, every session. It's a pointer, not the content — keep
it under ~30 lines so it stays cheap to load.

## Read in this order
1. `context/SOUL.md` — who you are as the agent on this project
2. `context/operators/<operator-name>.md` — who you're working with today
   (ask if unsure which operator file applies)
3. `context/memory/activeContext.md` — what's happening right now, and the
   handover note from the last session
4. `AGENTS.md` (repo root) — behavior & product rules
5. `AI.md` (repo root) — current task queue

## Deeper context (load only if relevant to the task)
Every file in `context/memory/` starts with a short YAML frontmatter block
(`description`, `updated`, `max_lines`). **Read the frontmatter first** —
it's a few lines — and only load the full body if the `description`
suggests it's relevant to the current task. Don't read all memory files
front-to-back by default; that's exactly the bloat this pattern avoids.

- Architecture & conventions → `context/memory/systemPatterns.md`
- Stack & environment setup → `context/memory/techContext.md`
- Recurring questions → `context/memory/faq.md` (entries also carry their
  own `tags:` line — scan those before reading full answers)
- Past decisions & lessons → `context/memory/learnings.md` (same per-entry
  `Tags:` pattern)
- Milestones & overall status → `context/memory/progress.md`

If a file's line count is visibly past its `max_lines`, that's a signal to
prune/archive it — flag this to the human rather than silently deleting
content.

## Quick facts
<!-- Keep this to 5-10 bullets of the things that would otherwise get
     re-explained every session. Prune aggressively. -->
- Project: <name>
- Primary stack: <e.g. TypeScript / Next.js / Postgres>
- Current milestone: <link to progress.md section>
- Repo conventions: see `systemPatterns.md`

## Before you finish this session
Write a handover note into `activeContext.md` using `context/HANDOVER.md` as
the template. Future-you (or another agent) will thank you.
