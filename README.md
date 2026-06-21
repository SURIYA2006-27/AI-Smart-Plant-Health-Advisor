# 🌱 AI Smart Plant Health Advisor

AI Smart Plant Health Advisor is a CNN-based web application that detects plant diseases from leaf images using TensorFlow and Streamlit. It provides disease predictions, treatment suggestions, prevention tips, fertilizer recommendations, and PDF reports to support sustainable agriculture.

---

## 📥 Dataset

Dataset used:

Kaggle PlantVillage Dataset
https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset

Download the dataset and create the following folder structure:

PlantHealthAdvisor/

├── dataset/
│   ├── Corn_(maize)__*Cercospora_leaf_spot Gray_leaf_spot*
*│   ├── Corn*(maize)_**Common_rust**
*│   ├── Corn*(maize)__*healthy*
*│   ├── Corn*(maize)***Northern_Leaf_Blight***
***│   ├── Grape___Black_rot***
***│   ├── Grape___Esca*****(Black_Measles)**
**│   ├── Grape___healthy**
**│   ├── Grape___Leaf_blight***(Isariopsis_Leaf_Spot)*
*│   ├── Orange___Haunglongbing*(Citrus_greening)
│   ├── Pepper,_bell___Bacterial_spot
│   ├── Pepper,_bell___healthy
│   ├── Potato___Early_blight
│   ├── Potato___healthy
│   ├── Potato___Late_blight
│   ├── Strawberry___healthy
│   ├── Strawberry___Leaf_scorch
│   ├── Tomato___Early_blight
│   ├── Tomato___healthy
│   └── Tomato___Late_blight

These are the 19 classes used to train the model.

---

## 🌿 Supported Plants

* Tomato
* Potato
* Corn
* Strawberry
* Orange (Citrus)
* Grape
* Bell Pepper

---

## 📂 Project Structure

PlantHealthAdvisor/

├── app.py
├── fertilizer_info.py
├── requirements.txt
├── train_model.py

├── models/
│   └── plant_disease_model.h5

├── knowledge_base/
│   └── disease_info.py

└── utils/
├── history_logger.py
├── leaf_validator.py
├── predictor.py
└── report_generator.py

---

## ⚙️ Installation

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 Model Training

You can either:

1. Use the provided `plant_disease_model.h5` file

OR

2. Train the model manually using:

```bash
python train_model.py
```

The trained model will automatically be saved inside the `models` folder.

---

## 📸 How to Use

1. Run the Streamlit app
2. Upload a plant leaf image
3. The AI model predicts the disease
4. View disease information and fertilizer recommendations
5. Download the generated PDF report

---

## 🎯 SDG Alignment

This project supports:

* SDG 2: Zero Hunger
* SDG 12: Responsible Consumption and Production
* SDG 15: Life on Land
