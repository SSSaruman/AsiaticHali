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
- The test password `123456` was never actually set through Supabase Auth, so it must not be assumed valid.
- `Admin.dc.html` has no password-recovery path and reduces all auth failures to generic `Giriş başarısız.`

### Minimum safe fix built
- Added `AdminReset.html` as an isolated recovery page; existing admin panel was not redesigned or refactored.
- Recovery request uses Supabase `/auth/v1/recover` and requests return to the deployed recovery page.
- Recovery callback reads the Supabase recovery access token, validates the new password, updates it through `/auth/v1/user`, and returns to `Admin.dc.html` after success.
- Existing admin authorization/RLS behavior remains untouched.

### Acceptance criteria
1. Deployed `Admin.dc.html` renders through the DC runtime, not raw unresolved `{{ }}`/`sc-*` markup.
2. Admin can recover/reset the password using the existing confirmed admin email.
3. Admin credentials accepted by Supabase create a valid session.
4. Admin check returns `is_admin=true` and panel content becomes visible.
5. Non-admin session cannot view admin data.
6. Logout clears the session and returns to login state.
7. A real browser-level test on the deployed page passes before this task is marked PASS.

### Flow status
- BUILD: PASS — minimal recovery page committed and statically verified.
- TEST: BLOCKED — requires live GitHub Pages + recovery email interaction / Supabase redirect validation.
- VERIFY: BLOCKED until TEST passes.
- PASS: NO.

### Next exact action
Open deployed `AdminReset.html`, send recovery mail to the locked admin email, set a known test password, then execute admin login / authorization / logout browser E2E. If redirect is rejected or returns to the wrong URL, fix only Supabase redirect configuration or the recovery redirect target, then rerun the same test.
