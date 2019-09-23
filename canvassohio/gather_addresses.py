import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import feather
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import os

#path to data:                                                                                                                               
data_path = '/Volumes/FileStorage/Insight_data/'
ohio_path = '/Volumes/FileStorage/Insight_data/Ohio_data/data_feather/'

#open four ohio data files                                                                                                                   
#files: SWVF_1_22.feather  SWVF_23_44.feather SWVF_45_66.feather SWVF_67_88.feather                                                          
'''oh1_df = feather.read_dataframe(ohio_path+'SWVF_1_22.feather')
oh2_df = feather.read_dataframe(ohio_path+'SWVF_23_44.feather')
oh3_df = feather.read_dataframe(ohio_path+'SWVF_45_66.feather')
oh4_df = feather.read_dataframe(ohio_path+'SWVF_67_88.feather')
'''
oh_df = feather.read_dataframe(ohio_path+"subset_oh.feather")
address_df=oh_df['RESIDENTIAL_ADDRESS1']+' '+oh_df['RESIDENTIAL_CITY']+' '+oh_df['RESIDENTIAL_STATE']+' '+oh_df['RESIDENTIAL_ZIP'].map(str)
address_df.drop_duplicates(keep='first',inplace=True) 

geolocator = Nominatim(user_agent="canvassohio")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
oh_df['location'] = oh_df['name'].apply(geocode)
oh_df['point'] = oh_df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
