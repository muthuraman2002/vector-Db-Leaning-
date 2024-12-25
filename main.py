from flask import Flask,session
import os 
import uuid
from vectordb.db.base import VectorDB
import numpy as np

# client = 

app=Flask(__name__)

@app.route("/", methods=['POST','GET'])
def home():
    try:
        vector1=np.array([0,1])
        print(vector1) 
        return "hii bro"
    except Exception as e:
        print(e)



if __name__=="__main__":
    app.run(host='0.0.0.0',port=3000,debug=True)
