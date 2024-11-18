import streamlit as st

# Add a centered header
st.markdown(
    """
    <h1 style="text-align: center;">NBA Database</h1>
    """,
    unsafe_allow_html=True,
)

# Add Player and Game Statistics with a white boundary and boxes
st.markdown(
    """
    <div style="border: 2px solid white; padding: 20px; text-align: center; font-size: 20px;">
        <h2>Player and Game Statistics</h2>
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

    <!-- Add filter above a single scrollable feature -->
    <div style="margin-top: 20px;">
        <h3 style="text-align: center; color: black;">Select Table</h3>
        <div style="text-align: center;">
            <select style="padding: 10px; width: 50%; font-size: 16px; margin: auto;">
                <option value="table1">Table 1</option>
                <option value="table2">Table 2</option>
                <option value="table3">Table 3</option>
             </select>
         </div>
     </div>
        
    <!-- Single scrollable feature -->
    <div style="border: 1px solid black; padding: 10px 20px; width: 90%; margin: 20px auto; background-color: #f9f9f9; text-align: center;">
         <h3 style="margin-bottom: 0; color: black; font-size: 16px; text-align: center;">Stat 5</h3>
         <hr style="border: 1px solid black; margin-top: 5px; margin-bottom: 10px;">
         <div style="max-height: 150px; overflow-y: auto; text-align: left;">
            <ul style="padding-left: 15px;">
                <li style="color: black;">Detail 1</li>
                <li style="color: black;">Detail 2</li>
                <li style="color: black;">Detail 3</li>
                <li style="color: black;">Detail 4</li>
                 <li style="color: black;">Detail 5</li>
                <li style="color: black;">Detail 6</li>
            </ul>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# Display the "Filter Data" heading
st.markdown(
    """
    <div style="margin-top: 40px;">
        <h3 style="text-align: center;">Filter Data</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# Add 4 dropdowns in a row
col1, col2, col3, col4 = st.columns(4)

# Dropdown 1: Select Team
with col1:
    team_options = ["Team A", "Team B", "Team C", "Team D"]
    team = st.selectbox("Select Team", ["Select One"] + team_options, index=0)

# Dropdown 2: Select Player
with col2:
    player_options = ["Player 1", "Player 2", "Player 3", "Player 4"]
    player = st.selectbox("Select Player", ["Select One"] + player_options, index=0)

# Dropdown 3: Select Season
with col3:
    season_options = ["2020-2021", "2021-2022", "2022-2023"]
    season = st.selectbox("Select Season", ["Select One"] + season_options, index=0)

# Dropdown 4: Select Match
with col4:
    match_options = ["Match 1", "Match 2", "Match 3", "Match 4"]
    match = st.selectbox("Select Match", ["Select One"] + match_options, index=0)

# Display the "Desired Output" heading
st.markdown(
    """
    <div style="margin-top: 40px;">
        <h3 style="text-align: center;">Desired Output</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# Add a large empty box for the desired output
st.markdown(
    """
    <div style="width: 100%; height: 300px; border: 2px solid grey; margin-top: 20px; text-align: center; display: flex; align-items: center; justify-content: center; background-color: white;">
        <p style="color: black; font-size: 18px;">Select the filters above to display the desired output here.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
