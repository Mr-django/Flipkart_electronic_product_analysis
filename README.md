# Flipkart Electronics Product Analysis

## Project Overview

This project demonstrates an end-to-end data analytics workflow by collecting real-world product data from Flipkart through web scraping, performing data cleaning and Exploratory Data Analysis (EDA) using Python, and building an interactive Power BI dashboard for business insights. The analysis focuses on three major electronics categories—Headphones, Laptops, and Smartphones—to understand pricing trends, customer reviews, discounts, and product ratings. The scraping process was implemented using Selenium and BeautifulSoup, while the data was cleaned and analyzed using Pandas and visualization libraries before being presented in Power BI. :contentReference[oaicite:0]{index=0}

---

# Project Workflow

```
Web Scraping
        ↓
Raw Product Dataset
        ↓
Data Cleaning & Preprocessing
        ↓
Exploratory Data Analysis (EDA)
        ↓
Power BI Dashboard
        ↓
Business Insights
```

---

# Objective

The primary objectives of this project are:

- Collect real-time electronics product data from Flipkart.
- Clean and preprocess scraped data for analysis.
- Analyze pricing, discounts, ratings, and customer reviews.
- Compare different electronics categories.
- Build an interactive Power BI dashboard.
- Generate actionable business insights from product data.

---

# Tools and Technologies

### Web Scraping

- Selenium
- BeautifulSoup (BS4)
- Chrome WebDriver

### Data Processing

- Python
- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Business Intelligence

- Power BI

### Development Environment

- Jupyter Notebook
- VS Code

---

# Dataset Information

The dataset was created by scraping Flipkart's website using Selenium and BeautifulSoup.

The dataset contains information such as:

- Product Name
- Category
- Brand
- Selling Price
- Original Price
- Discount Percentage
- Customer Rating
- Number of Reviews
- Product Link

The analysis focuses on three major product categories:

- Headphones
- Laptops
- Smartphones

---

# Data Collection

Product data was collected directly from Flipkart using automated web scraping.

### Steps Performed

- Opened Flipkart using Selenium WebDriver.
- Searched for electronics products.
- Navigated across multiple product pages.
- Extracted product details including:
  - Product Name
  - Price
  - Rating
  - Product URL
- Stored the collected data in CSV format for further analysis. :contentReference[oaicite:1]{index=1}

---

# Data Preprocessing

After scraping, the dataset underwent several preprocessing steps:

- Removed duplicate records.
- Handled missing values.
- Converted prices into numeric format.
- Cleaned review counts.
- Standardized category names.
- Corrected data types.
- Prepared the dataset for analysis.

---

# Exploratory Data Analysis (EDA)

Several analyses were performed to understand customer preferences and pricing behavior.

---

## 1. Product Overview

Key metrics generated:

| KPI | Value |
|------|-------|
| Total Reviews | 10 Million |
| Total Products | 1,281 |
| Maximum Price | ₹370K |
| Minimum Price | ₹99 |
| Average Price | ₹30.11K |

---

## 2. Reviews by Category

Customer review counts were compared across product categories.

### Observation

- Headphones received the highest number of customer reviews.
- Smartphones ranked second.
- Laptops received comparatively fewer reviews.

This indicates significantly higher customer engagement in the headphones category.

---

## 3. Price Distribution by Category

A donut chart compares the total product value across categories.

### Observation

- Laptops contribute the largest share of total pricing.
- Smartphones account for the second-highest share.
- Headphones represent the smallest share.

This reflects the higher average selling price of laptops.

---

## 4. Top Rated Categories

The analysis compares the number of highly rated products.

### Observation

- Laptops contain the highest number of top-rated products.
- Headphones follow closely.
- Smartphones rank third.

---

## 5. Discount Analysis

The relationship between discounts and product pricing was analyzed.

### Observation

- Products with higher discounts generally exhibit varying price ranges.
- Discount strategies differ across product categories.

---

## 6. Discounts by Category

The proportion of discounted products across categories was examined.

### Observation

- Laptops account for approximately **37%** of discounted products.
- Headphones contribute around **34%**.
- Smartphones contribute nearly **29%**.

---

# Dashboard Features

The Power BI dashboard includes:

- Interactive Category Filters
- KPI Cards
- Bar Charts
- Donut Charts
- Trend Analysis
- Category Comparison
- Dynamic Product Insights

---

# Key Insights

- Over **10 million customer reviews** were analyzed.
- The dataset contains **1,281 electronics products**.
- Laptop products have the highest overall price contribution.
- Headphones receive the largest volume of customer reviews.
- Smartphones maintain competitive pricing with substantial customer engagement.
- Laptops account for the highest proportion of discounted products.
- Product prices range from **₹99** to **₹370,000**, with an average price of approximately **₹30.11K**.

---

# Business Recommendations

- Increase inventory for high-demand product categories such as Headphones.
- Offer targeted discount campaigns for Smartphones to improve competitiveness.
- Maintain premium pricing strategies for high-value Laptop products.
- Use customer review analysis to identify high-performing products.
- Optimize promotional campaigns based on product ratings and customer engagement.
- Continuously monitor pricing and discount trends to remain competitive.

---

# Conclusion

This project demonstrates a complete data analytics pipeline, beginning with real-time web scraping from Flipkart using Selenium and BeautifulSoup, followed by data cleaning, exploratory data analysis using Python, and visualization through an interactive Power BI dashboard. The analysis provides meaningful insights into product pricing, customer reviews, ratings, and discount strategies across multiple electronics categories. It showcases practical applications of web scraping, data preprocessing, business intelligence, and data visualization to support data-driven decision-making in the e-commerce domain.

---

# Repository Structure

```
Flipkart-Electronics-Analysis/
│
├── Data/
│   └── flipkart_products.csv
│
├── Scraping/
│   └── flipkart_scraping_project.py
│
├── Notebook/
│   └── Flipkart_Project.ipynb
│
├── Dashboard/
│   └── Flipkart_Electronics_Dashboard.pbix
│
├── Images/
│   └── Dashboard.png
│
└── README.md
```

---

# Skills Demonstrated

- Web Scraping
- Selenium Automation
- BeautifulSoup
- Python Programming
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Power BI Dashboard Development
- Business Analytics
- Dashboard Design

---

# Author

**Shubham Singh**

**Aspiring Data Analyst**

### Technical Skills

- Python
- Selenium
- BeautifulSoup
- Pandas
- NumPy
- SQL
- Power BI
- Microsoft Excel
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
