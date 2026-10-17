# Current Task

## 01_GLOBAL_UI_UX_FIXES
Status: CODE REVIEW COMPLETE — LIVE QA PENDING

Code-level pass (2026-09-12): grep across the whole file for responsive anti-patterns (fixed px widths, `white-space:nowrap` without ellipsis, `overflow-x`, non-`minmax` grid tracks) found none — layout is `clamp()`/`%`/`vw` throughout, `grid-template-columns` switches via a measured-container `desktop` flag (`box.clientWidth >= 1081`, not `window.innerWidth`, so it's correct inside the DC's own scroller). No unwrapped nowrap text found outside intentional truncation (ellipsis labels) or a marquee ticker.
Still pending: an actual live 320/375/768/1024/1440/1920 screenshot pass — flag anything the verifier's screenshot catches at its own width, and fix from that evidence rather than further code guessing.

## 02_COLLECTION_MODAL
Status: NOT COMPLETE

- Uygulandı: scroll reset on open, prev/next nav + counter, sticky CTA footer split (modalBodyStyle/modalScrollStyle/modalFooterStyle), mobile full-screen sheet (100dvh).
- Son kaydedilen düzeltme: mobile modalMediaStyle artık sabit height+maxHeight+overflow:hidden (görsel grid satırını şişirip footer'ı kart dışına itiyordu — bu düzeltildi).
- Pending: final verification (scroll=0 on open + on prev/next, no double-scroll, sheet no overflow, counter correct, ESC/overlay/close, desktop close-button spacing too tight to panel corner — not yet fixed).
- Next session: resume from this file, finish verification, fix close-button spacing if still an issue, then mark 02_COLLECTION_MODAL: COMPLETE before moving to 03.

## 04_RANGE_BUILDER
Status: CODE COMPLETE — LIVE VERIFICATION PENDING

- Uygulandı: PRODUCTS'a gerçek colours[] eklendi, group+colour eşleşmesi düzeltildi (yoksa group-only fallback + görünür validation note). Adım rozetleri (1–4 → Result) eklendi. "View matching lines" CTA #s03'e filtreyle scroll ediyor (setState callback içinde). "Add to sample list" CTA functional setState ile stale-closure riski giderilmiş şekilde yeniden yazıldı.
- Pending: verifier'dan canlı doğrulama sonucu dönmedi (timeout/no response). Kod tarafında bilinen açık sorun yok; bir sonraki oturumda ready_for_verification tekrar çağrılıp sonuç alınmalı, sorun çıkarsa düzeltilip 04_RANGE_BUILDER: COMPLETE ile kapatılmalı.

## 06_CONTACT_FORM
Status: CODE COMPLETE — LIVE VERIFICATION PENDING

- Uygulandı: koyu bölüm kontrast düzeltmesi (başlık/gövde/link renkleri), label/checkbox okunabilirliği artırıldı, mailto kaldırıldı — gerçek Supabase REST insert (contact_requests tablosu, anon key). Client validation (name/email/phone/consent) + hata state (veri kaybolmuyor) + loading + double-submit guard + success state (client-side referans no, Prefer: return=minimal — SELECT grant gerektirmiyor).
- Supabase tarafı: tablo + RLS insert policy + anon GRANT INSERT kullanıcı tarafından çalıştırıldı; canlı insert kullanıcı tarafından ayrıca doğrulandı.
- Pending: verifier'dan son turda sonuç dönmedi (timeout/no response). Bilinen açık sorun yok; sıradaki oturumda ready_for_verification tekrar çağrılıp sonuç alınmalı, sorun çıkarsa düzeltilip 06_CONTACT_FORM: COMPLETE ile kapatılmalı.

## 07_BUSINESS_MODEL
Status: CODE COMPLETE — LIVE VERIFICATION PENDING

- Uygulandı: diyagram genişliği/oranları büyütüldü (modelCols, max-width), rota çizgileri #a55a34'e koyulaştırıldı + kalınlaştırıldı + görünürlük artırıldı (opacity .2→.85), 3 dal ucuna ok işareti eklendi (arrowDrop3/2/Left + arrowStyle animasyonu), producer/hub/output kart tipografisi büyütüldü ve kontrastı artırıldı (desktop + mobile).
- Pending: verifier'dan sonuç dönmedi (timeout/no response). Bilinen açık sorun yok; sıradaki oturumda ready_for_verification tekrar çağrılıp sonuç alınmalı, sorun çıkarsa düzeltilip 07_BUSINESS_MODEL: COMPLETE ile kapatılmalı.

## 08_SELECTED_RUGS_FILTER_STATE
Status: CODE COMPLETE — LIVE VERIFICATION PENDING

- Uygulandı: n>1 carousel (mevcut davranış), n=1 tek kart ortalanmış statik layout (oklar + drag gizli/no-op), n=0 empty-state + "tüm halıları gör" reset CTA. Filtre satırında canlı sonuç sayısı etiketi (rugCountLabel). rugDown artık isCarousel false ise no-op.
- Pending: verifier'dan sonuç dönmedi (timeout/no response). Bilinen açık sorun yok; sıradaki oturumda ready_for_verification tekrar çağrılıp sonuç alınmalı, sorun çıkarsa düzeltilip 08_SELECTED_RUGS_FILTER_STATE: COMPLETE ile kapatılmalı.

## 09_COLLECTIONS
Status: CODE COMPLETE — LIVE VERIFICATION PENDING

- Uygulandı: yan karta tıklayınca o kart merkeze geliyor (pointerEvents:auto + cursor:pointer + onClick tüm görünür kartlarda; aktif kart hâlâ modal açıyor), aktif kart altı gradient hafifletildi (ürün görseli daha görünür), progress groove kontrastı artırıldı, wrapStyle'daki duplicate transition temizlendi.
- Pending: verifier'dan sonuç dönmedi (timeout/no response). Bilinen açık sorun yok; sıradaki oturumda ready_for_verification tekrar çağrılıp sonuç alınmalı, sorun çıkarsa düzeltilip 09_COLLECTIONS: COMPLETE ile kapatılmalı.

## 10_WHOLESALE
Status: CODE COMPLETE — LIVE VERIFICATION PENDING

- Uygulandı (s04 Built for Trade): ilk viewport'a güçlü CTA eklendi ("Toptan fiyat iste" → #s10 contact form'a scroll), altına MOQ/dispatch/stock/samples fact strip eklendi (görünürlük erken). Sektör tab'larına hover background tint eklendi (tıklanabilirlik daha net); active/inactive state ve 2x2 kart okunabilirliği zaten yeterliydi, değiştirilmedi (minimum-change).
- Pending: verifier'dan sonuç dönmedi (timeout/no response). Bilinen açık sorun yok; sıradaki oturumda ready_for_verification tekrar çağrılıp sonuç alınmalı, sorun çıkarsa düzeltilip 10_WHOLESALE: COMPLETE ile kapatılmalı.

