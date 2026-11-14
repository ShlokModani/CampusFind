from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CampusFind - VIT Bibwewadi", page_icon="🧭", layout="wide")

st.markdown(
    "<style>.block-container{padding-top:1rem;padding-bottom:0;max-width:1200px}</style>",
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("campusfind.html").read_text(encoding="utf-8")
components.html(html, height=760, scrolling=True)
