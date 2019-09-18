#/Users/kristinalooper/WorkArea/insight/canvassohio/canvassohio.py

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import feather
import os

#path to data:
data_path = '/Volumes/FileStorage/Insight_data/'
ohio_path = '/Volumes/FileStorage/Insight_data/Ohio_data/data_feather/'

#open four ohio data files
#files: SWVF_1_22.feather  SWVF_23_44.feather SWVF_45_66.feather SWVF_67_88.feather
oh1_df = feather.read_dataframe(ohio_path+'SWVF_1_22.feather')
oh2_df = feather.read_dataframe(ohio_path+'SWVF_23_44.feather')
oh3_df = feather.read_dataframe(ohio_path+'SWVF_45_66.feather')
oh4_df = feather.read_dataframe(ohio_path+'SWVF_67_88.feather')

#combine into one dataframe
oh_df = pd.concat([oh1_df,oh2_df,oh3_df,oh4_df])
#oh_df = oh1_df #for debugging
columns=list(oh_df) #list of column names

grouped=oh_df.groupby('STATE_REPRESENTATIVE_DISTRICT')
grouped['SOS_VOTERID'].count().plot.bar()
plt.show()

os.system('say done')
print(oh_df.shape)
