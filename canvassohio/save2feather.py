import numpy as np
import pandas as pd
import feather
import os

def save2feather(data_path,file_n,output_path):
    file_name = data_path+file_n+".txt"
    file_encoding = 'ascii'
    input_od = open(file_name,encoding=file_encoding,errors='backslashreplace')
    df = pd.read_csv(input_od,low_memory=False)
    feather.write_dataframe(df,output_path+file_n+".feather")

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

#Plays sound when code is finished
os.system('say done')
