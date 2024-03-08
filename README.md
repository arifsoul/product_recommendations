<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
    <h1>Product Recommendation System</h1>
    <p>This is a Streamlit web application that recommends products based on customer interactions.</p>
    <h2>Usage</h2>
    <ol>
        <li>Clone this repository.</li>
        <li>Install the required libraries by running <code>pip install -r requirements.txt</code>.</li>
        <li>Run the application by executing <code>streamlit run app.py</code>.</li>
        <li>Enter the Customer ID in the sidebar and click "Get Recommendations" to see the recommended products.</li>
    </ol>
    <h2>Dependencies</h2>
    <ul>
        <li>pandas</li>
        <li>streamlit</li>
        <li>scikit-learn</li>
    </ul>
    <h2>File Structure</h2>
    <pre>
    .
    ├── dataset
    │   ├── customer_interactions.csv
    │   ├── product_details.csv
    │   └── purchase_history_extend.csv
    ├── app.py
    └── requirements.txt
    </pre>
    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>

</html>
