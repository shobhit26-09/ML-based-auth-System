# 🎤 Voice Authentication System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Librosa](https://img.shields.io/badge/Librosa-Audio%20Processing-orange)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-yellow)

🚀 **Voice Authentication System** uses state-of-the-art audio processing and machine learning techniques to authenticate users based on their voice. 

🔐 **Secure** | 🎛️ **Flexible** | 🤖 **AI-Powered**

---

## 🌟 Features

✨ **Real-time Voice Authentication**  
🎶 **Audio Feature Extraction using `librosa`**  
🤝 **Robust Machine Learning Models** (SVM, Isolation Forest)  
📊 **Detailed Logging of Authentication Attempts**  
📈 **Data Augmentation for Enhanced Model Accuracy**

---

## 🛠️ Technologies Used

| Technology         | Purpose                      |
|---------------------|------------------------------|
| 🎛️ `sounddevice`    | Audio recording             |
| 🎶 `librosa`         | Feature extraction          |
| 🤖 `scikit-learn`    | ML model training           |
| 🧰 `numpy`           | Data manipulation           |
| 📂 `pickle`          | Model persistence           |

---

## 🎯 Workflow

```mermaid
graph TD;
    A[Collect Data] --> B[Extract Features];
    B --> C[Augment Data];
    C --> D[Train Model];
    D --> E[Authenticate User];
