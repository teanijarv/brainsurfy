import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def plot_atlas(atlas_filepath, dpi=300):
    # Read the atlas data from the CSV file
    atlas = pd.read_csv(atlas_filepath, index_col=0)

    # Create the figure and axes for plotting
    fig, ax = plt.subplots(dpi=dpi)
    
    # Function to add polygons to the axes
    def add_polygons(data, axis):
        for region_name, points in data:
            if pd.notnull(region_name):
                poly = Polygon(points[['X1', 'X2']].values, closed=True, fill=True, facecolor='gray', edgecolor='black')
                axis.add_patch(poly)

    # Process each hemisphere and side, then plot polygons
    for hemi in atlas['hemi'].unique():
        hemi_data = atlas[atlas['hemi'] == hemi]
        for side in hemi_data['side'].unique():
            side_data = hemi_data[hemi_data['side'] == side].groupby('region')
            add_polygons(side_data, ax)

    # Set plot properties
    ax.set_aspect('equal')
    ax.set_xlim([atlas['X1'].min(), atlas['X1'].max()])
    ax.set_ylim([atlas['X2'].min(), atlas['X2'].max()])
    ax.axis('off')

    # Display the plot
    plt.show()

def simulate_atlas_data(atlas_filepath):
    # Read the atlas data from the CSV file
    atlas = pd.read_csv(atlas_filepath, index_col=0)
    
    # Assume the atlas has a 'region' column that identifies each ROI
    # We will add a new column with simulated values
    num_regions = atlas['region'].nunique()
    simulated_values = np.random.rand(num_regions)  # Generate a random value for each ROI
    
    # Map the simulated values to each ROI in the atlas
    value_map = dict(zip(atlas['region'].unique(), simulated_values))
    atlas['simulated_value'] = atlas['region'].map(value_map)

    return atlas

def plot_brain_data(atlas_data):
    # Create the figure and axes for plotting
    fig, ax = plt.subplots(dpi=300)
    
    # Get the colormap
    cmap = plt.cm.viridis
    
    # Plot polygons based on the atlas data
    # Process each hemisphere and side, then plot polygons
    for hemi in atlas_data['hemi'].unique():
        hemi_data = atlas_data[atlas_data['hemi'] == hemi]
        for side in hemi_data['side'].unique():
            side_data = hemi_data[hemi_data['side'] == side]
            for name, group in side_data.groupby('region'):
                color = cmap(group['simulated_value'].iloc[0])  # Use the simulated value to get a color from the colormap
                poly = Polygon(group[['X1', 'X2']].values, closed=True, facecolor=color, edgecolor='black')
                ax.add_patch(poly)

    # Set plot properties
    ax.set_aspect('equal')
    ax.set_xlim([atlas_data['X1'].min()-0.1, atlas_data['X1'].max()+0.1])
    ax.set_ylim([atlas_data['X2'].min()-0.1, atlas_data['X2'].max()+0.1])
    ax.axis('off')

    # Display the plot
    plt.show()