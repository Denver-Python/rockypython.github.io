"""Denver Python resources for bioinformatics"""
import streamlit as st

from helpers import page_preamble, column_content_from_csv

page_preamble(
    "Data Science and Machine Learning with Python",
    """Providing resources for students and practitioners at all levels of expertise. Our group holds regular Meetup events and is free to join.""",
)

col1, _, _ = st.columns(3)
column_content_from_csv(col1, "free-ds-learning-links.csv", "### Data Science Learning Resources")
