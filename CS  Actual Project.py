import turtle
import math
import random
import time

# Set up the screen       
window = turtle.Screen()
window.bgcolor("black")
window.title("A Dungeon Maze Game")
window.setup(700,700)
window.tracer(0)


# Create Pen 
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.score = 0
        self.hideturtle()
        self.update_score()
        
  # [ I implemented this part of the code ]
    def update_score(self):
        self.goto(0,300)
        self.clear()
        self.write("Gold: {}   Score:  Level: ".format(self.score),
                   align="center", font=("Courier", 26, "normal"))


# Create Player class
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold=0
        
        
    def go_up(self):
        # Calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # Calculate the spot to move to
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # Calculate the spot to move to
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        
        
        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y) 
    
    
    
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        
        
        if distance < 5:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
        
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()



class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x,y)
        self.direction = random.choice(["up", "down", "left", "right"])
    
    
    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("square")
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("square")
        else:
            dx = 0
            dy = 0  
            
        
        
    # [ I implemented this part of the code ]
        # Check if player is close
        # If so, go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
        elif player.xcor() > self.xcor():
                self.direction = "right"
        elif player.ycor() < self.ycor():
                self.direction = "down"
        elif player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            # Choose a different direction
            self.direction = random.choice(["up", "down", "left", "right"])

        

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000,20000)
        self.hideturtle()


#Create levels list
levels = [""]

#Define first level                  [ I implemented this part of the code ]
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXX",
"XXXX             PXXXXXX",
"XXXX     XX      XXXXXXX",
"XXXX      XX     XXXXXXX",      
"XXXX            XXXXXXXX",
"XXXX               XXXXX",
"XXXXXX              XXXX",
"XXXXXX    E        XXXXX",
"XXXXXXX            XXXXX",
"XX     XXXX      X XXXXX",
"XXE    XXXX        XXXXX",
"XX                XXXXXX",
"XX                  XXXX",
"XX                 XXXXX",     
"XXXXX           XXXXXXXX",
"XXXXXXXXX         XXXXXX",      
"XXXX            XXXXXXXX",
"XXXX          XX  XXXXXX",
"XXXXXE        XXXXXXXXXX",               
"XXXX                 XXX",
"XXXX        XXXXXXXXXXXX",
"XXXX        XXXXXXXXXXXX",
"XXXXXX                XX",      
"XXXXT                 XX",
"XXXXXXXXXXXXXXXXXXXXXXXX",      
 ]

# Define second level           [ I implemented this part of the code ]
level_2 = [
"XXXXXXXXXXXXXXXXXXXXXXX",
"XXP                XXXX",
"XX                    X",
"XXXXXXXXXX         XXXX",
"X       XX           XX",
"X       XX            X",
"XXXXXX  XX            X",
"XXXXXX  XX            X",
"XXXXXX  XX      XXXX  X",
"X  XXXE         XXXX  X",
"X  XXX         XXXXXXXX",
"X          XXXXXXXXXXXX",
"X E                XXXX",
"XXXXXXXXXXXX        XXX",
"XXXXXXXXXXXXXXX    XXXX",
"XXX  XXXXXXXXXX       X",
"XXX                   X",
"XXX                   X",
"XXXXXXXXXX         XXXX",
"XXXXXXXXXX         XXXX",
"XX    XXXX      XXXXXXX",
"XXE    XXXX      XXXXXX",
"XX     XXXX           X",
"XX                  TXX",
"XXXXXXXXXXXXXXXXXXXXXXX",
]


# Add second level to levels list          [ I implemented this part of the code ]
levels.append(level_2) 


#Add maze to mazes list                   [ I implemented this part of the code ]
levels.append(level_1)

# Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the character at each x, y coordinate
            # NOTE the order of y and x in the next line
            character = level[y][x]

            # Calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

                # Add coordinates to wall list
                walls.append((screen_x, screen_y))

            # Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)
            
            #Check if it is a T (representing Treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            #Check if it is an E (representing Enemy)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

# create instances of Pen and Player
pen = Pen()
player = Player()

# Create wall coordinate list
walls = []

# Add a treasures list
treasures = []

#Create enemy list
enemies = []

#set up the level
setup_maze(levels[1])        
        




# Keyboard Binding                      
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")
        
# Turn off screen updates
#wn.tracer(0)





#Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

# Main Game Loop         [ I implemented this part of the code ]
counter=0
current_level = 1
game_over = False  # Add a flag to track game over

while not game_over:
    # Check for player collision with treasure
    # Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            # Add the treasure gold to the player gold
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            
            # Destroy the treasure
            treasure.destroy()
            
            # Remove the treasure from the treasures list
            treasures.remove(treasure)
    
            
            # Update the score on the screen              [I implemented this part of the code]
            pen.update_score()
            
            
            # Move to the next level if the player has enough gold      [I impemented this part of the code]
            if player.gold >= 100:
                current_level += 1
                if current_level < len(levels):
                    print("Congratulations! Moving to Level {}".format(current_level))
                    setup_maze(levels[current_level])
                else:
                    print("You've completed all levels!")
                    turtle.bye()  # Close the game window
    
    # Check for player collision with enemies               [ I implemented this part of the code]
    for enemy in enemies:
        if player.is_collision(enemy):
            print("Game Over! Player collided with an enemy.")
            game_over = True  # Set the game over flag
            
    
    
    #Update screen
    window.update()
    
    # wait before next loop      [ I implemented this part of the code]
    time.sleep(0.01)
    counter += 1
    
    if counter % 100 == 0:
       print("here")
       for enemy in enemies:
           turtle.ontimer(enemy.move, t=random.randint(100,300)) 
           if player.is_collision(enemy):
               print("Enemy dies!")

      


# Start the game loop
turtle.mainloop()




        