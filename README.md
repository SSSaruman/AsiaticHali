# Asiatic Halı — v2 Katalog Güncellemesi (Claude Code / GitHub için)

Bu klasör **tam, çalışan sitedir** (tüm sayfalar, `support.js`, tüm görseller dahil). Doğrudan bir statik sunucuya veya GitHub'a yüklenebilir; giriş dosyası `index.html`. Önceki `paket/` klasörünün yerine geçer.

## Dosyalar
| Dosya | Durum |
|---|---|
| `Asiatic Hali.dc.html` | Güncellendi (ana sayfa) |
| `AtlasKatalog.dc.html` | Güncellendi (sayfa çevirmeli katalog, tüm koleksiyonlar için `?c=<id>`) |
| `Koleksiyon.dc.html` | **Yeni** (koleksiyon sayfası, `?c=<id>`) |
| `assets/catalog/**` | **Yeni** (24 koleksiyon, asiatic.co.uk'den alınan halı görselleri + `catalog.json`) |
| `yedek/Asiatic Hali eski.dc.html` | Değişiklik öncesi yedek |
| `Kataloglar.dc.html` | **Silindi** (liste sayfası kaldırıldı; paket içinde de silin) |

Çalışma için değişmeyen dosyalar: `support.js`, `image-slot.js`, `assets/atlas|collections|hero|model|bg|logo-*`.

## Ana sayfa değişiklikleri
- Menü: Anasayfa, Koleksiyonlar, Katalog, Hakkımızda, İş Modeli, İletişim (TR/EN). Çözümler, Toptan, Üretim, Numuneler menüden çıktı. Üretim bölümü (`#s05`) sayfada duruyor.
- Hero: "Trade Supply · FOB · Consolidation Service", "From Gaziantep to London and Beyond." (TR: "Gaziantep’ten Londra’ya ve Ötesine."), 1000+ SKUs in range (1000+, Türkiye, 1960 bold ve ortalı). Ticari hesap butonu kaldırıldı. Başlık puntosu küçültüldü.
- "Open a trade" butonu (header, footer, mobil menü) Shopify müşteri girişi linkine gider.
- Çözümler (`#s01b`) ve Toptan (`#s04`) bölümleri silindi. Yerine Hakkımızda / Misyonumuz / Vizyonumuz (`#s04a`, about.html içeriği, EN birebir, TR çeviri; kartlar sırayla animasyonla gelir).
- Katalog (`#s03`): önceki "Seçilmiş Halılar". İki seviyeli filtre yerine üstte grup filtresi (Tümü, Dokulu, Tasarım, Heritage, Doğal Dokuma, Uzun Havlı, Düz). Her koleksiyon bir kart, kartta "Koleksiyonu gör" → `Koleksiyon.dc.html?c=<id>`. Numune butonları kaldırıldı.
- Koleksiyon modalı: sadece "Kataloğu aç" (fiyat listesi / ticari talep butonları kaldırıldı).
- Numune ve fiyat listesi butonları (header, kartlar, mobil, modal) kaldırıldı.
- İş modeli: üretici kartlarında "Türkiye", merkez yazısı ("Konsolidasyon merkezi" etiketi kaldırıldı, başlık küçültüldü ve konumu `hubCopyOuterStyle` ile ayarlı), bina görseli 10 px yukarıda.
- Üretim bölümü: 700+ ve rakam tablosu ile "Lima Rust" bandı kaldırıldı.
- Tüm sitede sağ tık ve metin seçimi kapalı (form alanları hariç).
- 700+ → 1000+ tüm yerlerde (kayan yazı, sayaç, Neden Asiatic).

## Katalog (AtlasKatalog.dc.html)
- `?c=<koleksiyon-id>` ile çalışır, `#<halı-handle>` ile belirli halıdan başlar (Atlas'ta `#sage`, `#navy` gibi renk adı).
- Her halı kendi kitapçığı: kapak, bilgi sayfası (boyut, malzeme, hav, dokuma, menşe), iç görseller, arka kapak. Son sayfada ileri → sağdan sonraki halı kayarak gelir; ilk sayfada geri → önceki halı.
- Altta ortalı halı şeridi, üstte "Koleksiyonlar ▾" açılır menüsü (iki sütun).
- Veri kaynağı: gömülü `CATALOG` sabiti (aynısı `assets/catalog/catalog.json`).

## Notlar / bilinen noktalar
- Görseller asiatic.co.uk CDN'inden indirildi (koleksiyon başına en fazla 10 halı). Kullanım izni sahibine aittir.
- Mobil sürümde katalog listesi eski düzende, Hakkımızda eklenmedi.
- İletişim formu Supabase `contact_requests` tablosuna yazar (e-posta göndermez). Taşımada Supabase Auth → URL Configuration'a yeni alan adını ekleyin.
- `Koleksiyon.dc.html` yalnızca Türkçe.
- Dosya adları `.dc.html`; yayınlarken `support.js` ile birlikte aynı klasörde olmalı.
