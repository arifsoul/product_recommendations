import pandas as pd
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load data
customer_interactions = pd.read_csv("dataset/customer_interactions.csv")
product_details = pd.read_csv("dataset/product_details.csv", sep=";")
purchase_history = pd.read_csv("dataset/purchase_history_extend.csv", sep=";")

# Merge data
merged_data = pd.merge(customer_interactions, purchase_history, on="customer_id")
merged_data = pd.merge(merged_data, product_details, on="product_id")

# Normalize data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(merged_data[['page_views', 'time_spent']])

# Train KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_scaled, merged_data['category'])

# Create Streamlit UI
st.title("Product Recommendation")

st.sidebar.title("User Input")
customer_id = st.sidebar.number_input("Enter Customer ID", min_value=1, max_value=merged_data['customer_id'].max(), value=1)

if st.sidebar.button("Get Recommendations"):
    # Get recommendations
    customer_data = customer_interactions[customer_interactions['customer_id'] == customer_id]
    if not customer_data.empty:
        customer_data_scaled = scaler.transform(customer_data[['page_views', 'time_spent']])
        prediction = knn.predict(customer_data_scaled)
        recommended_products_id = merged_data[merged_data['category'] == prediction[0]]['product_id'].values
        recommended_products = merged_data[merged_data['category'] == prediction[0]]['category'].values
        recommended_price = merged_data[merged_data['category'] == prediction[0]]['price'].values
        recommended_ratings = merged_data[merged_data['category'] == prediction[0]]['ratings'].values
        name_products = merged_data[merged_data['category'] == prediction[0]]['name_products'].values

        # Display recommendations
        st.header(f"Recommended products for Customer ID {customer_id}:")
        for product_id,product,price,ratings,name in zip(recommended_products_id,recommended_products,recommended_price,recommended_ratings,name_products):
            st.write("- Product ID:", product_id, product, price, name)
    else:
        st.warning("Customer ID not found in the dataset.")
