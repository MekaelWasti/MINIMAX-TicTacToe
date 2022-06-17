from flask import Flask, request, jsonify
from flask_cors import CORS
from TicTacToeMinimax import *

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

   return data



# Send Data
@app.route("/sender", methods=["GET", "POST"])
def sendME():
   with open("data.txt", 'r') as f:
      data = str(f.readline())
      # data = "{'UserMove': '2', 'AIMove': 'YUR', 'GameEnded': False}"
      print("YER", data)

   # return "POLO"
   # return data
   return jsonify(data)



if __name__ == "__main__": 
   app.run(debug=True)



def tictactoeGame():
    while not gameEnded(board):
        gameStatDict = {}
        validMove = False
        while not validMove:        
            userMove = None


            time = os.path.getmtime('data.txt')
            read = False
            while not read :
                if (time != os.path.getmtime('data.txt')):
                    with open('data.txt', 'r') as f:
                        
                        gameStatDict = ast.literal_eval(f.read())
                        print(gameStatDict)
                        
                        
                        print(gameStatDict["UserMove"])
                        if selectPosition(board,int(gameStatDict["UserMove"]), "O"):
                            validMove = True
                        print("\n", board)
                        
                        print(f'Read UI Input: {gameStatDict["UserMove"]}')
                        read = True


        
        if gameEnded(board):
            gameStatDict["GameEnded"] = True
            with open("data.txt", 'w') as f:
                f.write(str(gameStatDict))
            break

        print("\nAI's Turn")

        gameStatDict["AIMove"] = minimax(board,True)[1]
        if selectPosition(board,gameStatDict["AIMove"], "X"):
            validMove = True
        print("\n", board)

        with open("data.txt", 'w') as f:
            f.write(str(gameStatDict))

        time = os.path.getmtime('data.txt')
    
        if gameEnded(board):
                gameStatDict["GameEnded"] = True
                with open("data.txt", 'w') as f:
                    f.write(str(gameStatDict))

