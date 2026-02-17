# 🛒 ShopNext E-Commerce Analytics Dashboard

An end-to-end Business Intelligence project analyzing sales growth, delivery performance, and customer behavior using Power BI and Streamlit.

This project transforms raw transactional data into actionable business insights and presents them through an interactive dashboard and web app.

---

## 🌐 Live Demo
👉 https://yourname-shopnext.streamlit.app

---

## 📊 Project Overview
ShopNext is an e-commerce platform experiencing rapid growth.  
The objective of this project is to evaluate:

- Revenue growth trends
- Delivery reliability
- Customer satisfaction
- Operational bottlenecks

The project provides both **executive monitoring** and **root cause investigation** capabilities.

---

## 🧠 Business Questions Answered

1. Is the business growing?
2. Are deliveries reliable?
3. Which categories take longest to deliver?
4. Which regions cause operational pressure?
5. How does delivery impact customer satisfaction?

---

## 📈 Key Insights

- Revenue increased **17% YoY**
- Only **8.1% orders delivered late**
- Average delivery time remains **12.5 days**
- Furniture & bulky items cause longest delivery times
- São Paulo drives highest revenue and most delays
- Delivery speed strongly influences product ratings

---

## 🧩 Dashboard Features

### Executive Dashboard
- Revenue & Growth KPIs
- On-time vs Late deliveries trend
- Top revenue categories
- Customer payment behavior
- Geographic performance

### Investigation Dashboard
- Late orders by category & state
- Delivery time distribution
- Order level analysis table
- Root cause identification

### Interactive Tooltip
- Quick KPI snapshot on hover

---

## 🛠 Tools & Technologies

| Tool | Purpose |
|-----|------|
Power BI | Data modeling & dashboard |
DAX | KPI calculations |
Streamlit | Interactive portfolio app |
Python | Web deployment |
GitHub | Version control |

---

## 📂 Project Structure

shopnext-ecommerce-analytics/
│── app.py
│── overview.png
│── investigation.png
│── report.pdf
│── README.md
│── data/
│── powerbi/


---

## ⚙️ Technical Implementation

- Star schema data model
- Calendar table for time intelligence
- YoY revenue calculation
- Delivery duration computation
- Drillthrough analysis page
- Conditional formatting KPIs
- Streamlit web app integration

---

## ▶️ Run Locally

```bash
pip install streamlit pillow
streamlit run app.py
