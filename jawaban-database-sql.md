# Tugas Mata Kuliah Teknologi Basis Data

**Topik:** Database Model Jaringan & Hierarki, serta Standar SQL Terbaru

---

## 1. Apakah Database Model Jaringan (Network) dan Hierarki (Hierarchical) Masih Dipakai Sampai Saat Ini?

### Jawaban Singkat

**Ya, keduanya masih dipakai hingga saat ini**, namun dalam skala yang sangat terbatas dan pada konteks yang spesifik. Kedua model ini sudah **tidak lagi menjadi pilihan utama** dalam pengembangan sistem baru — posisi tersebut telah digantikan oleh model Relasional (RDBMS) sejak tahun 1980-an, serta model-model modern lainnya seperti Document Store, Graph Database, dan Key-Value Store.

---

### A. Model Hierarki (Hierarchical Database)

| Aspek | Keterangan |
|-------|------------|
| **Struktur** | Data disusun dalam bentuk pohon (tree) — satu parent memiliki banyak child, tapi setiap child hanya punya satu parent. |
| **Contoh produk** | IBM IMS (Information Management System), Windows Registry |
| **Masih dipakai?** | **Ya, tapi sangat terbatas.** |

**Di mana masih dipakai:**

1. **IBM IMS** — Masih berjalan di banyak perusahaan besar (perbankan, penerbangan, asuransi, pemerintah) terutama yang menggunakan mainframe IBM. Alasannya:
   - Sistem legacy yang sudah berjalan puluhan tahun dan terlalu mahal/berisiko untuk dimigrasi.
   - Performa sangat tinggi untuk transaksi volume besar (mampu memproses jutaan transaksi per detik).
   - IBM masih aktif memberikan dukungan dan update untuk IMS.

2. **Windows Registry** — Secara teknis menggunakan struktur hierarki (key-subkey-value) dan masih digunakan di setiap komputer Windows hingga hari ini.

3. **LDAP (Lightweight Directory Access Protocol)** — Digunakan untuk directory services (Active Directory, OpenLDAP) yang menyimpan data user, organisasi, dll dalam struktur pohon.

4. **File System** — Struktur folder/direktori di setiap sistem operasi pada dasarnya adalah model hierarki.

5. **Format data XML dan JSON** — Secara konseptual merepresentasikan data hierarkis.

**Mengapa sudah jarang dipakai untuk sistem baru:**
- Tidak fleksibel — sulit merepresentasikan relasi many-to-many.
- Redundansi data tinggi jika child perlu punya lebih dari satu parent.
- Query hanya efisien jika mengikuti jalur pohon (navigational access).
- Perubahan struktur data sangat sulit dilakukan.

---

### B. Model Jaringan (Network Database)

| Aspek | Keterangan |
|-------|------------|
| **Struktur** | Mirip hierarki, tapi satu child bisa punya banyak parent (graph/jaringan). Menggunakan konsep *owner-member* (set). |
| **Standar** | CODASYL (Conference on Data Systems Languages) |
| **Contoh produk** | CA IDMS, Raima RDM, TurboIMAGE (HP), DBMS-32 |
| **Masih dipakai?** | **Ya, tapi sangat terbatas.** |

**Di mana masih dipakai:**

1. **CA IDMS (sekarang Broadcom IDMS)** — Masih digunakan di sejumlah perusahaan besar (terutama di sektor keuangan dan pemerintahan) yang berjalan di mainframe. Broadcom masih menyediakan dukungan aktif.

2. **Raima RDM** — Masih dikembangkan dan digunakan untuk embedded systems, IoT, dan aplikasi yang membutuhkan database ringan dan cepat di perangkat edge.

3. **TurboIMAGE** — Beberapa organisasi yang masih menggunakan HP 3000 masih menjalankan database ini.

**Mengapa sudah jarang dipakai untuk sistem baru:**
- Akses data bersifat navigasional (programmer harus tahu struktur fisik data) — tidak deklaratif seperti SQL.
- Kompleksitas tinggi dalam desain dan pemeliharaan.
- Tightly coupled antara aplikasi dan struktur database.
- Kurangnya tenaga ahli baru yang menguasai model ini.

---

### Kesimpulan Model Hierarki & Jaringan

