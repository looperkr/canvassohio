import numpy as np
import pandas as pd
import feather
from save2feather import save2feather
import os


#Convert ohio voter data from csv to feather dataframe
data_path = '/Volumes/FileStorage/Insight_data/Ohio_data/data_csv/'
output_path='/Volumes/FileStorage/Insight_data/Ohio_data/data_feather/'
oh_f_1='SWVF_1_22'
oh_f_2='SWVF_23_44'
oh_f_3='SWVF_45_66'
oh_f_4='SWVF_67_88'

save2feather(data_path,oh_f_1,output_path)
save2feather(data_path,oh_f_2,output_path)
save2feather(data_path,oh_f_3,output_path)
save2feather(data_path,oh_f_4,output_path)

df = feather.read_dataframe(output_path+oh_f_1+'.feather')
sub_df = df.iloc[:150]
feather.write_dataframe(sub_df,output_path+'subset_oh.feather')


#Plays sound when code is finished                                                                                                                 
os.system('say done')
