import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel , Field
from typing import Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

# Pydantic class 
class MovieInformation(BaseModel):
    movie_name: Optional[str] = Field(default=None, description="Name of the movie")
    genre: Optional[str] = Field(default=None, description="Genre of the movie")
    director: Optional[str] = Field(default=None, description="Director of the movie")
    cast: list[str] = Field(default_factory=list, description="Main cast members")
    rating: Optional[str] = Field(default=None, description="Movie rating")
    runtime: Optional[str] = Field(default=None, description="Runtime of the movie")
    language: Optional[str] = Field(default=None, description="Language of the movie")
    short_summary: Optional[str] = Field(default=None, description="Brief summary")


parser = PydanticOutputParser(pydantic_object=MovieInformation)

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Information Extractor")
st.write("Enter a movie description and let Gemini extract the important details.")

# -----------------------------
# Prompt Template
# -----------------------------
template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert movie information extraction assistant. "
        "Extract only the information explicitly mentioned in the description. "
        "If any field is missing, write 'Not Mentioned'."
    ),
    (
        "human",
        """
Extract the following information:

- Movie Name
- Genre
- Director
- Cast
- Rating
- Runtime
- Language
- Short Summary

Movie Description:
{movie_description}
"""
    )
])

# -----------------------------
# User Input
# -----------------------------
description = st.text_area(
    "Movie Description",
    height=220,
    placeholder="Paste a movie description here..."
)

# -----------------------------
# Button
# -----------------------------
if st.button("Extract Information"):

    if not description.strip():
        st.warning("Please enter a movie description.")
        st.stop()

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite"
    )

    prompt = template.invoke({
        "movie_description": description
    })

    with st.spinner("Analyzing movie..."):

        response = llm.invoke(prompt)

    st.success("Extraction Complete!")

    st.markdown("## 📄 Extracted Information")

    st.markdown(response.text)