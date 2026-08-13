import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# Page Title
# ==========================================

st.title("📱 Mobile Product Segmentation & Recommendation System")

# ==========================================
# Load Dataset
# ==========================================

@st.cache_data
def load_data():
    return pd.read_csv("final_mobile_reviews.csv")

df = load_data()

# ==========================================
# Sidebar
# ==========================================

st.sidebar.header("Project Navigation")

section = st.sidebar.radio(
    "Go to",
    [
    "Dataset Preview",
    "EDA Visualizations",
    "Cluster Comparison",
    "Cluster Explorer",
    "Recommendation System"
]
)

# ==========================================
# Dataset Preview
# ==========================================

if section == "Dataset Preview":

    st.header("Dataset Preview")

    st.dataframe(df.head())

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

# ==========================================
# EDA Visualizations
# ==========================================

elif section == "EDA Visualizations":

    st.header("Exploratory Data Analysis")

    # Brand Distribution
    fig, ax = plt.subplots(figsize=(10,5))

    sns.countplot(
        x='brand',
        data=df,
        ax=ax
    )

    ax.tick_params(axis="x", rotation=45)

    st.pyplot(fig)
    plt.close(fig)

    # Sentiment Distribution
    fig2, ax2 = plt.subplots(figsize=(6,4))

    sns.countplot(
        x='sentiment',
        data=df,
        ax=ax2
    )

    st.pyplot(fig2)
    plt.close(fig2)

# ==========================================
# Cluster Insights
# ==========================================

elif section == "Cluster Comparison":

    st.header("Cluster Comparison")

    st.markdown("""
### Cluster 0 – Average Performance Mobiles

These smartphones have moderate customer ratings and balanced feature scores.
They offer average battery life, camera quality, display quality, and overall performance, making them suitable for everyday users.

### Cluster 1 – High Performance Mobiles

These smartphones achieved the highest customer ratings and feature scores across battery, camera, display, and performance.
They represent the best-performing products with higher customer satisfaction.

### Cluster 2 – Low Performance Mobiles

These smartphones have the lowest customer ratings and feature scores.
They indicate lower customer satisfaction and comparatively weaker overall performance.

**The Elbow Method was used to determine the optimal number of clusters, and K = 3 was selected based on the elbow point.**
""")

    # ==========================================
    # Cluster Summary Table
    # ==========================================

    st.subheader("Cluster Summary")

    cluster_summary = df.groupby("Cluster")[
        [
            "price_usd",
            "rating",
            "battery_life_rating",
            "camera_rating",
            "performance_rating",
            "design_rating",
            "display_rating",
            "helpful_votes"
        ]
    ].mean().round(2)

    st.dataframe(cluster_summary)

    # ==========================================
    # Cluster Distribution
    # ==========================================

    st.subheader("Cluster Distribution")

    fig1, ax1 = plt.subplots(figsize=(7,5))

    sns.countplot(
        x='Cluster',
        data=df,
        ax=ax1
    )

    ax1.set_title("Cluster Distribution")

    st.pyplot(fig1)
    plt.close(fig1)

    # ==========================================
    # Average Rating by Cluster
    # ==========================================

    st.subheader("Average Rating by Cluster")

    cluster_rating = df.groupby('Cluster')['rating'].mean()

    fig2, ax2 = plt.subplots(figsize=(7,5))

    cluster_rating.plot(
        kind='bar',
        ax=ax2
    )

    ax2.set_title("Average Rating by Cluster")

    plt.ylabel("Average Rating")

    st.pyplot(fig2)
    plt.close(fig2)

    # ==========================================
    # Average Feature Ratings
    # ==========================================

    st.subheader("Average Feature Ratings by Cluster")

    feature_summary = df.groupby('Cluster')[
        [
            'battery_life_rating',
            'camera_rating',
            'performance_rating',
            'design_rating',
            'display_rating'
        ]
    ].mean().round(2)

    fig3, ax3 = plt.subplots(figsize=(10,6))

    feature_summary.T.plot(
        kind='bar',
        ax=ax3
    )

    ax3.set_title("Average Feature Ratings by Cluster")

    plt.ylabel("Average Rating")

    plt.tight_layout()

    st.pyplot(fig3)
    plt.close(fig3)

    # ==========================================
    # Price vs Rating Scatter Plot
    # ==========================================

    st.subheader("Price vs Rating by Cluster")

    fig4, ax4 = plt.subplots(figsize=(8,6))

    sns.scatterplot(
        x='price_usd',
        y='rating',
        hue='Cluster',
        palette='Set1',
        data=df,
        ax=ax4
    )

    ax4.set_title("Price vs Rating by Cluster")

    st.pyplot(fig4)
    plt.close(fig4)

# ==========================================
# Cluster Explorer
# ==========================================

