"""Simple streamlit app for Denver Python organization."""
from st_pages import Page, show_pages

page_list = [
    Page("pages/home.py", "Home"),
    Page("pages/general.py", "General Python Learning Resources"),
    Page("pages/data_science.py", "Data Science and Machine Learning with Python"),
    Page("pages/biology.py", "Biology and Bioinformatics with Python"),
]

show_pages(page_list)
