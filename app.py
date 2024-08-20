from flask import Flask
from flask import request
from flask import render_template
import pickle
import pandas as pd

app = Flask(__name__)

# load the model and data
df = pickle.load(open('models/df.pkl','rb'))
pipe = pickle.load(open('models/pipe.pkl','rb'))

@app.route('/',methods=['GET'])
def index():
    # sort the unique values
    CarName_sort = sorted(df['CarName'].unique())
    fueltype_sort = sorted(df['fueltype'].unique())
    aspiration_sort = sorted(df['aspiration'].unique())
    doornumber_sort = sorted(df['doornumber'].unique())
    carbody_sort = sorted(df['carbody'].unique())
    drivewheel_sort = sorted(df['drivewheel'].unique())
    enginelocation_sort = sorted(df['enginelocation'].unique())
    enginetype_sort = sorted(df['enginetype'].unique())
    cylindernumber_sort = sorted(df['cylindernumber'].unique())
    fuelsystem_sort = sorted(df['fuelsystem'].unique())
    
    return render_template(
        'index.html',CarNames=CarName_sort,fueltypes=fueltype_sort,
        aspirations=aspiration_sort,
        doornumbers=doornumber_sort,
        carbodys=carbody_sort,
        drivewheels=drivewheel_sort,
        enginelocations=enginelocation_sort,
        enginetypes=enginetype_sort,
        cylindernumbers=cylindernumber_sort,
        fuelsystems=fuelsystem_sort
        )

@app.route('/predict',methods=['POST'])
def predict():
    # rerieve form data
    CarName = request.form['CarName']
    fueltype = request.form['fueltype']
    aspiration = request.form['aspiration']
    doornumber = request.form['doornumber']
    carbody = request.form['carbody']
    drivewheel = request.form['drivewheel']
    enginelocation = request.form['enginelocation']
    wheelbase = float(request.form['wheelbase'])
    carlength = float(request.form['carlength'])
    carwidth = float(request.form['carwidth'])
    carheight = float(request.form['carheight'])
    curbweight = int(request.form['curbweight'])
    enginetype = request.form['enginetype']
    cylindernumber = request.form['cylindernumber']
    enginesize = int(request.form['enginesize'])
    fuelsystem = request.form['fuelsystem']
    boreratio = float(request.form['boreratio'])
    stroke = float(request.form['stroke'])
    compressionratio = float(request.form['compressionratio'])
    horsepower = int(request.form['horsepower'])
    peakrpm = int(request.form['peakrpm'])
    citympg = int(request.form['citympg'])
    highwaympg = int(request.form['highwaympg'])
    
    # create a DataFrame form the input data for the model
    query = pd.DataFrame([[CarName, fueltype, aspiration, doornumber, carbody, drivewheel, enginelocation, wheelbase, carlength, carwidth, carheight, curbweight, enginetype, cylindernumber, enginesize, fuelsystem, boreratio, stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg]],columns=['CarName', 'fueltype', 'aspiration', 'doornumber', 'carbody','drivewheel', 'enginelocation', 'wheelbase', 'carlength', 'carwidth','carheight', 'curbweight', 'enginetype', 'cylindernumber', 'enginesize', 'fuelsystem', 'boreratio', 'stroke', 'compressionratio', 'horsepower','peakrpm', 'citympg', 'highwaympg'])
    
    # predict car price
    # prediction = pipe.predict(query)[0]
    prediction = f"{pipe.predict(query)[0]:.2f}"


    # sort the unique values again for consistance dropdown options
    CarName_sort = sorted(df['CarName'].unique())
    fueltype_sort = sorted(df['fueltype'].unique())
    aspiration_sort = sorted(df['aspiration'].unique())
    doornumber_sort = sorted(df['doornumber'].unique())
    carbody_sort = sorted(df['carbody'].unique())
    drivewheel_sort = sorted(df['drivewheel'].unique())
    enginelocation_sort = sorted(df['enginelocation'].unique())
    enginetype_sort = sorted(df['enginetype'].unique())
    cylindernumber_sort = sorted(df['cylindernumber'].unique())
    fuelsystem_sort = sorted(df['fuelsystem'].unique())
    
    # render templates with prediction and input values
    return render_template(
        'index.html',
        prediction=prediction,
        CarNames=CarName_sort,
        fueltypes=fueltype_sort,
        aspirations=aspiration_sort,
        doornumbers=doornumber_sort,
        carbodys=carbody_sort,
        drivewheels=drivewheel_sort,
        enginelocations=enginelocation_sort,
        enginetypes=enginetype_sort,
        cylindernumbers=cylindernumber_sort,
        fuelsystems=fuelsystem_sort
        )
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)