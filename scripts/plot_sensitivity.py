#!/usr/bin/env python3
"""Reproduce project-page figures from the published Table 3 values.

Requires matplotlib. Run from any directory: python scripts/plot_sensitivity.py
Only the three reported settings are plotted for each factor. Connecting lines
are visual guides; the paper does not report uncertainty estimates for this table.
"""

import csv
from pathlib import Path
from xml.sax.saxutils import escape

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "assets/downloads/ebreg-sensitivity.csv"
OUTPUT = ROOT / "assets/images"
INK = "#19263c"
MUTED = "#5e6879"
BLUE = "#3858a6"
TEAL = "#08766e"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 14,
    "text.color": INK,
    "axes.labelcolor": INK,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "svg.fonttype": "none",
    "svg.hashsalt": "ebreg-table3",
    "axes.unicode_minus": False,
})


def plot(rows, *, factor, stem, xlabel, title, xlim):
    records = [row for row in rows if row["factor"] == factor]
    x = [float(row["value"]) for row in records]
    y = [float(row["linear_probe_accuracy_percent"]) for row in records]
    default = next(i for i, row in enumerate(records) if row["is_default"] == "true")
    description = (
        "ImageNet-1K linear-probe accuracy for ResNet-50, varying one factor at a time. "
        + "; ".join(
            f"{row['value']}: {row['linear_probe_accuracy_percent']} percent"
            + (" (default)" if row["is_default"] == "true" else "")
            for row in records
        )
        + ". Shared vertical axis: 55 to 70 percent. Source: paper Table 3. "
        "Connecting lines guide the eye; no uncertainty estimates are reported."
    )
    fig = plt.figure(figsize=(600 / 72, 400 / 72), facecolor="white")
    ax = fig.add_axes([0.15, 0.18, 0.80, 0.73])
    ax.set_facecolor("white")
    ax.set_axisbelow(True)
    ax.grid(axis="y", color="#dfe3eb", linewidth=0.8)
    ax.plot(x, y, color=BLUE, linewidth=2, marker="o", markersize=8,
            markerfacecolor="white", markeredgewidth=2, zorder=3)
    ax.scatter([x[default]], [y[default]], s=185, color="#dbeee9", zorder=4)
    ax.scatter([x[default]], [y[default]], s=75, color=TEAL,
               edgecolors="white", linewidths=1, zorder=5)
    for i, (value, accuracy) in enumerate(zip(x, y)):
        ax.annotate(f"{accuracy:.2f}", (value, accuracy), xytext=(0, 11),
                    textcoords="offset points", ha="center", va="bottom",
                    color=TEAL if i == default else INK,
                    fontsize=14, fontweight="bold" if i == default else "normal")
    ax.annotate("Default", (x[default], y[default]), xytext=(0, -16),
                textcoords="offset points", ha="center", va="top", color=TEAL,
                fontsize=11.5, bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5})
    ax.set_xlim(xlim)
    ax.set_ylim(55, 70)
    ax.set_xticks(x, [row["value"] for row in records])
    ax.set_yticks([55, 60, 65, 70])
    ax.tick_params(axis="both", length=0, pad=9, labelsize=13)
    ax.set_xlabel(xlabel, fontsize=14, labelpad=15)
    ax.set_ylabel("Linear-probe accuracy (%)", fontsize=14, labelpad=14)
    for edge in ("top", "right"):
        ax.spines[edge].set_visible(False)
    for edge in ("left", "bottom"):
        ax.spines[edge].set_color("#c4ccd9")
        ax.spines[edge].set_linewidth(0.8)
    fig.text(0.15, 0.965, "ImageNet-1K · ResNet-50", color=MUTED, fontsize=11)
    fig.savefig(OUTPUT / f"{stem}.png", dpi=144,
                metadata={"Title": title, "Description": description})
    svg = OUTPUT / f"{stem}.svg"
    fig.savefig(svg, metadata={"Title": title, "Description": description,
                              "Creator": "EBReg project page", "Date": None})
    plt.close(fig)
    # Native SVG semantics support use outside the website's figure/alt wrapper.
    content = svg.read_text()
    start = content.index("<svg ")
    end = content.index(">", start)
    content = (
        content[:end]
        + f' role="img" aria-labelledby="{stem}-title {stem}-desc"'
        + content[end:end + 1]
        + f'\n <title id="{stem}-title">{escape(title)}</title>'
        + f'\n <desc id="{stem}-desc">{escape(description)}</desc>'
        + content[end + 1:]
    )
    svg.write_text(content)


def main():
    with DATA.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    OUTPUT.mkdir(parents=True, exist_ok=True)
    plot(rows, factor="noise_sigma", stem="noise-sensitivity",
         xlabel="Gaussian noise scale σ", title="Sensitivity to Gaussian noise scale",
         xlim=(4.15, 5.10))
    plot(rows, factor="score_updates", stem="score-update-sensitivity",
         xlabel="Score updates per encoder step", title="Sensitivity to the number of score updates",
         xlim=(0, 36))


if __name__ == "__main__":
    main()
