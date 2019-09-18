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
