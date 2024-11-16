import streamlit as st

# Add a centered header
st.markdown(
    """
    <h1 style="text-align: center;">NBA Database</h1>
    """,
    unsafe_allow_html=True,
)

# Add styled text with a boundary
st.markdown(
    """
    <div style="border: 2px solid white; padding: 10px; text-align: center; font-size: 20px;">
        Player & Game Statistics
    </div>
    """,
    unsafe_allow_html=True,
)
