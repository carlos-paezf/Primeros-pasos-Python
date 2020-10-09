import turtle

# Obtener una pantalla de trabajo
ws = turtle.Screen()
# Definir una instancia Turtle
t = turtle.Turtle()
# Configurar la instancia en verde
t.color("Green")
# Configurar el ancho de 2
t.width("2")
# Configurar la velociadad en 2
t.speed(1)

# Bucle para 
for i in range(4):
	t.forward(300)
	t.left(90)

t.penup()
t.goto(0,100)
t.pendown()
t.forward(300)
t.penup()
t.goto(0,200)
t.pendown()
t.forward(300)
t.penup()
t.goto(100,0)
t.pendown()
t.left(90)
t.forward(300)
t.penup()
t.goto(200,0)
t.pendown()
t.forward(300)