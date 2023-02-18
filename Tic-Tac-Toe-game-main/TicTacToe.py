
import turtle
import time
print("This is the position of the numbers:"
      "\n|7|8|9|"
      "\n|4|5|6|"
      "\n|1|2|3|")

t = turtle.Turtle()
s = turtle.Screen()
move_list = []
move_2 = []

def circle():
    t.pensize(10)
    t.color("blue")
    t.pendown()
    r = 40
    t.circle(r)

def letterX(t,length):
    t.pensize(10)
    t.color("red")
    t.down()
    t.right(45)
    t.forward(length/2)
    t.right(180)
    t.forward(length)
    t.right(180)
    t.forward(length/2)
    t.left(90)
    t.forward(length/2)
    t.right(180)
    t.forward(length)
    t.right(180)
    t.forward(length/2)
    t.right(45)
    t.up()

ws = turtle.Screen()
t.color("Green")
t.width("10")
t.speed(5)
for i in range(4):
    t.forward(300)
    t.left(90)
t.penup()
t.goto(0, 100)
t.pendown()
t.forward(300)
t.penup()
t.goto(0, 200)
t.pendown()
t.forward(300)
t.penup()
t.goto(100, 0)
t.pendown()
t.left(90)
t.forward(300)
t.penup()
t.goto(200, 0)
t.pendown()
t.forward(300)

check_1 = [1, 2, 3]
check_2 = [1, 5, 9]
check_3 = [7, 5, 3]
check_4 = [4, 5, 6]
check_5 = [7, 8, 9]
check_6 = [7, 4, 1]
check_7 = [8, 5, 2]
check_8 = [9, 6, 3]


number = 1
move_1 = []
while number == 1:
    Move = int(input("Player 1, Where would you like to put your X (1 - 9)?: "))
    if Move in move_list:
        print("Sorry, square already taken")
        move_1.remove(Move)
        Move = int(input("Player 1, Where would you like to put your X (1 - 9)?: "))
    move_list.extend([Move])
    move_1.extend([Move])
    set1 = set(check_1)
    set2 = set(move_1)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break
    set1 = set(check_2)
    set2 = set(move_1)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break
    set1 = set(check_3)
    set2 = set(move_1)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break
    set1 = set(check_4)
    set2 = set(move_1)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break
    set1 = set(check_5)
    set2 = set(move_1)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break
    set1 = set(check_6)
    set2 = set(move_1)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break
    set1 = set(check_7)
    set2 = set(move_1)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break
    set1 = set(check_8)
    set2 = set(move_1)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break


    if Move == 1:
        t.penup()
        t.goto(50,50)
        letterX(t, 100)
    if Move == 2:
        t.penup()
        t.goto(150,50)
        letterX(t, 100)
    if Move == 3:
        t.penup()
        t.goto(250,50)
        letterX(t, 100)
    if Move == 4:
        t.penup()
        t.goto(50,150)
        letterX(t, 100)
    if Move == 5:
        t.penup()
        t.goto(150,150)
        letterX(t, 100)
    if Move == 6:
        t.penup()
        t.goto(250,150)
        letterX(t, 100)
    if Move == 7:
        t.penup()
        t.goto(50,250)
        letterX(t, 100)
    if Move == 8:
        t.penup()
        t.goto(150,250)
        letterX(t, 100)
    if Move == 9:
        t.penup()
        t.goto(250, 250)
        letterX(t, 100)


    time.sleep(0.6)

    Move2 = int(input("Player 2, Where would you like to put your O (1 - 9)?: "))
    if Move2 in move_list:
        print("Sorry, square already taken")
        Move2 = int(input("Player 2, Where would you like to put your O (1 - 9)?: "))
    move_list.append(Move2)
    move_2.extend([Move2])
    set1 = set(check_1)
    set2 = set(move_2)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 2 you won")
        break
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break
    set1 = set(check_3)
    set2 = set(move_2)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break

    set1 = set(check_4)
    set2 = set(move_2)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break
    set1 = set(check_5)
    set2 = set(move_2)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break
    set1 = set(check_6)
    set2 = set(move_2)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break
    set1 = set(check_7)
    set2 = set(move_2)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break
    set1 = set(check_8)
    set2 = set(move_2)
    is_subset = set1.issubset(set2)
    if is_subset == True:
        print("Congrats player 1 you won")
        break

    if Move2 == 1:
        t.penup()
        t.goto(90, 50)
        circle()
    if Move2 == 2:
        t.penup()
        t.goto(190, 50)
        circle()
    if Move2 == 3:
        t.penup()
        t.goto(290, 50)
        circle()
    if Move2 == 4:
        t.penup()
        t.goto(90, 150)
        circle()
    if Move2 == 5:
        t.penup()
        t.goto(190, 150)
        circle()
    if Move2 == 6:
        t.penup()
        t.goto(290, 150)
        circle()
    if Move2 == 7:
        t.penup()
        t.goto(90, 250)
        circle()
    if Move2 == 8:
        t.penup()
        t.goto(190, 250)
        circle()
    if Move2 == 9:
        t.penup()
        t.goto(290, 250)
        circle()
    if len(move_list) == 9:
        print ("End of Game")
        break

    time.sleep (1)




turtle.exitonclick()
