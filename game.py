import turtle
import random
import time
import winsound


winsound.Beep(1000, 200)

delay = 0.1
score = 0
high_score = 0
bodies = []


s1 = turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("green")
s1.setup(width=600, height=600)
s1.tracer(0)


head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("blue")
food.penup()
food.goto(200, 200)


sb = turtle.Turtle()
sb.speed(0)
sb.color("black")
sb.penup()
sb.hideturtle()
sb.goto(-280, 260)
sb.write("Score: 0 | High Score: 0", font=("Arial", 12, "bold"))


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)


s1.listen()
s1.onkey(go_up, "Up")
s1.onkey(go_down, "Down")
s1.onkey(go_left, "Left")
s1.onkey(go_right, "Right")


while True:
    s1.update()


    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

  
    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("black")
        body.penup()
        bodies.append(body)

        score += 10
        if score > high_score:
            high_score = score

        sb.clear()
        sb.write(f"Score: {score} | High Score: {high_score}",
                 font=("Arial", 12, "bold"))


    for i in range(len(bodies) - 1, 0, -1):
        bodies[i].goto(bodies[i - 1].xcor(), bodies[i - 1].ycor())

    if bodies:
        bodies[0].goto(head.xcor(), head.ycor())

    move()


    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for b in bodies:
                b.hideturtle()
            bodies.clear()

            score = 0
            sb.clear()
            sb.write(f"Score: {score} | High Score: {high_score}",
                     font=("Arial", 12, "bold"))

    time.sleep(delay)

