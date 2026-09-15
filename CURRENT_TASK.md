# CURRENT TASK

## P0 — Customer → Account → Admin end-to-end regression

### Locked acceptance criteria
1. Website contact form submissions appear in Admin → İletişim Talepleri with all submitted fields.
2. Hesabım → Firma Bilgileri saves to the real backend with explicit success/error.
3. Website sample request creates real `sample_requests` + `sample_request_items`; no false success.
4. Header profile opens account menu first; no direct redirect.
5. Logged-in sample flow is system-based; no misleading e-mail request path.
6. Multiple samples can be selected and sent in one request with visible count.
7. Successful request shows feedback and deliberately resets submitted selection/UI.
8. Same real request appears in Customer → Numune Taleplerim and corresponding Admin customer record.
9. Admin status/tracking uses exact real schema/status contract.
10. Empty/loading/error states are deliberate.
11. Desktop + mobile touched flows are browser-verified.
12. Admin and customer auth use e-mail + password only. Google/Apple OAuth is removed from scope and must not appear in login/register UI.
13. Admin and customer login screens include Şifremi unuttum. Password recovery uses the Supabase recovery flow and returns to the correct login surface.

### Locked auth/schema
- Customer/site auth: `ah_auth`.
- Admin auth: `ah_admin_auth`.
- Request statuses: `new`, `approved`, `preparing`, `shipped`, `delivered`, `cancelled`.
- Existing Supabase/RLS architecture stays unchanged unless a reproduced defect requires the minimum safe change.

### Flow
BUILD → TEST → VERIFY → USER_VISIBLE_SUCCESS → PASS → NEXT

### Current status
- Account read/write session refresh fix is deployed.
- Customer password recovery page exists.
- Admin and customer accounts are confirmed and e-mail/password auth is the only required sign-in method.
- Google/Apple OAuth work is cancelled by user decision and must be removed from visible login/register UI.
- Production DB currently has no real sample request yet; sample request E2E remains open.
- FINAL PASS: NO.

### FIRST_BLOCKER
Remove Google/Apple social-login UI from site, customer account and admin login surfaces, then continue the real customer sample-request E2E using e-mail/password auth.

### NEXT_ACTION
Keep auth simple: e-mail/password + password recovery only. Then run the same real customer → sample request → customer history → admin request/status/tracking chain.