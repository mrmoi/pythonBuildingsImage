import turtle
from math import sqrt

# Accepts a as width
# Accepts t as item to be drawn
def star(a, t):
    # Calculate Diameter
    diameter = a * 0.0616
    # This is the size of the star
    radius = diameter / 2
    # draw a circle to test coordinates
    # -> position turtle at bottom-center of circle
    t.speed(10)
    t.penup()
    t.right(90)
    t.forward(radius)
    t.left(90)
    #  -> draw circle
    #t.pendown()
    #t.circle(radius)
    #  -> go back to center
    t.penup()
    t.left(90)
    t.forward(radius)
    t.right(90)
    # In order to draw a star, I need to figure out the length of one 'leg' of the star.
    # This took a diagram and bit of trigonometry to figure out ...
    leg = radius * sqrt(5 - 2 * sqrt(5))
    # Go to top of star, and point the turtle down the first leg of the star
    t.penup()
    t.left(90)
    t.forward(radius)
    t.right(162)
    # Draw the star, starting at the top
    t.begin_fill()
    t.fillcolor('white')
    t.pendown()
    for i in range(5):
        t.forward(leg)
        t.left(72)
        t.forward(leg)
        t.right(144)
    t.end_fill()
    # Return to initial location
    t.penup()
    t.right(18)
    t.forward(radius)
    t.left(90)


def reposition(item):
    # Re-Position Arrow to upper left corner of flag
    item.speed(10)
    item.penup()
    item.right(180)
    item.forward(0) #275
    item.right(90)
    item.forward(0) #250
    item.right(90)

# Accept item as turtle instance object
# Accept x as union length
def top_stripe_reposition(item, x):
    # Re-Position Arrow to union length start
    item.speed(10)
    item.penup()
    item.right(180)
    item.forward(0) #275
    item.right(90)
    item.forward(0) #250
    item.right(90)
    item.forward(x)


def printrectangle(x):
    # Create instance of turtle
    rectangle = turtle.Turtle()
    # Call reposition function
    reposition(rectangle)
    # Times by 1.9 to match the specifications
    length = x * 1.9
    # Draw Rectangle
    rectangle.speed(10)
    rectangle.pendown()
    rectangle.forward(length)
    rectangle.right(90)
    rectangle.forward(x)
    rectangle.right(90)
    rectangle.forward(length)
    rectangle.right(90)
    rectangle.forward(x)
    rectangle.penup()
    rectangle.home()

    return length

# Calculate width of union (C)
def innerwidth(x):
    # Calculate inner width
    inner_width = x * 0.5385
    return inner_width

# Calculate length of union (D)
def innerlength(x):
    # Calculate inner length
    inner_length = x * 0.76
    return inner_length

# Draw Union
def drawinnersquare(x, y, unioncolor):
    # Create instance of turtle to start drawing
    insquare = turtle.Turtle()
    insquare.speed(10)
    # Call reposition function
    reposition(insquare)
    # Draw Rectangle
    insquare.begin_fill()
    insquare.fillcolor(unioncolor)
    insquare.pendown()
    insquare.forward(y)
    insquare.right(90)
    insquare.forward(x)
    insquare.right(90)
    insquare.forward(y)
    insquare.right(90)
    insquare.forward(x)
    insquare.end_fill()

    insquare.penup()
    insquare.home()

# Calculate stripe width
def stripewidth(x):
    # Calculate stripe width
    stripe_width = x * 0.0769
    return stripe_width

# Calculate top stripes' length
# Accept x as width
def topstripelength(x):
    # Call inner length function and Set y equals to it
    y = innerlength(x)
    # Calculate lenght again and set to z
    z = x * 1.9
    # Calculate top stripe length
    top_stripe_length = z - y
    return top_stripe_length

# Draw top stripes
# Accept x as stripe width
# Accept y as top stripe length
# Accept z as union length
def drawtopstripe(a, x, y, z, firststripecolor, secondstripecolor):
    # Create instance of turtle
    topStripe = turtle.Turtle()
    topStripe.speed(10)
    # Call function to position at end of union length
    top_stripe_reposition(topStripe, z)
    bottomstripe = a * 1.9

    topStripe.begin_fill()
    topStripe.fillcolor(firststripecolor)
    topStripe.pendown()
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor(secondstripecolor)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor(firststripecolor)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor(secondstripecolor)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor(firststripecolor)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor(secondstripecolor)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor(firststripecolor)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor(secondstripecolor)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor(firststripecolor)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor(secondstripecolor)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor(firststripecolor)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor(secondstripecolor)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor(firststripecolor)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.penup()
    topStripe.home()

# Draw Stars
# accept a as width
def drawstars(a):
    # Create object to draw stars
    d = turtle.Turtle()
    # Call reposition function
    reposition(d)
    d.right(90)
    d.forward(a * 0.054)
    d.left(90)
    d.forward(a * 0.063)

    return d


