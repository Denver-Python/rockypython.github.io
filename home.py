"""Home page of this streamlit app."""
import streamlit as st

from helpers import page_preamble

page_preamble(
    "Rocky Python",
    """A Denver-Boulder area Python interest group connecting people with interests in web development, data science, biology, and anything related to the Python programming language, at all levels of expertise.""",
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Sponsors")
    st.markdown("""If you or your business would like to sponsor our groups by providing food, venue, or giveaways, please [email us](rockypython@googlegroups.com).""")

with col2:
    st.markdown("### Join us on Discord")
    st.markdown("""Meetup events aren't the only time for chatting. There's also a [Discord server](https://discord.gg/7RXCGwxAzw). Sign on to ask questions, give answers, or just hang out. Discord is great place to promote a job posting at your company.""")

with col3:
    st.markdown("### Upcoming meetups")
    st.markdown("""We have a bi-weekly co-working & study group meetup on Sundays and a monthly meetup on Sundays with 5-7 minute lightning talks.

If you're interested in giving a talk, please sign up.

You can find our schedule of events on our Meetup page. If you or your business would like to sponsor a meetup with food, space, or giveaways, please [contact us](rockypython@googlegroups.com).""")
