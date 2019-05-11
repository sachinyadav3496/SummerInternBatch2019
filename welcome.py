import turtle as t

p = t.Pen()

p.speed(0)
p.color('red','yellow')
p.begin_fill()

for var in range(200) : 
    p.forward(300)
    p.left(171)
p.end_fill()

t.exitonclick()
