# CURRENT TASK

## P0 — Admin core data contract must match Supabase

### Previous gate
`Admin login` is PASS on the deployed GitHub Pages site.

Verified in browser:
- Recovery email redirects to deployed `AdminReset.html`.
- Password reset form accepts the recovery session.
- Admin credentials create a valid Supabase session.
- `profiles.is_admin=true` is recognized and the admin panel becomes visible.
- A non-admin site session is denied admin access.
- Logout returns to the login flow.

### Active target
Fix only the existing `Admin.dc.html` ↔ Supabase schema mismatches that make core admin data appear empty or save invalid fields. Do not expand CRM/UI scope.

### Verified root causes
- `profiles` table has column `company`, while `Admin.dc.html` requests/reads `company_name`.
- `sample_requests` has `shipping_tracking_no`, while `Admin.dc.html` requests/updates `courier_ref`.
- Valid request statuses are `new`, `approved`, `preparing`, `shipped`, `delivered`, `cancelled`; current admin UI still uses legacy `requested`.
- RLS admin policies already exist; this is not an RLS absence issue.
- Database currently contains one profile only: the admin profile. No real customer profile has been created yet.

### Acceptance criteria
1. Company/customer list query uses real `profiles` columns and does not fail on nonexistent fields.
2. Request detail query uses `shipping_tracking_no`.
3. Status control uses exactly the DB status contract.
4. Status/tracking save writes only valid DB columns/values.
5. Existing login/auth/RLS behavior remains unchanged.
6. Deployed browser test shows no false `Firmalar (0)` caused by query failure; with only the admin profile present, data behavior is explained correctly and no fake customer is created.

### Flow
BUILD → TEST → VERIFY → PASS → NEXT

### Status
FAIL — root cause verified; minimum frontend fix pending.
