
# Copyright 2020 Google Inc. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# import os
# import logging
# import random
# from flask import Flask, request

# logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
# logger = logging.getLogger(__name__)

# app = Flask(__name__)
# moves = ['F', 'T', 'L', 'R']

# @app.route("/", methods=['GET'])
# def index():
#     return "Let the battle begin!"

# @app.route("/", methods=['POST'])
# def move():
#     currentPlayers = request.json["https://cloud-run-hackathon-python-qqzvxlxlfq-uc.a.run.app"].get("players");
#     request.get_data()
#     logger.info(request.json)
#     currentX = request.json["https://cloud-run-hackathon-python-qqzvxlxlfq-uc.a.run.app"].x;
#     currentY = request.json["https://cloud-run-hackathon-python-qqzvxlxlfq-uc.a.run.app"].y;
#     currentDirection = request.json["https://cloud-run-hackathon-python-qqzvxlxlfq-uc.a.run.app"].direction;
#     moveNeeded = True;
#     if (currentDirection != "W" and currentX != 0):
#         print("turn left for X");
#         moveNeeded = False;
#         move = "L";
#     elif (currentX != 0 and moveNeeded):
#         print("move forward for x");
#         moveNeeded = False;
#         move = "F";
#     elif (currentDirection != "N" and currentY != 0 and moveNeeded):
#         print("face up for y");
#         moveNeeded = False;
#         move = "T";
#     elif (currentY != 0 and moveNeeded):
#         print("move forward for y");
#         moveNeeded = False;
#         move = "F";
#     elif (currentDirection != "E" and currentDirection != "S" and moveNeeded):
#         moveNeeded = True;
#         print("face east");
#         move = "R";
#     elif (currentDirection == "E"):
#         moveNeeded = True;
#         print("check other players");
#         move = "F";
#     elif (currentDirection == "S"):
#         moveNeeded = True;
#         print("check other players");
#         move = "F";
#     return moves[random.randrange(len(moves))]


# if __name__ == "__main__":
#   app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))

# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
