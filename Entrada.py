import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(10)  # Set the drawing speed

# Function to draw a petal
def draw_petal():
    flower.color("yellow")
    flower.begin_fill()
    flower.circle(100, 60)  # Draw a partial circle for the petal
    flower.left(120)  # Turn left to draw the next petal
    flower.circle(100, 60)
    flower.end_fill()

# Draw the flower
for _ in range(6):  # Draw 6 petals to form a flower
    draw_petal()
    flower.left(60)  # Turn left to position the next petal

# Draw the flower's center
flower.color("yellow")
flower.penup()
flower.goto(0, -30)  # Move to the center position
flower.pendown()
flower.begin_fill()
flower.circle(30)  # Draw a small circle for the center
flower.end_fill()

# Close the turtle graphics window when clicked
screen.exitonclick()
