# Import libraries
from flask import Flask, request, render_template,jsonify
import io
from PIL import Image
import base64
import os
import random
import string
import time
# Import files
import data
import visualisation as viz

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

    if "Choisissez" in [year[:10], classe[:10], gender[:10], tmpLoc[:10]]:
        print("test")
        return jsonify(res=False)

    location = tmpLoc.split(",")[0]
    locationName = None
    if tmpLoc != "fr":
        locationName = tmpLoc.split(",")[1]

    characters = string.ascii_letters + string.digits
    filename = ''.join(random.choice(characters) for i in range(20))

    TIME_start = time.time()
    dataResult = data.speCount(classe+".csv",year,gender,location,locationName)
    TIME_datascrap = time.time() - TIME_start
    TIME_start = time.time()
    plt = viz.barPlot(dataResult,year,classe,gender,location,locationName)
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    im = Image.open(img_buf)
    im.save(filename+".png")
    tmpData = {}
    with open(filename+".png", mode='rb') as file:
        img = file.read()
    tmpData['img'] = base64.encodebytes(img).decode('utf-8')
    os.remove(filename+".png")
    TIME_image = time.time() - TIME_start

    return jsonify(res=True,image=tmpData['img'],scrap_time=TIME_datascrap,image_time=TIME_image)

@app.route('/background_process_pie')
def background_process_pie():
    year = request.args.get('year',"",str)
    classe = request.args.get('class',"",str)
    tmpLoc = request.args.get('location',"",str)
    spe = request.args.get('spe',"",str)
    gender = "All"

    if "Choisissez" in [year[:10], classe[:10], spe[:10], tmpLoc[:10]]:
        return jsonify(res=False)

    location = tmpLoc.split(",")[0]
    locationName = None
    if tmpLoc != "fr":
        locationName = tmpLoc.split(",")[1]

    characters = string.ascii_letters + string.digits
    filename = ''.join(random.choice(characters) for i in range(20))

    TIME_start = time.time()
    dataResult = data.speCount(classe+".csv",year,gender,location,locationName)
    TIME_datascrap = time.time() - TIME_start
    TIME_start = time.time()
    plt = viz.piePlot(dataResult,year,classe,location,locationName,spe)
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    im = Image.open(img_buf)
    im.save(filename+".png")
    tmpData = {}
    with open(filename+".png", mode='rb') as file:
        img = file.read()
    tmpData['img'] = base64.encodebytes(img).decode('utf-8')
    os.remove(filename+".png")
    TIME_image = time.time() - TIME_start

    return jsonify(res=True,image=tmpData['img'],scrap_time=TIME_datascrap,image_time=TIME_image)

# todo
@app.route('/background_process_map')
def background_process_map():
    year = request.args.get('year',"",str)
    classe = request.args.get('class',"",str)
    spe = request.args.get('spe',"",str)
    loc = request.args.get('location',"",str)

    if "Choisissez" in [year[:10], classe[:10], spe[:10], loc[:10]]:
        return jsonify(res=False)

    characters = string.ascii_letters + string.digits
    filename = ''.join(random.choice(characters) for i in range(20))

    TIME_start = time.time()
    if loc == "dep":
        dataResult = data.speCountDep(classe+".csv",year,spe)
    elif loc == "region":
        dataResult = data.speCountRegion(classe+".csv",year,spe)
    TIME_datascrap = time.time() - TIME_start
    TIME_start = time.time()
    plt = viz.mapPlot(dataResult,year,classe,loc,spe)
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    im = Image.open(img_buf)
    im.save(filename+".png")
    tmpData = {}
    with open(filename+".png", mode='rb') as file:
        img = file.read()
    tmpData['img'] = base64.encodebytes(img).decode('utf-8')
    os.remove(filename+".png")
    TIME_image = time.time() - TIME_start

    return jsonify(res=True,image=tmpData['img'],scrap_time=TIME_datascrap,image_time=TIME_image)

if __name__ == "__main__":
    app.run(debug=True)
