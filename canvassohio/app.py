#!/usr/bin/env python

from flask import Flask, render_template, request, send_file, Response, redirect, url_for
from wtforms import Form, TextAreaField, validators
import geopandas as gpd
import matplotlib.pyplot as plt
import pickle
import os

with open('./canvassohio/static/precinct_dict.pickle', 'rb') as handle:
    districts_dic = pickle.load(handle)
    districts=districts_dic.items()

with open('./canvassohio/static/results_dict.pickle','rb') as handle:
    results_dic = pickle.load(handle)
    results=results_dic.items()

with open('./canvassohio/static/party_dict.pickle','rb') as handle:
    lean_dic = pickle.load(handle)

app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/',methods=['GET','POST'])
#def dropdown():
#    districts = [1,2,3]
#    return render_template('dropdown.html',districts=districts)

def dropdown():
    print(os.getcwd())
    if request.method == "POST":
        d = int(request.form.get('districts'))
        data0=results_dic[d][0]
        data1=results_dic[d][1]
        data2=results_dic[d][2]
        lean0=lean_dic[data0]
        lean1=lean_dic[data1]
        lean2=lean_dic[data2]
        return render_template('dropdown.html',districts=results,data=districts_dic[d],data0=data0,data1=data1,data2=data2,lean0=lean0,lean1=lean0,lean2=lean2,fname='district_'+str(d)+'.png',key=d)
    else:
        return render_template('dropdown.html',districts=results)

#Following logic from user The Internet on stackexchange: https://stackoverflow.com/a/13798135
#Sets cached copy to immediately expire
@app.after_request
def html_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run(debug = True)
