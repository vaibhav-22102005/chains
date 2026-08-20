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


template_ = """for given {meal}, give me a step by step reciepe, including all necessary details and quantity required
YOUR REPONSE:
"""

prompt_reciepe = PromptTemplate(
    llm = client,
    input_variables = ["meal"],
    template = template_
)

reciepe_chain = LLMChain(lmm = client, prompt = prompt_reciepe, output_key = "reciepe")

time_template = """given the reciepe {reciepe}, estimate how much time do i need to cook it
YOUR REPONSE
"""

prompt_time = PromptTemplate(
    llm = client,
    input_variables = ['reciepe'],
    template = time_template
)

time_chain = LLMChain(llm = client, prompt= prompt_time, ouput_key = "time")