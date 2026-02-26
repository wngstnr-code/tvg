# Tugas Mata Kuliah Teknologi Basis Data

**Topik:** Database Model Jaringan & Hierarki, serta Standar SQL Terbaru

---

## 1. Apakah Database Model Jaringan (Network) dan Hierarki (Hierarchical) Masih Dipakai Sampai Saat Ini?

**Ya, keduanya masih dipakai**, namun sangat terbatas dan hanya pada konteks tertentu. Keduanya sudah digantikan oleh model Relasional (RDBMS) sebagai pilihan utama sejak tahun 1980-an.

### A. Model Hierarki

- **Struktur:** Data berbentuk pohon (tree) — satu parent punya banyak child, tapi tiap child hanya punya satu parent.
- **Contoh:** IBM IMS, Windows Registry, LDAP, struktur folder di OS, XML/JSON.
- **Masih dipakai?** Ya — terutama IBM IMS di perusahaan besar (perbankan, pemerintah) karena sistem legacy yang terlalu mahal untuk dimigrasi.
- **Kekurangan:** Tidak fleksibel untuk relasi many-to-many, redundansi tinggi, dan sulit diubah strukturnya.

### B. Model Jaringan

- **Struktur:** Mirip hierarki, tapi satu child bisa punya banyak parent (berbentuk graf). Standar: CODASYL.
- **Contoh:** Broadcom IDMS, Raima RDM.
- **Masih dipakai?** Ya — di beberapa perusahaan besar yang masih pakai mainframe dan embedded systems.
- **Kekurangan:** Akses data navigasional (harus tahu struktur fisik), kompleks, dan sulit dipelihara.

### Kesimpulan

| Kriteria | Hierarki | Jaringan | Relasional (SQL) |
|----------|----------|----------|-------------------|
| Penggunaan saat ini | Legacy systems | Legacy & embedded | **Dominan** |
| Untuk sistem baru? | Hampir tidak | Sangat jarang | **Ya, mayoritas** |
| Alasan bertahan | Biaya migrasi tinggi | Biaya migrasi tinggi | Fleksibel & standar |

---

## 2. Standar SQL Terbaru

### SQL:2023 (ISO/IEC 9075:2023)

Standar terbaru, diterbitkan **Juni 2023** oleh ISO/IEC.

### Evolusi Standar SQL

| Standar | Tahun | Keterangan |
|---------|-------|------------|
| SQL-86 | 1986 | Versi pertama |
| SQL-92 | 1992 | SQL-2 |
| SQL:1999 | 1999 | SQL-3 |
| SQL:2003 | 2003 | — |
| SQL:2008 | 2008 | — |
| SQL:2011 | 2011 | — |
| SQL:2016 | 2016 | Standar major sebelumnya |
| **SQL:2023** | **2023** | **Terbaru** |

> **Catatan:** SQL:2019 hanya berupa koreksi (Technical Corrigendum) dari SQL:2016, bukan standar major baru.

### Fitur Baru Utama di SQL:2023

#### A. Dukungan JSON Native (SQL/JSON)

Perubahan terbesar — JSON kini menjadi **tipe data resmi** di SQL (sebelumnya hanya disimpan sebagai string).

Fungsi-fungsi baru: `JSON_TABLE()`, `JSON_OBJECT()`, `JSON_ARRAY()`, `JSON_VALUE()`, `JSON_EXISTS()`, `JSON_SERIALIZE()`, dll.

**Contoh:**
```sql
-- Membuat objek JSON
SELECT JSON_OBJECT('nama': nama, 'umur': umur) FROM mahasiswa;

-- Membaca nilai dari JSON
SELECT JSON_VALUE(data, '$.alamat.kota') FROM pelanggan;
```

#### B. Property Graph Queries (SQL/PGQ)

Fitur **baru sepenuhnya** — memungkinkan query graf langsung di SQL tanpa perlu database graf terpisah.

**Contoh:**
```sql
SELECT *
FROM GRAPH_TABLE (my_graph
    MATCH (p:Person)-[k:KENAL]->(t:Person)
    WHERE p.nama = 'Budi'
    COLUMNS (p.nama AS orang, t.nama AS teman)
);
```

#### C. Fungsi Baru Lainnya

| Fungsi | Keterangan |
|--------|------------|
| `GREATEST()` / `LEAST()` | Nilai terbesar/terkecil dari daftar — akhirnya resmi standar |
| `LPAD()` / `RPAD()` | Padding string kiri/kanan |
| `LTRIM()` / `RTRIM()` | Trim spesifik kiri/kanan |
| `ANY_VALUE()` | Nilai sembarang dari grup agregasi |

### Perbandingan: SQL:2016 vs SQL:2023

| Aspek | SQL:2016 | SQL:2023 |
|-------|----------|----------|
| JSON | Dukungan dasar | **Tipe data native + fungsi lengkap** |
| Graph Query | Tidak ada | **SQL/PGQ** |
| Fungsi string | Terbatas | **+ LPAD, RPAD, LTRIM, RTRIM** |
| GREATEST/LEAST | Belum standar | **Resmi standar** |

---

## Daftar Referensi

1. Connolly, T. M., & Begg, C. E. (2015). *Database Systems: A Practical Approach to Design, Implementation, and Management* (6th ed.). Pearson Education.
2. Elmasri, R., & Navathe, S. B. (2016). *Fundamentals of Database Systems* (7th ed.). Pearson.
3. ISO/IEC 9075:2023. *Information technology — Database languages — SQL*. International Organization for Standardization.
4. Michels, J.-E., Kulkarni, K., Zemke, F., & Hammerschmidt, B. (2024). The New Features of SQL:2023. *ACM SIGMOD Record*, 53(1), 38–49.
