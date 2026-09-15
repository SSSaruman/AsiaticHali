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
- Google/Apple social login is removed from the active auth implementation; e-mail/password + password recovery remains.
- Both real Supabase Auth accounts are confirmed and have successful sign-in history.
- Account read/write session refresh fix is deployed.
- Production DB currently has 2 profiles and 5 contact requests.
- Production DB currently has 0 `sample_requests` and 0 `sample_request_items`.
- Therefore the customer sample-request chain has not yet produced a real final output.
- FINAL PASS: NO.

### FIRST_BLOCKER
Create one real multi-item sample request from the deployed customer UI while authenticated. Until a real request exists in `sample_requests` + `sample_request_items`, downstream customer-history and Admin verification cannot be truthfully passed.

### NEXT_ACTION
From the deployed site with a real customer session, select at least two samples and submit one request. Immediately verify the resulting rows in production, then verify the same request in Customer → Numune Taleplerim and Admin → customer record before testing status/tracking propagation.