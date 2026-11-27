# 🛍️ Retail Sales Intelligence & Demand Forecasting Platform

## 📌 Project Overview

The **Retail Sales Intelligence & Demand Forecasting Platform** is a data-driven project designed to analyze retail sales data, discover meaningful business insights, and support better decision-making.

The project covers the complete data analysis workflow, starting with data exploration and preprocessing, followed by SQL-based data management, exploratory data analysis (EDA), and machine learning models for sales prediction. The results will be presented through an interactive dashboard built with Streamlit.

## 🎯 Project Objectives

- Analyze retail sales performance and identify important business trends.
- Discover top-performing and underperforming products and categories.
- Understand customer purchasing behavior and sales patterns.
- Evaluate the impact of discounts on sales performance.
- Compare sales across different regions and sales channels.
- Build machine learning models to predict sales.
- Present key insights through an interactive dashboard.

## ❓ Business Questions

This project aims to answer the following business questions:

1. How does total sales revenue change over time?
2. Which products and categories generate the highest and lowest revenue?
3. Which regions contribute the most to total sales?
4. Which customer segments generate the highest revenue?
5. How do sales performance and purchasing patterns differ across sales channels?
6. What is the relationship between discounts, quantities sold, and sales revenue?
7. Which payment methods are most frequently used?

## 📊 Dataset Description

The project uses a retail sales dataset containing transaction-level information, including customer details, product information, and sales records.

| Dataset Information | Details |
|---|---|
| Number of Columns | 17 |
| Data Type | Structured Tabular Data |
| Time Period | 2024–2025  |
| Number of Rows | 120,000 |
| Dataset Source | https://www.kaggle.com/datasets/noopurbhatt/retail-sales-dataset |

### Dataset Features

| Column | Description |
|---|---|
| `transaction_id` | Unique identifier for each transaction. |
| `transaction_date` | Date when the transaction occurred. |
| `customer_id` | Unique identifier for each customer. |
| `customer_gender` | Gender category of the customer. |
| `customer_age_group` | Age group of the customer. |
| `customer_segment` | Customer classification, such as New, Returning, Loyal, or VIP. |
| `product_id` | Unique identifier for each product. |
| `product_name` | Name of the purchased product. |
| `category` | Product category. |
| `brand` | Brand associated with the product. |
| `quantity` | Number of units purchased. |
| `unit_price` | Price per unit before discount. |
| `discount_pct` | Discount percentage applied to the transaction. |
| `sales_amount` | Final sales amount after discount. |
| `payment_method` | Payment method used by the customer. |
| `sales_channel` | Channel through which the purchase was made. |
| `region` | Geographical sales region. |

## 🛠️ Technologies & Tools

### Programming & Data Analysis
- **Python** – Main programming language.
- **Pandas** – Data manipulation and analysis.
- **NumPy** – Numerical operations.

### Data Visualization
- **Matplotlib** – Static data visualizations.
- **Seaborn** – Statistical data visualization.
- **Plotly** – Interactive charts and visualizations.

### Database
- **SQL** – Data storage, querying, filtering, and aggregation.
- **SQLite** – Database & SQL Queries.

### Machine Learning
- **Scikit-learn** – Machine learning models and evaluation.
- **Machine learning models & metrices** – Machine learning models and evaluation.

### Dashboard & Development
- **Streamlit** – Interactive dashboard development.
- **Jupyter Notebook / Google Colab** – Data analysis and experimentation.
- **Git & GitHub** – Version control and collaboration.

## 🗄️ Database Structure

The project uses a SQL database containing **one main table** that stores the retail sales dataset.

The table includes all 17 columns, covering transaction details, customer information, product information, and sales records.

SQL queries are used to retrieve, filter, group, and aggregate the data to support the analysis and answer the project's business questions.

## 🔍 Project Workflow

1. **Data Understanding & Exploration** – Inspect the dataset, understand its structure, and identify data quality issues.
2. **Data Preprocessing** – Handle missing values, duplicates, incorrect data types, and inconsistencies.
3. **Database Management** – Store and manage the dataset using SQL.
4. **Exploratory Data Analysis (EDA)** – Analyze sales trends, customer behavior, products, regions, and discounts.
5. **Data Visualization** – Create meaningful visualizations to communicate business insights.
6. **Machine Learning** – Build and evaluate models for sales prediction.
7. **Interactive Dashboard** – Integrate key metrics, visualizations, and insights into a Streamlit application.

## 🤖 Machine Learning

Several regression algorithms will be explored and compared to predict sales-related values.

The models may include:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- K-Nearest Neighbors Regressor
- Support Vector Machine Regressor

Model performance will be evaluated using appropriate regression metrics, such as:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## 📈 Dashboard

An interactive dashboard will be developed using **Streamlit** to present the project's main findings.

It will provide an overview of sales performance, interactive visualizations, and useful business insights to help users explore the data and understand retail trends.

## 👥 Team Members

- Mahmoud Abdelmegeed
- Menna Fawzy
- Hazem Harby
- Malak Mohamed
- Safie eldin

## 🚀 Future Improvements

- Improve sales forecasting performance through model tuning.
- Add more advanced customer and product analysis.
- Expand dashboard functionality and interactivity.
- Introduce additional business KPIs and analytical features.

---

**Retail Sales Intelligence & Demand Forecasting Platform**  
*Turning retail data into meaningful insights and smarter business decisions.*
