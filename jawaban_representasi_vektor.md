# Representasi Bentuk Geometris dalam Gambar Vektor

## Berdasarkan Presentasi "Programmer's View" — Overview of Graphics Systems

---

## Konsep Dasar dari Presentasi

Berdasarkan presentasi, representasi objek dalam grafika komputer menggunakan metode **VERTEX**:

- **Vertex (titik)**: Sebuah titik dalam ruang 2D atau 3D.
- **Edge (sisi)**: Menghubungkan dua vertex.
- **Connectivity (konektivitas)**: Informasi yang mendefinisikan vertex mana yang terhubung dengan vertex lainnya melalui edge.

Format model file (seperti contoh persegi panjang di slide):
```
v [jumlah vertex] e [jumlah edge]
[koordinat vertex 1]
[koordinat vertex 2]
...
[konektivitas edge: vertex_awal vertex_akhir]
```

---

## 1. Lingkaran (Circle)

### Asumsi:
- Pusat lingkaran: **(cx, cy) = (0, 0)**
- Jari-jari: **r = 5**
- Lingkaran diaproksimasi menggunakan **poligon reguler** dengan **n = 36 vertex** (setiap 10°)
- Semakin banyak vertex, semakin halus tampilan lingkaran

### Representasi Vektor:
Karena lingkaran bukan poligon, dalam grafika vektor kita mengaproksimasi lingkaran sebagai **poligon reguler dengan banyak sisi**.

**Rumus vertex:**
```
x_i = cx + r * cos(i * 2π / n)
y_i = cy + r * sin(i * 2π / n)
```
untuk i = 0, 1, 2, ..., n-1

**Model file:**
```
v 36 e 36
5.000  0.000       ← vertex 1 (i=0, sudut 0°)
4.924  0.868       ← vertex 2 (i=1, sudut 10°)
4.698  1.710       ← vertex 3 (i=2, sudut 20°)
...                 (dst. hingga vertex 36)
1 2                 ← edge menghubungkan vertex 1 ke 2
2 3                 ← edge menghubungkan vertex 2 ke 3
...
36 1                ← edge menghubungkan vertex 36 kembali ke 1 (menutup lingkaran)
```

### Persamaan Matematis:
$$x^2 + y^2 = r^2$$

---

## 2. Elips (Ellipse)

### Asumsi:
- Pusat elips: **(cx, cy) = (0, 0)**
- Semi-major axis (sumbu panjang): **a = 7**
- Semi-minor axis (sumbu pendek): **b = 4**
- Diaproksimasi menggunakan **n = 36 vertex** (setiap 10°)

### Representasi Vektor:
Sama seperti lingkaran, elips diaproksimasi sebagai poligon dengan banyak sisi, tetapi menggunakan dua jari-jari berbeda (a dan b).

**Rumus vertex:**
```
x_i = cx + a * cos(i * 2π / n)
y_i = cy + b * sin(i * 2π / n)
```
untuk i = 0, 1, 2, ..., n-1

**Model file:**
```
v 36 e 36
7.000  0.000       ← vertex 1
6.894  0.694       ← vertex 2
6.578  1.368       ← vertex 3
...                 (dst. hingga vertex 36)
1 2
2 3
...
36 1                ← menutup elips
```

### Persamaan Matematis:
$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$

---

## 3. Pentagon (Segi Lima Beraturan)

### Asumsi:
- Pusat pentagon: **(cx, cy) = (0, 0)**
- Jari-jari lingkaran luar (circumradius): **r = 5**
- Pentagon memiliki tepat **5 vertex** dan **5 edge**
- Vertex pertama dimulai dari atas (sudut 90°)

### Representasi Vektor:
Pentagon adalah poligon reguler sehingga dapat langsung direpresentasikan dengan vertex dan edge tanpa aproksimasi.

**Rumus vertex:**
```
x_i = cx + r * cos(90° + i * 360° / 5)
y_i = cy + r * sin(90° + i * 360° / 5)
```
untuk i = 0, 1, 2, 3, 4

**Model file:**
```
v 5 e 5
0.000   5.000      ← vertex 1 (atas)
-4.755  1.545      ← vertex 2 (kiri atas)
-2.939 -4.045      ← vertex 3 (kiri bawah)
2.939  -4.045      ← vertex 4 (kanan bawah)
4.755   1.545      ← vertex 5 (kanan atas)
1 2
2 3
3 4
4 5
5 1                 ← menutup pentagon
```

### Sudut Interior:
$$\text{Sudut interior} = \frac{(5-2) \times 180°}{5} = 108°$$

---

## 4. Kubus (Cube) — Proyeksi 3D ke 2D

### Asumsi:
- Kubus 3D dengan panjang sisi: **s = 4**
- Pusat kubus di origin **(0, 0, 0)**
- Kubus memiliki **8 vertex** dan **12 edge**
- Untuk menampilkan di layar 2D, digunakan **proyeksi isometrik** (sesuai konsep Viewing di slide 47)
- Offset untuk kedalaman: faktor 0.4 dari panjang sisi

### Representasi Vektor:
Kubus adalah objek 3D, sehingga perlu diproyeksikan ke 2D. Menurut presentasi (slide 47), kita menggunakan parameter kamera untuk memetakan 3D ke 2D (view volume → image plane).

**Vertex 3D:**
```
Vertex 1: (-2, -2, -2)    Vertex 5: (-2, -2,  2)
Vertex 2: ( 2, -2, -2)    Vertex 6: ( 2, -2,  2)
Vertex 3: ( 2,  2, -2)    Vertex 7: ( 2,  2,  2)
Vertex 4: (-2,  2, -2)    Vertex 8: (-2,  2,  2)
```

**Model file (3D):**
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
1 2    ← sisi depan bawah
2 3    ← sisi depan kanan
3 4    ← sisi depan atas
4 1    ← sisi depan kiri
5 6    ← sisi belakang bawah
6 7    ← sisi belakang kanan
7 8    ← sisi belakang atas
8 5    ← sisi belakang kiri
1 5    ← penghubung depan-belakang
2 6
3 7
4 8
```

---

## Ringkasan

| Bentuk    | Jumlah Vertex | Jumlah Edge | Tipe Representasi                  |
|-----------|:------------:|:-----------:|-------------------------------------|
| Lingkaran | 36 (aprox.)  | 36          | Poligon reguler (aproksimasi)       |
| Elips     | 36 (aprox.)  | 36          | Poligon dengan 2 radii (aproksimasi)|
| Pentagon  | 5            | 5           | Poligon reguler (eksak)             |
| Kubus     | 8            | 12          | Wireframe 3D → proyeksi 2D         |

### Catatan:
- Sesuai presentasi (slide 18), metode **vertex** adalah metode paling umum untuk merepresentasikan objek dalam grafika komputer.
- **Connectivity** (konektivitas) penting karena menentukan bagaimana vertex dihubungkan (slide 18).
- Untuk bentuk melengkung (lingkaran, elips), digunakan **aproksimasi poligon** karena grafika vektor berbasis garis lurus.
- Kubus menggunakan representasi **wireframe** (slide 8, 59) sesuai konsep yang dibahas dalam presentasi.
