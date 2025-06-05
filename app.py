import streamlit as st
from PIL import Image
from outfit_suggester import match_outfits
from size_predictor import estimate_size
from fitbot import ask_fitbot

st.set_page_config(page_title="FitSnap AI", layout="wide")
st.title("👟 FitSnap AI – Outfit Match & Size Predictor")

st.markdown("📸 Upload a full-body image to get fashion advice and size prediction.")

img_file = st.file_uploader("Upload Image", type=["jpg", "png"])
height = st.number_input("Enter height (cm)", min_value=100, max_value=250, step=1)
weight = st.number_input("Enter weight (kg)", min_value=30, max_value=200, step=1)
body_type = st.selectbox("Choose your body type", ["Slim", "Curvy", "Athletic"])

if st.button("🧵 Suggest Outfits"):
    outfits = match_outfits(body_type)
    size = estimate_size(height, weight)
    st.success(f"✅ Recommended size: {size}")
    st.subheader("🧥 Outfit Suggestions")
    for item in outfits:
        st.markdown(f"- {item}")

if st.button("📥 Download Style-Fit Report"):
    report = f"Body Type: {body_type}\nSize: {estimate_size(height, weight)}\nRecommended Outfits: {', '.join(match_outfits(body_type))}"
    st.download_button("Download Report", report, file_name="style_report.txt")

st.divider()
st.subheader("💬 Ask FitBot")
query = st.text_input("Type your fashion/fit question here")
if query:
    response = ask_fitbot(query)
    st.markdown(response)
