import pandas as pd
import feather

df = feather.read_dataframe('/Volumes/FileStorage/Insight_data/Ohio_data/data_feather/SWVF_1_22.feather')
print(df.head())
