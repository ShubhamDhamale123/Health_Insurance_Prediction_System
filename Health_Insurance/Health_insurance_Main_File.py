from flask import Flask ,render_template,jsonify,request

import config
from project_app.utils import MedicalInsurance
app=Flask(__name__)

@app.route("/")
def insurance():
    age	= 21
    gender = "male"
    bmi = 25.745000
    children = 2
    smoker = "no"
    region ="northeast"
                    
    med_ins=MedicalInsurance(age,gender,bmi,children,smoker,region)
    charges=med_ins.get_predicted_charges()

    return jsonify({"result":f"predicted medical insurance charges are :{charges}"})
if __name__=="__main__":
    app.run(host="0.0.0.0",port=2005,debug=True)


