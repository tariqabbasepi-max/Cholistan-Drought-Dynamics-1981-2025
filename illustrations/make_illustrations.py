"""Methodological illustrations for the Cholistan drought manuscript.

Produces Analytical_Workflow.(svg|tiff) and Conceptual_Framework.(svg|tiff)
at 174 mm width (double column), 600 dpi, flattened RGB, LZW, using the colour
palette and typography of the analysis notebook (Liberation Sans/Arial).

Usage:  python make_illustrations.py <output_folder>
"""
import io
import sys
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Patch
from matplotlib.lines import Line2D
from PIL import Image

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
OUT.mkdir(parents=True, exist_ok=True)
MM = 1 / 25.4
PAL = dict(ink="#231F23", muted="#5E565E", purple="#91278F", purple_dark="#5F175E", purple_mid="#B468B2",
           purple_light="#E6D0E5", grey="#A9A3A9", grey_light="#DCD8DC", teal="#2B8C8C", amber="#C9822B",
           blue="#4F6DB8", white="#FFFFFF")
mpl.rcParams.update({"font.family": "sans-serif",
                     "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"],
                     "font.size": 8, "svg.fonttype": "none", "pdf.fonttype": 42})


def save(fig, name):
    fig.savefig(OUT / f"{name}.svg", format="svg", facecolor="white")
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=600, facecolor="white")
    buf.seek(0)
    with Image.open(buf) as im:
        im.convert("RGB").save(OUT / f"{name}.tiff", format="TIFF", dpi=(600, 600), compression="tiff_lzw")
    plt.close(fig)


def box(ax, x, y, w, h, title, body="", fc=PAL["white"], ec=PAL["purple_dark"], ls="-", lw=0.9,
        title_color=None, hatch=None, size=8, body_size=8, body_offset=None):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=1.2", fc=fc, ec=ec, lw=lw, ls=ls,
                       hatch=hatch, zorder=2)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h - 2.2, title, ha="center", va="top", fontsize=size, fontweight="bold",
            color=title_color or PAL["ink"], zorder=3, wrap=True)
    if body:
        off = body_offset if body_offset is not None else (10.8 if "\n" in title else 6.6)
        ax.text(x + w / 2, y + h - off, body, ha="center", va="top", fontsize=body_size, color=PAL["ink"],
                linespacing=1.25, zorder=3)
    return p


def arrow(ax, x0, y0, x1, y1, ls="-", color=None, lw=1.0):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=8, lw=lw,
                                 color=color or PAL["muted"], ls=ls, zorder=1, shrinkA=0, shrinkB=0))


# =============================================================================
# 1. Analytical workflow
# =============================================================================
W, H = 174, 184
fig = plt.figure(figsize=(W * MM, H * MM))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

band = dict(fc=PAL["purple_light"], ec="none")
rows = [("Inputs", 160, 20), ("Processing", 134, 19), ("Series", 116, 13), ("Indicators", 75, 36),
        ("Spatial", 52, 18), ("Robustness", 31, 16), ("Synthesis", 10, 16)]
for label, y, h in rows:
    ax.text(2, y + h / 2, label, rotation=90, ha="center", va="center", fontsize=8, color=PAL["muted"])

# Inputs
iw, ig, x0 = 39, 2.6, 5.5
inputs = [("CHIRPS v2 pentads", "UCSB-CHG/CHIRPS/\nPENTAD; 0.05°;\n1981–2025 (primary)", PAL["purple"]),
          ("CHIRPS v3 pentads", "UCSB-CHC/CHIRPS/\nV3/PENTAD; 0.05°;\n1981–2025 (sensitivity)", PAL["purple_mid"]),
          ("Other products", "PERSIANN-CDR,\nERA5-Land, IMERG V07\n(agreement only)", PAL["teal"]),
          ("Study boundary", "Cholistan shapefile\nWGS 84 (EPSG:4326)\n24,790 km²", PAL["muted"])]
for i, (t, b, c) in enumerate(inputs):
    box(ax, x0 + i * (iw + ig), 160, iw, 20, t, b, ec=c, title_color=c)
