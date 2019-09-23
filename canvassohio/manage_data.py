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

#save2feather(data_path,oh_f_1,output_path)
#save2feather(data_path,oh_f_2,output_path)
#save2feather(data_path,oh_f_3,output_path)
#save2feather(data_path,oh_f_4,output_path)

df_oh1 = feather.read_dataframe(output_path+oh_f_1+'.feather')
df_oh2 = feather.read_dataframe(output_path+oh_f_2+'.feather')
df_oh3 = feather.read_dataframe(output_path+oh_f_3+'.feather')
df_oh4 = feather.read_dataframe(output_path+oh_f_4+'.feather')
oh_df = pd.concat([df_oh1,df_oh2,df_oh3,df_oh4])

#oh_df = feather.read_dataframe(output_path+oh_f_1+'.feather')

#sub_df = df.iloc[:150]
#feather.write_dataframe(sub_df,output_path+'subset_oh.feather')

#RESIDENTIAL_ADDRESS1RESIDENTIAL_SECONDARY_ADDRRESIDENTIAL_CITYRESIDENTIAL_STATERESIDENTIAL_ZIP
oh_unique = oh_df.drop_duplicates(subset=['RESIDENTIAL_ADDRESS1','RESIDENTIAL_CITY','RESIDENTIAL_STATE','RESIDENTIAL_ZIP'])
oh_addresses = oh_unique.loc[:,'RESIDENTIAL_ADDRESS1':'RESIDENTIAL_ZIP']
oh_input_form = oh_addresses.drop(columns=['RESIDENTIAL_SECONDARY_ADDR'])

i_start = 0
i_end = 9999
i_max = len(oh_input_form.index)

while i_start<i_max :
    if i_end >= i_max:
        i_end = i_max-1
    output_name = data_path+'addr_slice_'+str(i_start)+'_'+str(i_end)+'.csv'
    oh_input_form.iloc[i_start:i_end].to_csv(output_name,index=True,header=False)
    i_end+=10000
    i_start+=10000

#Plays sound when code is finished                                                                                                                 
os.system('say done')
