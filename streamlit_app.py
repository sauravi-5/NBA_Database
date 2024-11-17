import streamlit as st

# Set page configuration
st.set_page_config(page_title="NBA Database", page_icon=":basketball:", layout="centered")

# Header Section
st.markdown("<h1 style='text-align: center; color: black;'>NBA Database</h1>", unsafe_allow_html=True)

# Player and Game Statistics Box
st.markdown("""
    <div style='border: 2px solid white; padding: 20px; margin-top: 30px;'>
        <h2 style='text-align: center; color: black;'>Player and Game Statistics</h2>
        <div style="display: flex; justify-content: space-around; margin-top: 30px;">
            
            <!-- Box 1 -->
            <div style="border: 1px solid black; padding: 10px 20px; width: 20%; height: 250px; background-color: #f9f9f9; text-align: center;">
                <h4 style="margin-bottom: 10px; color: black;">Stat 1</h4>
                <hr style="border-top: 1px solid black;">
                <p style="font-size: 30px; color: black;">30</p>
            </div>
            
            <!-- Box 2 -->
            <div style="border: 1px solid black; padding: 10px 20px; width: 20%; height: 250px; background-color: #f9f9f9; text-align: center;">
                <h4 style="margin-bottom: 10px; color: black;">Stat 2</h4>
                <hr style="border-top: 1px solid black;">
                <p style="font-size: 30px; color: black;">45</p>
            </div>

            <!-- Box 3 -->
            <div style="border: 1px solid black; padding: 10px 20px; width: 20%; height: 250px; background-color: #f9f9f9; text-align: center;">
                <h4 style="margin-bottom: 10px; color: black;">Stat 3</h4>
                <hr style="border-top: 1px solid black;">
                <p style="font-size: 30px; color: black;">12</p>
            </div>

            <!-- Box 4 -->
            <div style="border: 1px solid black; padding: 10px 20px; width: 20%; height: 250px; background-color: #f9f9f9; text-align: center;">
                <h4 style="margin-bottom: 10px; color: black;">Stat 4</h4>
                <hr style="border-top: 1px solid black;">
                <p style="font-size: 30px; color: black;">20</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Scrollable List Boxes Section
st.markdown("""
    <div style="display: flex; justify-content: space-around; margin-top: 30px;">
        
        <!-- Box 1: List of Players -->
        <div style="border: 1px solid black; padding: 10px 20px; width: 30%; height: 250px; background-color: #f9f9f9; text-align: center; overflow-y: scroll;">
            <h4 style="margin-bottom: 10px; color: black; font-size: 18px;">Box 1: List of Players</h4>
            <ul style="list-style-type: none; padding-left: 0; margin: 0; overflow-y: scroll; max-height: 200px;">
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
                <li>Jimmy Butler</li>
                <li>Damian Lillard</li>
                <li>Chris Paul</li>
                <li>Trae Young</li>
            </ul>
        </div>
        
        <!-- Box 2: Top Games -->
        <div style="border: 1px solid black; padding: 10px 20px; width: 30%; height: 250px; background-color: #f9f9f9; text-align: center; overflow-y: scroll;">
            <h4 style="margin-bottom: 10px; color: black; font-size: 18px;">Box 2: Top Games</h4>
            <ul style="list-style-type: none; padding-left: 0; margin: 0; overflow-y: scroll; max-height: 200px;">
                <li>Game 1: Lakers vs Warriors</li>
                <li>Game 2: Clippers vs Bucks</li>
                <li>Game 3: Celtics vs Heat</li>
                <li>Game 4: Suns vs Nuggets</li>
                <li>Game 5: Raptors vs Sixers</li>
                <li>Game 6: Mavs vs Jazz</li>
                <li>Game 7: Hornets vs Pacers</li>
                <li>Game 8: Knicks vs Bulls</li>
                <li>Game 9: Hawks vs Magic</li>
                <li>Game 10: Pelicans vs Timberwolves</li>
            </ul>
        </div>

        <!-- Box 3: Team Achievements -->
        <div style="border: 1px solid black; padding: 10px 20px; width: 30%; height: 250px; background-color: #f9f9f9; text-align: center; overflow-y: scroll;">
            <h4 style="margin-bottom: 10px; color: black; font-size: 18px;">Box 3: Team Achievements</h4>
            <ul style="list-style-type: none; padding-left: 0; margin: 0; overflow-y: scroll; max-height: 200px;">
                <li>2016: Cavaliers Championship</li>
                <li>2015: Warriors Championship</li>
                <li>2020: Lakers Championship</li>
                <li>1996: Bulls Championship</li>
                <li>2012: Heat Championship</li>
                <li>2008: Celtics Championship</li>
                <li>2019: Raptors Championship</li>
                <li>2004: Pistons Championship</li>
                <li>1994: Rockets Championship</li>
                <li>1989: Pistons Championship</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)
