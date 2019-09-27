import numpy as np
import pandas as pd
import feather
from datetime import date, datetime
from tqdm import tqdm_notebook as tqdm
tqdm().pandas()

df=feather.read_dataframe(ohio_path+'oh_df.feather')
election_list = []
election_i = []
general_list = []
primary_list = []

for key in df:
        if key[:7]=='GENERAL':
                election_list.append(key)
                general_list.append(key)
        elif key[:7]=='PRIMARY':
                election_list.append(key)
                primary_list.append(key)
        elif key[:7]=='SPECIAL':
                election_list.append(key)
                
def el_to_date(election):
    el_date_str = election.split('-')[1]
    el_obj = datetime.strptime(el_date_str, '%m/%d/%Y')
    return el_obj
date_list = [el_to_date(e) for e in election_list]
date_dict = dict(zip(election_list, date_list))

def n_eligible_voted(row, start_date, end_date):
    reg_date = datetime.strptime(row['REGISTRATION_DATE'],'%Y-%m-%d')
    eligible_list = [l for l in election_list if date_dict[l]>reg_date and date_dict[l]>start_date and date_dict[l]<end_date]
    n_el = row[eligible_list].count()
    return n_el

def n_eligible(row, start_date, end_date):
    reg_date = datetime.strptime(row['REGISTRATION_DATE'],'%Y-%m-%d')
    eligible_list = [l for l in election_list if date_dict[l]>reg_date and date_dict[l]>start_date and date_dict[l]<end_date]
    return len(eligible_list)

def row_ratio(row,year):
    eligible_column = 'N_ELIGIBLE_'+year
    voted_column = 'N_VOTED_ELIGIBLE_'+year
    voted_i= row[voted_column]
    eligible_i = row[eligible_column]
    if eligible_i != 0:
        v_ratio = voted_i/eligible_i
    else:
        v_ratio = float('Inf')
    return v_ratio

date_2000=datetime(2000, 11, 7)
date_2004=datetime(2004,11,2)
date_2008=datetime(2008,11,4)
date_2012=datetime(2012,11,6)
date_2016=datetime(2016,11,8)
date_2020=datetime(2020,11,3)

df['N_VOTED_ELIGIBLE_2012'] = df.progress_apply(lambda row: n_eligible_voted(row,date_2000,date_2012), axis=1)
df['N_ELIGIBLE_2012'] = df.progress_apply(lambda row: n_eligible(row,date_2000,date_2012), axis=1)
df['N_VOTED_ELIGIBLE_2016'] = df.progress_apply(lambda row: n_eligible_voted(row,date_2004,date_2016), axis=1)
df['N_ELIGIBLE_2016'] = df.progress_apply(lambda row: n_eligible(row,date_2004,date_2016), axis=1)
df['N_VOTED_ELIGIBLE_2020'] = df.progress_apply(lambda row: n_eligible_voted(row,date_2008,date_2020), axis=1)
df['N_ELIGIBLE_2020'] = df.progress_apply(lambda row: n_eligible(row,date_2008,date_2020), axis=1)

oh_df['RATIO_2012'] = oh_df.progress_apply(lambda row: row_ratio(row,'2012'), axis=1)
oh_df['RATIO_2016'] = oh_df.progress_apply(lambda row: row_ratio(row,'2016'), axis=1)
oh_df['RATIO_2020'] = oh_df.progress_apply(lambda row: row_ratio(row,'2020'), axis=1)


feather.write_dataframe(df,'ohdf_withratio.feather')
