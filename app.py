from flask import Flask, request, jsonify
from flask_cors import CORS

# <strong>#Set up Flaskstrong>:

app = Flask(__name__)
#Set up Flask to bypass CORS at the front end:
cors = CORS(app)
#Run the app:
if __name__ == "__main__":
    #  app.run(port = 5500)
     app.run()



#Create the receiver API POST endpoint:
@app.route("/receiver", methods=["POST"])
def postME():
   data = request.get_json()
   data = jsonify(data)
   print(data)
   return data
if __name__ == "__main__": 
   app.run(debug=True)