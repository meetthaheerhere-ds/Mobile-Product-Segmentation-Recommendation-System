import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics.pairwise import cosine_similarity

# Page Title
st.title("📱 Mobile Product Segmentation & Recommendation System")

# Load Dataset
df = pd.read_csv("final_mobile_reviews.csv")

# Sidebar
st.sidebar.header("Project Navigation")

section = st.sidebar.radio(
    "Go to",
    [
        "Dataset Preview",
        "EDA Visualizations",
        "Cluster Insights",
        "Recommendation System"
    ]
)

# Dataset Preview
if section == "Dataset Preview":

    st.header("Dataset Preview")

    st.dataframe(df.head())

    st.write("Dataset Shape:", df.shape)

# EDA Visualizations
elif section == "EDA Visualizations":

    st.header("Exploratory Data Analysis")

    # Brand Distribution
    fig, ax = plt.subplots(figsize=(10,5))

    sns.countplot(x='brand', data=df, ax=ax)

    plt.xticks(rotation=45)

    st.pyplot(fig)

    # Sentiment Distribution
    fig2, ax2 = plt.subplots(figsize=(6,4))

    sns.countplot(x='sentiment', data=df, ax=ax2)

    st.pyplot(fig2)

# Cluster Insights
elif section == "Cluster Insights":

    st.header("Cluster Insights")

    st.markdown("""
    ### Cluster 0 - Mid-Range Mobiles
    Balanced smartphones with moderate pricing and average feature ratings.

    ### Cluster 1 - Premium High-Performance Mobiles
    Highly rated smartphones with excellent performance, camera, battery, and display quality.

    ### Cluster 2 - Low Satisfaction Segment
    Products with lower customer satisfaction and weak feature ratings.

    ### Cluster 3 - Ultra Premium Segment
    Expensive smartphones with above-average performance and premium positioning.
    """)

    # Cluster Distribution
    st.subheader("Cluster Distribution")

    fig1, ax1 = plt.subplots(figsize=(7,5))

    sns.countplot(x='Cluster', data=df, ax=ax1)

    st.pyplot(fig1)

    # Average Rating by Cluster
    st.subheader("Average Rating by Cluster")

    cluster_rating = df.groupby('Cluster')['rating'].mean()

    fig2, ax2 = plt.subplots(figsize=(7,5))

    cluster_rating.plot(kind='bar', ax=ax2)

    plt.ylabel("Average Rating")

    st.pyplot(fig2)

    # Price vs Rating Scatter Plot
    st.subheader("Price vs Rating by Cluster")

    fig3, ax3 = plt.subplots(figsize=(8,6))

    sns.scatterplot(
        x='price_usd',
        y='rating',
        hue='Cluster',
        palette='Set1',
        data=df,
        ax=ax3
    )

    st.pyplot(fig3)

# Recommendation System
elif section == "Recommendation System":

    st.header("Mobile Recommendation System")

    recommend_features = [
        'price_usd',
        'rating',
        'battery_life_rating',
        'camera_rating',
        'performance_rating',
        'design_rating',
        'display_rating'
    ]

    # Use sample dataset to reduce memory usage
    sample_df = df.sample(2000, random_state=42).reset_index(drop=True)

    similarity = cosine_similarity(sample_df[recommend_features])

    mobile_list = sample_df['model'].unique()

    selected_mobile = st.selectbox(
        "Select a Mobile",
        mobile_list
    )

    def recommend_mobile(model_name):

        index = sample_df[sample_df['model'] == model_name].index[0]

        distances = list(enumerate(similarity[index]))

        similar_products = sorted(
            distances,
            key=lambda x: x[1],
            reverse=True
        )

        recommended = similar_products[1:6]

        return recommended

    if st.button("Recommend"):

        recommendations = recommend_mobile(selected_mobile)

        st.subheader("Recommended Mobiles")

        for i in recommendations:

            st.write(
                sample_df.iloc[i[0]]['brand'],
                "-",
                sample_df.iloc[i[0]]['model']
            )