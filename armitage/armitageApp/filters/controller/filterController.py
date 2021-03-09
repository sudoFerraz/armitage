from flask import Blueprint
from .. service import filterService as filterService
from flask_cors import CORS, cross_origin
from flask import request
import json
from flask_api import status
from flask import abort

filter = Blueprint('filter', __name__)

def wrapValidAnswer(answer):
    content = json.dumps({"content": str(answer)})
    return content, status.HTTP_200_OK

def returnInvalidRequest():
    content = json.dumps({"error": "Something went wrong", "content": ""})
    return content, status.HTTP_400_BAD_REQUEST

def returnInvalidParams():
    content.json.dumps({"error": "Not a valid request", "content": ""})
    return content, status.HTTP_400_BAD_REQUEST

@filter.route('/filters', methods=['GET'])
@cross_origin()
def getAllRegisteredFilters():
    if request.method == 'GET':
        return wrapValidAnswer(filterService.getAllFilters())

@filter.route('/filters', methods=['POST'])
@cross_origin()
def registerNewFilter():
    if request.method == 'POST':
        if not request.json:
            abort(400)
        try:
            registeredSuccesfully = filterService.registerNewFilter(request.json)
