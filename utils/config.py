import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from utils.constants import DOCUMENTATION_SYSTEM_PROMPT, DOCUMENTATION_STYLE, DOCUMENTATION_MIGRATION_SYSTEM_PROMPT
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

load_dotenv()


def setup_llm(provider, model, api_key):
    match provider:
        case "Google":
            return setup_google_llm(model, api_key)
        case "OpenAI":
            return setup_openai_llm(model, api_key)
        case _:
            raise ValueError(f"Provider {provider} not supported")


def setup_google_llm(model, api_key):
    llm = ChatGoogleGenerativeAI(model=model, google_api_key=api_key)
    return llm


def setup_openai_llm(model, api_key):
    llm = ChatOpenAI(model=model, api_key=api_key)
    return llm


def analyze_content(filename, filecontent, language, provider, model, api_key):

    llm = setup_llm(provider, model, api_key)
    prompt = PromptTemplate.from_template(template=DOCUMENTATION_SYSTEM_PROMPT)
    prompt_formatted = prompt.format(
        filename=filename, code=filecontent, language=language, documentation_style=DOCUMENTATION_STYLE
    )

    response = llm.invoke(prompt_formatted)
    return response.content


def create_migration_documentation(filecontent, language, provider, model, api_key):


    llm = setup_llm(provider, model, api_key)

    prompt = PromptTemplate.from_template(template=DOCUMENTATION_MIGRATION_SYSTEM_PROMPT)
    
    prompt_formatted = prompt.format(
        documentation=filecontent, language=language, documentation_style=DOCUMENTATION_STYLE
    )

    response = llm.invoke(prompt_formatted)
    return response.content
