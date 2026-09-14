# CURRENT TASK

## P1 — Professionalize Customer / Hesabım UI without expanding scope

### Previous gates
`Admin login`: PASS.
`Admin core data contract`: PASS.
`Admin/customer session isolation`: PASS.
`Admin UI`: PASS by user acceptance after deployed UI rebuild.

### Active target
Improve only `Hesabim.dc.html` so the current customer account flow is professional, clear, readable, useful, and responsive. Do not add CRM, WhatsApp, AI bot, new backend tables, new roles, or unrelated features in this task.

### Locked behavior to preserve
- Existing customer/site auth via `ah_auth`.
- Existing verification, login/register, logout, sample list, sample request, company profile and password/account flows.
- Existing Supabase schema and RLS behavior.
- Existing TR/EN capability.
- Existing sample request status contract.

### UI acceptance criteria
1. Login/register/verification screens are clear and readable.
2. Authenticated account screen gives the customer useful context, not only sparse counters.
3. Sample list actions are obvious and usable.
4. Sample request history clearly communicates status and tracking.
5. Company/profile editing is understandable and safe.
6. Typography is comfortably readable at normal desktop scale.
7. Desktop and mobile layouts work without horizontal overflow.
8. Empty/loading/error states are deliberate.
9. No backend/schema/auth changes and no speculative features.
10. Deployed browser verification required before PASS.

### Flow
BUILD → TEST → VERIFY → PASS → NEXT

### Status
- BUILD: PENDING.
- TEST: BLOCKED until build.
- VERIFY: BLOCKED until test.
- PASS: NO.

### Next exact action
Read only `Hesabim.dc.html`, preserve all working behavior, then make the minimum safe UI/UX changes needed to meet the criteria above. Deploy and verify in browser before moving to the next task.
