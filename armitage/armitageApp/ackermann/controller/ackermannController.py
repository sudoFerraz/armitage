from flask import Blueprint
from ..service import ackermannService as ackermannService
from flask_cors import CORS, cross_origin
from flask import request
import json
from flask_api import status
from flask import abort

ackermann = Blueprint('ackermann', __name__)

def wrapValidAnswer(answer):
    content = json.dumps({"answer": str(answer)})
    return content, status.HTTP_200_OK

def returnInvalidRequest():
    content = json.dumps({"error": "Not valid key value params"})
    return content, status.HTTP_400_BAD_REQUEST


def returnInvalidParams():
    content = json.dumps({"error": "Not valid request"})
    return content, status.HTTP_400_BAD_REQUEST

@ackermann.route('/<int:m>/<int:n>', methods=['GET'])
@cross_origin()
def calculateAckermannGet(m, n):
    if request.method == 'GET':
        try:
            ackermannResult = ackermannService.sanitizeAndCalculate(m, n)
            return wrapValidAnswer(ackermannResult) if (ackermannResult != None) else returnInvalidParams()
        except:
            return returnInvalidRequest()

@ackermann.route('', methods=['POST'])
@cross_origin()
def calculateAckermann():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        try:
            print(ackermannService.sanitizeAndCalculate(1, 2))
            ackermannResult = ackermannService.sanitizeAndCalculate(request.json['m'], request.json['n'])
            return wrapValidAnswer(ackermannResult) if (ackermannResult != None) else returnInvalidParams()
        except:
            return returnInvalidRequest()