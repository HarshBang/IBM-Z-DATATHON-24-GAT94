import streamlit as st
import joblib
import pandas as pd
import numpy as np

# ----------------------------------
# Load trained pipeline
# ----------------------------------
pipeline = joblib.load("youtube_engagement_pipeline.pkl")

st.set_page_config(
    page_title="YouTube Engagement Predictor",
    layout="centered"
)

st.title("📊 YouTube Engagement Rate Predictor")
st.write("Predict expected engagement **before uploading a video**")

st.divider()

# ----------------------------------
# User Inputs
# ----------------------------------

title = st.text_input("📌 Video Title")
description = st.text_area("📝 Video Description")

subscriber_count = st.number_input(
    "👥 Channel Subscriber Count",
    min_value=0,
    value=1000,
    step=100
)

upload_hour = st.slider(
    "⏰ Planned Upload Hour",
    min_value=0,
    max_value=23,
    value=18
)

# Weekday dropdown (UI-friendly)
weekday_map = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

selected_day = st.selectbox(
    "📅 Planned Upload Day",
    list(weekday_map.keys())
)

upload_day = weekday_map[selected_day]

# Weekend logic (background)
is_weekend = 1 if upload_day in [5, 6] else 0

# ----------------------------------
# Prediction
# ----------------------------------

if st.button("🚀 Predict Engagement"):
    if title.strip() == "":
        st.warning("Please enter a video title")
    else:
        input_df = pd.DataFrame({
            "text_combined": [title + " " + description],
            "log_subscriber_count": [np.log1p(subscriber_count)],
            "upload_hour": [upload_hour],
            "upload_day": [upload_day],
            "is_weekend": [is_weekend]
        })

        prediction = pipeline.predict(input_df)[0]

        st.divider()
        st.subheader("📈 Prediction Result")

        st.success(f"**Predicted Engagement Rate: {prediction:.2f}%**")

        # Interpretation
        if prediction < 3:
            st.info("⚠️ Low expected engagement")
        elif prediction < 7:
            st.info("👍 Medium expected engagement")
        else:
            st.success("🔥 High expected engagement")

        # Debug / transparency (optional)
        with st.expander("🔍 See internal feature values"):
            st.write(f"Upload day (number): {upload_day}")
            st.write(f"Is weekend: {is_weekend}")
