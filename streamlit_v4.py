import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="B.rad Fishing Report", page_icon="🎣")

st.title("🎣 B.rad Fishing Report")

st.write("Enter your fishing conditions below:")

lake = st.text_input("Lake", "Wilson")
species = st.selectbox("Species", ["Largemouth", "Smallmouth", "Spotted Bass"])
season = st.selectbox("Season", ["Winter", "Prespawn", "Spring", "Summer", "Fall"])
water_temp = st.text_input("Water Temp", "65")
water_clarity = st.selectbox("Water Clarity", ["Muddy", "Stained", "Clear"])
wind = st.selectbox("Wind", ["Calm", "Light", "Moderate", "Strong"])
sky = st.selectbox("Sky", ["Sunny", "Cloudy", "Mixed"])
structure = st.selectbox("Structure", ["Grass", "Rock", "Points", "Ledges", "Timber"])
notes = st.text_area("Notes")

if st.button("Generate Report"):
    prompt = f"""
    Create a bass fishing report.

    Lake: {lake}
    Species: {species}
    Season: {season}
    Water Temp: {water_temp}
    Water Clarity: {water_clarity}
    Wind: {wind}
    Sky: {sky}
    Structure: {structure}
    Notes: {notes}

    Include:
    - Pattern
    - Where to fish
    - Best baits
    - Depth
    - Backup plan
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    st.markdown(response.output_text)