def drawFlag(width, firststripecolor, secondstripecolor, unioncolor):
    # -------------  Start Main -------------  #
    # Width value entered by user
    # Will have to be in form of a question with input validation


    # variable declaration
    verticalgap = width * 0.054
    horizontalgap = width * 0.063

    doublehorizontal = horizontalgap * 2
    doublevertical = verticalgap * 2

    # Store width in backup width for further use
    backupWidth = width

    # Call function to draw rectangle
    printrectangle(width)

    # Call function to calculate inner width
    unionWidth = innerwidth(width)

    # Call function to calculate inner length
    unionLength = innerlength(width)

    # Call function to draw inner square
    drawinnersquare(unionWidth, unionLength, unioncolor)

    # Call function to calculate stripe width
    stripeWidth = stripewidth(width)

    # Call function to calculate top stripe length
    topStripeLength = topstripelength(width)

    # Draw top stripes using stripeWidth and topStripeLength variables
    drawtopstripe(width, stripeWidth, topStripeLength, unionLength, firststripecolor, secondstripecolor)

    # Position Star
    # Create object to draw stars
    d = turtle.Turtle()

    # Call reposition function
    reposition(d)
    # Position to draw first star
    d.right(90)
    d.forward(verticalgap) #1
    d.left(90)
    d.forward(horizontalgap)
    star(width, d)

    # Draw Star
    # First Row
    for i in range(5):
        d.forward(doublehorizontal)
        star(width, d)

    d.home()

    # Second Row
    e = turtle.Turtle()
    e.speed(10)
    reposition(e)

    e.right(90)
    for i in range(2):
        e.forward(verticalgap)
    e.left(90)
    e.forward(horizontalgap)
    e.forward(horizontalgap)
    star(width, e)

    for i in range(4):
        e.forward(doublehorizontal)
        star(width, e)

    e.home()

    # Third Row
    f = turtle.Turtle()
    f.speed(10)
    reposition(f)
    f.right(90)
    for i in range(3):
        f.forward(verticalgap)
    f.left(90)
    f.forward(horizontalgap)
    star(width, f)

    for i in range(5):
        f.forward(doublehorizontal)
        star(width, f)

    f.home()

    # Fourth Row
    g = turtle.Turtle()
    g.speed(10)
    reposition(g)
    g.right(90)
    for i in range(4):
        g.forward(verticalgap)
    g.left(90)
    g.forward(horizontalgap)
    g.forward(horizontalgap)
    star(width, g)

    for i in range(4):
        g.forward(doublehorizontal)
        star(width, g)

    g.home()

    # Fifth Row
    h = turtle.Turtle()
    h.speed(10)
    reposition(h)
    h.right(90)
    for i in range(5):
        h.forward(verticalgap)
    h.left(90)
    h.forward(horizontalgap)
    star(width, h)

    for i in range(5):
        h.forward(doublehorizontal)
        star(width, h)

    h.home()


    # Sixth Row
    i = turtle.Turtle()
    i.speed(10)
    reposition(i)
    i.right(90)
    for j in range(6):
        i.forward(verticalgap)
    i.left(90)
    i.forward(horizontalgap)
    i.forward(horizontalgap)
    star(width, i)

    for w in range(4):
        i.forward(doublehorizontal)
        star(width, i)

    i.home()

    # Seventh Row
    j = turtle.Turtle()
    j.speed(10)
    reposition(j)
    j.right(90)
    for i in range(7):
        j.forward(verticalgap)
    j.left(90)
    j.forward(horizontalgap)
    star(width, j)

    for w in range(5):
        j.forward(doublehorizontal)
        star(width, j)

    j.home()

    # Eight Row
    m = turtle.Turtle()
    m.speed(10)
    reposition(m)
    m.right(90)
    for i in range(8):
        m.forward(verticalgap)
    m.left(90)
    m.forward(horizontalgap)
    m.forward(horizontalgap)
    star(width, m)

    for w in range(4):
        m.forward(doublehorizontal)
        star(width, m)

    m.home()

    # Ninth Row
    n = turtle.Turtle()
    n.speed(10)
    reposition(n)
    n.right(90)
    for i in range(9):
        n.forward(verticalgap)
    n.left(90)
    n.forward(horizontalgap)
    star(width, n)

    for w in range(5):
        n.forward(doublehorizontal)
        star(width, n)

    n.home()


# Main #
def askwidth():

    width = int(raw_input('Enter the width: '))

    if width > 49 and width < 601:

        return width

    else:

        print 'Please enter a width between 50 and 600'
        askwidth()


def askoddstripe():

    a = str(raw_input('Enter odd stripe color: '))

    if a == 'red' or a == 'white' or a == 'black' or a == 'blue' or a == 'green' or a == 'orange':
        return a
    else:
        print 'Please any of these colors: red, white, black, blue, green, orange'
        askoddstripe()


def askevenstripe():

    b = str(raw_input('Enter even stripe color: '))

    if b == 'red' or b == 'white' or b == 'black' or b == 'blue' or b == 'green' or b == 'orange':
        return b
    else:
        print 'Please any of these colors: red, white, black, blue, green, orange'
        askevenstripe()


def askunioncolor():

    c = str(raw_input('Enter the union color: '))

    if c == 'red' or c == 'white' or c == 'black' or c == 'blue' or c == 'green' or c == 'orange':
        return c
    else:
        print 'Please any of these colors: red, white, black, blue, green, orange'
        askunioncolor()

# Start Main #

print 'lets draw the flag..'

print 'Please enter a width between 50 and 600'

width = askwidth()

a = askoddstripe()

b = askevenstripe()

unioncolor = askunioncolor()

drawFlag(width, a, b, unioncolor)

# Keep screen open
turtle.mainloop()