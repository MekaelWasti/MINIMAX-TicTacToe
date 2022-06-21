from turtle import pos
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json



# <strong>#Set up Flaskstrong>:

app = Flask(__name__)
#Set up Flask to bypass CORS at the front end:
CORS(app)
# cors = CORS(app)

#Run the app:
# if __name__ == "__main__":
    #  app.run(port = 5500)
    #  app.run()



#Create the receiver API POST endpoint:
@app.route("/receiver", methods=["GET", "POST"])
def postME():
   data = request.get_json()
   #    data = jsonify(data)
   print(data)


   with open("data.txt", 'w') as f:
      f.write(str(data))
   
   with open("data2.txt", 'w') as f:
      f.write("Modify Check File")

   return data



# Send Data
@app.route("/sender", methods=["GET", "POST"])
def sendME():
   time = os.path.getmtime('data.txt')
   read = False
   while not read:
      if time != os.path.getmtime('data.txt'):
         print(f"YERR  {time}")
         with open("data.txt", 'r') as f:
            data = str(f.readline())
            print("YER", data)
            read = True

   # return "POLO"
   # return data
   # return json.dumps(data)
   return jsonify(data)



if __name__ == "__main__": 
   app.run(debug=True)


