import turtle
#IS A PRE-DEFINED LIBRARY THAT ENABLES USER TO CREATE PICTURES AND SHAPES BY PROVISING THEM A VIRTUAL CANVAS.
turtle.bgcolor("black")
#USED FOR CHANGING THE BACKGROUND COLOUR. 
t = turtle.Pen()
#This function is used to return or set the pen’s attributes 
t.speed(50)
#WE USE THIS TO INCREASE AND DECREASE THE SPEED OF TEXT
colours = ["red","yellow","blue","green","white","cyan"]
#USED THIS FOR SELECTING MUMTIPLE COLOURS
yourname = turtle.textinput("Enter Your name", "ENTER A STRING")
#IS USED FOR TAKING INPUT DATA
for x in range(100):
    #FOR LOOP
    t.pencolor(colours[x%6])
    #PROVIDING NUMBER OF TIMES THE STRING PRINT IN A ROW IN TERMS OF COLOURS.
    t.penup()
    #Moving the turtle without drawing.
    #This is useful for repositioning the turtle.
    #making breaks in the drawing.
    t.forward(x * 6)
    #PROVIDING NUMBER OF TIMES THE STRING PRINT IN A ROW IN TERMS OF FORWARD MOVEMENT.
    t.pendown()
    #Moving the turtle for drawing.
    #This is useful for repositioning the turtle.
    #used after breaks in the drawing.
    t.write(yourname, font=("Arial",int((x + 4) / 4), "bold"))
    #TAKES FONT SIZE AND TYPE FOR YOUR ENTERED STRING.
    t.left(100)
    #used to change the direction of the turtle by the value of the argument that it takes.
