from flask import Blueprint
from ..service import factorialService as factorialService
from flask_cors import CORS, cross_origin
from flask import request
import json
from flask_api import status
from flask import abort

factorial = Blueprint('factorial', __name__)

def wrapValidAnswer(answer):
    content = json.dumps({"answer": str(answer)})
    return content, status.HTTP_200_OK

def returnInvalidRequest():
    content = json.dumps({"error": "Not valid key value params"})
    return content, status.HTTP_400_BAD_REQUEST

def returnInvalidParams():
    content = json.dumps({"error": "Not valid request"})
    return content, status.HTTP_400_BAD_REQUEST

@factorial.route('/<int:factorialTarget>', methods=['GET'])
@cross_origin()
def calculateFactorialGet(factorialTarget):
    if request.method == 'GET':
        try:
            return wrapValidAnswer(factorialService.sanitizeAndCalculate(factorialTarget))
        except:
            return returnInvalidParams()

@factorial.route('', methods=['POST'])
@cross_origin()
def calculateFactorial():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        try:
            factorialResult = factorialService.sanitizeAndCalculate(request.json['factorialTarget'])
            return wrapValidAnswer(factorialResult) if (factorialResult != None) else returnInvalidParams()
        except:
            return returnInvalidRequest()