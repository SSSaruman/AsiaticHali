# CURRENT TASK

## P0 — Admin login must work on deployed site

### Active target
Make `Admin.dc.html` authentication work reliably on the deployed GitHub Pages site for the existing admin account, without expanding CRM/UI scope.

### Locked facts
- Admin email: `ufuk.karahann@gmail.com`
- Supabase project: `dytyehxybhzlmwxarbpc`
- Existing auth user is email-confirmed, not banned, and `profiles.is_admin = true`.
- Current task is login only. CRM V2, WhatsApp, AI bot, inbox expansion, social login and broader UX improvements are blocked until this task passes.

### Current diagnosis
- `Admin.dc.html` includes `support.js` but no explicit React/ReactDOM scripts.
- `support.js` calls `getReact()` / `getReactDOM()` and expects `window.React` / `window.ReactDOM` to already exist.
- This is a likely static GitHub Pages runtime failure and must be verified/fixed with the minimum safe change.

### Acceptance criteria
1. Deployed `Admin.dc.html` renders through the DC runtime, not raw unresolved `{{ }}`/`sc-*` markup.
2. Admin credentials accepted by Supabase create a valid session.
3. Admin check returns `is_admin=true` and panel content becomes visible.
4. Non-admin session cannot view admin data.
5. Logout clears the session and returns to login state.
6. A real browser-level test on the deployed page passes before this task is marked PASS.

### Flow
BUILD → TEST → VERIFY → PASS → NEXT

### Status
FAIL — root cause diagnosis in progress. No feature work permitted.
