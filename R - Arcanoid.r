# Load the tcltk package
library(tcltk)

# Create the main window
win <- tktoplevel()

# Set the window title
tcl("wm", "title", win, "Arkanoid")

# Set the window size
tcl("wm", "geometry", win, "+0+0")

# Create the canvas widget
canvas <- tkcanvas(win, width = 400, height = 400)
pack(canvas)

# Create the ball
ball <- tkcircles(canvas, 200, 200, 5, fill = "red", tags = "ball")

# Create the paddle
paddle <- tkrectangles(canvas, 150, 390, 250, 395, fill = "blue", tags = "paddle")

# Create the bricks
bricks <- tkrectangles(canvas, 1, 1, 50, 10, fill = "green", tags = "brick")

# Set the game variables
lives <- 3
score <- 0

# Set the ball movement
movement <- c(3, -3)

# Set the paddle movement
paddle_movement <- 0

# Function to move the ball
move_ball <- function() {
  coords <- tkcget(ball, "coords")
  if (coords[2] > 400 || coords[4] < 0) movement[2] <- -movement[2]
  if (coords[1] > 400 || coords[3] < 0) movement[1] <- -movement[1]
  
  # Check for collision with paddle
  paddle_coords <- tkcget(paddle, "coords")
  if (coords[4] > paddle_coords[2] && coords[3] < paddle_coords[3] && coords[1] > paddle_coords[1] && coords[2] < paddle_coords[4]) {
    movement[2] <- -movement[2]
  }
  
  # Check for collision with bricks
  bricks_coords <- tkcget(bricks, "coords")
  if (length(bricks_coords) > 0) {
    for (i in 1:nrow(bricks_coords)) {
      if (coords[4] > bricks_coords[i,2] && coords[3] < bricks_coords[i,4] && coords[1] > bricks_coords[i,1] && coords[2] < bricks_coords[i,3]) {
        tkdelete(bricks[i])
        bricks <- bricks[-i]
        movement[2] <- -movement[2]
        score <- score + 1
      }
    }
  }
  
  # Update the ball position
  tkmove(ball, movement[1], movement[2])
}

# Function to move the paddle
move_paddle <- function(direction) {
  coords <- tkcget(paddle, "coords")
  if ((direction == "left" && coords[1] > 0) || (direction == "right" && coords[3] < 400)) {
    tkmove(paddle, ifelse(direction == "left", -10, 10), 0)
  }
}

# Bind the keys to the paddle movement
tcl("bind", win, "<KeyPress-Left>", function() move_paddle("left"))
tcl("bind", win, "<KeyPress-Right>", function() move_paddle("right"))

# Main game loop
while (length(bricks) > 0 && lives > 0) {
  Sys.sleep(0.01)
  move_ball()
  tkupdate()
  
  # Check if the ball has fallen off the screen
  coords <- tkcget(ball, "coords")
  if (coords[4] > 400) {
    lives <- lives - 1
    tkdelete(ball)
    ball <- tkcircles(canvas, 200, 200, 5, fill = "red", tags = "ball")
  }
}

# Game over message
if (lives == 0) {
  tkmessagebox(title = "Game Over", message = "You lost all your lives.")
} else {
  tkmessagebox(title = "Congratulations", message = "You won the game with a score of " + score + ".")
}