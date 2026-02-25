# TUGAS: Representasi Bentuk Geometris dalam Gambar Vektor

**Mata Kuliah:** Teknik Visualisasi Grafika  
**Materi:** Programmer's View — Overview of Graphics Systems  
**Nama:** _(isi nama Anda)_  
**NIM:** _(isi NIM Anda)_  
**Tanggal:** 26 Februari 2026

---

## Soal

Untuk setiap bentuk geometris berikut, tentukan bagaimana merepresentasikannya menggunakan gambar vektor:
1. Lingkaran
2. Elips
3. Pentagon
4. Kubus

---

## Landasan Teori

Berdasarkan materi presentasi "Programmer's View", metode yang paling umum untuk merepresentasikan objek dalam grafika komputer adalah **metode vertex** (slide 18). Objek didefinisikan sebagai kumpulan titik (**vertex**) beserta informasi hubungan antar titik (**connectivity**) melalui sisi (**edge**).

Terdapat tiga komponen utama:
- **Vertex** — titik dalam ruang 2D atau 3D
- **Edge** — garis yang menghubungkan dua vertex
- **Connectivity** — informasi yang mendefinisikan vertex mana saja yang saling terhubung

Dalam presentasi, format model file diberikan sebagai berikut (slide 19):

```
v [jumlah_vertex] e [jumlah_edge]
[koordinat vertex 1]
[koordinat vertex 2]
...
[edge: vertex_awal vertex_akhir]
```

---

## Jawaban

### 1. Lingkaran (Circle)

**Asumsi yang digunakan:**
- Pusat lingkaran: (cx, cy) = (0, 0)
- Jari-jari: r = 5
- Karena lingkaran adalah kurva, maka diaproksimasi menggunakan poligon reguler dengan n = 36 vertex (interval sudut 10°). Semakin banyak vertex, semakin halus bentuk lingkaran.

**Penjelasan representasi:**

Lingkaran bukan poligon, sehingga tidak dapat direpresentasikan secara eksak hanya dengan vertex dan edge (garis lurus). Oleh karena itu, lingkaran diaproksimasi sebagai **poligon reguler dengan banyak sisi**. Setiap vertex ditempatkan pada keliling lingkaran dengan jarak sudut yang sama.

**Rumus untuk menghitung posisi setiap vertex:**

```
x_i = cx + r × cos(i × 2π / n)
y_i = cy + r × sin(i × 2π / n)
```

dengan i = 0, 1, 2, ..., n−1

**Persamaan matematis lingkaran:**

```
x² + y² = r²
```

**Contoh model file (3 vertex pertama ditampilkan):**

```
v 36 e 36
5.0000  0.0000       ← vertex 1  (sudut 0°)
4.9240  0.8682       ← vertex 2  (sudut 10°)
4.6985  1.7101       ← vertex 3  (sudut 20°)
...                    (dan seterusnya hingga vertex 36)
1 2
2 3
3 4
...
36 1                   ← edge terakhir menutup lingkaran kembali ke vertex 1
```

**Jumlah komponen:** 36 vertex, 36 edge

---

### 2. Elips (Ellipse)

**Asumsi yang digunakan:**
- Pusat elips: (cx, cy) = (0, 0)
- Semi-major axis (sumbu panjang): a = 7
- Semi-minor axis (sumbu pendek): b = 4
- Diaproksimasi menggunakan n = 36 vertex (interval sudut 10°)

**Penjelasan representasi:**

Elips merupakan generalisasi dari lingkaran dengan dua jari-jari berbeda. Sama seperti lingkaran, elips diaproksimasi sebagai poligon dengan banyak sisi. Perbedaannya terletak pada penggunaan dua parameter radius (a dan b) pada sumbu yang berbeda.

**Rumus untuk menghitung posisi setiap vertex:**

```
x_i = cx + a × cos(i × 2π / n)
y_i = cy + b × sin(i × 2π / n)
```

dengan i = 0, 1, 2, ..., n−1

**Persamaan matematis elips:**

```
x²/a² + y²/b² = 1
```

**Contoh model file (3 vertex pertama ditampilkan):**

```
v 36 e 36
7.0000  0.0000       ← vertex 1  (sudut 0°)
6.8940  0.6946       ← vertex 2  (sudut 10°)
6.5778  1.3681       ← vertex 3  (sudut 20°)
...                    (dan seterusnya hingga vertex 36)
1 2
2 3
3 4
...
36 1                   ← menutup elips
```

**Jumlah komponen:** 36 vertex, 36 edge

---

### 3. Pentagon (Segi Lima Beraturan)

**Asumsi yang digunakan:**
- Pusat pentagon: (cx, cy) = (0, 0)
- Jari-jari lingkaran luar (circumradius): r = 5
- Pentagon memiliki tepat 5 vertex dan 5 edge
- Vertex pertama dimulai dari posisi atas (sudut 90°)

**Penjelasan representasi:**

Pentagon adalah poligon reguler dengan 5 sisi, sehingga dapat direpresentasikan **secara eksak** menggunakan vertex dan edge tanpa perlu aproksimasi. Kelima vertex ditempatkan dengan jarak sudut yang sama (72° antar vertex) pada circumradius.

