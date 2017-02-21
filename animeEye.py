'''
@author: Matthew Kataryniak
=========================================================
Really long turtle program that draws a character
in the style of Japanese anime/manga.
'''
from turtle import *

tracer(False)

t = Turtle()
t.speed(0)
for i in range(10):
    t.fd(10)
    t.lt(i)
t.lt(70)
for i in range(10):
    t.pensize(i)
    t.fd(10)
    t.lt(i)
for i in range(10):
    t.lt(i)
    t.fd(8)
t.fd(20)
t.lt(20)
for i in range(9):
    t.pensize(10-i)
    t.lt(5)
    t.fd(8)
t.lt(50)
for i in range(3):
    t.fd(4)
    t.lt(1)
t.fd(15)

for i in range(3):
    t.fd(4)
    t.lt(1)

r = Turtle()
r.speed(0)
r.color('white')
r.pu()
r.setx(10)
r.sety(23)
r.pd()
r.begin_fill()
r.circle(40)
r.end_fill()

e = Turtle()
e.speed(0)
e.pu()
e.setx(-30)
e.sety(63)
e.pd()
e.color('blue')
for i in range(179):
    e.fd(80)
    e.lt(179)

y = Turtle()
y.speed(0)
y.pu()
y.setx(0)
y.sety(63)
y.color('white')
y.pd()
for i in range(179):
    y.fd(20)
    y.lt(179)

v = Turtle()
v.speed(0)
v.pu()
v.setx(-100)
v.sety(150)
v.pd()
for i in range(10):
    v.pensize(i * 3)
    if (v.pensize() >= 20):
        v.pensize(20)
    v.fd(15)
    v.rt(3)
v.lt(3)
for i in range(5):
    v.pensize(20 - i * 3)
    if (v.pensize() <= 1):
        v.pensize(1)
    v.fd(15)
    v.lt(3)

# Eye 2
t = Turtle()
t.speed(0)
t.pu()
t.setx(300)
t.pd()
for i in range(10):
    t.bk(10)
    t.rt(i)
t.rt(70)
for i in range(10):
    t.pensize(i)
    t.bk(10)
    t.rt(i)
for i in range(10):
    t.rt(i)
    t.bk(8)
t.bk(20)
t.rt(20)
for i in range(9):
    t.pensize(10-i)
    t.rt(5)
    t.bk(8)
t.rt(50)
for i in range(3):
    t.bk(4)
    t.rt(1)
t.bk(15)
for i in range(3):
    t.bk(4)
    t.rt(1)

r = Turtle()
r.speed(0)
r.color('white')
r.pu()
r.setx(310)
r.sety(23)
r.pd()
r.begin_fill()
r.circle(40)
r.end_fill()

e = Turtle()
e.speed(0)
e.pu()
e.setx(250)
e.sety(63)
e.pd()
e.color('blue')
for i in range(179):
    e.fd(80)
    e.lt(179)

y = Turtle()
y.speed(0)
y.pu()
y.setx(280)
y.sety(63)
y.color('white')
y.pd()
for i in range(179):
    y.fd(20)
    y.lt(179)

v = Turtle()
v.speed(0)
v.pu()
v.setx(400)
v.sety(150)
v.pd()
for i in range(10):
    v.pensize(i * 3)
    if (v.pensize() >= 20):
        v.pensize(20)
    v.bk(15)
    v.lt(3)
v.rt(3)
for i in range(5):
    v.pensize(20 - i * 3)
    if (v.pensize() <= 1):
        v.pensize(1)
    v.bk(15)
    v.rt(3)

#Mouth and Nose
m = Turtle()
m.speed(0)
m.pu()
m.setx(180)
m.sety(-120)
m.pd()
for i in range(10):
    m.pensize(i * 3)
    if m.pensize() >= 16:
        m.pensize(16)
    m.bk(20)
    m.rt(i)

n = Turtle()
n.speed(0)
n.pu()
n.setx(150)
n.rt(85)
n.pd()
for i in range(15):
    n.pensize(i)
    n.fd(2)
    n.rt(2)

#The faic
g = Turtle()
g.pu()
g.speed(0)
g.setx(150)
g.sety(-230)
g.pd()
g.lt(30)
for i in range(20):
    g.fd(20)
    g.lt(1)
    g.pensize(i)
g.lt(30)
for i in range(5):
    g.fd(20)
    g.pensize(i + 20)
    if g.pensize() >= 25:
        g.pensize(25)
    g.lt(5)
fu = g.xcor()
print(fu)
fu = g.ycor()
print(fu)

g = Turtle()
g.pu()
g.speed(0)
g.setx(150)
g.sety(-230)
g.pd()
g.lt(180)
g.rt(30)
for i in range(20):
    g.fd(20)
    g.rt(1)
    g.pensize(i)
g.rt(30)
for i in range(5):
    g.fd(20)
    g.pensize(i + 20)
    if g.pensize() >= 25:
        g.pensize(25)
    g.rt(5)
fu = g.xcor()
print(fu)
fu = g.ycor()
print(fu)

#Ears
q = Turtle()
q.speed(0)
q.pu()
q.setx(457)
q.sety(122)
q.pd()
q.lt(30)
q.pensize(10)
for i in range(15):
    q.fd(10)
    q.rt(12)
    q.pensize(25 - i)
q.fd(10)
for i in range(4):
    q.fd(10)
    q.rt(6)
    q.pensize(10 - i)
    if q.pensize() <= 1:
        q.pensize(1)

q = Turtle()
q.speed(0)
q.pu()
q.setx(-157)
q.sety(122)
q.pd()
q.rt(30)
q.lt(180)
q.pensize(10)
for i in range(15):
    q.fd(10)
    q.lt(12)
    q.pensize(25 - i)
q.fd(10)
for i in range(4):
    q.fd(10)
    q.lt(6)
    q.pensize(10 - i)
    if q.pensize() <= 1:
        q.pensize(1)


#Hair
#Bangs
c = Turtle()
c.speed(0)
c.pu()
c.setx(-155)
c.sety(124)
c.pd()
c.color('#663300')
c.pensize(20)
c.rt(35)
for k in range(9):
    for i in range(20):
        c.fd(6.5)
        c.lt(2)
        c.pensize(20 - i)
        if c.pensize() <= 3:
            c.pensize(3)
    c.lt(140)
    for i in range(20):
        c.fd(6.5)
        c.rt(2)
        c.pensize(3 + i)
        if c.pensize() >= 20:
            c.pensize(20)
    c.rt(154)
   
tracer(True)
c.lt(180)
##c.rt(30)
##c.fd(15)

#Top
c.lt(60)
for i in range(20):
    c.fd(40)
    c.lt(5)
    c.pensize(c.pensize() + 1)
c.pensize(20)
c.pu()
c.setx(-157)
c.sety(122)
c.pd()
c.rt(80)
for i in range(20):
    c.fd(40)
    c.rt(5)
    c.pensize(c.pensize() + 1)

#Neck
l = Turtle()
l.pu()
l.setx(-10)
l.sety(-120)
l.rt(95)
l.pensize(10)
l.pd()
for i in range(7):
    l.fd(30)
    l.rt(5)
    l.pensize(l.pensize() - 1)
fu = l.xcor()
print(fu)
fu = l.ycor()
print(fu)

l.pu()
l.pensize(10)
l.setx(310)
l.sety(-120)
l.setheading(85)
l.lt(180)
l.pd()
for i in range(7):
    l.fd(30)
    l.lt(5)
    l.pensize(l.pensize() - 1)
l.rt(90)
for i in range(10):
    l.fd(46.6)
    l.rt(7.1)