| Kriteria | Hierarki | Jaringan | Relasional (SQL) |
|----------|----------|----------|-------------------|
| Penggunaan saat ini | Legacy systems, mainframe | Legacy systems, embedded | **Dominan di industri** |
| Sistem baru? | Hampir tidak pernah | Sangat jarang | **Ya, mayoritas** |
| Alasan bertahan | Biaya migrasi tinggi, performa | Biaya migrasi tinggi | Fleksibel, standar, deklaratif |
| Masa depan | Terus menyusut | Terus menyusut | Tetap kuat + bersaing dengan NoSQL |

---

## 2. Standar SQL Terbaru

### Standar SQL Terbaru: **SQL:2023** (ISO/IEC 9075:2023)

Standar ini diterbitkan pada **Juni 2023** oleh ISO (International Organization for Standardization) dan IEC. Nama resminya adalah **ISO/IEC 9075:2023 — Information technology — Database languages — SQL**.

---

### Daftar Evolusi Standar SQL

| Standar | Tahun | Nama Populer |
|---------|-------|--------------|
| SQL-86 | 1986 | SQL-1 |
| SQL-89 | 1989 | SQL-1 (revisi minor) |
| SQL-92 | 1992 | SQL-2 |
| SQL:1999 | 1999 | SQL-3 |
| SQL:2003 | 2003 | — |
| SQL:2006 | 2006 | — |
| SQL:2008 | 2008 | — |
| SQL:2011 | 2011 | — |
| SQL:2016 | 2016 | — |
| SQL:2019 | 2019 | — (Technical Corrigendum) |
| **SQL:2023** | **2023** | **Terbaru** |

---

### Fitur Baru di SQL:2023 vs SQL:2016 (Standar Major Sebelumnya)

#### A. **Dukungan JSON yang Ditingkatkan Secara Signifikan (SQL/JSON)**

Ini adalah perubahan **paling besar** di SQL:2023.

| Fitur | Keterangan |
|-------|------------|
| `JSON` sebagai tipe data native | JSON sekarang menjadi tipe data SQL resmi (sebelumnya hanya disimpan sebagai string/CLOB). |
| `JSON_TABLE()` | Mengubah data JSON menjadi tabel relasional untuk di-query dengan SQL biasa. |
| `JSON_OBJECT()` | Membuat objek JSON dari data relasional. |
| `JSON_ARRAY()` | Membuat array JSON dari data relasional. |
| `JSON_OBJECTAGG()` | Fungsi agregasi untuk membangun objek JSON. |
| `JSON_ARRAYAGG()` | Fungsi agregasi untuk membangun array JSON. |
| `JSON_QUERY()` | Mengekstrak bagian JSON (mengembalikan JSON). |
| `JSON_VALUE()` | Mengekstrak nilai skalar dari JSON. |
| `JSON_EXISTS()` | Mengecek apakah path tertentu ada di dalam JSON. |
| `JSON_SCALAR()` | Membuat nilai JSON skalar. |
| `JSON_SERIALIZE()` | Mengonversi tipe JSON ke string. |
| `IS JSON` predicate | Mengecek apakah suatu nilai adalah JSON yang valid. |

**Contoh:**
```sql
-- Membuat objek JSON
SELECT JSON_OBJECT('nama': nama, 'umur': umur) FROM mahasiswa;

-- Membaca JSON
SELECT JSON_VALUE(data, '$.alamat.kota') FROM pelanggan;

-- JSON ke tabel
SELECT jt.*
FROM pesanan,
     JSON_TABLE(detail, '$[*]' COLUMNS (
         produk VARCHAR(100) PATH '$.nama',
         qty INT PATH '$.jumlah'
     )) AS jt;
```

---

#### B. **Property Graph Queries (SQL/PGQ)**

Fitur **baru sepenuhnya** di SQL:2023 — belum ada di standar sebelumnya.

| Fitur | Keterangan |
|-------|------------|
| `GRAPH_TABLE` | Mendefinisikan dan melakukan query terhadap graf (graph) yang disimpan di tabel relasional. |
| Pattern Matching pada Graf | Mencocokkan pola node dan edge seperti di bahasa graph (Neo4j/Cypher). |

**Contoh:**
```sql
SELECT *
FROM GRAPH_TABLE (my_graph
    MATCH (p:Person)-[k:KENAL]->(t:Person)
    WHERE p.nama = 'Budi'
    COLUMNS (p.nama AS orang, t.nama AS teman)
);
```

Ini memungkinkan query graf langsung di dalam SQL tanpa memerlukan database graf terpisah.

---

#### C. **Fungsi dan Fitur Baru Lainnya**

