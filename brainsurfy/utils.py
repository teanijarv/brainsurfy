# TO-DO
# - check that the paths work correctly to atlases also when running scripts from other places

import os
import numpy as np
import pandas as pd

def list_available_atlases():
    dir = os.path.join(os.path.dirname(__file__), 'atlases')
    try:
        # Get all files in the directory
        files = os.listdir(dir)
        # Filter out files that are not .csv
        atlas_files = [os.path.splitext(f)[0] for f in files if f.endswith('.csv')]
        return atlas_files
    except Exception as e:
        raise ValueError(f"No available atlases. {e}")

def fetch_atlas_data(fname):
    path = os.path.join(os.getcwd(), 'brainsurfy', 'atlases', fname)
    try:
        data = pd.read_csv(path+'.csv', index_col=0)
        return data
    except Exception as e:
        raise ValueError(f"No such atlas available. {e}")

def simulate_data(atlas_data, simulate_func=np.random.rand):
    num_regions = len(atlas_data['region'].unique())
    sim_vals = simulate_func(num_regions)

    sim_dict = dict(zip(atlas_data['region'].unique(), sim_vals))
    sim_df = pd.DataFrame(index=sim_dict.keys(), data=sim_dict.values(), columns=['value'])

    return sim_df