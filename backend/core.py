from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

from .models import MovieInformation


load_dotenv()


# -------------------------
# Parser
# -------------------------

parser = PydanticOutputParser(
    pydantic_object=MovieInformation
)


# -------------------------
# Prompt
# -------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert movie information extraction assistant.

Extract only the information explicitly mentioned.

Do NOT hallucinate.

If information is missing, return null.

{format_instructions}
"""
        ),
        (
            "human",
            """
Movie Description:

{movie_description}
"""
        ),
    ]
)


# -------------------------
# LLM
# -------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)


# -------------------------
# Main Function
# -------------------------

def extract_movie_information(description: str):

    final_prompt = prompt.invoke(
        {
            "movie_description": description,
            "format_instructions": parser.get_format_instructions(),
        }
    )

    response = llm.invoke(final_prompt)

    movie = parser.parse(response.text)

    return movie