elif section == "Cluster Explorer":

    st.header("Cluster Explorer")

    cluster_option = st.selectbox(
        "Select Cluster",
        [0, 1, 2]
    )

    cluster_df = df[df["Cluster"] == cluster_option]

    st.subheader(f"Cluster {cluster_option}")

    st.metric(
        "Number of Records",
        cluster_df.shape[0]
    )

    st.dataframe(cluster_df.head())

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", cluster_df.shape[0])

    with col2:
        st.metric("Columns", cluster_df.shape[1])

    st.subheader("Top 5 Brands")

    top_brands = (
        cluster_df["brand"]
        .value_counts()
        .head()
        .rename_axis("Brand")
        .reset_index(name="Count")
    )

    st.dataframe(top_brands)

    st.subheader("Average Ratings")

    st.dataframe(
        cluster_df[
            [
                "rating",
                "battery_life_rating",
                "camera_rating",
                "performance_rating",
                "design_rating",
                "display_rating"
            ]
        ].mean().round(2)
    )

    st.subheader("Brand Distribution")

    fig1, ax1 = plt.subplots(figsize=(10,5))

    sns.countplot(
        x="brand",
        data=cluster_df,
        ax=ax1
    )

    ax1.tick_params(axis="x", rotation=45)

    ax1.set_title("Brand Distribution")

    st.pyplot(fig1)
    plt.close(fig1)

    st.subheader("Sentiment Distribution")

    fig2, ax2 = plt.subplots(figsize=(6,4))

    sns.countplot(
        x="sentiment",
        data=cluster_df,
        ax=ax2
    )

    ax2.set_title("Sentiment Distribution")

    st.pyplot(fig2)
    plt.close(fig2)

    st.subheader("Price Distribution")

    fig3, ax3 = plt.subplots(figsize=(8,5))

    sns.histplot(
        cluster_df["price_usd"],
        bins=25,
        kde=True,
        ax=ax3
    )

    ax3.set_title("Price Distribution")

    st.pyplot(fig3)
    plt.close(fig3)

    st.subheader("Rating Distribution")

    fig4, ax4 = plt.subplots(figsize=(8,5))

    sns.boxplot(
        x=cluster_df["rating"],
        ax=ax4
    )

    ax4.set_title("Rating Distribution")

    st.pyplot(fig4)
    plt.close(fig4)

    st.subheader("Correlation Heatmap")

    fig5, ax5 = plt.subplots(figsize=(10,6))

    sns.heatmap(
        cluster_df.select_dtypes(include="number").corr(),
        annot=True,
        cmap="coolwarm",
        ax=ax5
    )

    ax5.set_title("Correlation Heatmap")

    st.pyplot(fig5)
    plt.close(fig5)

    if cluster_option == 0:

        st.success("""
Average Performance Mobiles

• Moderate customer ratings

• Balanced specifications

• Suitable for everyday users
""")

    elif cluster_option == 1:

        st.success("""
High Performance Mobiles

• Highest customer ratings

• Excellent battery, camera and display

• Premium quality smartphones
""")

    else:

        st.success("""
Low Performance Mobiles

• Lowest ratings

• Lower feature scores

• Lower customer satisfaction
""")    

# ==========================================
# Recommendation System
# ==========================================

elif section == "Recommendation System":

    st.header("📱 Mobile Recommendation System")

    st.write("Select your preferences to get recommended mobiles.")

    # ------------------------------------------
    # Features used for Similarity
    # ------------------------------------------

    recommend_features = [
        "price_usd",
        "rating",
        "battery_life_rating",
        "camera_rating",
        "performance_rating",
        "design_rating",
        "display_rating"
    ]

    # NOTE: We do NOT precompute the full similarity matrix here.
    # With 50,000 rows, a full NxN matrix needs ~18.6 GB of RAM.
    # Instead, similarity is computed only against the selected
    # reference mobile (1 row vs all rows) inside the button block below.

    # ------------------------------------------
    # User Inputs
    # ------------------------------------------

    selected_brand = st.selectbox(
        "Select Brand",
        sorted(df["brand"].unique())
    )

    min_price = int(df["price_usd"].min())
    max_price = int(df["price_usd"].max())

    selected_price = st.slider(
        "Select Price Range ($)",
        min_price,
        max_price,
        (min_price, max_price)
    )

    selected_rating = st.slider(
        "Minimum Rating",
        float(df["rating"].min()),
        float(df["rating"].max()),
        4.0,
        step=0.1
    )

    # ------------------------------------------
    # Recommend Button
    # ------------------------------------------

    if st.button("Recommend"):

        # Find mobiles matching user preference
        filtered = df[
            (df["brand"] == selected_brand) &
            (df["price_usd"] >= selected_price[0]) &
            (df["price_usd"] <= selected_price[1]) &
            (df["rating"] >= selected_rating)
        ]

        if filtered.empty:

            st.warning("No mobile found for the selected preferences.")

        else:

            # Pick the highest rated matching mobile
            selected_mobile = filtered.sort_values(
                by="rating",
                ascending=False
            ).iloc[0]

            st.success(
                f"Selected Mobile : {selected_mobile['brand']} {selected_mobile['model']}"
            )

            selected_index = selected_mobile.name

            # Compute similarity for just this one mobile vs the whole
            # dataset (1 x N), instead of the full N x N matrix.
            reference_vector = df.loc[[selected_index], recommend_features]

            similarity_scores = cosine_similarity(
                reference_vector,
                df[recommend_features]
            )[0]

            # Get indices of the most similar mobiles (highest score first)
            top_indices = similarity_scores.argsort()[::-1]

            st.subheader("Recommended Similar Mobiles")

            shown = 0

            for index in top_indices:

                if index == selected_index:
                    continue

                mobile = df.iloc[index]

                st.markdown("---")

                st.markdown(
                    f"## 📱 {mobile['brand']} {mobile['model']}"
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"⭐ Rating : {mobile['rating']}")
                    st.write(f"💲 Price : ${mobile['price_usd']}")
                    st.write(f"😊 Sentiment : {mobile['sentiment']}")

                with col2:
                    st.write(f"🔋 Battery : {mobile['battery_life_rating']}")
                    st.write(f"📷 Camera : {mobile['camera_rating']}")
                    st.write(f"⚡ Performance : {mobile['performance_rating']}")
                    st.write(f"🖥️ Display : {mobile['display_rating']}")

                shown += 1

                if shown == 5:
                    break