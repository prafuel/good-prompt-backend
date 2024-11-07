from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

import os
import json

from dotenv import load_dotenv
load_dotenv()

'''
current idea, 
select most similer prompt from prebuilt prompts based on query by user, 
and treat them as examples, and use it to make customize prompt for user

'''

# templates = json.load(open("src/templates.json", "r"))["prompts"]


def str_output(str):
    return (
        str.content
        .strip()
        .replace("**", "")
    )


class Gemini:
    def __init__(self) -> None:
        self.model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

    def customize_prompt(self, message: str | dict, refine=True, generate=False) -> str:
        pass

    def transform_prompt(self, from_this: str, to_this: str) -> str:
        pass

    def generate(self, messages, input_dict: dict) -> str:
        chain = (
            messages
            | self.model
            | str_output
        )
        return chain.invoke(input_dict)


if __name__ == "__main__":
    gemini = Gemini()

    examples = '''
	'user': 'An Ethereum Developer', 'prompt': 'Imagine you are an experienced Ethereum developer tasked with 
    creating a smart contract for a blockchain messenger. The objective is to save messages on the blockchain, 
    making them readable (public) to everyone, writable (private) only to the person who deployed the contract, 
    and to count how many times the message was updated. Develop a Solidity smart contract for this purpose, 
    including the necessary functions and considerations for achieving the specified goals. Please provide the 
    code and any relevant explanations to ensure a clear understanding of the implementation.
	
	'''

    # testing
    messages = ChatPromptTemplate([
        ("system", "You are assistant bot, who act as per the instruction given, and dont inturrupt into anything user asked for, solves all the issue that are regarding to given task and role"),
        ("human",
         """Understand user and its relevent task, based on role the following generate prompt which will be customized for given user role={role}, task={task},
         For Examples, {examples}
         """)
    ])
    task = "working on e-commarce website, and implementing features such as admin panel, customer panel, buying etc, default task you can think of."
    role = "web developer"
    
    res = gemini.generate(
        messages, {"role": task, "task": task, "examples": examples}
    )
    
    messages.append(res)
    print("Response >", res)

    # while True:
    #     user = input("You> ")
    #     messages.append(("human", user))

    #     res = gemini.generate(
    #         messages, {"role": role, "task": task, "examples" : examples})
    #     messages.append(("ai", res))
    #     print("Response >", res)
