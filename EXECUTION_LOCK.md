# EXECUTION LOCK

## ÇALIŞMA ANAYASASI — SAPMA YASAK

Bu dosya bağlayıcıdır. `CURRENT_TASK.md` dışında aktif iş yoktur.

1. Kullanıcının verdiği geometri, oran, sıra, adet, stil, referans, ölçü, üretim yöntemi ve onaylı kararlar SPECIFICATION’dır. Yorumlama, yeniden tasarlama veya yaratıcı ekleme yapma.
2. Onaylanan kararlar LOCKED’dır. Kullanıcı açıkça değiştirmedikçe değiştirme. Yalnız istenen şeyi değiştir; geri kalan her şeyi koru.
3. En kısa güvenli yolu kullan. Gereksiz refactor, abstraction, yeniden yazım, entegrasyon, servis, özellik veya “ileride lazım olur” geliştirmesi YASAK.
4. Aynı anda yalnızca bir aktif hedef vardır. `CURRENT_TASK.md` tek aktif kaynaktır. Yeni fikirler aktif işi kesmez; BACKLOG’a gider.
5. Akış zorunludur: BUILD → TEST → VERIFY → PASS → NEXT. Bir aşama PASS olmadan diğerine geçme. FAIL varsa yalnız kök nedeni düzelt, targeted test yap ve aynı aşamayı tekrar doğrula.
6. “Neredeyse çalışıyor”, “muhtemelen tamam”, “büyük ölçüde hazır” PASS değildir. Tamamlandı demek için kod çalışmış, test edilmiş ve acceptance criteria geçmiş olmalıdır.
7. Koddan önce varsa sırayla oku: `EXECUTION_LOCK.md` → `CURRENT_TASK.md` → `PROJECT_STATE.md` → `DECISIONS.md` → gerektiğinde `ARCHITECTURE.md`. Full repo taraması yapma; yalnız gerekli dosyaları oku.
8. Varsayılan prensip MINIMUM SAFE CHANGE. Çalışan sistemi gereksiz yere yeniden kurma. P0 hata varken yeni özellik geliştirme.
9. Kullanıcıya değer veya gelire doğrudan katkısı olmayan kodu yazma. MVP için zorunlu değilse yapma.
10. UI yalnız mevcut akışı tamamlayacak kadar yapılır. Dashboard, polish, animasyon, admin, CRM, affiliate, enterprise özellikleri doğrulanmadan eklenmez.
11. Gerçek kullanım oluşmadan ölçek optimizasyonu, microservice, Kubernetes, karmaşık queue/cache veya enterprise mimarisi kurma.
12. Ücretli servis/provider eklemeden önce zorunluluk, alternatif, gerçek maliyet ve kullanıcı başına maliyeti ölç. Free tier → usage based → gelir sonrası ölçekleme önceliklidir.
13. AI/provider seçimini tahminle değil; kalite, fidelity, retry oranı, latency ve gerçek maliyet ölçümüyle yap.
14. Harici servislerde timeout, quota, provider down, malformed output, generation failure, duplicate request, payment failure, upload failure ve retry failure senaryolarını kapsa.
15. Ödeme, credit ve AI generation işlemleri idempotent olmalı; çift request çift ödeme/credit/generation yaratmamalı.
16. Free kullanımda quota, rate limit, maximum retry ve server-side usage accounting zorunludur.
17. Kritik state kaybolmamalı. Job durumu, provider/model, maliyet, retry, hata ve PASS/FAIL nedeni kaydedilmeli.
18. Gerçek ürün sadakati estetikten önce gelir. Ürünün formu, rengi, logosu, materyali veya bileşenleri değişirse FAIL.
19. Ölçülmemiş sonuçlar için “satışı artırır”, “en iyi”, “%X daha fazla dönüşüm” gibi kanıtsız sonuç iddiaları kullanma.

## MUTLAK YASAKLAR
- Kontrol etmeden “kontrol ettim” deme.
- TEST + VERIFY olmadan “düzeldi”, “tamamlandı” veya PASS deme.
- Kullanıcıyı oyalama, süreci uzatma, aktif görevden başka yöne gitme.
- Boş görev, gereksiz kod, gereksiz test altyapısı, gereksiz geliştirme üretme.
- Mimariyi veya onaylı akışı kafana göre değiştirme.
- FAIL varken başka hedefe geçme.
- Kullanıcı bir eksik/hata gösterdiğinde önce o eksik/hatanın kök nedenini çöz; başka geliştirmeye sapma.

## UYGULAMA KURALI
Her turda önce `CURRENT_TASK.md` içindeki tek aktif hedefe bak. Yalnız gerekli dosyayı aç. Minimum değişikliği yap. Targeted test et. Gerçek sonucu doğrula. PASS değilse aynı hedefte kal.