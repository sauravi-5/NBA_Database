import streamlit as st

# Set up the page
st.set_page_config(page_title="Custom Dashboard", layout="wide")

# Add custom CSS for styling
st.markdown(
    """
    <style>
    .box {
        border: 1px solid #d3d3d3; 
        padding: 20px; 
        border-radius: 10px; 
        background-color: #f9f9f9;
        margin-bottom: 20px;
    }
    .scrollable-list {
        height: 150px; 
        overflow-y: scroll; 
        padding: 10px; 
        border: 1px solid #d3d3d3; 
        border-radius: 5px; 
        background-color: #ffffff;
    }
    .output-area {
        border: 2px solid #0073e6;
        padding: 20px; 
        border-radius: 10px; 
        background-color: #eef7ff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.title("Custom Dashboard")
st.markdown("### An Interactive Dashboard with Stats, Filters, and Outputs")

# Overview Section (Static Stats + Scrollable List inside a box)
st.markdown("## Overview")
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)

    # Static Stats (First Row)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Stat 1", value="123")
    with col2:
        st.metric(label="Stat 2", value="456")
    with col3:
        st.metric(label="Stat 3", value="789")
    with col4:
        st.metric(label="Stat 4", value="1011")

    # Scrollable List (Second Row)
    st.markdown("### Scrollable List")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="scrollable-list">', unsafe_allow_html=True)
        for i in range(1, 11):  # Example list items
            st.write(f"Item {i}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="scrollable-list">', unsafe_allow_html=True)
        for i in range(11, 21):  # Example list items
            st.write(f"Item {i}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="scrollable-list">', unsafe_allow_html=True)
        for i in range(21, 31):  # Example list items
            st.write(f"Item {i}")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Filter Section
st.markdown("## Filters")
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)

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
st.markdown("## Output Area")
st.markdown('<div class="output-area">', unsafe_allow_ht
