# EXECUTION LOCK

## Locked working protocol
- User specifications and approved decisions are binding. Do not reinterpret geometry, ratios, order, quantity, style, references, dimensions, production method, or approved decisions.
- Change only the requested thing; preserve everything else.
- Use MINIMUM SAFE CHANGE. No unnecessary refactor, abstraction, rewrite, integration, service, feature, or speculative future work.
- One active target only. `CURRENT_TASK.md` is the active source of truth. New ideas go to backlog and do not interrupt the active task.
- Mandatory flow: BUILD → TEST → VERIFY → PASS → NEXT. FAIL means fix root cause only, run targeted test, verify the same stage again.
- No partial PASS language. A task is complete only after code runs and acceptance criteria pass.
- Read in order when present: `EXECUTION_LOCK.md` → `CURRENT_TASK.md` → `PROJECT_STATE.md` → `DECISIONS.md` → `ARCHITECTURE.md` only when needed. Never full-scan the repo by default.
- P0 defects block feature work.
- Do not build code without direct user/value impact. No enterprise-scale architecture before validated need.
- External providers must cover timeout/quota/down/malformed output/failure/duplicate/retry failure scenarios. Paid providers require necessity, alternative and cost review first.
- Critical state and PASS/FAIL reasons must be retained where applicable.
- UI only to complete the active flow; no unrelated dashboard/polish/animation/CRM expansion during a P0 fix.
