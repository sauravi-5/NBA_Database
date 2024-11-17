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

        <!-- New Row with 3 Boxes -->
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

# Add filters outside the boundary for selecting options (all in one row)
st.markdown(
    """
    <div style="margin-top: 40px;">
        <h3 style="text-align: center;">Filter Data</h3>
        <div style="display: flex; justify-content: space-around;">

            <!-- Dropdown 1: Select Team -->
            <div style="width: 23%; padding: 10px; text-align: center;">
                <h4>Select Team</h4>
                <hr style="border: 1px solid black; margin-top: 5px;">
                """,
    unsafe_allow_html=True,
)

team_options = ["Team A", "Team B", "Team C", "Team D"]
team = st.selectbox("Select Team", team_options)

st.markdown(
    f"""
    <p style="font-size: 20px; color: black;">Selected: {team}</p>
    </div>

    <!-- Dropdown 2: Select Player -->
    <div style="width: 23%; padding: 10px; text-align: center;">
        <h4>Select Player</h4>
        <hr style="border: 1px solid black; margin-top: 5px;">
        """,
    unsafe_allow_html=True,
)

player_options = ["Player 1", "Player 2", "Player 3", "Player 4"]
player = st.selectbox("Select Player", player_options)

st.markdown(
    f"""
    <p style="font-size: 20px; color: black;">Selected: {player}</p>
    </div>

    <!-- Dropdown 3: Select Season -->
    <div style="width: 23%; padding: 10px; text-align: center;">
        <h4>Select Season</h4>
        <hr style="border: 1px solid black; margin-top: 5px;">
        """,
    unsafe_allow_html=True,
)

season_options = ["2020-2021", "2021-2022", "2022-2023"]
season = st.selectbox("Select Season", season_options)

st.markdown(
    f"""
    <p style="font-size: 20px; color: black;">Selected: {season}</p>
    </div>

    <!-- Dropdown 4: Select Match -->
    <div style="width: 23%; padding: 10px; text-align: center;">
        <h4>Select Match</h4>
        <hr style="border: 1px solid black; margin-top: 5px;">
        """,
    unsafe_allow_html=True,
)

match_options = ["Match 1", "Match 2", "Match 3", "Match 4"]
match = st.selectbox("Select Match", match_options)

st.markdown(
    f"""
    <p style="font-size: 20px; color: black;">Selected: {match}</p>
    </div>
    </div>
    </div>
    """,
    unsafe_allow_html=True,
)
