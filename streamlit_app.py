import streamlit as st
from math import floor
import pandas as pd

st.title("Oh Hell Scoreboard")

players      = st.text_input("List all player names seperated by commas:")
if players  == "": st.stop()
player_list  = players.split(",")
player_count = len(player_list)
player_list  = [name.lstrip() for name in player_list]
column_names = []
bets = []
wins = []
points = []

# st.write(f"You have input {player_count} players, the maximum cards in a single round will be {floor(52/player_count)}.")

for player in player_list:
    column_names.append(f"{player} Bet")
    bets.append(f"{player} Bet")
    column_names.append(f"{player} Win")
    wins.append(f"{player} Win")
    column_names.append(f"{player} Points")
    points.append(f"{player} Points")

df = pd.DataFrame(columns=column_names)
df.loc[df.shape[0]] = [None] * len(df.columns)

# st.dataframe(df[bets])
st.write("---")
st.header("Round 1")

col1, col2 = st.columns(2)
with col1:
    for player in player_list:
        temp = st.number_input(f"{player}'s Bet", step = 1)
with col2:
    card_count = st.number_input("Cards", step = 1, min_value=1, max_value=floor(52/player_count), placeholder = 1)
    st.subheader("Winners")
    for player in player_list:
        temp = st.checkbox(f"{player}")


col3, col4 = st.columns(2)
with col3:
    next_button = st.button("Next Round")
with col4:
    end_game = st.button("End Game")




# col1, col2 = st.columns(2)
# with col1:
#     max_cards = st.number_input("Maximum numbers of cards in a single round:", min_value = 0, max_value = floor(52/player_count), value = min(floor(52/player_count), 7))

# with col2: 
#     if(max_cards > 1):
#         st.write(f"You have selected to play {max_cards*2-1} rounds, the highest number of cards in one round will be {max_cards}")
        
# st.divider()
# player_list = ["Round"] + player_list

# df = pd.DataFrame(columns=player_list)

# for rounds in range(max_cards*2-1):
#     new_row = {"Round": rounds}
#     df = df.append(new_row, ignore_index=True)

# st.dataframe(df, hide_index = True)




# # st.write(player_list)

# # st.write(player_count)




# st.stop()











# ## Variables
# player_count = st.number_input("How many people are playing?", step = 1, min_value = 0, max_value = 26)

# if (player_count == 0): st.stop()

# max_cards = floor(52/player_count)
# round_num = 1
# # st.write("There are ", player_count, " people playing this game. The highest number of cards in a round will be ", max_cards)
# # st.divider()

# players = st.text_input("List all player names seperated by commas:")
# player_list = players.split(", ")
# # st.write(player_list)
# # st.write(len(player_list))

# if (len(player_list) != player_count): 
#     st.warning("Make sure that you have assigned each player a name")
#     st.stop()

# st.divider()
# st.header(f"Round {round_num}")



# # Create a dictionary from the lists
# data = {'Name': player_list}

# # Create a dataframe from the dictionary
# df = pd.DataFrame(data)
# st.data_editor(df, hide_index = True)
