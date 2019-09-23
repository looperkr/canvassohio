import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
import geopandas as gpd
from matplotlib.figure import Figure


def draw_map():
    fp = "/Volumes/FileStorage/Insight_data/cb_2018_39_sldl_500k/cb_2018_39_sldl_500k.shp"
    fig = Figure()
    map_df = gpd.read_file(fp)
    map_df.plot()
    return fig

draw_map()
plt.show()
