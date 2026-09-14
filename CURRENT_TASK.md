# CURRENT TASK

## P0 — Customer → Account → Admin end-to-end regression

### Why this replaced the previous task
The previous `Hesabim.dc.html` UI task was too narrow and did not cover the user-reported cross-site failures. Those flows are now the single active target. No CRM/WhatsApp/AI work until this gate passes.

### Locked reported failures / acceptance criteria
1. Website contact form submissions must appear in Admin → İletişim Talepleri with all submitted fields.
2. `Hesabım → Firma Bilgileri` save must persist and show an explicit success state; failures must show an explicit error.
3. Website sample request must create real backend records; success may only appear after DB success.
4. Header profile control must open an account menu first, not redirect immediately. Menu includes Hesabım / Kayıtlı Numuneler / Numune Talepleri / Çıkış.
5. Sample flow is system-based; no misleading “E-postayla gönder” path for logged-in sample requests.
6. Multiple samples must be selectable and submitted in one request; UI must show the selected count.
7. After a successful sample request, success feedback must be visible and the submitted selection/request UI must reset deliberately.
8. The request must then be visible in both Customer → Numune Taleplerim and the corresponding Admin customer record.
9. Admin must display request status and tracking using the real schema/status contract.
10. Empty/loading/error states must be deliberate; no silent success, stale screen or false PASS.
11. Desktop + mobile browser regression is required for the touched flows.

### Locked schema/auth
- Customer/site auth: `ah_auth`.
- Admin auth: `ah_admin_auth`.
- Request statuses: `new`, `approved`, `preparing`, `shipped`, `delivered`, `cancelled`.
- Existing Supabase/RLS architecture is preserved unless a reproduced backend defect requires a minimum safe change.

### Flow
BUILD → TEST → VERIFY → PASS → NEXT

### Current status
- Previous individual fixes are NOT accepted as a complete PASS.
- Automated browser regression infrastructure exists but is currently FAILING before full scenario coverage.
- Latest E2E infrastructure failure: account-control locator selected a hidden duplicate element. Test must target the visible control, then continue until it exposes real product defects.
- PASS: NO.

### Next exact action
Fix only the E2E locator failure, rerun the regression, then fix the first real failing product scenario. Repeat targeted test until all 11 acceptance criteria pass. Do not start another feature.