# Processing
box(ax, 5.5, 134, 78, 19, "Native-grid extraction",
    "Earth Engine computePixels on the CHIRPS lattice\n43 × 65 cells; 1,077 touch the boundary;\n"
    "915 cells ≥50% inside (spatial domain)")
box(ax, 86.5, 134, 82, 19, "Area-weighted aggregation and QC",
    "w = coverage fraction × cell area; P̄ = Σ w·P / Σ w\n72 pentads per year verified;\nr = 1.000 with archived regional series")
for i in range(4):
    arrow(ax, x0 + i * (iw + ig) + iw / 2, 160, x0 + i * (iw + ig) + iw / 2 if i < 2 else 127, 153.3)
# Series
box(ax, 5.5, 116, 163, 13, "Regional and cell-level series",
    "Pentad (72 per year)  ·  monthly (sum of 6 pentads)  ·  JJAS / JAS  ·  annual")
arrow(ax, 44.5, 134, 44.5, 129.3); arrow(ax, 127.5, 134, 127.5, 129.3)
# Analysis modules
mw, mg = 39.5, 1.7
mods = [("SPI", "SPI-1/3/6/12; gamma,\nL-moments, by ending\nmonth; full-record\ncalibration; zero mass q\nGOF: KS, AD, S–W\nEvents and episodes"),
        ("Dry pentads", "Calendar-pentad\npercentiles (1991–2020):\nP25/P20/P10/P05;\neligible pentads only;\nabsolute <1, <2 mm\nRuns; attribution"),
        ("Wet-pentad metrics", "Wet pentad ≥5 mm:\nfrequency, intensity\nTop-10 share, Gini,\nPCI, maximum pentad\nLog-scale frequency–\nintensity split"),
        ("Temporal change", "Hamed–Rao MK, TFPW\nSen slope, block-\nbootstrap 95% CI\nBH-FDR by family\nPettitt, Buishand, SNHT\nBIC step vs trend")]
for i, (t, b) in enumerate(mods):
    box(ax, 5.5 + i * (mw + mg), 75, mw, 36, t, b, ec=PAL["purple_dark"])
    arrow(ax, 5.5 + i * (mw + mg) + mw / 2, 116, 5.5 + i * (mw + mg) + mw / 2, 111.3)
# Spatial
box(ax, 5.5, 52, 163, 18, "Cell-level analysis (915 native CHIRPS cells)",
    "Pixel-wise Hamed–Rao MK and Sen slope; BH-FDR across cells (q ≤ 0.10, field significance)\n"
    "Global Moran's I; Local Moran's I (queen contiguity, 9,999 permutations, q ≤ 0.05)\n"
    "Exploratory zones: spatially constrained Ward clustering with stability check")
arrow(ax, 87, 75, 87, 70.3)
# Robustness
rw = 53.3
rob = [("Dataset version", "CHIRPS v2 vs v3, same\nmetrics on the same grid"),
       ("Product agreement", "r, KGE, bias, trend, Pettitt\nyear (not gauge validation)"),
       ("Method sensitivity", "SPI calibration, zero mass,\neight dry-pentad definitions")]
for i, (t, b) in enumerate(rob):
    box(ax, 5.5 + i * (rw + 1.55), 31, rw, 16, t, b, ec=PAL["teal"], title_color=PAL["teal"])
    arrow(ax, 87 if i == 1 else 5.5 + i * (rw + 1.55) + rw / 2, 52, 5.5 + i * (rw + 1.55) + rw / 2, 47.3)
# Interpretation
box(ax, 5.5, 10, 163, 16, "Interpretation alongside participatory findings",
    "Independent line of evidence: 30 individual herder consultations and stakeholder review;\n"
    "no statistical linkage between rainfall indicators and participant responses",
    ec=PAL["amber"], ls=(0, (4, 2)), title_color=PAL["amber"])
arrow(ax, 87, 31, 87, 26.3, ls=(0, (3, 2)), color=PAL["amber"])
save(fig, "Analytical_Workflow")

