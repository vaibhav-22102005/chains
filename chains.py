# langgchain sequential chain
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
template = """your job is to come up with classic dish from areas user suggests.
{location}
YOUR REPONSE:
"""
client = OpenAI()

prompt = PromptTemplate(
    llm = client,
    input_variables=["location"],
    template=template,
)

location_chain = LLMChain(llm = client, prompt = prompt, output_key = "meal")