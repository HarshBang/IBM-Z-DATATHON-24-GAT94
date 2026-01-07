# 📊 YouTube Pre-Upload Engagement Rate Predictor

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![NLTK](https://img.shields.io/badge/NLP-TFIDF%20%7C%20Text%20Processing-blue?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

A machine learning system that predicts the **expected engagement rate of a YouTube video before upload**, using only pre-publish information such as the video title, description, planned upload time, and channel subscriber count.

## 🔍 Why This Project?
Most analytics tools analyze performance **after** a video is published. This project addresses the **cold-start problem** by helping creators estimate engagement **before uploading**, enabling better content and timing decisions.

## 🧠 System Flow 

<img width="378" height="1120" alt="image" src="https://github.com/user-attachments/assets/0b5040e0-1fe3-4d04-82f2-bd97b695690b" />

## 📈 Model Performance 

- The model predicts engagement within approximately **±1 percentage point**, which is strong given the noisy nature of social media engagement.
- The reported performance was achieved after tuning the Random Forest model with **200 estimators** and a **maximum depth of 15**, balancing bias and variance for stable generalization.

## 🛠️ Tech Stack

- **Language:** Python  
- **ML & NLP:** Scikit-learn, TF-IDF  
- **Model:** Random Forest Regressor  
- **Frontend:** Streamlit  
- **Version Control:** Git & GitHub  

## 🚀 Streamlit Application [Link](https://erpredictor.streamlit.app/)

The Streamlit app allows users to:
1. Enter video title and description  
2. Select upload day (Monday–Sunday)  
3. Choose upload time  
4. Input subscriber count  
5. Instantly receive predicted engagement rate  

> All preprocessing is embedded inside a single ML pipeline, ensuring consistency between training and inference.

## 🔐 Data Handling Note

- Dataset uses **public YouTube metadata**
- Raw datasets are excluded from version control
- Data can be regenerated using the data collection scripts

This follows standard industry practices for data security, reproducibility, and responsible ML development.

## 👤 About Me

I am a passionate student at **NMIMS School of Technology Management and Engineering**, pursuing **Computer Science Engineering with a specialization in Data Science**.

This project reflects my interest in building **practical, deployable ML systems** that solve real-world problems, combining **machine learning, NLP, and system design**.


## 📩 Contact

- **Email:** harshbang10@gmail.com  
- **LinkedIn:** [Harsh Bang](https://www.linkedin.com/in/harshbang/)

⭐ If you find this project interesting, feel free to explore the code or connect with me.
