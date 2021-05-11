from controller import Robot

robot = Robot()

leftWheel = robot.getDevice("left wheel motor")
rightWheel = robot.getDevice("right wheel motor")

#Establecer velocidad
leftWheel.setVelocity(3)
rightWheel.setVelocity(3)

#Ir hacia delante hasta la primer vuelta
leftWheel.setPosition(1000)
rightWheel.setPosition(1000)
robot.step(12500)

#Gira a la izquierda
leftWheel.setPosition(-1000)
rightWheel.setPosition(1000)
robot.step(800)

#Ir hacia adelante hasta la suiguiente esquina
leftWheel.setPosition(1000)
rightWheel.setPosition(1000)
robot.step(6500)

#Gira a la izquierda
leftWheel.setPosition(-1000)
rightWheel.setPosition(1000)
robot.step(700)

#Ir hacia adelante hasta la suiguiente esquina
leftWheel.setPosition(1000)
rightWheel.setPosition(1000)
robot.step(12000)

#Detener
leftWheel.setVelocity(0)
rightWheel.setVelocity(0)