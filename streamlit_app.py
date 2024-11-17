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

        <!-- Add boxes with scrollable lists -->
        <div style="display: flex; justify-content: space-around; margin-top: 30px;">
            <div style="border: 1px solid black; padding: 10px 20px; width: 20%; height: 250px; background-color: #f9f9f9; text-align: center; overflow-y: scroll;">
                <h4 style="margin-bottom: 10px; color: black; font-size: 18px;">Box 1: List of Players</h4>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li>LeBron James</li>
                    <li>Stephen Curry</li>
                    <li>Kawhi Leonard</li>
                    <li>Kevin Durant</li>
                    <li>Giannis Antetokounmpo</li>
                    <li>James Harden</li>
                    <li>Joel Embiid</li>
                    <li>Anthony Davis</li>
                    <li>Luka Dončić</li>
                    <li>Jayson Tatum</li>
                    <li>Zion Williamson</li>
                </ul>
            </div>
            <div style="border: 1px solid black; padding: 10px 20px; width: 20%; height: 250px; background-color: #f9f9f9; text-align: center; overflow-y: scroll;">
                <h4 style="margin-bottom: 10px; color: black; font-size: 18px;">Box 2: Top Games</h4>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li>Game 1: Lakers vs Warriors</li>
                    <li>Game 2: Clippers vs Bucks</li>
                    <li>Game 3: Celtics vs Heat</li>
                    <li>Game 4: Suns vs Nuggets</li>
                    <li>Game 5: Raptors vs Sixers</li>
                    <li>Game 6: Mavs vs Jazz</li>
                    <li>Game 7: Hornets vs Pacers</li>
                </ul>
            </div>
            <div style="border: 1px solid black; padding: 10px 20px; width: 20%; height: 250px; background-color: #f9f9f9; text-align: center; overflow-y: scroll;">
                <h4 style="margin-bottom: 10px; color: black; font-size: 18px;">Box 3: Team Achievements</h4>
                <ul style="list-style-type: none; padding-left: 0;">
                    <li>2016: Cavaliers Championship</li>
                    <li>2015: Warriors Championship</li>
                    <li>2020: Lakers Championship</li>
                    <li>1996: Bulls Championship</li>
                    <li>2012: Heat Championship</li>
                    <li>2008: Celtics Championship</li>
                    <li>2019: Raptors Championship</li>
                </ul>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
