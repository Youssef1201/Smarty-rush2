from flask import Flask
import pymongo
import json
from pymongo import  MongoClient
app= Flask(__name__)
@app.route("/test", methods=["get"])
def test():
    return "<p> hello worl </p>"

@app.route("/test2", methods=["get"])
def test2():
    client = pymongo.MongoClient('mongodb+srv://test:test@cluster0.nqkny.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', ssl=True)
    db = client["test"]
    collection=db["test"]
    

    x = collection.find({})
    list=[]
    for i in x:
        list.append(i)
    return(json.dumps({"data":list}))
    
if(__name__=="__main__"):
    app.run(debug=True)

   
  
    
    
