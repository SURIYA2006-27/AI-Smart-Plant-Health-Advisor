import streamlit as st
from PIL import Image
import pandas as pd
import os
from fertilizer_info import fertilizer_info
import tempfile
from datetime import datetime
from utils.report_generator import create_report
from utils.predictor import predict_image
from utils.leaf_validator import is_leaf
from knowledge_base.disease_info import DISEASE_INFO
from utils.history_logger import save_prediction
st.set_page_config(
    page_title="AI Smart Plant Health Advisor",
    page_icon="🌱"
)

st.title("🌱 AI Smart Plant Health Advisor")

st.info("""
Supported Plants:
🌽 Corn
🍇 Grape
🍊 Orange
🫑 Bell Pepper
🥔 Potato
🍓 Strawberry
🍅 Tomato
""")

st.write("Upload a plant leaf image to detect diseases and get treatment advice.")

uploaded_file = st.file_uploader(
    "Upload a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        image.save(tmp.name)
        image_path = tmp.name

    if not is_leaf(image_path):

        st.error(
            "❌ Not a plant leaf image. Please upload a valid plant leaf."
        )

    else:

        predicted_class, confidence, top_predictions = predict_image(image_path)

        report_time = datetime.now().strftime("%d %b %Y, %I:%M:%S %p")

        if confidence < 60:

            st.warning("⚠️ Unsupported plant species or uncertain prediction.")

            st.write("The uploaded leaf may not belong to the supported plants ""(Corn, Grape, Orange, Bell Pepper, Potato, Strawberry, Tomato).")

            st.stop()

        plant, disease = predicted_class.split("___")

        st.success("🌱 Plant Leaf Detected")

        st.write(f"### Plant: {plant}")

        if "healthy" in disease.lower():
            st.write("### Status: Healthy ✅")
        else:
            st.write(f"### Disease: {disease}")

        st.write(f"### Confidence: {confidence:.2f}%")

        # Confidence Level
        if confidence >= 90:
            st.success("High Confidence Prediction ✅")
        elif confidence >= 70:
            st.warning("Moderate Confidence Prediction ⚠️")
        else:
            st.error("Low Confidence Prediction ❗")

        # Top 3 Predictions
        st.subheader("🔍 Top 3 Predictions")

        for i, (cls, conf) in enumerate(top_predictions, start=1):
            st.write(f"{i}. {cls} — {conf:.2f}%")

        # Disease Information
        if predicted_class in DISEASE_INFO:

            info = DISEASE_INFO[predicted_class]

            st.subheader("📋 Disease Information")

            st.write("**Cause:**")
            st.write(info["cause"])

            st.write("**Treatment:**")
            st.write(info["treatment"])

            st.write("**Prevention:**")
            st.write(info["prevention"])

            st.subheader("🚜 Farmer Action Plan")

            if "healthy" in predicted_class.lower():

                st.success("✅ Plant appears healthy.")

                st.write("• Continue regular monitoring.")
                st.write("• Maintain proper watering and nutrition.")
                st.write("• Inspect leaves weekly for any unusual symptoms.")
                st.write("• Follow good farming practices.")

            else:

                st.write("• Inspect nearby plants for similar symptoms.")
                st.write("• Remove severely infected leaves or plant parts.")
                st.write("• Follow the recommended treatment mentioned above.")
                st.write("• Monitor disease spread every few days.")
                st.write("• Keep tools and equipment clean to avoid spreading infection.")
                st.write("• Consult local agricultural experts if the disease worsens.")

            st.subheader("🌱 Fertilizer Recommendation")

            fert_info = fertilizer_info.get(predicted_class)

            if fert_info:

                st.write("### Recommended")

                for item in fert_info["recommended"]:
                    st.write(f"✅ {item}")

                if fert_info["avoid"]:

                    st.write("### Avoid")

                    for item in fert_info["avoid"]:
                        st.write(f"❌ {item}")

            else:

                st.info("No fertilizer recommendations available.")

            st.write(f"🕒 Prediction Time: {report_time}")

            create_report(
                    "plant_report.pdf",
                    plant,
                    disease,
                    confidence,
                    info["cause"],
                    info["treatment"],
                    info["prevention"],
                    report_time
                )

            with open("plant_report.pdf", "rb") as pdf_file:

                st.download_button(
                    label="📥 Download Report",
                    data=pdf_file,
                    file_name="plant_report.pdf",
                    mime="application/pdf"
            )
                
            st.subheader("📊 Prediction History")

            if os.path.exists("prediction_history.csv"):

                history = pd.read_csv("prediction_history.csv")

                st.dataframe(
                    history.tail(10),
                    use_container_width=True
                )

            else:

                st.info("No prediction history available.")

        else:
            st.warning("Disease information not available.")


        save_prediction(
                plant,
                disease,
                confidence,
                report_time
        )