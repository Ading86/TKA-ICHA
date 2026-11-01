SQUAD SEMANGAT ICHAA - struktur project
==========================================
index.html                 -> halaman utama (buka langsung di browser / hosting)
assets/characters/         -> TARUH GAMBAR KARAKTER DI SINI
build.py                   -> gabungkan jadi 1 file (dist/ichaa-squad.html)

NAMA FILE (ganti file lama dengan nama yang sama):
  levi.webp  eren.webp  nouzen.webp  mikasa.webp  akame.webp  lena.webp
Kalau memakai format lain (mis. levi.png), ubah nama file di bagian FILES pada index.html.

SARAN GAMBAR
- PNG/WebP dengan latar TRANSPARAN (render/sticker karakter), menghadap depan
- Setengah badan atau seluruh badan, lebar 600-900 px, di bawah ~300 KB per file
- Gambar dipakai untuk: avatar bulat di chat, notifikasi, dan stiker besar

ATUR CROP AVATAR
Di index.html cari konstanta K: p = posisi wajah ("50% 14%" = tengah, 14% dari atas),
z = zoom dalam %. Naikkan z untuk lebih dekat, ubah p agar wajah pas di lingkaran.

BUILD SATU FILE
  python build.py   (hasil: dist/ichaa-squad.html, gambar sudah tertanam)
