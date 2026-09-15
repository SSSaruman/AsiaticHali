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
12. Admin and customer login screens include Şifremi unuttum plus Google and Apple entry points with visible provider icons. OAuth callback must persist the correct isolated session (`ah_admin_auth` / `ah_auth`). Admin OAuth users still require real `is_admin=true` authorization.
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
- Admin + customer login UI contains forgot-password, Google, and Apple entry points with callback session handling.
- Google and Apple SVG provider icons were added in commit `893dfc43e2b0c18b0f8155ee412a8dbfdc1c03f7`; Pages deployment is still being verified.
- Direct runtime probe against the real Supabase Auth `/authorize` endpoint returned HTTP 400 for both providers with `Unsupported provider: provider is not enabled`.
- Therefore the button code is not the current OAuth blocker; both providers are disabled in the Supabase Auth provider configuration.
- Direct mutation of the existing admin password through the available database tool was blocked by the tool security layer; therefore no new password has been claimed/set.
- FINAL PASS: NO.

### FIRST_BLOCKER
Enable/configure Google and Apple in the real Supabase Auth provider settings. Until provider-side credentials/configuration exist, both OAuth buttons necessarily fail before callback handling.

### NEXT_ACTION
Configure the real Google OAuth client and Apple Sign in with Apple credentials in Supabase Auth, ensure the GitHub Pages callback URLs are allowlisted, then rerun the same real `/authorize` probe. Only after each provider returns an OAuth redirect instead of HTTP 400 continue to browser login verification.