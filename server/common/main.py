# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response
from flask import request
import subprocess
from flask_cors import CORS
import base64
import os
import aiml
import json
import htmlParse

api = Flask(__name__)
CORS(api)

@api.route('/getUser/<string:userId>', methods=['GET'])
def get_user(userId):

    #textToWav('hello world','C:/Users/9222034/Desktop/tts/ello_ttest')
    BRAIN_FILE="brain.dump"

    k = aiml.Kernel()
    if os.path.exists(BRAIN_FILE):
        print("Loading from brain file: " + BRAIN_FILE)
        k.loadBrain(BRAIN_FILE)
    else:
        print("Parsing aiml files")
        k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
        print("Saving brain file: " + BRAIN_FILE)
        k.saveBrain(BRAIN_FILE)

    response = k.respond(userId)

    result = {
        "result":True,
        "data":{
            "userId":"test"
            }
        }

    #return make_response(jsonify(result))
    img_file = 'C:/Users/9222034/Downloads/new/suzi.jpg'
    b64 = base64.encodestring(open(img_file, 'rb').read())
    #return "data:image/png;base64,"+b64.decode('utf8')
    return response
    # Unicodeにしたくない場合は↓
    # return make_response(json.dumps(result, ensure_ascii=False))

@api.route('/transPage', methods=['POST'])
def changeTransPage():
  parsed = json.loads(request.data)
  textValue = parsed['transValue']
  print(textValue)
  myclass = htmlParse.HtmlSourceClass()
  myclass.setInfo(textValue)
  myclass.editHtmlPageSource()
  print(myclass.getInfo())
  result = {
    "data": {
      "id": 1,
      "textValue": myclass.getInfo() 
      }
    }
  del myclass
  return jsonify(result) 

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def textToWav(text,file_name):
   subprocess.Popen(["C:/Program Files (x86)/eSpeak/command_line/espeak.exe", "-w"+file_name+".wav", text],shell=True)

if __name__ == '__main__':
    api.run(host='127.0.0.1', port=3000)
