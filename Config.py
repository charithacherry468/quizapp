# Config.py — reads flat keys from Streamlit secrets
import streamlit as st

DB_HOST     = st.secrets["DB_HOST"]
DB_USER     = st.secrets["DB_USER"]
DB_PASSWORD = st.secrets["DB_PASSWORD"]
DB_NAME     = st.secrets["DB_NAME"]

SENDER_EMAIL        = st.secrets["SENDER_EMAIL"]
SENDER_APP_PASSWORD = st.secrets["SENDER_APP_PASSWORD"]

SPECIAL_CHARS = st.secrets.get("SPECIAL_CHARS", "!@#$%^&*()_+-=[]{}|;':\",./<>?")
