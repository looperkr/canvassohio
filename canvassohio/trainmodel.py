import numpy as np
import pandas as pd
import pickle
import feather
from sklearn.model_selection import train_test_split

def train_validate_test_split(df, train_percent=.6, validate_percent=.2, seed=None):
    np.random.seed(seed)
    perm = np.random.permutation(df.index)
    m = len(df.index)
    train_end = int(train_percent * m)
    validate_end = int(validate_percent * m) + train_end
    train = df.iloc[perm[:train_end]]
    validate = df.iloc[perm[train_end:validate_end]]
    test = df.iloc[perm[validate_end:]]
    return train, validate, test

isDebug = True
#path to data
data_path = '/Volumes/FileStorage/Insight_data/'
ohio_path = '/Volumes/FileStorage/Insight_data/Ohio_data/data_feather/'

#open all datasets
oh1_df = feather.read_dataframe(ohio_path+'SWVF_1_22.feather')
oh2_df = feather.read_dataframe(ohio_path+'SWVF_23_44.feather')
oh3_df = feather.read_dataframe(ohio_path+'SWVF_45_66.feather')
oh4_df = feather.read_dataframe(ohio_path+'SWVF_67_88.feather')

#combine into one dataframe
if not isDebug:
    oh_df = pd.concat([oh1_df,oh2_df,oh3_df,oh4_df])
else:
    oh_df = oh1_df #for debugging     

oh_train, oh_validate, oh_test = train_validate_test_split(oh_df,seed=1)

target='GENERAL-11/08/2016'
y_train = oh_train.pop(target).values
y_validate = oh_validate.pop(target).values
y_test = oh_test.pop(target).values

x_train = oh_train.loc[:,'GENERAL-11/06/2012']
x_validate = oh_validate.loc[:,'GENERAL-11/06/2012']
x_test = oh_test.loc[:,'GENERAL-11/06/2012']

print(y_train.shape)
print(x_train.shape)
