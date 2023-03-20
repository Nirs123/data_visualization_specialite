# Import libraries
from flask import Flask, request, render_template,jsonify
from PIL import Image
import os
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

# BAR
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

    TIME_start = time.time()
    dataResult = data.speCount(classe+".csv",year,gender,location,locationName)
    TIME_datascrap = time.time() - TIME_start
    TIME_start = time.time()
    plt = viz.barPlot(dataResult,year,classe,gender,location,locationName)
    TIME_graphic = time.time() - TIME_start
    myPWD = os.getcwd()
    pathfile = str(time.time_ns()) + "_bar"
    plt.savefig(myPWD + "/static/generatedGraphic/"+pathfile+".png")
    TIME_start = time.time()
    
    TIME_image = time.time() - TIME_start

    return jsonify(res=True,path=pathfile,scrap_time=TIME_datascrap,graphic_time=TIME_graphic,image_time=TIME_image)

# PIE
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

    TIME_start = time.time()
    dataResult = data.speCount(classe+".csv",year,gender,location,locationName)
    TIME_datascrap = time.time() - TIME_start
    TIME_start = time.time()
    plt = viz.piePlot(dataResult,year,classe,location,locationName,spe)
    TIME_graphic = time.time() - TIME_start
    TIME_start = time.time()
    myPWD = os.getcwd()
    pathfile = str(time.time_ns()) + "_pie"
    plt.savefig(myPWD + "/static/generatedGraphic/"+pathfile+".png")
    TIME_image = time.time() - TIME_start

    return jsonify(res=True,path=pathfile,scrap_time=TIME_datascrap,graphic_time=TIME_graphic,image_time=TIME_image)

# MAP
@app.route('/background_process_map')
def background_process_map():
    year = request.args.get('year',"",str)
    classe = request.args.get('class',"",str)
    spe = request.args.get('spe',"",str)
    loc = request.args.get('location',"",str)

    print(year,year[:10])
    if "Choisissez" in [year[:10], classe[:10], spe[:10], loc[:10]]:
        return jsonify(res=False)

    TIME_start = time.time()
    if loc == "dep":
        dataResult = data.speCountDep(classe+".csv",year,spe)
    elif loc == "region":
        dataResult = data.speCountRegion(classe+".csv",year,spe)
    TIME_datascrap = time.time() - TIME_start
    TIME_start = time.time()
    plt = viz.mapPlot(dataResult,year,classe,loc,spe)
    TIME_graphic = time.time() - TIME_start
    TIME_start = time.time()
    myPWD = os.getcwd()
    pathfile = str(time.time_ns()) + "_map"
    plt.savefig(myPWD + "/static/generatedGraphic/"+pathfile+".png")
    TIME_image = time.time() - TIME_start

    return jsonify(res=True,path=pathfile,scrap_time=TIME_datascrap,graphic_time=TIME_graphic,image_time=TIME_image)

if __name__ == "__main__":
    app.run(debug=True)
