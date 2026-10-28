# Host adapters

The skill is portable instructions, not a browser extension or background service. A supported installation needs both Chrome control and native scheduled actions with that same Chrome access at run time. Discover actual tools and inspect schemas rather than copying hypothetical calls.

## OpenAI: ChatGPT desktop / Codex

Install and enable the ChatGPT Chrome extension through Settings → Computer Use and select the signed-in Chrome profile. A browser-capable desktop host may expose `cua`/browser tools; use their documented entry point to inventory Chrome tabs, then read a relevant tab. Never use the built-in browser when the brief specifies Chrome.

For wake-ups, discover native scheduled actions/automations (for example `automation_update` in Codex desktop). Read its schema; choose a thread heartbeat when supported and appropriate. Include the complete brief and exact date guard in the prompt, retain the returned ID and verify next run. Tool names and scheduling formats differ between hosts. Ordinary API models and CLI installations do not automatically include these desktop capabilities. Do not promise unattended Chrome access from a cloud task.

Sources:
- https://learn.chatgpt.com/docs/chrome-extension
- https://learn.chatgpt.com/docs/build-skills

## Claude: Chrome-enabled desktop / Claude Code

Use the Claude in Chrome extension and a compatible Chrome-enabled agent session. Claude Code documents starting with `claude --chrome`; discover its extension tools and read a tab to verify the active account. Do not assume the Chrome extension alone supplies multi-day durable scheduling.

Prefer the host's persistent desktop scheduled tasks when they can access Chrome and the durable media. Discover their tools and schedule format. Claude Code's session cron tools (`CronCreate`, `CronList`, `CronDelete`, when exposed) are session-dependent, with expiry and restart limitations; they are not a reliable substitute for an independent multi-day desktop scheduler. Explain this limitation and save the plan if a durable compatible scheduler is unavailable. Cloud scheduled tasks do not have your local files or local Chrome profile by default.

Sources:
- https://code.claude.com/docs/en/chrome
- https://code.claude.com/docs/en/scheduled-tasks

## No compatible scheduler

Produce the complete dated plan and executable briefs, with status `unarmed`. State the missing capability and how to enable a supported host. Do not claim a wake-up was created, invent an action ID, silently create OS jobs, or replace the requested extension with social APIs.