**Rumus untuk menghitung posisi setiap vertex:**

```
x_i = cx + r × cos(90° + i × 360° / 5)
y_i = cy + r × sin(90° + i × 360° / 5)
```

dengan i = 0, 1, 2, 3, 4

**Sudut interior pentagon:**

```
Sudut interior = ((5 − 2) × 180°) / 5 = 108°
```

**Model file (lengkap):**

```
v 5 e 5
 0.0000   5.0000     ← vertex 1 (atas)
-4.7553   1.5451     ← vertex 2 (kiri atas)
-2.9389  -4.0451     ← vertex 3 (kiri bawah)
 2.9389  -4.0451     ← vertex 4 (kanan bawah)
 4.7553   1.5451     ← vertex 5 (kanan atas)
1 2
2 3
3 4
4 5
5 1                    ← menutup pentagon
```

**Jumlah komponen:** 5 vertex, 5 edge

---

### 4. Kubus (Cube) — Proyeksi 3D ke 2D

**Asumsi yang digunakan:**
- Panjang sisi kubus: s = 4
- Pusat kubus di titik origin (0, 0, 0)
- Kubus memiliki 8 vertex dan 12 edge
- Untuk menampilkan di layar 2D, digunakan **proyeksi isometrik** (sesuai konsep Viewing pada slide 47 presentasi)

**Penjelasan representasi:**

Kubus adalah objek 3D. Berdasarkan presentasi (slide 47), untuk menampilkan objek 3D di layar 2D diperlukan proses **viewing** yang memetakan 3D ke 2D melalui proyeksi. Representasi menggunakan format wireframe (kerangka kawat) di mana semua vertex dan edge ditampilkan sebagai garis-garis (sesuai konsep di slide 8 dan 59).

Kubus memiliki:
- **6 muka** (face), masing-masing berupa persegi
- **8 vertex** di sudut-sudut kubus
- **12 edge** yang menghubungkan vertex-vertex tersebut

**Koordinat 8 vertex dalam ruang 3D:**

```
Vertex 1: (-2, -2, -2)       Vertex 5: (-2, -2,  2)
Vertex 2: ( 2, -2, -2)       Vertex 6: ( 2, -2,  2)
Vertex 3: ( 2,  2, -2)       Vertex 7: ( 2,  2,  2)
Vertex 4: (-2,  2, -2)       Vertex 8: (-2,  2,  2)
```

**Model file (lengkap):**

```
v 8 e 12
-2 -2 -2
 2 -2 -2
 2  2 -2
-2  2 -2
-2 -2  2
 2 -2  2
 2  2  2
-2  2  2
1 2        ← edge muka z = -2
2 3
3 4
4 1
5 6        ← edge muka z = +2
6 7
7 8
8 5
1 5        ← edge penghubung antar muka (kedalaman)
2 6
3 7
4 8
```

**Jumlah komponen:** 8 vertex, 12 edge

---

## Ringkasan

| No | Bentuk    | Vertex | Edge | Tipe Representasi                     |
|----|-----------|:------:|:----:|---------------------------------------|
| 1  | Lingkaran |   36   |  36  | Poligon reguler (aproksimasi kurva)   |
| 2  | Elips     |   36   |  36  | Poligon dengan 2 radii (aproksimasi)  |
| 3  | Pentagon  |    5   |   5  | Poligon reguler (representasi eksak)  |
| 4  | Kubus     |    8   |  12  | Wireframe 3D dengan proyeksi ke 2D    |

---

## Kesimpulan

Berdasarkan materi presentasi "Programmer's View":

1. **Metode vertex** merupakan cara paling umum untuk merepresentasikan objek dalam grafika komputer (slide 18). Setiap objek didefinisikan melalui kumpulan vertex dan informasi connectivity-nya.

2. Untuk bentuk **melengkung** (lingkaran dan elips), tidak dapat direpresentasikan secara eksak hanya dengan garis lurus, sehingga digunakan **aproksimasi poligon** dengan jumlah sisi yang cukup banyak (dalam tugas ini 36 sisi).

3. Untuk bentuk **poligon** (pentagon), representasi vertex dan edge bersifat **eksak** — tepat 5 vertex dan 5 edge sudah cukup.

4. Untuk bentuk **3D** (kubus), diperlukan proses **viewing/proyeksi** dari ruang 3D ke bidang gambar 2D (slide 47). Representasi wireframe menampilkan seluruh vertex dan edge objek.

---

## Lampiran: Visualisasi

Visualisasi keempat bentuk geometris dibuat menggunakan Python (matplotlib) dan tersedia pada file `visualisasi_bentuk.py`. Hasil visualisasi menunjukkan vertex (titik merah), edge (garis biru/hijau/oranye/ungu), serta parameter masing-masing bentuk.

File pendukung:
- `visualisasi_bentuk.py` — kode sumber Python untuk visualisasi
- `visualisasi_bentuk_vektor.png` — hasil visualisasi (format raster)
- `visualisasi_bentuk_vektor.svg` — hasil visualisasi (format vektor)
- `model_lingkaran.txt` — model file lingkaran
- `model_elips.txt` — model file elips
- `model_pentagon.txt` — model file pentagon
- `model_kubus.txt` — model file kubus
