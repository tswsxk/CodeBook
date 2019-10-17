# coding: utf-8
# 2019/10/17 @ tongshiwei

"""
colormap
https://matplotlib.org/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py
"""

import numpy as np
import matplotlib.pyplot as plt


cmap = plt.get_cmap("Set1")
print(cmap.colors)
# gradient = np.linspace(0, 1, 256)
# gradient = np.vstack((gradient, gradient))
#
# nrows = 1
# figh = 0.35 + 0.15 + (nrows + (nrows-1)*0.1)*0.22
# fig, axes = plt.subplots(nrows=nrows, figsize=(6.4, figh))
# fig.subplots_adjust(top=1-.35/figh, bottom=.15/figh, left=0.2, right=0.99)
#
# ax = axes
# name = "Set1"
# ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
# ax.text(-.01, .5, name, va='center', ha='right', fontsize=10,
#         transform=ax.transAxes)
#
# # Turn off *all* ticks & spines, not just the ones with colormaps.
# ax.set_axis_off()
#
# plt.show()
