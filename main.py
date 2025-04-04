import pandas as pd
import turtle
import time

# Setting Up Screen
screen = turtle.Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
screen.title("U.S. State Game")
turtle.shape(image)
screen.tracer(0)

# Reading the data
data = pd.read_csv('50_states.csv')
state_names = data['state'].tolist()
guessed_states = []
missed_states = []

# Ask user for game duration
game_duration = int(screen.textinput("Game Setup", "How many seconds do you need? (10-120):"))
while game_duration < 10 or game_duration > 120:
    game_duration = int(screen.textinput("Invalid", "Please enter between 10-120 seconds:"))

start_time = time.time()
end_time = start_time + game_duration

# Game loop
while time.time() < end_time:
    # Getting User Input
    user_input = screen.textinput(title='US State Game', 
                                prompt='Guess the state').title()
    
    if user_input == 'Exit':
        break
        
    if user_input in state_names and user_input not in guessed_states:
        state = data[data.state == user_input]
        x_cor = state.x.item()
        y_cor = state.y.item()

        # Mark the state on map
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(x_cor, y_cor)
        tim.write(user_input)
        guessed_states.append(user_input)
        
    screen.update()

# getting score of the user
score = len(guessed_states)

# reading the highscore file
with open('high_score.txt') as data:
    high_score = int(data.read())

# updating the highscore 
if score > high_score:
    high_score = score
    with open('high_score.txt' , 'w') as data:
        data.write(str(high_score))

# High Score Display
display_high_score = turtle.Turtle()
display_high_score.hideturtle()
display_high_score.penup()
display_high_score.color('red')
display_high_score.goto(0,-100)
display_high_score.write(f'High Score: {high_score}' , align="center", font=("Arial", 20, "bold"))

# Game over display
result = turtle.Turtle()
result.hideturtle()
result.penup()
result.goto(0, 0)
result.color('blue')
result.write(f"Game Over! You guessed {score} / {len(state_names)} states", 
            align="center", font=("Arial", 20, "bold"))

# Getting all the missed states
missed_states = [name for name in state_names if name not in guessed_states]
new_df = pd.DataFrame(missed_states)
new_df.to_csv('missed_states.csv')

screen.exitonclick()