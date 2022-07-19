import turtle
# define some colors
colors= ['red','yellow','green','blue','cyan','burlygreen']

# set up the turtle and set the background color
t=turtle.Pen()
turtle.bgcolor('black')

# now to the movements
for x in range(200):
    # set the color 
    t.pencolor(color[x%6])
    # set the width 
    t.width(x/100+1)
    #move the turtle 
    t.forward(x)
    # rotate the turtle
    t.left(59)