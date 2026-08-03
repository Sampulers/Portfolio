import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title='Suhas Shangrapawar | Portfolio', page_icon='📊', layout='wide')

base_dir = Path(__file__).resolve().parent
html_content = (base_dir / 'index.html').read_text(encoding='utf-8')
style_content = (base_dir / 'style.css').read_text(encoding='utf-8')
script_content = (base_dir / 'script.js').read_text(encoding='utf-8')

html_content = html_content.replace('<link rel="stylesheet" href="style.css" />', f'<style>{style_content}</style>')
html_content = html_content.replace('<script src="script.js"></script>', f'<script>{script_content}</script>')

components.html(html_content, height=2400, scrolling=True)
