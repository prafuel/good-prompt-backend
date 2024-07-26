
from flask import Flask, request
from flask_cors import CORS
import json

from dotenv import load_dotenv
load_dotenv()

from src.modules import llms,mongodb

app = Flask(__name__)
CORS(app)

gemini = llms.Gemini()
mongo = mongodb.Mongo()

# current model, gemini
model = gemini

# helper
def output_format(result: str):
	return {
			"output" : result
		}

@app.route("/", methods=['get'])
def main():
	return output_format("200, Server is on")

@app.route("/refine", methods=['post'])
def refine():
	# {data : {"input" : "text"}}
	data = request.json['data']

	output = model.customize_prompt(data['input'], refine=True)
	return output_format(output)

@app.route("/generate_prompt", methods=['post'])
def generate_prompt():
	# {data : {"input":"<question>", "type":"<list>", "format":"```1. <point 1>, 2. <point 2> ```" ...}}
	data = request.json['data']

	output = model.customize_prompt(data, refine=False, generate=True)
	return output_format(output)

@app.route("/transform", methods=['post'])
def transform_prompt():
	# {data : {"from_this" : <prompt>, "to_this" : <prompt>}}
	data = request.json['data']
	from_this = data['from_this']
	to_this = data['to_this']

	output = model.transform_prompt(from_this=from_this, to_this=to_this)
	return output_format(output)

@app.route("/result", methods=['post'])
def result():
	# {data : {"prompt" : "abc"}}
	data = request.json['data']
	output = model.result(data['input'])
	return output_format(output)

@app.route("/mongo/collection/<collection>", methods=['get'])
def get(collection:str):
	output = mongo.get(collection)
	return output_format(output)

# if __name__ == '__main__':
# 	app.run(debug=True, port=8000)