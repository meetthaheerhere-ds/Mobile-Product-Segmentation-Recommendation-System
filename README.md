# 📱 Mobile Product Segmentation & Recommendation System

## 📌 Project Overview

This project focuses on analyzing global mobile product reviews using Python, Machine Learning, and Streamlit.

The dataset contains mobile phone reviews, ratings, pricing information, product specifications, and customer sentiment collected from multiple brands and platforms.

The project performs data preprocessing, exploratory data analysis (EDA), feature engineering, product segmentation using K-Means Clustering, and builds a content-based recommendation system using the K-Nearest Neighbors (KNN) algorithm.

An interactive Streamlit dashboard allows users to explore mobile clusters, compare product segments, and receive personalized mobile recommendations based on their preferred brand, price range, and minimum rating.

---

# 🚀 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

---

# 📊 Key Features

✔ Data Cleaning & Preprocessing

✔ Exploratory Data Analysis (EDA)

✔ Feature Engineering

✔ Feature Scaling

✔ K-Means Clustering

✔ Product Segmentation

✔ Cluster Comparison Dashboard

✔ Cluster Explorer Dashboard

✔ K-Nearest Neighbors (KNN) Recommendation System

✔ Brand, Price & Rating Based Mobile Recommendation

✔ Interactive Streamlit Dashboard

✔ Business Insights Generation

---

# 📁 Project Structure

```bash
📦 Global Mobile Project
 ┣ 📄 app.py
 ┣ 📄 Global_Mobile_Project.ipynb
 ┣ 📄 README.md
 ┣ 📄 requirements.txt
 ┣ 📄 final_mobile_reviews.csv
 ┣ 📄 Mobile_Project_Presentation.pptx
 ┣ 📄 Mobile Reviews Sentiment null.csv
 ┗ 📄 Global Mobile Reviews.docx.pdf
```

---

# ⚙️ How to Run the Project

## 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 2️⃣ Run the Streamlit Dashboard

```bash
streamlit run app.py
```

---

# 🤖 Machine Learning Workflow

## 🔹 Data Preprocessing

- Dataset Loading
- Missing Value Handling
- Duplicate Removal
- Data Cleaning
- Feature Selection

---

## 🔹 Exploratory Data Analysis

- Brand Distribution
- Sentiment Distribution
- Price Analysis
- Rating Analysis
- Correlation Analysis

---

## 🔹 Feature Engineering

- Feature Selection
- Feature Scaling
- Numerical Feature Preparation

---

## 🔹 Product Segmentation

- Elbow Method
- K-Means Clustering
- Cluster Assignment
- Cluster Analysis

---

## 🔹 Recommendation System

- User selects Brand
- User selects Price Range
- User selects Minimum Rating
- Best matching mobile is identified
- K-Nearest Neighbors (KNN) finds similar mobiles
- Top 5 recommended mobiles are displayed

---

# 📊 Cluster Insights

## Cluster 0 – Average Performance Mobiles

- Moderate customer ratings
- Balanced specifications
- Suitable for everyday users

---

## Cluster 1 – High Performance Mobiles

- Highest customer ratings
- Excellent battery performance
- Excellent camera quality
- Premium display quality
- High overall customer satisfaction

---

## Cluster 2 – Low Performance Mobiles

- Lowest customer ratings
- Lower feature scores
- Lower customer satisfaction

---

# 📊 Dashboard Features

The Streamlit Dashboard includes:

✔ Dataset Preview

✔ EDA Visualizations

✔ Cluster Comparison

✔ Cluster Explorer

✔ Cluster Distribution Analysis

✔ Price vs Rating Analysis

✔ Feature Comparison Across Clusters

✔ Mobile Recommendation System

✔ Interactive Navigation

---

# 🔍 Recommendation Workflow

1. User selects a preferred mobile brand.
2. User selects the desired price range.
3. User selects the minimum acceptable rating.
4. The system identifies the best matching mobile.
5. K-Nearest Neighbors (KNN) finds the five most similar mobiles.
6. Recommended mobiles are displayed with:

- Brand
- Model
- Rating
- Price
- Battery Rating
- Camera Rating
- Display Rating
- Performance Rating
- Sentiment

---

# 📈 Key Insights

📱 Premium smartphones generally receive higher customer ratings.

📊 Product pricing alone does not determine customer satisfaction.

📈 K-Means clustering successfully segments smartphones into meaningful customer groups.

⭐ The KNN recommendation system suggests similar smartphones using multiple product features.

📉 Customer sentiment plays an important role in overall product ratings.

---

# 🎯 Project Outcome

✔ Cleaned and processed the mobile reviews dataset.

✔ Performed exploratory data analysis.

✔ Applied feature engineering techniques.

✔ Built a K-Means clustering model for product segmentation.

✔ Developed a K-Nearest Neighbors (KNN) recommendation system.

✔ Created an interactive Streamlit dashboard.

✔ Generated meaningful business insights from customer reviews.

---

# 📌 Future Enhancements

- Hybrid Recommendation System

- Deep Learning Recommendation Engine

- SQL Database Integration

- Advanced NLP Sentiment Analysis

- Real-time Recommendation API

- Cloud Deployment using Streamlit Community Cloud

---

# 👨‍💻 Presented By

**Thaheer**

---

# 🌟 Conclusion

This project demonstrates a complete end-to-end Machine Learning workflow including data preprocessing, exploratory data analysis, feature engineering, K-Means clustering, a K-Nearest Neighbors (KNN) recommendation system, business insights generation, and an interactive Streamlit dashboard for mobile product segmentation and recommendation.

The project provides valuable insights into customer preferences and helps recommend similar mobile products based on user requirements using machine learning techniques.