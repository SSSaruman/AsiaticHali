# CURRENT TASK

## P0 — Admin login must work on deployed site

### Active target
Make `Admin.dc.html` authentication work reliably on the deployed GitHub Pages site for the existing admin account, without expanding CRM/UI scope.

### Locked facts
- Admin email: `ufuk.karahann@gmail.com`
- Supabase project: `dytyehxybhzlmwxarbpc`
- Existing auth user is email-confirmed, not banned, and `profiles.is_admin = true`.
- Current task is login only. CRM V2, WhatsApp, AI bot, inbox expansion, social login and broader UX improvements are blocked until this task passes.

### Verified diagnosis
- The previous "missing React/ReactDOM" diagnosis was incorrect: `support.js` contains its own React/ReactDOM CDN loader.
- Supabase user state is valid: account exists, email is confirmed, not banned, and admin flag is true.
- The known unresolved blocker is credential recovery: the test password `123456` was never actually set through Supabase Auth, so it must not be assumed valid.
- `Admin.dc.html` currently has no password-recovery path and reduces all auth failures to the generic text `Giriş başarısız.`

### Minimum safe fix
1. Add password recovery to the existing admin login only; do not redesign the panel.
2. Recovery must use Supabase Auth and return to the deployed `Admin.dc.html` URL.
3. Handle the recovery callback and allow setting a new password through the authenticated recovery session.
4. Preserve existing admin authorization/RLS behavior.
5. Expose the real auth error category/message sufficiently to distinguish invalid credentials, unconfirmed account, rate limit, and network failure during verification.

### Acceptance criteria
1. Deployed `Admin.dc.html` renders through the DC runtime, not raw unresolved `{{ }}`/`sc-*` markup.
2. Admin can recover/reset the password using the existing confirmed admin email.
3. Admin credentials accepted by Supabase create a valid session.
4. Admin check returns `is_admin=true` and panel content becomes visible.
5. Non-admin session cannot view admin data.
6. Logout clears the session and returns to login state.
7. A real browser-level test on the deployed page passes before this task is marked PASS.

### Flow
BUILD → TEST → VERIFY → PASS → NEXT

### Status
FAIL — root cause isolated to unresolved credentials/recovery path. Minimum safe fix pending; no feature work permitted.
