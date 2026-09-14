# CURRENT TASK

## P1 — Professionalize Customer / Hesabım UI without expanding scope

### Previous gates
`Admin login`: PASS.
`Admin core data contract`: PASS.
`Admin/customer session isolation`: PASS.
`Admin UI`: PASS by user acceptance after deployed UI rebuild.

### Active target
Improve only `Hesabim.dc.html` so the current customer account flow is professional, clear, readable, useful, and responsive. Do not add CRM, WhatsApp, AI bot, new backend tables, new roles, or unrelated features in this task.

### Locked behavior preserved
- Customer/site auth remains `ah_auth`.
- Verification, login/register, logout, sample list, sample request, company profile and password/account flows remain in place.
- Supabase/RLS architecture is unchanged.
- TR/EN remains available.
- Request status contract remains `new`, `approved`, `preparing`, `shipped`, `delivered`, `cancelled`.

### Build completed
- Reworked only `Hesabim.dc.html` presentation plus existing read/write field names needed for the real schema.
- Increased typography/control sizes and strengthened account information hierarchy.
- Rebuilt login/register and verification states with labeled fields and deliberate notices.
- Rebuilt authenticated layout with clearer identity/navigation and responsive behavior.
- Overview now loads the existing request history so counts are real instead of remaining `0` until the request tab is opened.
- Sample list now has explicit context, deliberate empty state and clearer request action.
- Request history now displays request id/date, all real statuses and tracking number.
- Company/profile form is labeled and split from account security.
- Corrected pre-existing schema mismatches found in this same flow: `company_name` → `company`, `courier_ref` → `shipping_tracking_no`.
- No new backend tables, roles, integrations or speculative features were added.

### UI acceptance criteria
1. Login/register/verification screens are clear and readable.
2. Authenticated account screen gives the customer useful context, not only sparse counters.
3. Sample list actions are obvious and usable.
4. Sample request history clearly communicates status and tracking.
5. Company/profile editing is understandable and safe.
6. Typography is comfortably readable at normal desktop scale.
7. Desktop and mobile layouts work without horizontal overflow.
8. Empty/loading/error states are deliberate.
9. No backend/schema/auth expansion and no speculative features.
10. Deployed browser verification required before PASS.

### Flow
BUILD → TEST → VERIFY → PASS → NEXT

### Status
- BUILD: PASS — targeted code inspection confirms the rebuild is limited to the customer account flow and the real existing schema contract.
- TEST: BLOCKED on deployed browser verification.
- VERIFY: BLOCKED until browser test passes.
- PASS: NO.

### Next exact action
Refresh deployed `Hesabim.dc.html` with Ctrl+F5. Verify desktop overview, sample list, sample request history, company/profile edit, logout, login/register/verification, and one narrow/mobile viewport. If these pass without broken controls or overflow, mark Customer UI PASS and move to the next active task.
