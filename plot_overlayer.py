import matplotlib.pyplot as plt
import numpy as np
import argparse

# ----------------------------
# Argument Parsing (getopts-like)
# ----------------------------
parser = argparse.ArgumentParser(description='Overlay RMSF plots of WT and MUT proteases.')
parser.add_argument('-w', '--wt', required=True, help='Path to WT RMSF data file (e.g., prod_backbone_rmsf_WT.dat)')
parser.add_argument('-m', '--mut', required=True, help='Path to MUT RMSF data file (e.g., prod_backbone_rmsf_MUT.dat)')
parser.add_argument('-o', '--output', default='rmsf_overlay_plot.png', help='Output image file name')
args = parser.parse_args()

# ----------------------------
# Data
# ----------------------------
wt_data = np.loadtxt(args.wt)
mut_data = np.loadtxt(args.mut)

residues_wt = wt_data[:, 0]
rmsf_wt = wt_data[:, 1]
residues_mut = mut_data[:, 0]
rmsf_mut = mut_data[:, 1]

# ----------------------------
# Plotting
# ----------------------------
plt.figure(figsize=(10, 5))
plt.plot(residues_wt, rmsf_wt, label='WT Protease', color='blue', linewidth=2)
plt.plot(residues_mut, rmsf_mut, label='MUT Protease', color='red', linewidth=2, linestyle='--')

plt.title('Backbone RMSF: WT vs MUT Protease')
plt.xlabel('Residue Index')
plt.ylabel('RMSF (Å)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(args.output, dpi=300)
plt.show()

