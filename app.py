from flask import Flask, render_template, request
import numpy as np
import pickle
app = Flask(__name__)
@app.route('/')
def student():
   return render_template('index.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
    testData =[]
    if request.method == 'POST':
        result = request.form
        print(result)
        testData.append(int(result['Age']))
        if result['sex']=='Male':
            testData.append(1)
        else:
            testData.append(0)

        if result['ChestPainType']=='ASY':
            testData.append(0)
        elif result['ChestPainType']=='ATA':
            testData.append(1)
        elif result['ChestPainType']=='NAP':
            testData.append(2)
        else:
            testData.append(3)

        testData.append(int(result['restingBP']))
        testData.append(int(result['Cholesterol']))

        testData.append(int(result['FastingBS']))

        if result['RestingECG']=='LVH':
            testData.append(0)
        elif result['RestingECG']=='Normal':
            testData.append(1)
        else:
            testData.append(2)
        testData.append(int(result['MaxHR']))

        if result['ExerciseAngina']=='Yes':
            testData.append(1)
        else:
            testData.append(0)

        testData.append(float(result['Oldpeak']))

        if result['ST_Slope']=='Down':
            testData.append(0)
        elif result['ST_Slope']=='Flat':
            testData.append(1)
        else:
            testData.append(2)



        print(testData)
        # testData = [58, 1, 1, 136, 211, 0, 2, 99, 0, 2.0, 1]
        test_sample = np.array(testData)
        Pkl_Filename = "Pickle_RL_Model.pkl"
        with open(Pkl_Filename, 'rb') as file:
            Pickled_LR_Model = pickle.load(file)
        predict=Pickled_LR_Model.predict([test_sample])
        print(predict[0])
        predictResult = ""
        if predict[0]==0:
        	predictResult = "The patient may have heart disease."
        else:
        	predictResult = "The patient is completely normal."
        return render_template("result.html",result = result, predict = predictResult)
if __name__ == '__main__':
   app.run(debug = True)
