from controller import Robot


def run(robot):
    ThDist=500
    timestep = int(robot.getBasicTimeStep())
    
    leftWheel = robot.getDevice("motorLeft")
    rightWheel = robot.getDevice("motorRight")

    left_distance_sensor = robot.getDevice("dsLeft")
    right_distance_sensor = robot.getDevice("dsRight")
    left_distance_sensor.enable(timestep)
    right_distance_sensor.enable(timestep)
    
    leftWheel.setPosition(float('inf'))
    leftWheel.setVelocity(0.0)
    rightWheel.setPosition(float('inf'))
    rightWheel.setVelocity(0.0)
    
    
    while robot.step(64)!=-1: 
        #Establecer velocidad
        dsL=left_distance_sensor.getValue()
        dsR=right_distance_sensor.getValue()
        
        #print("sensores: {} {}".format(dsL,dsR))
        
        if dsL<ThDist or dsL<ThDist:
            leftWheel.setVelocity(0)
            rightWheel.setVelocity(0)   
            break
            
        leftWheel.setVelocity(2)
        rightWheel.setVelocity(2)
        
            
    
if __name__=="__main__":
    robot = Robot()
    run(robot)