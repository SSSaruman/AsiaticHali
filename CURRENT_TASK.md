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
- `profiles` table has column `company`, while old `Admin.dc.html` requested/read `company_name`.
- `sample_requests` has `shipping_tracking_no`, while old `Admin.dc.html` requested/updated `courier_ref`.
- Valid request statuses are `new`, `approved`, `preparing`, `shipped`, `delivered`, `cancelled`; old admin UI used legacy `requested`.
- RLS admin policies already exist; this is not an RLS absence issue.
- Database currently contains one profile only: the admin profile. No fake customer profile will be created for this gate.

### Minimum safe change built
- Company query/render now uses `profiles.company`.
- Request query/render/save now uses `sample_requests.shipping_tracking_no`.
- Status select now contains exactly: `new`, `approved`, `preparing`, `shipped`, `delivered`, `cancelled`.
- Status change save passes the selected value directly, avoiding stale state on immediate save.
- Removed the false UI hint claiming an admin RLS policy was missing.
- Login/auth/RLS logic was not refactored.

### Targeted static verification
- Current `main` source was re-fetched after commit and contains the corrected profile query, request query, tracking save field and status mapping.
- Supabase schema was checked directly and matches these field/status names.

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
- BUILD: PASS
- TEST: pending deployed browser refresh
- VERIFY: pending browser result
- PASS: NO

### Next exact action
Refresh deployed `Admin.dc.html` after GitHub Pages picks up commit `6f6185cf3015ffefb7ad0f586eed1d12a0172999`. The list should no longer be falsely empty because of a nonexistent `company_name` column. With the current database state, the single admin profile may appear as the only profile. Do not create fake customer data for this gate.
