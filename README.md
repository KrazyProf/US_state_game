# US_state_game
## 🗺️ U.S. State Guessing Game
An interactive geography quiz game built with Python and Turtle graphics. The objective is to correctly name as many U.S. states as possible within a time limit that you choose.
![us](https://github.com/user-attachments/assets/b3bee6f6-a86c-469b-94a6-ac53ce77448f)

## 🎯 Features
- **⏱ Customizable game duration (10–120 seconds).**
- **🖼 Interactive U.S. map with live state labeling.**
- **🧠 Educational and fun for all ages.**
- **📊 High score tracking saved across game sessions.**
- **📄 Generates a list of missed states to learn from.**

## 📁 Files Required
- main.py – Main game script.
- 50_states.csv – Contains the names and coordinates of U.S. states.
- blank_states_img.gif – The map image used in the game.
- high_score.txt – File for saving the highest score.
- missed_states.csv – Auto-generated file listing unguessed states.

## 🚀 How to Run
Make sure Python 3 is installed.
Install required Python packages (if not already installed):
  ``` bash
pip install pandas
```
Place the following files in the same directory:
- main.py
- 50_states.csv
- blank_states_img.gif
- high_score.txt (can be a blank file with 0 in it initially)

Run the game:
```bash
python main.py
```

## 🕹 How to Play
- Choose your preferred time limit (between 10 and 120 seconds).
- A map of the U.S. will appear.
- Type the names of U.S. states one by one.
- Correct guesses are labeled on the map.
- Type Exit to end the game early.
- At the end, your score and the high score will be shown.
- States you missed will be saved to missed_states.csv.
