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
12. Admin and customer login screens include Şifremi unuttum plus Google and Apple entry points. OAuth callback must persist the correct isolated session (`ah_admin_auth` / `ah_auth`). Admin OAuth users still require real `is_admin=true` authorization.
13. Password recovery must use Supabase recovery flow and return to the correct login surface.

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
- Admin + customer login UI now contains forgot-password, Google, and Apple entry points with callback session handling.
- Embedded JS syntax check passed for the touched Admin/Hesabım scripts.
- GitHub Pages deployment for commit `a2dc310c4ff8f7555fcb71a83f9229160f3f8370` succeeded.
- Direct mutation of the existing admin password through the available database tool was blocked by the tool security layer; therefore no new password has been claimed/set.
- Google/Apple provider enablement has not yet been proven from provider-side runtime; UI presence alone is not PASS.
- FINAL PASS: NO.

### FIRST_BLOCKER
Restore admin access through the real Supabase recovery/login path, then verify admin login. Do not move to downstream sample-flow verification until admin access succeeds.

### NEXT_ACTION
Use the deployed Admin → Şifremi unuttum recovery flow for the existing admin account, set a new password through the recovery token, verify real Admin login, then continue the same real E2E chain.