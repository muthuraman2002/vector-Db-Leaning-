from flask import Flask,session
import os 
import uuid
from vectordb.db.base import VectorDB


# client = 

app=Flask(__name__)

@app.route("/", methods=['POST','GET'])
def home():
    try:
        return "hii bro"
    except Exception as e:
        print(e)



if __name__=="__main__":
    app.run(host='0.0.0.0',port=3000,debug=True)
