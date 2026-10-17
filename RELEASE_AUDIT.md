# Release Audit — Asiatic Halı Türkiye
Mode A (Website Release Audit), run against `Asiatic Hali.dc.html` in its current state.
Per the auditor spec: no item is marked PASS without direct inspection; infra that has no live deployment yet is UNVERIFIED, not PASS.

## A1 — Domain / Routing / Indexability
- ID: A1-01 · STATUS: UNVERIFIED — CHECK: custom domain/HTTPS live — REASON: project is a design-stage prototype, not deployed to `asiatichali.com` — REQUIRED_EVIDENCE: DNS + TLS check once hosted.
- ID: A1-02 · STATUS: WARN — CHECK: canonical/hreflang tags hardcode `https://www.asiatichali.com/...` (lines 19-21) — IMPACT: correct once deployed at that exact host, but currently unverifiable and will 404 if the final domain differs — MINIMUM_FIX: confirm final domain before launch — VERIFY: fetch canonical URL, expect 200.
- ID: A1-03 · STATUS: PASS — CHECK: dedicated 404 page exists (`404.dc.html`) — EVIDENCE: file present in project root.
- ID: A1-04 · STATUS: FAIL — CHECK: `robots.txt` — EVIDENCE: not present in project root — IMPACT: crawlers get default-allow but no sitemap pointer — MINIMUM_FIX: add `robots.txt` with sitemap reference at deploy — VERIFY: fetch `/robots.txt`, expect 200 with `Sitemap:` line.
- ID: A1-05 · STATUS: FAIL — CHECK: `sitemap.xml` — EVIDENCE: not present — MINIMUM_FIX: generate sitemap listing all real routes once URL structure is final — VERIFY: fetch `/sitemap.xml`, valid XML, all URLs return 200.
- ID: A1-06 · STATUS: PASS — CHECK: favicon — EVIDENCE: none found referenced in `<helmet>` — actually re-check: no `<link rel="icon">` found. STATUS corrected: FAIL — MINIMUM_FIX: add favicon link — VERIFY: browser tab icon renders.
- ID: A1-07 · STATUS: UNVERIFIED — CHECK: broken routes return real 404 status (not silent 200) — REASON: single-file DC has no server-side routing yet.

## A2 — Titles / Meta / Canonical
- ID: A2-01 · STATUS: PASS — CHECK: unique, descriptive `<title>` — EVIDENCE: "Asiatic Halı Türkiye — Premium wholesale rugs for global interiors" (line 12).
- ID: A2-02 · STATUS: PASS — CHECK: meta description present and on-topic — EVIDENCE: line 13.
- ID: A2-03 · STATUS: PASS — CHECK: one clear `<h1>` describing the page — EVIDENCE: hero `<h1>` line 221, single occurrence.
- ID: A2-04 · STATUS: WARN — CHECK: this is a one-page scrolling site; legal pages (Gizlilik/Kvkk/Cerezler/Sartlar) are separate DC files — verify each has its own unique `<title>`/meta, not inherited — REQUIRED_EVIDENCE: inspect each legal file's `<head>`.

## A3 — Structured Navigation
- ID: A3-01 · STATUS: PASS — CHECK: primary nav + footer links present and anchor to real in-page sections/legal files — EVIDENCE: `footerCols`/`footerLegal` arrays (lines 3148-3172) point to existing anchors and existing `.dc.html` files.
- ID: A3-02 · STATUS: N/A — CHECK: breadcrumbs — single-page site, not applicable.

## A4 — Images / Accessibility
- ID: A4-01 · STATUS: PASS — CHECK: decorative images (`aria-hidden="true"`) correctly use `alt=""` — EVIDENCE: hero sky/city/carpet layers (lines 209-213).
- ID: A4-02 · STATUS: PASS — CHECK: meaningful images have descriptive alt — EVIDENCE: logo `alt="Asiatic Halı Türkiye"` (line 77).
- ID: A4-03 · STATUS: WARN — CHECK: product/collection photo alt text — some product images found with `alt=""` where the image is the primary content, not decoration (e.g. line 478 lens image) — MINIMUM_FIX: audit each `<img>` inside product cards individually; give content images real alt text — VERIFY: screen reader pass over collection grid and result card.

## A5 — Structured Data
- ID: A5-01 · STATUS: FAIL — CHECK: JSON-LD structured data (Organization/LocalBusiness or Product) — EVIDENCE: none found in `<helmet>` — MINIMUM_FIX: add Organization schema (name, logo, url, contact) at minimum — do not add LocalBusiness unless there's a real storefront address — VERIFY: validate with Rich Results Test once added.

