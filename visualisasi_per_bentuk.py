"""
Visualisasi Bentuk Geometris — Satu Bentuk per File
====================================================
Menghasilkan 4 file gambar terpisah:
  1. lingkaran.png
  2. elips.png
  3. pentagon.png
  4. kubus.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "/Users/mac/Downloads/tvg"

# ============================================================
# KONFIGURASI
# ============================================================
CIRCLE_R = 5
CIRCLE_N = 36
ELLIPSE_A = 7
ELLIPSE_B = 4
ELLIPSE_N = 36
PENTAGON_R = 5
CUBE_SIDE = 4


# ============================================================
# FUNGSI GENERATE VERTEX
# ============================================================

def circle_vertices(cx, cy, r, n):
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return cx + r * np.cos(angles), cy + r * np.sin(angles)


def ellipse_vertices(cx, cy, a, b, n):
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    return cx + a * np.cos(angles), cy + b * np.sin(angles)


def pentagon_vertices(cx, cy, r):
    angles = np.array([np.pi / 2 + i * 2 * np.pi / 5 for i in range(5)])
    return cx + r * np.cos(angles), cy + r * np.sin(angles)


def cube_projected(s):
    h = s / 2
    v3d = np.array([
        [-h, -h, -h], [h, -h, -h], [h, h, -h], [-h, h, -h],
        [-h, -h,  h], [h, -h,  h], [h, h,  h], [-h, h,  h],
    ])
    edges = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7),
    ]
    ax = np.radians(35.264)
    ay = np.radians(45)
    Ry = np.array([[np.cos(ay),0,np.sin(ay)],[0,1,0],[-np.sin(ay),0,np.cos(ay)]])
    Rx = np.array([[1,0,0],[0,np.cos(ax),-np.sin(ax)],[0,np.sin(ax),np.cos(ax)]])
    p = (Rx @ Ry @ v3d.T).T
    return p[:, 0], p[:, 1], v3d, edges


# ============================================================
# FUNGSI PLOT UMUM
# ============================================================

def setup_ax(ax, title):
    ax.set_title(title, fontsize=16, fontweight='bold', pad=14)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.axhline(y=0, color='gray', linewidth=0.5, alpha=0.5)
    ax.axvline(x=0, color='gray', linewidth=0.5, alpha=0.5)
    ax.plot(0, 0, 'k+', markersize=10, markeredgewidth=1.5, zorder=4)


def draw_polygon(ax, x, y, color, fill=True, label_verts=False):
    xc = np.append(x, x[0])
    yc = np.append(y, y[0])
    ax.plot(xc, yc, '-', color=color, linewidth=2, zorder=2)
    if fill:
        ax.fill(x, y, alpha=0.12, color=color, zorder=1)
    ax.scatter(x, y, color='#F44336', s=35, zorder=3,
               edgecolors='white', linewidth=0.5)
    if label_verts:
        for i in range(len(x)):
            lbl = f"V{i+1}\n({x[i]:.1f}, {y[i]:.1f})"
            ha = 'left' if x[i] >= 0 else 'right'
            ox = 14 if x[i] >= 0 else -14
            oy = 10 if y[i] >= 0 else -10
            ax.annotate(lbl, (x[i], y[i]), textcoords="offset points",
                        xytext=(ox, oy), fontsize=7, color='#333', ha=ha)


def draw_wireframe(ax, x, y, edges, color, label_verts=True):
    for i, j in edges:
        ax.plot([x[i], x[j]], [y[i], y[j]], '-', color=color, linewidth=2, zorder=2)
    ax.scatter(x, y, color='#F44336', s=35, zorder=3,
               edgecolors='white', linewidth=0.5)
    if label_verts:
        for i in range(len(x)):
            lbl = f"V{i+1}\n({x[i]:.1f}, {y[i]:.1f})"
            ha = 'left' if x[i] >= 0 else 'right'
            ox = 14 if x[i] >= 0 else -14
            oy = 10 if y[i] >= 0 else -10
            ax.annotate(lbl, (x[i], y[i]), textcoords="offset points",
                        xytext=(ox, oy), fontsize=7, color='#333', ha=ha)


def add_info_box(ax, text):
    ax.text(0.03, 0.97, text, transform=ax.transAxes, fontsize=9,
            verticalalignment='top',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow',
                      edgecolor='gray', alpha=0.9),
            fontfamily='monospace')


def save(fig, name):
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"  Disimpan: {path}")
    plt.close(fig)


# ============================================================
# 1. LINGKARAN
# ============================================================
def plot_lingkaran():
    x, y = circle_vertices(0, 0, CIRCLE_R, CIRCLE_N)
    fig, ax = plt.subplots(figsize=(8, 8))
    setup_ax(ax, f"LINGKARAN\n({CIRCLE_N} vertex, {CIRCLE_N} edge)")
    draw_polygon(ax, x, y, '#2196F3', fill=True, label_verts=False)

    # Jari-jari
    ax.annotate('', xy=(CIRCLE_R, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(CIRCLE_R / 2, -0.5, f'r = {CIRCLE_R}', color='red',
            fontsize=11, ha='center', fontweight='bold')

    add_info_box(ax,
        f"Persamaan:  x² + y² = r²\n"
        f"Pusat:      (0, 0)\n"
        f"Jari-jari:  r = {CIRCLE_R}\n"
        f"Vertex:     n = {CIRCLE_N}\n"
        f"Edge:       n = {CIRCLE_N}\n"
        f"Metode:     Aproksimasi poligon reguler")

    margin = CIRCLE_R * 1.4
    ax.set_xlim(-margin, margin)
    ax.set_ylim(-margin, margin)
    save(fig, "lingkaran.png")


# ============================================================
# 2. ELIPS
# ============================================================
def plot_elips():
    x, y = ellipse_vertices(0, 0, ELLIPSE_A, ELLIPSE_B, ELLIPSE_N)
    fig, ax = plt.subplots(figsize=(10, 7))
    setup_ax(ax, f"ELIPS\n({ELLIPSE_N} vertex, {ELLIPSE_N} edge)")
    draw_polygon(ax, x, y, '#4CAF50', fill=True, label_verts=False)

    # Semi-major axis
    ax.annotate('', xy=(ELLIPSE_A, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(ELLIPSE_A / 2, -0.6, f'a = {ELLIPSE_A}', color='red',
            fontsize=11, ha='center', fontweight='bold')

    # Semi-minor axis
    ax.annotate('', xy=(0, ELLIPSE_B), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='purple', lw=2))
    ax.text(0.5, ELLIPSE_B / 2, f'b = {ELLIPSE_B}', color='purple',
            fontsize=11, ha='left', fontweight='bold')

    add_info_box(ax,
        f"Persamaan:  x²/a² + y²/b² = 1\n"
        f"Pusat:      (0, 0)\n"
        f"Semi-major: a = {ELLIPSE_A}\n"
        f"Semi-minor: b = {ELLIPSE_B}\n"
        f"Vertex:     n = {ELLIPSE_N}\n"
        f"Edge:       n = {ELLIPSE_N}\n"
        f"Metode:     Aproksimasi poligon 2-radii")

    ax.set_xlim(-ELLIPSE_A * 1.4, ELLIPSE_A * 1.4)
    ax.set_ylim(-ELLIPSE_B * 1.8, ELLIPSE_B * 1.8)
    save(fig, "elips.png")


# ============================================================
# 3. PENTAGON
# ============================================================
def plot_pentagon():
    x, y = pentagon_vertices(0, 0, PENTAGON_R)
    fig, ax = plt.subplots(figsize=(8, 8))
    setup_ax(ax, "PENTAGON\n(5 vertex, 5 edge)")
    draw_polygon(ax, x, y, '#FF9800', fill=True, label_verts=True)

    # Circumradius
    ax.annotate('', xy=(x[0], y[0]), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='red', lw=2,
                                linestyle='dashed'))
    ax.text(x[0] / 2 + 0.4, y[0] / 2, f'r = {PENTAGON_R}', color='red',
            fontsize=11, fontweight='bold')

    add_info_box(ax,
        f"Pusat:           (0, 0)\n"
        f"Circumradius:    r = {PENTAGON_R}\n"
        f"Vertex:          5 (eksak)\n"
        f"Edge:            5\n"
        f"Sudut interior:  108°\n"
        f"Metode:          Poligon reguler (eksak)")

    margin = PENTAGON_R * 1.5
    ax.set_xlim(-margin, margin)
    ax.set_ylim(-margin, margin)
    save(fig, "pentagon.png")


# ============================================================
# 4. KUBUS
# ============================================================
def plot_kubus():
    x, y, v3d, edges = cube_projected(CUBE_SIDE)
    fig, ax = plt.subplots(figsize=(8, 8))
    setup_ax(ax, "KUBUS (Proyeksi Isometrik)\n(8 vertex, 12 edge)")
    draw_wireframe(ax, x, y, edges, '#9C27B0', label_verts=True)

    add_info_box(ax,
        f"Panjang sisi:  s = {CUBE_SIDE}\n"
        f"Vertex:        8\n"
        f"Edge:          12\n"
        f"Face:          6\n"
        f"Proyeksi:      Isometrik (3D → 2D)\n"
        f"Metode:        Wireframe + proyeksi")

    margin = CUBE_SIDE * 1.2
    ax.set_xlim(-margin, margin)
    ax.set_ylim(-margin, margin)
    save(fig, "kubus.png")


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("Membuat 4 gambar terpisah...")
    print("=" * 50)

    plot_lingkaran()
    plot_elips()
    plot_pentagon()
    plot_kubus()

    print("\nSelesai! 4 file gambar telah dibuat:")
    print("  1. lingkaran.png")
    print("  2. elips.png")
    print("  3. pentagon.png")
    print("  4. kubus.png")
