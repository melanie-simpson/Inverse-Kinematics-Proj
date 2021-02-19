#Enzo Signorelli & Melanie Simpson
from arm_controller import ArmController
import numpy as np

if __name__=='__main__':
    ac = ArmController()
    
    x = input('X Coordinate: ')
    y = input('Y Coordinate: ')
    z = input('Z Coordinate: ')
    roll = input('Roll: ')
    pitch = input('Pitch: ')
    yaw = input('Yaw: ')

    #First digit is row, second digit is column -> T00 = T[0, 0]
    #After doing the matrix multiplication and simplification of work, 
    # we learned that we only needed the following indices of the matrix
    T01 = (-np.sin(yaw))*(np.cos(roll)) + (np.cos(yaw))*(np.sin(pitch))*(np.sin(roll))
    T11 = (np.cos(yaw))*(np.cos(roll)) + (np.sin(yaw))*(np.sin(pitch))*(np.sin(roll))
    T02 = (np.sin(yaw))*(np.sin(roll)) + (np.cos(yaw))*(np.sin(pitch))*(np.cos(roll))
    T22 = (np.cos(pitch))*(np.cos(roll))
    T03 = x
    T23 = z

    d1 = 0.077
    l2 = 0.0383
    l4 = 0.126

    s1 = -T01
    c1 = T11
    angle1 = np.arctan2(s1, c1)

    s2 = (T23-l4*T02-d1)/(l2)
    c2 =  (T03-l4*T11*T22)/(T11*l2)
    angle2 = np.arctan2(s2, c2)

    #angle3 is equal to zero, because we do not intend for joint3 to move at all
    angle3 = 0

    angle4 = np.arctan2(T02, T22) - angle2

    #Move that arm
    ac.set_joints([angle1, angle2, angle3, angle4])
#    print(ac.get_pose())

