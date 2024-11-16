import streamlit as st

# Set up the page
st.set_page_config(page_title="Custom Dashboard", layout="wide")

# CSS for styling
st.markdown(
    """
    <style>
    .box {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 20px;
        background-color: #f9f9f9;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    .scrollable-list {
        max-height: 150px;
        overflow-y: auto;
        padding: 8px;
        border: 1px solid #ddd;
        border-radius: 8px;
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.title("📊 Custom Dashboard")

# Overview Section (Static Stats + Scrollable List)
st.markdown("## Overview")
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)
    
    # Static Stats (First Row)
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
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="scrollable-list">', unsafe_allow_html=True)
        for i in range(1, 11):  # Add list items
            st.write(f"📌 Item {i}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="scrollable-list">', unsafe_allow_html=True)
        for i in range(11, 21):  # Add list items
            st.write(f"📌 Item {i}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="scrollable-list">', unsafe_allow_html=True)
        for i in range(21, 31):  # Add list items
            st.write(f"📌 Item {i}")
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
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.write("🔍 This is where your output will be displayed.")
    st.markdown('</div>', unsafe_allow_html=True)
