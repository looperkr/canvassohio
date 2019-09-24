from os import listdir
from os import system
from os.path import isfile, join

mypath = '/Volumes/FileStorage/Insight_data/Ohio_data/data_csv/'
onlyfiles = ['addr_slice_80000_89999.csv','addr_slice_810000_819999.csv','addr_slice_820000_829999.csv','addr_slice_830000_839999.csv','addr_slice_840000_849999.csv','addr_slice_850000_859999.csv','addr_slice_860000_869999.csv','addr_slice_870000_879999.csv','addr_slice_880000_889999.csv','addr_slice_890000_899999.csv','addr_slice_900000_909999.csv',' addr_slice_90000_99999.csv']

#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f[:10]=='addr_slice' and f[-5:]!='t.csv']
output = [fn.split('.')[0]+'_output.csv' for fn in onlyfiles]
'''finished = [ft for ft in listdir(mypath) if isfile(join(mypath,ft)) and ft[-5:]=='t.csv']
for f in onlyfiles:
    d=f.split('.')[0]+'_output.csv'
    if d in finished:
        output.remove(d)
        onlyfiles.remove(f)
'''
for i in range(0,len(output)):
    fin=onlyfiles[i]
    fout=output[i]
    command = 'curl --form addressFile=@/Volumes/FileStorage/Insight_data/Ohio_data/data_csv/'+fin+' --form benchmark=Public_AR_Current https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output /Volumes/FileStorage/Insight_data/Ohio_data/data_csv/'+fout
    print(command)
    system(command)
