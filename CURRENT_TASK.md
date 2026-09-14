# CURRENT TASK

## P1 — Professionalize Admin UI without expanding scope

### Previous gates
`Admin login`: PASS.
`Admin core data contract`: PASS.
`Admin/customer session isolation`: PASS.

Verified in browser:
- Admin logout does not close the customer/site session.
- Customer/site logout does not close the admin session.
- Both sessions survive independently as intended.

### Active target
Improve only the existing `Admin.dc.html` interface so the current working admin flow is professional, clear, and responsive. Do not add CRM, WhatsApp, AI bot, new backend tables, new roles, or unrelated features in this task.

### Locked behavior preserved
- Existing admin auth and `ah_admin_auth` isolation.
- Existing RLS/admin authorization.
- Existing tabs and data functions: Firms/Customers, sample requests, contact requests.
- Existing Supabase schema contract.
- Existing status values: `new`, `approved`, `preparing`, `shipped`, `delivered`, `cancelled`.

### UI acceptance criteria
1. Clear professional admin information hierarchy; no empty-looking prototype feel.
2. Existing data/actions remain obvious and usable.
3. Firms/customers list and selected-detail area are visually distinct and readable.
4. Sample request status/tracking controls have clear labels/states and fit the current workflow.
5. Contact requests are readable and scannable.
6. Loading, empty, unauthorized, and error states are deliberate rather than raw placeholders.
7. Responsive behavior works on desktop and mobile without horizontal overflow.
8. No dashboard/bento/SaaS visual expansion; no unrelated polish or animation.
9. No backend/schema/auth changes.
10. Deployed browser verification required before PASS.

### Build completed
- Reworked only `Admin.dc.html` presentation layer.
- Added clearer header, page hierarchy, labeled form controls, stronger firm/detail separation, deliberate empty/loading/unauthorized states, and readable contact cards.
- Added responsive single-column behavior for narrow screens and removed likely horizontal overflow points.
- Kept auth/session keys, RLS calls, Supabase queries, status contract, save behavior, and existing tabs unchanged.

### Flow
BUILD → TEST → VERIFY → PASS → NEXT

### Status
- BUILD: PASS — targeted code inspection confirms UI-only change and locked auth/data behavior remains intact.
- TEST: BLOCKED on deployed browser verification.
- VERIFY: BLOCKED until browser test passes.
- PASS: NO.

### Next exact action
Refresh deployed `Admin.dc.html` with Ctrl+F5 and verify desktop layout, firm selection/detail, contact requests tab, login/unauthorized states, and one narrow/mobile viewport. If these pass without horizontal overflow or broken controls, mark Admin UI PASS and move to Customer Panel UI as the next task.
