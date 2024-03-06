# TO-DO: 
# - if defining ax rn then the function doesnt work for plot_single_surf
# - cbar limits including which are plotted to be added so could limit the values plotted

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable
import pandas as pd
import numpy as np

def plot_single_surf(atlas_data, value_data, hemi, side, cmap=None, ax=None):
    if ax is None:
        fig, ax = plt.subplots(dpi=300, figsize=(2, 2))
        plt.tight_layout()
    if cmap == None:
        cmap = plt.cm.viridis
    else:
        cmap = cmap

    # Replace NaN values with a placeholder string
    placeholder = 'nan_region'
    atlas_data['region'].fillna(placeholder, inplace=True)

    # Filter data for the specified hemisphere and side
    filtered_data = atlas_data[(atlas_data['hemi'] == hemi) & (atlas_data['side'] == side)]
    filtered_data = filtered_data.merge(value_data, left_on='region', right_index=True, how='left')

    # Normalize the values for the colormap
    norm = mcolors.Normalize(vmin=filtered_data['value'].min(), vmax=filtered_data['value'].max())

    # Plot each region
    for region_name, region_group in filtered_data.groupby('region'):
        # Check for placeholder string to set color to grey
        color = 'darkgrey' if region_name == placeholder else cmap(norm(region_group['value'].iloc[0]))
        poly = Polygon(region_group[['X1', 'X2']].values, closed=True, facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(poly)

    # Set plot properties
    ax.set_aspect('equal')
    ax.set_xlim(filtered_data['X1'].min(), filtered_data['X1'].max())
    ax.set_ylim(filtered_data['X2'].min(), filtered_data['X2'].max())
    ax.axis('off')
    ax.set_title(f"{hemi.capitalize()} {side.capitalize()}", size='x-small')

    return ax

def plot_surf(atlas_data, value_data, cmap=None, cbar=None):
    fig, axs = plt.subplots(2, 2, dpi=300, figsize=(3, 3))
    hemispheres = ['left', 'right']
    sides = ['lateral', 'medial']

    for i, hemi in enumerate(hemispheres):
        for j, side in enumerate(sides):
            plot_single_surf(atlas_data, value_data, hemi, side, cmap=cmap, ax=axs[i, j])

    plt.tight_layout()

    # Add a colorbar if specified
    if cbar:
        # Create a ScalarMappable and initialize a colorbar
        sm = ScalarMappable(cmap=cmap, norm=mcolors.Normalize(vmin=value_data['value'].min(), vmax=value_data['value'].max()))
        sm.set_array([])
        cbar_ax = fig.add_axes([1.00, 0.15, 0.03, 0.7])
        fig.colorbar(sm, cax=cbar_ax, orientation='vertical')

    plt.show()