import google.generativeai as genai
from langchain.prompts import PromptTemplate

import os
import json

templates = json.load(open("src/templates.json", "r"))["prompts"]

class Gemini:
	def __init__(self) -> None:
		genai.configure(api_key=os.environ['GOOGLE_GEMINI_TOKEN'])
		self.model = genai.GenerativeModel('gemini-pro')

	def handle_error(self, message:str) -> str:
		try : 
			res = self.model.generate_content(message)
			return res.text
		except Exception as e:
			return str(e)

	def customize_prompt(self, message:str|dict, refine=True, generate=False) -> str:
		if refine:
			# refine / correct its language
			prompt = PromptTemplate(template=templates["refine"], input_variables=["text"]).format(text=message)

		if generate:
			# generation
			prompt = PromptTemplate(template=templates["generate"], input_variables=["json"]).format(json=message)

		return self.handle_error(prompt)

	def transform_prompt(self, from_this:str, to_this:str) -> str:
		prompt = PromptTemplate(template=templates["transform"], input_variables=["from_this", "to_this"]).format(from_this=from_this, to_this=to_this)
		return self.handle_error(prompt)

	def result(self, message:str) -> str:
		return self.handle_error(message)