| Fitur | Keterangan |
|-------|------------|
| `ANY_VALUE()` | Fungsi agregasi yang mengembalikan nilai sembarang dari grup (berguna untuk kolom non-agregat di GROUP BY). |
| `GREATEST()` dan `LEAST()` | Mengembalikan nilai terbesar/terkecil dari daftar ekspresi — akhirnya distandarkan! |
| `LPAD()` dan `RPAD()` | Padding string kiri/kanan — sebelumnya hanya ekstensi vendor, sekarang resmi standar. |
| `LTRIM()`, `RTRIM()`, `BTRIM()` | Trim spesifik kiri/kanan/keduanya — sebelumnya hanya `TRIM()` yang standar. |
| Peningkatan `ORDER BY` di fungsi agregasi | `ARRAY_AGG(x ORDER BY y)` dan agregasi lainnya kini lebih konsisten. |
| `UNIQUE` predicate yang disederhanakan | Pengecekan keunikan yang lebih baik. |

---

#### D. **Perbandingan Ringkas: SQL:2016 vs SQL:2023**

| Aspek | SQL:2016 | SQL:2023 |
|-------|----------|----------|
| JSON | Dukungan dasar (SQL/JSON path, beberapa fungsi) | **Tipe data JSON native**, fungsi lengkap, JSON_TABLE, serialisasi |
| Graph Query | **Tidak ada** | **SQL/PGQ** — query graf terintegrasi |
| Fungsi string | Terbatas (TRIM, SUBSTRING, dll) | **+ LPAD, RPAD, LTRIM, RTRIM, BTRIM** |
| Fungsi agregasi | Standar | **+ ANY_VALUE()** |
| GREATEST/LEAST | **Tidak standar** (hanya ekstensi vendor) | **Resmi distandarkan** |
| Polymorphic Table Functions | Diperkenalkan | Tetap ada |
| Row Pattern Recognition | Diperkenalkan | Tetap ada |
| Multi-dimensional arrays | Terbatas | Peningkatan |

---

### Catatan Penting

- **SQL:2019** bukan standar major baru, melainkan **Technical Corrigendum** (koreksi/perbaikan) dari SQL:2016. Jadi perbandingan utama yang relevan adalah SQL:2016 → SQL:2023.
- Tidak semua RDBMS sudah mengimplementasikan seluruh fitur SQL:2023. PostgreSQL, Oracle, dan MySQL secara bertahap mengadopsi fitur-fitur ini. PostgreSQL termasuk yang paling cepat mengadopsi fitur JSON standar.
- SQL:2023 terdiri dari beberapa bagian (parts), termasuk:
  - Part 1: SQL/Framework
  - Part 2: SQL/Foundation
  - Part 4: SQL/PSM (Persistent Stored Modules)
  - Part 9: SQL/MED (Management of External Data)
  - Part 10: SQL/OLB (Object Language Bindings)
  - Part 13: SQL/JRT (Java Routines and Types)
  - Part 14: SQL/XML
  - Part 15: SQL/MDA (Multi-Dimensional Arrays)
  - **Part 16: SQL/PGQ** (Property Graph Queries) — **BARU**

---

---

## Daftar Referensi

1. Connolly, T. M., & Begg, C. E. (2015). *Database Systems: A Practical Approach to Design, Implementation, and Management* (6th ed.). Pearson Education.
2. Elmasri, R., & Navathe, S. B. (2016). *Fundamentals of Database Systems* (7th ed.). Pearson.
3. ISO/IEC 9075:2023. *Information technology — Database languages — SQL*. International Organization for Standardization.
4. IBM Corporation. (2024). *IMS - Overview*. https://www.ibm.com/products/ims
5. Broadcom Inc. (2024). *IDMS — Integrated Database Management System*. https://www.broadcom.com/products/mainframe/databases-database-mgmt/idms
6. Eisenberg, A., Melton, J., Kulkarni, K., Michels, J.-E., & Zemke, F. (2004). SQL:2003 Has Been Published. *ACM SIGMOD Record*, 33(1), 119–126.
7. Michels, J.-E., Kulkarni, K., Zemke, F., & Hammerschmidt, B. (2024). The New Features of SQL:2023. *ACM SIGMOD Record*, 53(1), 38–49.
8. PostgreSQL Global Development Group. (2024). *PostgreSQL Documentation — JSON Functions and Operators*. https://www.postgresql.org/docs/current/functions-json.html
