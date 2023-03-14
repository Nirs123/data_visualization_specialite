from flask import Flask, request, render_template,jsonify
import data
import visualisation as viz
import io
from PIL import Image
import base64
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bar')
def bar():
    return render_template('bar.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/pie')
def pie():
    return render_template('pie.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/background_process_bar')
def background_process_bar():
    year = request.args.get('year',"",str)
    classe = request.args.get('class',"",str)
    gender = request.args.get('gender',"",str)
    tmpLoc = request.args.get('location',"",str)

    locationErrors = ["--Lieu--","--Régions--","--Académies--"]
    if year == "--Année--" or classe == "--Classe--" or gender == "--Genre--" or tmpLoc in locationErrors:
        return jsonify(res=False)
    

    location = tmpLoc.split(",")[0]
    locationName = None
    if tmpLoc != "fr":
        locationName = tmpLoc.split(",")[1]

    dataResult = data.speCount(classe+".csv",year,gender,location,locationName)
    plt = viz.barPlot(dataResult,year,classe,gender,location,locationName)
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    im = Image.open(img_buf)
    im.save("test.png")
    tmpData = {}
    with open('test.png', mode='rb') as file:
        img = file.read()
    tmpData['img'] = base64.encodebytes(img).decode('utf-8')

    os.remove('test.png')

    return jsonify(res=True,image=tmpData['img'])

if __name__ == "__main__":
    app.run(debug=True)
