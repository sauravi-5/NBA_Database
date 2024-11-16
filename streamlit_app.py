import streamlit as st

# Add a centered header
st.markdown(
    """
    <h1 style="text-align: center;">NBA Database</h1>
    """,
    unsafe_allow_html=True,
)

# Add styled text with a white boundary and row of four boxes
st.markdown(
    """
    <div style="border: 2px solid white; padding: 20px; text-align: center; font-size: 20px;">
        Player and Game Statistics
        <div style="display: flex; justify-content: space-around; margin-top: 20px;">
            <div style="border: 1px solid black; padding: 10px; width: 20%; background-color: #f9f9f9;">
                <h3>Box 1</h3>
                <p>100</p>
            </div>
            <div style="border: 1px solid black; padding: 10px; width: 20%; background-color: #f9f9f9;">
                <h3>Box 2</h3>
                <p>200</p>
            </div>
            <div style="border: 1px solid black; padding: 10px; width: 20%; background-color: #f9f9f9;">
                <h3>Box 3</h3>
                <p>300</p>
            </div>
            <div style="border: 1px solid black; padding: 10px; width: 20%; background-color: #f9f9f9;">
                <h3>Box 4</h3>
                <p>400</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
