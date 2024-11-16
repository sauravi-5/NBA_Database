import streamlit as st

# Set up the page
st.set_page_config(page_title="Custom Dashboard", layout="wide")

# CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #20232a;
        color: #ffffff;
    }
    .box {
        border: 1px solid #444;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 20px;
        background-color: #282c34;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
    }
    .scrollable-list {
        max-height: 200px;
        overflow-y: auto;
        padding: 10px;
        border: 1px solid #444;
        border-radius: 8px;
        background-color: #3c4047;
        margin-top: 10px;
    }
    .metric-box {
        text-align: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.title("📊 Custom Dashboard")

# Overview Section (Static Stats + Scrollable List)
st.markdown('<div class="box">', unsafe_allow_html=True)

# Static Stats (First Row)
st.markdown("## Overview")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="💡 Stat 1", value="123")
with col2:
    st.metric(label="💡 Stat 2", value="456")
with col3:
    st.metric(label="💡 Stat 3", value="789")
with col4:
    st.metric(label="💡 Stat 4", value="1011")

# Scrollable List (Second Row)
st.markdown("### Scrollable List")
scrollable_row = st.columns(3)
for col, start in zip(scrollable_row, [1, 11, 21]):
    with col:
        st.markdown('<div class="scrollable-list">', unsafe_allow_html=True)
        for i in range(start, start + 10):  # Add items dynamically
            st.write(f"📌 Item {i}")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Filter Section
st.markdown('<div class="box">', unsafe_allow_html=True)
st.markdown("## Filters")
col1, col2, col3, col4 = st.columns(4)
with col1:
    table_filter = st.selectbox("Select Table", ["Table 1", "Table 2", "Table 3"])
with col2:
    date_filter = st.date_input("Select Date")
with col3:
    other_filter_1 = st.selectbox("Other Filter 1", ["Option 1", "Option 2", "Option 3"])
with col4:
    other_filter_2 = st.selectbox("Other Filter 2", ["Option A", "Option B", "Option C"])
st.markdown('</div>', unsafe_allow_html=True)

# Custom Output Area
st.markdown('<div class="box">', unsafe_allow_html=True)
st.markdown("## Output Area")
st.write("🔍 This is where your output will be displayed.")
st.markdown('</div>', unsafe_allow_html=True)
