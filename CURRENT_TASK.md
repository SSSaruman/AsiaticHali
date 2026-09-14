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
Improve only the existing `Admin.dc.html` interface so the current working admin flow is professional, clear, readable, information-rich enough for operations, and responsive. Do not add CRM, WhatsApp, AI bot, new backend tables, new roles, or unrelated features in this task.

### Locked behavior preserved
- Existing admin auth and `ah_admin_auth` isolation.
- Existing RLS/admin authorization.
- Existing tabs and data functions: Firms/Customers, sample requests, contact requests.
- Existing Supabase schema contract.
- Existing status values: `new`, `approved`, `preparing`, `shipped`, `delivered`, `cancelled`.

### UI acceptance criteria
1. Clear professional admin information hierarchy; no empty-looking prototype feel.
2. Body text and controls are comfortably readable at normal desktop scale.
3. Existing data/actions remain obvious and usable.
4. Firms/customers list shows useful identity/contact context, not only a name.
5. Selected customer area shows useful contact context plus request summary.
6. Sample request status/tracking controls have clear labels/states and fit the current workflow.
7. Contact requests are readable and scannable.
8. Loading, empty, unauthorized, and error states are deliberate rather than raw placeholders.
9. Responsive behavior works on desktop and mobile without horizontal overflow.
10. No dashboard/bento/SaaS expansion, unrelated animation, backend/schema/auth changes, or speculative features.
11. Deployed browser verification required before PASS.

### Build completed
- Reworked only `Admin.dc.html` presentation and read-only profile query fields.
- Increased typography and control sizing across the admin UI.
- Customer list now shows identity plus available email/phone context.
- Selected customer area now shows available email, phone, address and request counts derived from already-loaded request data.
- Request cards now expose request id/date/products/status/tracking more clearly.
- Contact request cards use larger, more readable typography.
- Responsive single-column behavior remains in place.
- Auth/session keys, RLS behavior, status contract and save behavior remain unchanged.

### Flow
BUILD → TEST → VERIFY → PASS → NEXT

### Status
- BUILD: PASS — readability/information-density rebuild committed.
- TEST: BLOCKED on deployed browser verification.
- VERIFY: BLOCKED until browser test passes.
- PASS: NO.

### Next exact action
Refresh deployed `Admin.dc.html` with Ctrl+F5. Verify the larger typography, richer customer list, selected-customer summary, request controls, contact requests tab, and one narrow/mobile viewport. If these pass without overflow or broken controls, mark Admin UI PASS and move to Customer Panel UI.
