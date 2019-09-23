from os import listdir
from os import system
from os.path import isfile, join

mypath = '/Volumes/FileStorage/Insight_data/Ohio_data/data_csv/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f[:10]=='addr_slice' and f[-5:]!='t.csv']
output = [fn.split('.')[0]+'_output.csv' for fn in onlyfiles]
finished = [ft for ft in listdir(mypath) if isfile(join(mypath,ft)) and ft[-5:]=='t.csv']
for f in onlyfiles:
    d=f.split('.')[0]+'_output.csv'
    if d in finished:
        output.remove(d)
        onlyfiles.remove(f)

for i in range(0,len(output)):
    fin=onlyfiles[i]
    fout=output[i]
    command = 'curl --form addressFile=@/Volumes/FileStorage/Insight_data/Ohio_data/data_csv/'+fin+' --form benchmark=Public_AR_Current https://geocoding.geo.census.gov/geocoder/locations/addressbatch --output /Volumes/FileStorage/Insight_data/Ohio_data/data_csv/'+fout
    print(command)
    system(command)
