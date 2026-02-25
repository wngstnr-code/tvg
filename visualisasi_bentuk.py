"""
Visualisasi Bentuk Geometris sebagai Gambar Vektor
===================================================
Berdasarkan presentasi "Programmer's View" — Overview of Graphics Systems

Setiap bentuk direpresentasikan menggunakan metode VERTEX:
- Vertex: titik-titik dalam ruang 2D/3D
- Edge: garis yang menghubungkan vertex
- Connectivity: informasi hubungan antar vertex

Menghasilkan 4 file SVG + 1 gambar gabungan PNG.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import math

# ============================================================
# KONFIGURASI
# ============================================================
CIRCLE_N = 36          # jumlah vertex untuk aproksimasi lingkaran
ELLIPSE_N = 36         # jumlah vertex untuk aproksimasi elips
CIRCLE_R = 5           # jari-jari lingkaran
ELLIPSE_A = 7          # semi-major axis elips
ELLIPSE_B = 4          # semi-minor axis elips
PENTAGON_R = 5         # circumradius pentagon
CUBE_SIDE = 4          # panjang sisi kubus


def generate_circle_vertices(cx, cy, r, n):
    """Menghasilkan vertex lingkaran menggunakan aproksimasi poligon reguler."""
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = cx + r * np.cos(angles)
    y = cy + r * np.sin(angles)
    return x, y, angles


def generate_ellipse_vertices(cx, cy, a, b, n):
    """Menghasilkan vertex elips dengan dua jari-jari berbeda."""
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = cx + a * np.cos(angles)
    y = cy + b * np.sin(angles)
    return x, y, angles


def generate_pentagon_vertices(cx, cy, r):
    """Menghasilkan 5 vertex pentagon beraturan, dimulai dari atas."""
    n = 5
    angles = np.array([np.pi / 2 + i * 2 * np.pi / n for i in range(n)])
    x = cx + r * np.cos(angles)
    y = cy + r * np.sin(angles)
    return x, y, angles


def generate_cube_vertices(s):
    """
    Menghasilkan 8 vertex kubus 3D dan memproyeksikan ke 2D
    menggunakan proyeksi isometrik sederhana.
    """
    half = s / 2
    # 8 vertex kubus dalam 3D
    vertices_3d = np.array([
        [-half, -half, -half],  # 0: kiri-bawah-depan
        [ half, -half, -half],  # 1: kanan-bawah-depan
        [ half,  half, -half],  # 2: kanan-atas-depan
        [-half,  half, -half],  # 3: kiri-atas-depan
        [-half, -half,  half],  # 4: kiri-bawah-belakang
        [ half, -half,  half],  # 5: kanan-bawah-belakang
        [ half,  half,  half],  # 6: kanan-atas-belakang
        [-half,  half,  half],  # 7: kiri-atas-belakang
    ])

    # 12 edge kubus (pasangan indeks vertex)
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),  # muka depan
        (4, 5), (5, 6), (6, 7), (7, 4),  # muka belakang
        (0, 4), (1, 5), (2, 6), (3, 7),  # penghubung depan-belakang
    ]

    # Proyeksi isometrik: rotasi 30° pada sumbu X dan 45° pada sumbu Y
    angle_x = np.radians(35.264)  # arctan(1/√2)
    angle_y = np.radians(45)

    # Matriks rotasi Y
    Ry = np.array([
        [ np.cos(angle_y), 0, np.sin(angle_y)],
        [0,                1, 0               ],
        [-np.sin(angle_y), 0, np.cos(angle_y)],
    ])

    # Matriks rotasi X
    Rx = np.array([
        [1, 0,                 0                ],
        [0, np.cos(angle_x), -np.sin(angle_x)],
        [0, np.sin(angle_x),  np.cos(angle_x)],
    ])

    # Terapkan transformasi: Rx · Ry · vertex
    projected = (Rx @ Ry @ vertices_3d.T).T

    # Ambil koordinat x dan y saja (proyeksi ortografik)
    x_2d = projected[:, 0]
    y_2d = projected[:, 1]

    return x_2d, y_2d, vertices_3d, edges


def plot_shape(ax, title, x, y, vertices_label=True, edges=None,
               vertex_indices=None, color='#2196F3', fill_alpha=0.1,
               show_formula=None):
    """Menggambar bentuk vektor pada subplot."""

    ax.set_title(title, fontsize=14, fontweight='bold', pad=12)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.axhline(y=0, color='gray', linewidth=0.5, alpha=0.5)
    ax.axvline(x=0, color='gray', linewidth=0.5, alpha=0.5)

    if edges is not None:
        # Gambar edge dari daftar pasangan indeks (untuk kubus)
        for i, j in edges:
            ax.plot([x[i], x[j]], [y[i], y[j]], '-', color=color,
                    linewidth=2, zorder=2)
    else:
        # Gambar edge berurutan + menutup poligon
        x_closed = np.append(x, x[0])
        y_closed = np.append(y, y[0])
        ax.plot(x_closed, y_closed, '-', color=color, linewidth=2, zorder=2)

        # Fill
        ax.fill(x, y, alpha=fill_alpha, color=color, zorder=1)

    # Gambar vertex
    ax.scatter(x, y, color='#F44336', s=30, zorder=3, edgecolors='white',
               linewidth=0.5)

    # Label vertex
    if vertices_label and len(x) <= 10:
        for idx in range(len(x)):
            label = f"V{idx+1}\n({x[idx]:.1f}, {y[idx]:.1f})"
            offset_x = 0.3 if x[idx] >= 0 else -0.3
            offset_y = 0.3 if y[idx] >= 0 else -0.3
            ax.annotate(label, (x[idx], y[idx]),
                        textcoords="offset points",
                        xytext=(15 * np.sign(offset_x), 10 * np.sign(offset_y)),
                        fontsize=6, color='#333333',
                        ha='left' if x[idx] >= 0 else 'right')

    # Gambar pusat
    ax.plot(0, 0, 'k+', markersize=10, markeredgewidth=1.5, zorder=4)

    if show_formula:
        ax.text(0.05, 0.95, show_formula, transform=ax.transAxes,
                fontsize=8, verticalalignment='top',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow',
                          edgecolor='gray', alpha=0.9),
                fontfamily='monospace')


def create_model_file(filename, vertices, edges_list, is_3d=False):
    """Membuat model file dalam format yang dibahas di presentasi."""
    n_v = len(vertices)
    n_e = len(edges_list)

    with open(filename, 'w') as f:
        f.write(f"# Model file (format dari presentasi Programmer's View)\n")
        f.write(f"v {n_v} e {n_e}\n")
        f.write(f"# Vertices:\n")
        for v in vertices:
            if is_3d:
                f.write(f"{v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")
            else:
                f.write(f"{v[0]:.4f} {v[1]:.4f}\n")
        f.write(f"# Edges (connectivity):\n")
        for e in edges_list:
            f.write(f"{e[0]} {e[1]}\n")

    print(f"  Model file disimpan: {filename}")


def main():
    print("=" * 60)
    print("VISUALISASI BENTUK GEOMETRIS SEBAGAI GAMBAR VEKTOR")
    print("Berdasarkan presentasi 'Programmer's View'")
    print("=" * 60)

    # --------------------------------------------------------
    # 1. LINGKARAN
    # --------------------------------------------------------
    print(f"\n1. LINGKARAN")
    print(f"   Pusat: (0,0), Jari-jari: {CIRCLE_R}, Vertex: {CIRCLE_N}")
    cx, cy, _ = generate_circle_vertices(0, 0, CIRCLE_R, CIRCLE_N)

    circle_verts = list(zip(cx, cy))
    circle_edges = [(i + 1, (i + 1) % CIRCLE_N + 1) for i in range(CIRCLE_N)]
    create_model_file("/Users/mac/Downloads/tvg/model_lingkaran.txt",
                      circle_verts, circle_edges)

    # --------------------------------------------------------
    # 2. ELIPS
    # --------------------------------------------------------
    print(f"\n2. ELIPS")
    print(f"   Pusat: (0,0), a={ELLIPSE_A}, b={ELLIPSE_B}, Vertex: {ELLIPSE_N}")
    ex, ey, _ = generate_ellipse_vertices(0, 0, ELLIPSE_A, ELLIPSE_B, ELLIPSE_N)

    ellipse_verts = list(zip(ex, ey))
    ellipse_edges = [(i + 1, (i + 1) % ELLIPSE_N + 1) for i in range(ELLIPSE_N)]
    create_model_file("/Users/mac/Downloads/tvg/model_elips.txt",
                      ellipse_verts, ellipse_edges)

    # --------------------------------------------------------
    # 3. PENTAGON
    # --------------------------------------------------------
    print(f"\n3. PENTAGON")
    print(f"   Pusat: (0,0), Circumradius: {PENTAGON_R}")
    px, py, _ = generate_pentagon_vertices(0, 0, PENTAGON_R)

    pentagon_verts = list(zip(px, py))
    pentagon_edges = [(i + 1, (i % 5) + 1 + 1 if i < 4 else 1) for i in range(5)]
    # Perbaiki edge: 1-2, 2-3, 3-4, 4-5, 5-1
    pentagon_edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)]
    create_model_file("/Users/mac/Downloads/tvg/model_pentagon.txt",
                      pentagon_verts, pentagon_edges)

    # --------------------------------------------------------
    # 4. KUBUS
    # --------------------------------------------------------
    print(f"\n4. KUBUS")
    print(f"   Panjang sisi: {CUBE_SIDE}, Proyeksi isometrik ke 2D")
    kx, ky, verts_3d, cube_edges = generate_cube_vertices(CUBE_SIDE)

    cube_verts_3d = [tuple(v) for v in verts_3d]
    cube_edges_model = [(e[0] + 1, e[1] + 1) for e in cube_edges]
    create_model_file("/Users/mac/Downloads/tvg/model_kubus.txt",
                      cube_verts_3d, cube_edges_model, is_3d=True)

    # ============================================================
    # VISUALISASI
    # ============================================================
    print("\n" + "=" * 60)
    print("Membuat visualisasi...")

    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    fig.suptitle("Representasi Bentuk Geometris dalam Gambar Vektor\n"
                 "(Berdasarkan Presentasi 'Programmer\\'s View')",
                 fontsize=16, fontweight='bold', y=0.98)

    # --- Lingkaran ---
    ax1 = axes[0, 0]
    plot_shape(ax1, f"1. LINGKARAN\n({CIRCLE_N} vertex, {CIRCLE_N} edge)",
               cx, cy, vertices_label=False, color='#2196F3', fill_alpha=0.15,
               show_formula=f"x² + y² = r²\nr = {CIRCLE_R}\nn = {CIRCLE_N} vertex")
    # Gambar jari-jari
    ax1.annotate('', xy=(CIRCLE_R, 0), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    ax1.text(CIRCLE_R / 2, -0.5, f'r = {CIRCLE_R}', color='red', fontsize=9,
             ha='center')

    # --- Elips ---
    ax2 = axes[0, 1]
    plot_shape(ax2, f"2. ELIPS\n({ELLIPSE_N} vertex, {ELLIPSE_N} edge)",
               ex, ey, vertices_label=False, color='#4CAF50', fill_alpha=0.15,
               show_formula=f"x²/a² + y²/b² = 1\na = {ELLIPSE_A}, b = {ELLIPSE_B}\nn = {ELLIPSE_N} vertex")
    # Gambar sumbu
    ax2.annotate('', xy=(ELLIPSE_A, 0), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    ax2.text(ELLIPSE_A / 2, -0.7, f'a = {ELLIPSE_A}', color='red', fontsize=9,
             ha='center')
    ax2.annotate('', xy=(0, ELLIPSE_B), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='purple', lw=1.5))
    ax2.text(0.5, ELLIPSE_B / 2, f'b = {ELLIPSE_B}', color='purple', fontsize=9,
             ha='left')

    # --- Pentagon ---
    ax3 = axes[1, 0]
    plot_shape(ax3, f"3. PENTAGON\n(5 vertex, 5 edge)",
               px, py, vertices_label=True, color='#FF9800', fill_alpha=0.15,
               show_formula=f"Sudut interior = 108°\nr = {PENTAGON_R}")
    # Gambar circumradius
    ax3.annotate('', xy=(px[0], py[0]), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='red', lw=1.5,
                                 linestyle='dashed'))
    ax3.text(px[0] / 2 + 0.3, py[0] / 2, f'r = {PENTAGON_R}', color='red',
             fontsize=9)

    # --- Kubus ---
    ax4 = axes[1, 1]
    plot_shape(ax4, f"4. KUBUS (Proyeksi Isometrik)\n(8 vertex, 12 edge)",
               kx, ky, vertices_label=True, edges=cube_edges,
               color='#9C27B0', fill_alpha=0.0,
               show_formula=f"Sisi = {CUBE_SIDE}\nProyeksi 3D → 2D\n8 vertex, 12 edge")

    plt.tight_layout(rect=[0, 0, 1, 0.94])

    output_path = "/Users/mac/Downloads/tvg/visualisasi_bentuk_vektor.png"
    plt.savefig(output_path, dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"\nGambar disimpan: {output_path}")

    # Juga simpan sebagai SVG (true vector format)
    svg_path = "/Users/mac/Downloads/tvg/visualisasi_bentuk_vektor.svg"
    plt.savefig(svg_path, format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"SVG disimpan:    {svg_path}")

    plt.show()

    # ============================================================
    # RINGKASAN
    # ============================================================
    print("\n" + "=" * 60)
    print("RINGKASAN REPRESENTASI VEKTOR")
    print("=" * 60)
    print(f"{'Bentuk':<12} {'Vertex':>8} {'Edge':>6}  {'Tipe'}")
    print("-" * 52)
    print(f"{'Lingkaran':<12} {CIRCLE_N:>8} {CIRCLE_N:>6}  Poligon reguler (aproksimasi)")
    print(f"{'Elips':<12} {ELLIPSE_N:>8} {ELLIPSE_N:>6}  Poligon 2-radii (aproksimasi)")
    print(f"{'Pentagon':<12} {5:>8} {5:>6}  Poligon reguler (eksak)")
    print(f"{'Kubus':<12} {8:>8} {12:>6}  Wireframe 3D → proyeksi 2D")
    print()
    print("File yang dihasilkan:")
    print("  - jawaban_representasi_vektor.md  (dokumen jawaban)")
    print("  - visualisasi_bentuk_vektor.png   (gambar visualisasi)")
    print("  - visualisasi_bentuk_vektor.svg   (gambar vektor SVG)")
    print("  - model_lingkaran.txt             (model file lingkaran)")
    print("  - model_elips.txt                 (model file elips)")
    print("  - model_pentagon.txt              (model file pentagon)")
    print("  - model_kubus.txt                 (model file kubus)")


if __name__ == "__main__":
    main()