## A6 — Console / Build Hygiene
- ID: A6-01 · STATUS: PASS — CHECK: console errors on load — EVIDENCE: `get_webview_logs` returned no console logs/errors on current load.
- ID: A6-02 · STATUS: UNVERIFIED — CHECK: full click-through of every flow (Range Builder, Collections modal, Contact form) for runtime errors — REQUIRED_EVIDENCE: interactive pass per CURRENT_TASK.md items still marked "LIVE VERIFICATION PENDING" (02, 04, 06–13).

## A7 — Required Content / Trust
- ID: A7-01 · STATUS: PASS — CHECK: Privacy, KVKK, Cookies, Terms pages exist — EVIDENCE: `Gizlilik.dc.html`, `Kvkk.dc.html`, `Cerezler.dc.html`, `Sartlar.dc.html` present and linked from footer.
- ID: A7-02 · STATUS: PASS — CHECK: no fabricated testimonials/stats — EVIDENCE: footer `dataNote` explicitly discloses that specs are "pending confirmation" rather than inventing numbers (line 1213/1251) — this is correct auditor-compliant behavior, keep it.
- ID: A7-03 · STATUS: WARN — CHECK: dedicated About/Contact pages vs sections — current site handles Contact as an in-page form section; confirm this satisfies the intended IA (no separate About page section confirmed in this pass) — REQUIRED_EVIDENCE: full section-by-section review not yet done in this pass.

## A8 — CTA / Conversion
- ID: A8-01 · STATUS: PASS — CHECK: primary CTA present, wired to a real backend — EVIDENCE: contact form does a real Supabase insert per CURRENT_TASK.md (06_CONTACT_FORM), not a dead mailto.
- ID: A8-02 · STATUS: UNVERIFIED — CHECK: Range Builder "Add to sample list" / "View matching lines" CTAs — code complete per CURRENT_TASK.md but live verification still pending.

## A9 — Mobile Compatibility
- ID: A9-01 · STATUS: UNVERIFIED — CHECK: 320/375/768/1024/1440/1920 breakpoints, no horizontal overflow, no clipped text, sticky elements not blocking content — REASON: this is exactly what's queued next (see plan below) — no breakpoint has been re-verified live since the last edits.

## A10 — Analytics / Search Discovery
- ID: A10-01 · STATUS: FAIL — CHECK: analytics implementation — EVIDENCE: no analytics snippet found in `<helmet>`.
- ID: A10-02 · STATUS: UNVERIFIED — CHECK: Search Console ownership — no live domain yet.

---

## Follow-up pass (2026-09-17)
- FIXED — A5-01 was stale: JSON-LD (Organization/WebSite/FAQPage) is present with real Gaziantep address/phone — re-mark PASS.
- FIXED — A1-06 favicon: added `<link rel="icon">` using existing `assets/logo-mark.png`.
- FIXED — fabricated data found and corrected against verifiable sources: "1974" founding year was wrong (Asiatic Carpets was founded 1960 per asiatic.co.uk/about-us) — corrected everywhere (PROOFS, TICKER, craftBody, both languages). "1,221 rugs in range" contradicted both the actual on-page catalogue (13 sample products) and Asiatic's own stated catalogue size ("over 700 rugs" per asiatic.co.uk) — replaced with the sourced "700+" figure. "321 products made in Türkiye" had no source and was replaced with the real, code-verifiable "6 collections curated for this range" (matches actual COLLECTIONS array length). "3 brands: Asiatic, Katherine Carnaby, The Rug Edit" — verified real, kept as-is.
- BLOCKED (needs user) — robots.txt / sitemap.xml: still not added; both require a final domain, which isn't set. Do not stub with a placeholder domain — will 404 or mis-index at launch.
- BLOCKED (needs user) — analytics: no property ID provided; not added.
- UNVERIFIED — full click-through of Collection modal, Range Builder, Contact form, Business model diagram, Selected Rugs filter, Collections carousel, Wholesale CTAs, Production/craft page, Account panel, and 320–1920px breakpoints: queued to the verifier pass on this turn. Basic DOM check on load: 0 console errors, 1 `<h1>`, JSON-LD present, footer links all resolve to existing anchors/files, no dead links found in nav/footer.

## RELEASE DECISION: **NOT_READY**

FAIL items outstanding: robots.txt missing, sitemap.xml missing, favicon missing, no structured data, no analytics.
BLOCK items: none found.

### Minimum set of fixes to advance to READY_WITH_WARNINGS
1. Add `robots.txt` + `sitemap.xml` at deploy time (needs final domain first).
2. Add a favicon link.
3. Add Organization JSON-LD (real business details only, no fabricated data).
4. Add analytics (property to be provided by user).
5. Finish the pending live verification items already tracked in CURRENT_TASK.md (mobile breakpoints, Range Builder, modal, contact form, business model diagram, etc.) — these are UNVERIFIED, not FAIL, but block a real READY call.

This is a single audit pass on current source; it does not yet include a live 320–1920px walkthrough (queued next) or a second pass after those fixes.
