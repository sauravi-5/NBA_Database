import streamlit as st

# Set up the page
st.set_page_config(page_title="Custom Dashboard", layout="wide")

# Header
st.title("Dashboard Header")

# Overview Section (Static Stats + Scrollable List)
st.markdown("## Overview")
with st.container():
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
    scrollable_list = st.container()
    with scrollable_list:
        st.write("Item 1")
        st.write("Item 2")
        st.write("Item 3")
        # Add more items as needed

# Filter Section
st.markdown("## Filters")
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        table_filter = st.selectbox("Select Table", ["Table 1", "Table 2", "Table 3"])
    with col2:
        date_filter = st.date_input("Select Date")
    with col3:
        other_filter_1 = st.selectbox("Other Filter 1", ["Option 1", "Option 2", "Option 3"])
    with col4:
        other_filter_2 = st.selectbox("Other Filter 2", ["Option A", "Option B", "Option C"])

# Custom Output Area
st.markdown("## Output Area")
output_area = st.container()
with output_area:
    st.write("This is where your output will be displayed.")