## 11_PRODUCTION
Status: CODE COMPLETE — LIVE VERIFICATION PENDING

- Uygulandı (s05 Why Asiatic/Craft lens): touch drag-to-zoom eklendi (touch-action:none + onTouchStart/Move/End, aynı lens state'ini kullanıyor), stat satırları (1.221/321/3) artık tek paylaşılan grid'de (display:contents row wrapper) hizalı, sağ metin kolonu genişletildi (craftGridCols 1.1/0.95 → 1/1.05, max-width 520→600px) sağdaki boşluk azaltıldı.
- Pending: verifier'dan sonuç dönmedi (timeout/no response). Bilinen açık sorun yok; sıradaki oturumda ready_for_verification tekrar çağrılıp sonuç alınmalı, sorun çıkarsa düzeltilip 11_PRODUCTION: COMPLETE ile kapatılmalı.

## 12_HOME_HERO
Status: CODE COMPLETE — LIVE VERIFICATION PENDING

- Uygulandı (s01 Hero): eyebrow pill-badge'e çevrildi (hedef müşteri/trade sinyali daha net), başlık/açıklamaya text-shadow eklendi (kontrast güvencesi), secondary CTA (Ticari hesap açın) alt çizili text-link'e indirgendi — primary CTA belirgin baskın, alt beyaz fade yüksekliği/kapsamı azaltıldı (12%→8%, strip fade daralttırıldı), istatistik sayıları için backing plate güçlendirildi (daha erken opak, halı dokusundan ayrışma artırıldı). Mevcut görsel dil korunmuş, redesign yapılmamış (DS/Nocturne bundle'ları bilerek kullanılmadı — görev "mevcut onaylı görsel dili bozma" diyor).
- Pending: verifier'dan sonuç dönmedi (timeout/no response). Bilinen açık sorun yok; sıradaki oturumda ready_for_verification tekrar çağrılıp sonuç alınmalı, sorun çıkarsa düzeltilip 12_HOME_HERO: COMPLETE ile kapatılmalı.

## 14_ACCOUNT_PANEL
Status: CODE COMPLETE — LIVE VERIFICATION PENDING

Hesabım ayrı bir sayfaya taşındı: `Hesabim.dc.html` (müşteri hesap paneli — Genel Bakış, Numune Listem, Numune Taleplerim, Firma Bilgileri + şifre değiştirme) ve `Admin.dc.html` (Asiatic personel paneli — kayıtlı firmalar listesi + firma detayında numune talepleri/durum güncelleme, ayrıca tüm iletişim taleplerinin listesi). Ana sayfadaki (Asiatic Hali.dc.html) "Hesabım" dropdown'ı kaldırıldı, artık `Hesabim.dc.html`'e link veriyor. Oturum `ah_auth` localStorage anahtarıyla sayfalar arası paylaşılıyor; guest numune listesi artık `{id,name}` olarak persist ediliyor (Hesabim sayfası PRODUCTS kataloğuna ihtiyaç duymadan isimleri gösterebiliyor).

GEREKLİ SUPABASE DEĞİŞİKLİKLERİ (kullanıcı tarafından SQL editor'de çalıştırılmalı — kod tarafı hazır, bunlar olmadan ilgili özellik sessizce boş/başarısız döner):
1. `profiles` tablosuna `phone text`, `address text`, `is_admin boolean default false` kolonları eklenmeli.
2. Firma Bilgileri kaydetmenin çalışması için: `profiles` üzerinde kullanıcının kendi satırını UPDATE edebildiği bir RLS policy (`using (auth.uid() = id)`).
3. Admin panelinin firmaları/talepleri görebilmesi için: `profiles`, `sample_requests`, `sample_request_items`, `contact_requests` tablolarında admin bypass RLS policy'leri — örn. `using ((select is_admin from profiles where id = auth.uid()) = true)` ile SELECT (ve sample_requests için UPDATE, çünkü admin panelinden durum/kargo no güncelleniyor).
4. En az bir kullanıcının `profiles.is_admin = true` yapılması (admin panelinden giriş yapabilmesi için).
5. contact_requests şu an sadece INSERT policy'sine sahip (audit'te not edilmişti) — admin SELECT policy'si eklenmeden "İletişim Talepleri" sekmesi boş görünür.

Next: canlı doğrulama, ardından kullanıcı Supabase tarafını uyguladıktan sonra admin/firma akışının uçtan uca testi.

## 15_EMAIL_VERIFICATION_UX
Status: CODE COMPLETE — SUPABASE DASHBOARD CONFIG PENDING (kullanıcı tarafında)

Signup/login akışına doğrulama state machine'i eklendi (idle / signup_success_pending_verification / login_unverified / verified / auth_error) — hem ana sayfadaki auth modal'da (Asiatic Hali.dc.html) hem Hesabim.dc.html'de. Kayıt sonrası email doğrulaması bekleniyorsa hata gösterilmiyor; "E-postanızı doğrulayın" ekranı açılıyor (Maili doğrula / Doğrulama mailini tekrar gönder / Doğrulamayı kontrol et / Girişe dön). Doğrulanmamış hesapla giriş denemesi de aynı ekrana düşüyor, jenerik "giriş başarısız" hatası göstermiyor. Sayfa yenilendiğinde localStorage'daki oturumun `email_confirmed_at` alanı kontrol ediliyor; yoksa hesap paneli açılmıyor, doğrulama ekranı açılıyor.

YAPILAMAYAN KISIM (Supabase Dashboard'da elle yapılmalı — koddan erişilemez):
- Authentication → URL Configuration → Site URL ve Redirect URLs listesine deployment domain'i (ve varsa localhost:3000) eklenmeli, yoksa doğrulama linki kullanıcıyı hiçbir yere veya yanlış yere yönlendirir.
- Bu proje tek sayfalık DC dosyaları olarak çalıştığı için ayrı bir `/auth/callback` route yok; Supabase'in email template'indeki confirmation linki confirm sonrası kullanıcıyı `Hesabim.dc.html`'e (veya sitenin barındırıldığı asıl URL'e) yönlendirecek şekilde ayarlanmalı. Link tıklandığında uygulama açık değilse veya callback başarısızsa kullanıcı boş sayfa görebilir — bu, uygulama kodunun değil, dashboard/redirect ayarının kapsamı.
- `checkVerified` düğmesi bu boşluğu bir ölçüde kapatıyor: kullanıcı linke tıkladıktan sonra uygulamaya dönüp "Doğrulamayı kontrol et"e basarak devam edebilir.


## 13_SOLUTIONS
Status: CODE COMPLETE — LIVE VERIFICATION PENDING

- Doğrulama akışı yanıt vermedi (timeout/no response). Yeni kod değişikliği yapılmadı.
- Next session: ready_for_verification tekrar çağrılıp sonuç alınmalı; sorun çıkarsa düzeltilip 13_SOLUTIONS: COMPLETE ile kapatılmalı.
