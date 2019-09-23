from flask import Flask, render_template, request, send_file, Response, redirect
from wtforms import Form, TextAreaField, validators
import geopandas as gpd
import matplotlib.pyplot as plt
import pickle

with open('./canvassohio/static/precinct_dict.pickle', 'rb') as handle:
    districts_dic = pickle.load(handle)
    districts=districts_dic.items()

app = Flask(__name__, static_url_path='/static')

@app.route('/',methods=['GET','POST'])
#def dropdown():
#    districts = [1,2,3]
#    return render_template('dropdown.html',districts=districts)

def dropdown():
    if request.method == "POST":
        d = int(request.form.get('districts'))
        return render_template('dropdown.html',districts=districts,data=districts_dic[d])
    else:
        return render_template('dropdown.html',districts=districts)


#@app.route('/plot.png', methods=['GET'])
#def district_map():
#    fig=draw_map()
#    output = io.BytesIO()
#    FigureCanvas(fig).print_png(output)
#    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug = True)
