# CURRENT TASK

## P0 — Isolate admin session from customer/site session

### Previous gate
`Admin core data contract` is PASS on the deployed GitHub Pages site.

Verified in browser and code:
- `profiles` query now uses real `company` column.
- `sample_requests` uses `shipping_tracking_no`.
- Status control matches DB contract: `new`, `approved`, `preparing`, `shipped`, `delivered`, `cancelled`.
- Admin panel no longer shows false `Firmalar (0)` from schema-query failure; browser shows the one real profile currently present.
- No fake customer was created.

### Active target
Prevent the admin panel from reusing the public/customer session stored under `ah_auth`. Admin auth must have its own storage key so a logged-in customer cannot be mistaken for the active admin session.

### Verified root cause
`index.html`, `Hesabim.dc.html`, and `Admin.dc.html` all use the same localStorage key `ah_auth`. This caused the admin page to read the current site/customer user and show unauthorized until that session was manually cleared.

### Minimum safe change
Change only `Admin.dc.html` session persistence from `ah_auth` to `ah_admin_auth`. Do not modify public/customer auth behavior and do not expand UI/CRM scope.

### Acceptance criteria
1. Admin login stores session only in `ah_admin_auth`.
2. Admin reload restores from `ah_admin_auth`.
3. Admin logout removes only `ah_admin_auth`.
4. Public/customer `ah_auth` remains untouched.
5. Admin authorization/RLS behavior remains unchanged.
6. Browser test: customer/site session can remain logged in while admin panel independently authenticates and remains accessible after refresh.

### Flow
BUILD → TEST → VERIFY → PASS → NEXT

### Status
BUILD pending.
