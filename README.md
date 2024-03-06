# brainsurfy

Simple surface plots in Python based on ggseg parcellations.

```
import matplotlib.pyplot as plt

from brainsurfy import fetch_atlas_data, simulate_data, plot_surf

atlas_data = fetch_atlas_data('schaefer7_400')
sim_data = simulate_data(atlas_data)

plot_surf(atlas_data, sim_data, cmap=plt.cm.viridis, cbar=True)
```

Output:

![image](docs/images/output_v0.1.0.png)

### to-do:
- a lot of things...
- look into 3d surface plots
- docs (once there is more stuff)
- form into package and upload to pypi