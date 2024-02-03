"""File of common routines."""
import csv

import streamlit as st


def page_preamble(
    title: str,
    description: str,
    image_file: str = "static-files/img/mountain-group-2.jpg",
):
    """Set up the start of the page."""
    st.set_page_config(layout="wide")
    st.image(image_file, caption="Denver pythonistas searching for a wifi connection")
    st.title(title)
    st.markdown(description)


def column_content_from_csv(column, filename: str, title: str):
    """Populate a column with links from CSV file."""
    with open(filename, encoding="utf-8") as handle:
        column.markdown(title)
        reader = csv.reader(handle, delimiter=",")
        _ = next(reader, None)  # CSV headers
        for (text, link)in reader:
            column.markdown(f"- [{text}]({link})  ")
