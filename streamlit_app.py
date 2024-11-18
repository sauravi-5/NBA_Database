import streamlit as st

# Add a centered header
st.markdown(
    """
    <h1 style="text-align: center;">NBA Database</h1>
    """,
    unsafe_allow_html=True,
)

# Simulated data for player and game statistics
statistics = {
    "Stat 1": 100,
    "Stat 2": 200,
    "Stat 3": 300,
    "Stat 4": 400
}

# Simulated data for dropdown options and scrollable details
table_options = ["Table 1", "Table 2", "Table 3"]
scrollable_details = {
    "Table 1": ["Detail 1", "Detail 2", "Detail 3"],
    "Table 2": ["Detail A", "Detail B", "Detail C"],
    "Table 3": ["Detail X", "Detail Y", "Detail Z"]
}

# Display section header
st.markdown(
    """
    <div style="border: 2px solid white; padding: 20px; text-align: center; font-size: 20px;">
        <h2>Player and Game Statistics</h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# Display statistics dynamically in a horizontal layout
st.markdown(
    """
    <div style="display: flex; justify-content: space-around; margin-top: 20px;">
    """,
    unsafe_allow_html=True,
)

stat_boxes = ""
for stat_name, stat_value in statistics.items():
    stat_boxes += f"""
    <div style="border: 1px solid black; padding: 10px 20px; width: 20%; background-color: #f9f9f9; text-align: center;">
        <h3 style="margin-bottom: 0; color: black; font-size: 16px; text-align: center;">{stat_name}</h3>
        <hr style="border: 1px solid black; margin-top: 5px; margin-bottom: 10px;">
        <p style="font-size: 30px; color: black; text-align: center;">{stat_value}</p>
    </div>
    """

st.markdown(f"<div style='display: flex; justify-content: space-evenly;'>{stat_boxes}</div>", unsafe_allow_html=True)

# Dropdown filter for selecting a table
selected_table = st.selectbox("Select Table", options=table_options)

# Display scrollable feature dynamically based on selected table
st.markdown(
    f"""
<div style="border: 1px solid black; padding: 10px 20px; width: 90%; margin: 20px auto; background-color: #f9f9f9; text-align: center;">
    <div style="max-height: 150px; overflow-y: auto; text-align: left;">
        {"".join([f"<p style='color: black;'>{detail}</p>" for detail in scrollable_details[selected_table]])}
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
