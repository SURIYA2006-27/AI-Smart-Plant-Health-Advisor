# AI-Smart-Plant-Health-Advisor
AI Smart Plant Health Advisor is a CNN-based web application that detects plant diseases from leaf images. Built using TensorFlow and Streamlit, it provides disease predictions, treatment suggestions, prevention tips, fertilizer recommendations, and PDF reports to support sustainable agriculture.
Download dataset from Kaggle:https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset
Download Dataset and make a Folder PlantHealthAdvisor,inside create a folder dataset .
Inside dataset paste Images 1.Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot,2.Corn_(maize)___Common_rust_,3.Corn_(maize)___healthy,4.Corn_(maize)___Northern_Leaf_Blight,5.Grape___Black_rot,6.Grape___Esca_(Black_Measles),7.Grape___healthy,8.Grape___Leaf_blight_(Isariopsis_Leaf_Spot),9.Orange___Haunglongbing_(Citrus_greening),10.Pepper,_bell___Bacterial_spot,11.Pepper,_bell___healthy,12.Potato___Early_blight,13.Potato___healthy,14.Potato___Late_blight,15.Strawberry___healthy,16.Strawberry___Leaf_scorch,17.Tomato___Early_blight,18.Tomato___healthy,19.Tomato___Late_blight.
Thsese are the 19 classes used to train the model.
Plants are Tomato,Potato,Corn,Strawberry,Citus,Grape,BellPeppper.If confused of point 5 download dataset and search name for exact name of folder and copy that folder and paste inside Dataset.
Create a another Folder Named knowledge_base and paste disease_info.py.
Create a folder named utils and paste files history_logger.py,leaf_validator.py,predictor.py,report_generator.py.
create a folder models and paste plant_disease_model.h5 or you can train the model by just running thhe train_model.py ,it will automatically store the plant_disease_model.h5 inside models.do any one.That train_model.py should be inside plantHealthAdvisor folder without any folder(normal file).
Paste app.py,fertilizer_info.py,requirements.txt without any folder but inside PlantHealthAdvisor.
After all setUp done use command  "  pip install -r requirements.txt " to download all necessaary libraries.
