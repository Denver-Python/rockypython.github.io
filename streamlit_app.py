"""Simple streamlit app for Denver Python organization."""
from st_pages import Page, show_pages

page_list = [
    Page("home.py", "Home"),
    Page("general.py", "General Python Learning Resources"),
    Page("data_science.py", "Data Science and Machine Learning with Python"),
    Page("biology.py", "Biology and Bioinformatics with Python"),
]

show_pages(page_list)
