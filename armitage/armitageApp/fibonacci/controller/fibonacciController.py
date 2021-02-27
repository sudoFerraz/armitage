from flask import Blueprint
from ..service import fibonacciService as fibonacciService
from flask_cors import CORS, cross_origin
from flask import request
import json
from flask_api import status
from flask import abort

fibonacci = Blueprint('fibonacci', __name__)

def wrapValidAnswer(answer):
    content = json.dumps({"answer": str(answer)})
    return content, status.HTTP_200_OK

def returnInvalidRequest():
    content = json.dumps({"error": "Not valid key value params"})
    return content, status.HTTP_400_BAD_REQUEST

def wrapValidRow(fibonacciCalculationRow):
    content = json.dumps({"id": fibonacciCalculationRow.id,\
         "time_spent": fibonacciCalculationRow.time_spent,\
              "result": fibonacciCalculationRow.time_spent})
    return content, status.HTTP_200_OK

def returnInvalidParams():
    content = json.dumps({"error": "Not valid request"})
    return content, status.HTTP_400_BAD_REQUEST

@fibonacci.route('/async/<int:fibonacciStep>', methods=['GET'])
@cross_origin()
def calculateFibonacciAsync(fibonacciStep):
    if request.method == 'GET':
            fibonacciRowId = fibonacciService.ayncSanitizeAndCalculate(fibonacciStep)
            return wrapValidAnswer(fibonacciRowId) if (fibonacciRowId != None) else returnInvalidParams()

@fibonacci.route('/results/<int:row>', methods=['GET'])
@cross_origin()
def retrieveFibonacciResults(row):
    if request.method == 'GET':
        fibonacciResult = fibonacciService.retrieve_calculation_row(row)
        return wrapValidRow(fibonacciResult) if (row != None) else returnInvalidParams()

@fibonacci.route('/<int:fibonacciStep>', methods=['GET'])
@cross_origin()
def calculateFibonacciGet(fibonacciStep):
    if request.method == 'GET':
        try:
            fibonacciResult = fibonacciService.sanitizeAndCalculate(fibonacciStep)
            return wrapValidAnswer(fibonacciResult) if (fibonacciResult != None) else returnInvalidParams()
        except:
            return returnInvalidParams()

@fibonacci.route('', methods=['POST'])
@cross_origin()
def calculateFibonacci():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        try:
            fibonacciResult = fibonacciService.sanitizeAndCalculate(request.json['fibonacciStep'])
            return wrapValidAnswer(fibonacciResult) if (fibonacciResult != None) else returnInvalidParams()
        except:
            return returnInvalidRequest()