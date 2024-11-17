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
            <div style="border: 1px solid black; padding: 10px 20px; width: 20%; background-color: #f9f9f9; text-align: center;">
                <h3 style="margin-bottom: 0; color: black; font-size: 16px; text-align: center;">Stat 1</h3>
                <hr style="border: 1px solid black; margin-top: 5px; margin-bottom: 10px;">
                <p style="font-size: 30px; color: black; text-align: center;">100</p>
            </div>
            <div style="border: 1px solid black; padding: 10px 20px; width: 20%; background-color: #f9f9f9; text-align: center;">
                <h3 style="margin-bottom: 0; color: black; font-size: 16px; text-align: center;">Stat 2</h3>
                <hr style="border: 1px solid black; margin-top: 5px; margin-bottom: 10px;">
                <p style="font-size: 30px; color: black; text-align: center;">200</p>
            </div>
            <div style="border: 1px solid black; padding: 10px 20px; width: 20%; background-color: #f9f9f9; text-align: center;">
                <h3 style="margin-bottom: 0; color: black; font-size: 16px; text-align: center;">Stat 3</h3>
                <hr style="border: 1px solid black; margin-top: 5px; margin-bottom: 10px;">
                <p style="font-size: 30px; color: black; text-align: center;">300</p>
            </div>
            <div style="border: 1px solid black; padding: 10px 20px; width: 20%; background-color: #f9f9f9; text-align: center;">
                <h3 style="margin-bottom: 0; color: black; font-size: 16px; text-align: center;">Stat 4</h3>
                <hr style="border: 1px solid black; margin-top: 5px; margin-bottom: 10px;">
                <p style="font-size: 30px; color: black; text-align: center;">400</p>
            </div>
        </div>

        <div style="display: flex; justify-content: space-around; margin-top: 40px;">
            <div style="border: 2px solid black; padding: 20px; width: 25%; background-color: #e9e9e9; text-align: center; height: 150px;">
                <h3 style="margin-bottom: 10px; color: black; font-size: 16px;">Box 1</h3>
                <p style="font-size: 20px; color: black;">Content 1</p>
            </div>
            <div style="border: 2px solid black; padding: 20px; width: 25%; background-color: #e9e9e9; text-align: center; height: 150px;">
                <h3 style="margin-bottom: 10px; color: black; font-size: 16px;">Box 2</h3>
                <p style="font-size: 20px; color: black;">Content 2</p>
            </div>
            <div style="border: 2px solid black; padding: 20px; width: 25%; background-color: #e9e9e9; text-align: center; height: 150px;">
                <h3 style="margin-bottom: 10px; color: black; font-size: 16px;">Box 3</h3>
                <p style="font-size: 20px; color: black;">Content 3</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
