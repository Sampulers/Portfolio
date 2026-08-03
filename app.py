import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title='Suhas Shangrapawar | Portfolio', page_icon='📊', layout='wide')
html_path = Path(__file__).with_name('index.html')
html_content = html_path.read_text(encoding='utf-8')
components.html(html_content, height=2200, scrolling=True)