# =============================================================================
# 2. Conceptual integration framework
# =============================================================================
W, H = 174, 128
fig = plt.figure(figsize=(W * MM, H * MM))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
STY = {"measured": dict(ec=PAL["purple_dark"], ls="-", fc=PAL["purple_light"], lw=1.2),
       "participant": dict(ec=PAL["amber"], ls=(0, (5, 2)), fc="#FBF1E4", lw=1.2),
       "literature": dict(ec=PAL["teal"], ls=(0, (1, 1.5)), fc="#E5F2F2", lw=1.2),
       "unmeasured": dict(ec=PAL["grey"], ls=(0, (1, 1.5)), fc=PAL["white"], lw=1.0)}


def cbox(x, y, t, b, k, w=52, h=33):
    s_ = STY[k]
    if k == "unmeasured":   # light hatching drawn underneath so the text stays readable
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=1.2", fc="white",
                                    ec="#E3DFE3", lw=0, hatch="////", zorder=1))
        fc = "none"
    else:
        fc = s_["fc"]
    box(ax, x, y, w, h, t, b, fc=fc, ec=s_["ec"], ls=s_["ls"], lw=s_["lw"])


y1, y2 = 71, 26
cbox(4, y1, "1  Drought hazard", "Rainfall totals (annual, JJAS)\nSPI-3/6/12 and episodes\nDry and wet pentads;\ncell-level trends (CHIRPS)", "measured")
cbox(61, y1, "2  Exposure", "Herds and households that\ndepend on rain-fed Tobas,\nrangeland forage and\nseasonal mobility", "literature")
cbox(118, y1, "3  Vulnerability pathways", "Remoteness; brackish\ngroundwater; Toba siltation;\ngrazing fragmentation;\nweak services and finance", "participant")
cbox(118, y2, "4  Potential livestock impacts", "Water and feed shortage, body\ncondition, disease, mortality,\ndistress sales\n(not measured in this study)", "unmeasured")
cbox(61, y2, "5  Coping and adaptation", "Mobility, crop residues,\nborrowing, livestock sales,\nToba and water management", "participant")
cbox(4, y2, "6  Locally identified\nresilience priorities", "Toba and water, rangeland,\nbreeding, feed reserves,\nfinance, veterinary services", "participant")
dash = (0, (4, 2.5))
arrow(ax, 56, y1 + 16.5, 61, y1 + 16.5, ls=dash)
arrow(ax, 113, y1 + 16.5, 118, y1 + 16.5, ls=dash)
arrow(ax, 144, y1, 144, y2 + 33.3, ls=dash)
arrow(ax, 118, y2 + 16.5, 113, y2 + 16.5, ls=dash)
arrow(ax, 61, y2 + 16.5, 56, y2 + 16.5, ls=dash)
ax.text(87, 111, "The hazard was characterised quantitatively; links between components are conceptual and were not tested",
        ha="center", va="center", fontsize=8, color=PAL["muted"], style="italic")
defs = ("Definitions. Drought (meteorological): precipitation well below the local normal. Exposure: people, livestock and "
        "resources located where drought occurs. Vulnerability: susceptibility to harm and limited capacity to cope. "
        "Preparedness: capacities built before drought. Coping: short-term responses during drought. Adaptation: longer-term "
        "adjustment to drought risk. Resilience: capacity to anticipate, absorb and recover; not measured here, where only "
        "locally identified priorities for strengthening it were recorded.")
ax.text(4, 20, defs, ha="left", va="top", fontsize=8, color=PAL["ink"], wrap=True, linespacing=1.3)
legend = [Patch(fc=STY["measured"]["fc"], ec=STY["measured"]["ec"], lw=1.2, label="Measured in this study (CHIRPS)"),
          Patch(fc=STY["participant"]["fc"], ec=STY["participant"]["ec"], ls="--", lw=1.2, label="Participant-reported (this study)"),
          Patch(fc=STY["literature"]["fc"], ec=STY["literature"]["ec"], ls=":", lw=1.2, label="Literature-supported"),
          Patch(fc="white", ec=PAL["grey"], hatch="////", ls=":", label="Not measured"),
          Line2D([], [], color=PAL["muted"], ls="--", lw=1, label="Conceptual link (not tested)")]
fig.legend(handles=legend, loc="upper center", bbox_to_anchor=(0.5, 0.995), ncol=3, frameon=False, fontsize=8,
           handlelength=2.2, columnspacing=1.2)
save(fig, "Conceptual_Framework")
print("Illustrations written to", OUT)
