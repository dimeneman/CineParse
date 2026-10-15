import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
from backend.core import extract_movie_information


st.set_page_config(
    page_title="CineParse",
    page_icon="🎬",
    layout="centered",
)

st.title("🎬 CineParse")

st.write(
    "Extract structured movie information from any movie description using Gemini."
)

description = st.text_area(
    "Movie Description",
    height=250,
)

if st.button("Extract Information"):

    if not description.strip():

        st.warning("Please enter a movie description.")

    else:

        with st.spinner("Analyzing movie..."):

            movie = extract_movie_information(description)

        st.success("Extraction completed!")

        st.divider()

        st.header(movie.movie_name or "Unknown Movie")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Genre**")
            st.write(movie.genre)

            st.write("**Director**")
            st.write(movie.director)

            st.write("**Language**")
            st.write(movie.language)

            st.write("**Runtime**")
            st.write(movie.runtime)

        with col2:
            st.write("**Rating**")
            st.write(movie.rating)

            st.write("**Cast**")

            if movie.cast:
                for actor in movie.cast:
                    st.write(f"• {actor}")
            else:
                st.write("Not Available")

        st.subheader("Summary")

        st.write(movie.short_summary)

        with st.expander("View Raw JSON"):

            st.json(movie.model_dump())