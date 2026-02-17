import streamlit as st
from PIL import Image

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="ShopNext Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------
st.sidebar.title("📊 ShopNext Analytics")
st.sidebar.markdown("E-Commerce Performance & Delivery Analysis")

page = st.sidebar.radio(
    "Navigate",
    ["Overview", "Delivery Investigation", "Project Insights", "About Project", "GitHub"]
)

# ---------------------------------------------------
# OVERVIEW PAGE
# ---------------------------------------------------
if page == "Overview":
    st.title("🛒 E-Commerce Performance Overview")

    st.markdown("""
    This dashboard analyzes revenue growth, delivery reliability,
    and customer behavior for ShopNext e-commerce platform.
    """)

    # KPI Row
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.metric("Total Revenue", "15.84M")
    col2.metric("YoY Growth", "17.1%")
    col3.metric("Late Delivery Rate", "8.1%")
    col4.metric("Total Orders", "99K")
    col5.metric("Late Deliveries", "8K")
    col6.metric("Avg Delivery Time", "12.5 Days")

    st.info("""
    **Key Insight:** Revenue increased significantly while delivery time remained high,
    indicating scaling challenges in logistics operations.
    """)

    st.markdown("---")
    st.subheader("Power BI Executive Dashboard")

    try:
        overview = Image.open("images/overview.png")
        st.image(overview, use_column_width=True)
    except:
        st.warning("Add overview.png to project folder")

# ---------------------------------------------------
# DELIVERY INVESTIGATION PAGE
# ---------------------------------------------------
elif page == "Delivery Investigation":
    st.title("🚚 Delivery Delay Investigation")

    st.markdown("""
    This page analyzes operational causes of delayed deliveries,
    identifying problematic states and product categories.
    """)

    try:
        investigation = Image.open("images/investigation.png")
        st.image(investigation, use_column_width=True)
    except:
        st.warning("Add investigation.png to project folder")

    st.markdown("""
    ### Observations
    - Furniture categories have the longest delivery duration
    - São Paulo state contributes most delays
    - Delay distribution shows few extreme outliers
    """)

# ---------------------------------------------------
# PROJECT INSIGHTS PAGE
# ---------------------------------------------------
elif page == "Project Insights":
    st.title("📈 Business Insights")

    st.markdown("""
    ### Key Findings

    **Revenue Growth**
    - 17% YoY increase between 2016–2018
    - Demand expanding rapidly

    **Operational Performance**
    - Only 8% deliveries late (good SLA compliance)
    - Average delivery time still high → 12.5 days

    **Customer Satisfaction**
    - Lower ratings linked to bulky products
    - Delivery time affects reviews

    **Geographical Impact**
    - SP state highest revenue & delays
    """)

    st.success("""
    **Recommendation:**
    Implement regional warehouses & optimize logistics for heavy items.
    """)

# ---------------------------------------------------
# ABOUT PROJECT PAGE
# ---------------------------------------------------
elif page == "About Project":
    st.title("🧠 About This Project")

    st.markdown("""
    ### Objective
    Analyze ShopNext e-commerce data to evaluate sales growth and delivery performance.

    ### Tools Used
    - Power BI
    - DAX
    - Data Modeling
    - Streamlit (Portfolio App)

    ### Skills Demonstrated
    - Data Cleaning & Modeling
    - Time Intelligence (YoY Growth)
    - KPI Design
    - Root Cause Analysis
    - Interactive Dashboard Development
    """)

    try:
        with open("report.pdf", "rb") as file:
            st.download_button(
                label="📄 Download Project Report",
                data=file,
                file_name="ShopNext_Report.pdf",
                mime="application/pdf"
            )
    except:
        st.warning("Add report.pdf to enable download")

# ---------------------------------------------------
# GITHUB PAGE
# ---------------------------------------------------
elif page == "GitHub":
    st.title("🔗 Project Repository")

    st.markdown("""
    Access full source code, dataset and Power BI dashboard here:

    👉 **[Open GitHub Repository](https://github.com/YOUR_USERNAME/shopnext-ecommerce-analytics)**

    Upload in repo:
    - Power BI (.pbix)
    - Dataset
    - Screenshots
    - Report PDF
    - Streamlit app
    """)

    st.info("Replace the GitHub link inside the code before deployment.")
