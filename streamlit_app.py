import streamlit as st

# Add a centered header
st.markdown(
    """
    <h1 style="text-align: center;">NBA Database</h1>
    """,
    unsafe_allow_html=True,
)

# Add styled text with a white boundary and row of four boxes for stats
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

        <!-- Scrollable Boxes -->
        <div style="margin-top: 40px; text-align: left;">
            <h3>List 1</h3>
            <div style="border: 1px solid black; width: 90%; max-height: 150px; overflow-y: scroll; padding: 10px; margin-bottom: 20px;">
                <p>Item 1</p>
                <p>Item 2</p>
                <p>Item 3</p>
                <p>Item 4</p>
                <p>Item 5</p>
                <p>Item 6</p>
                <p>Item 7</p>
                <p>Item 8</p>
                <p>Item 9</p>
            </div>
            <h3>List 2</h3>
            <div style="border: 1px solid black; width: 90%; max-height: 150px; overflow-y: scroll; padding: 10px; margin-bottom: 20px;">
                <p>Item A</p>
                <p>Item B</p>
                <p>Item C</p>
                <p>Item D</p>
                <p>Item E</p>
                <p>Item F</p>
                <p>Item G</p>
                <p>Item H</p>
            </div>
            <h3>List 3</h3>
            <div style="border: 1px solid black; width: 90%; max-height: 150px; overflow-y: scroll; padding: 10px;">
                <p>Record 1</p>
                <p>Record 2</p>
                <p>Record 3</p>
                <p>Record 4</p>
                <p>Record 5</p>
                <p>Record 6</p>
                <p>Record 7</p>
                <p>Record 8</p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
