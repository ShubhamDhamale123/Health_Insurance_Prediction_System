import pickle
import json
import config
import numpy as np 

class MedicalInsurance():
    def __init__(self,age,gender,bmi,children,smoker,region):
        self.age=age
        self.gender=gender
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region="region_"+ region

    def load_model(self):
        with open(config.model_file_path,"rb") as f:
            self.model= pickle.load(f)

        with open(config.json_file_path,"r") as f:
            self.json_data=json.load(f)
        
    def get_predicted_charges(self):

        self.load_model()
        region_index=self.json_data["columns"].index(self.region)
        test_array=np.zeros(len(self.json_data["columns"]))
             
        test_array[0]=self.age
        test_array[1]=self.json_data["gender"][self.gender]
        test_array[2]=self.bmi
        test_array[3]=self.children
        test_array[4]=self.json_data["smoker"][self.smoker]
        test_array[region_index]=1
  
        print("test array:",test_array)
        predicted_charges=self.model.predict([test_array])
        return np.around(predicted_charges,2) 