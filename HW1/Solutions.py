## HACETTEPE UNIVERSITY COMPUTER ENGIINERING DEPARTMENT
## CMP 755 ROBOTICS
## Homework 1
import numpy as np
import math

from numpy.core.fromnumeric import argmax

## Q1 (functions)
## Q1.a
def f1_x(PB,degTheta):
    radTheta = degTheta * math.pi / 180
    R_x=np.array([[1, 0, 0],[0, math.cos(radTheta), -math.sin(radTheta)],[0, math.sin(radTheta), math.cos(radTheta)]])
    PA=R_x.dot(PB)
    return PA
## Q1.b
def f1_y(PB,degTheta):
    radTheta = degTheta * math.pi / 180
    R_y=np.array([[math.cos(radTheta), 0, math.sin(radTheta)],[0, 1, 0],[-math.sin(radTheta), 0, math.cos(radTheta)]])
    PA=R_y.dot(PB)
    return PA
## Q1.c
def f1_z(PB,degTheta):
    radTheta = degTheta * math.pi / 180
    R_z=np.array([[math.cos(radTheta), -math.sin(radTheta), 0],[math.sin(radTheta), math.cos(radTheta), 0],[0, 0, 1]])
    PA=R_z.dot(PB)
    return PA
## Q1 done

## Q2 (test)
print("\n\nQuestion 2 test started: rotation around individual axes")
PB=[3.0 , 5.0 , 0.0]
print("\n Rotation around X-axis")
PA=f1_x(PB,90)
print("Current coordinates: " + str([round(coordinate,2) for coordinate in PB]))
print("New coordinates: " + str([round(coordinate,2) for coordinate in PA]))
print("\n Rotation around Y-axis")
PA=f1_y(PB,90)
print("Current coordinates: " + str([round(coordinate,2) for coordinate in PB]))
print("New coordinates: " + str([round(coordinate,2) for coordinate in PA]))
print("\n Rotation around Z-axis")
PA=f1_z(PB,90)
print("Current coordinates: " + str([round(coordinate,2) for coordinate in PB]))
print("New coordinates: " + str([round(coordinate,2) for coordinate in PA]))

""" Results: 
Question 2 test started: rotation around individual axes

 Rotation around X-axis
Current coordinates: [3.0, 5.0, 0.0]
New coordinates: [3.0, 0.0, 5.0]

 Rotation around Y-axis
Current coordinates: [3.0, 5.0, 0.0]
New coordinates: [0.0, 5.0, -3.0]

 Rotation around Z-axis
Current coordinates: [3.0, 5.0, 0.0]
New coordinates: [-5.0, 3.0, 0.0]
"""
## Q2 test is done

## Q3 (function)
def f2(alpha, beta, gamma, PB):
    PA=f1_x(PB, alpha)
    PA=f1_y(PA, beta)
    PA=f1_z(PA, gamma)
    return PA
## Q3 done

## Q4 (test)
print("\n\n Question 4 test started: rotation around all axes sequentially")
PB=[2, 5, 0]
print("Current coordinates: " + str([round(coordinate,2) for coordinate in PB]))
PA=f2(30,90,60,PB)
print("New coordinates: " + str([round(coordinate,2) for coordinate in PA]))

""" Results: 
 Question 4 test started: rotation around all axes sequentially
Current coordinates: [2, 5, 0]
New coordinates: [-2.5, 4.33, -2.0]
"""
## Q4 test is done

## Q5 (function)
def f3(alpha, beta, gamma):
    # create rotation matrix
    R=f1_x(np.identity(3), alpha)
    R=f1_y(R, beta)
    R=f1_z(R, gamma)
    # calculate quaternions
    euler_parameters=np.array([math.sqrt(abs(1+R[0,0]-R[1,1]-R[2,2])), math.sqrt(abs(1-R[0,0]+R[1,1]-R[2,2])),
                                math.sqrt(abs(1-R[0,0]-R[1,1]+R[2,2])), math.sqrt(abs(1+R[0,0]+R[1,1]+R[2,2]))
                                ])
    euler_parameters=euler_parameters / 2
    temp=np.argmax(euler_parameters)
    if temp==3:
        euler_parameters[0]=(R[2,1]-R[1,2]) / (4*euler_parameters[temp])
        euler_parameters[1]=(R[0,2]-R[2,0]) / (4*euler_parameters[temp])
        euler_parameters[2]=(R[1,0]-R[0,1]) / (4*euler_parameters[temp])
    elif temp==0:
        euler_parameters[1]=(R[0,1]+R[1,0]) / (4*euler_parameters[temp])
        euler_parameters[2]=(R[0,2]+R[2,0]) / (4*euler_parameters[temp])
        euler_parameters[3]=(R[2,1]-R[1,2]) / (4*euler_parameters[temp])
    elif temp==1:
        euler_parameters[0]=(R[0,1]+R[1,0]) / (4*euler_parameters[temp])
        euler_parameters[2]=(R[1,2]+R[2,1]) / (4*euler_parameters[temp])
        euler_parameters[3]=(R[0,2]-R[2,0]) / (4*euler_parameters[temp])
    else:
        euler_parameters[0]=(R[0,2]+R[2,0]) / (4*euler_parameters[temp])
        euler_parameters[1]=(R[1,2]+R[2,1]) / (4*euler_parameters[temp])
        euler_parameters[3]=(R[0,1]-R[1,0]) / (4*euler_parameters[temp])

    return euler_parameters
## Q5 done

## Q6 (function)
def f4(Rotation_angles, Translation_coordinates, PB):
    PA=f2(Rotation_angles[0], Rotation_angles[1], Rotation_angles[2], PB)
    PA=PA+Translation_coordinates
    return PA
## Q6 done

## Q7 (function)
def f5(e, Translation_coordinates, PB):
    R=np.array([
        [1 - 2*e[1]**2 - 2*e[2]**2      , 2 * (e[0]*e[1] - e[2]*e[3])   , 2 * (e[0]*e[2] + e[1]*e[3]) ],
        [2 * (e[0]*e[1] + e[2]*e[3])    , 1 - 2*e[0]**2 - 2*e[2]**2     , 2 * (e[1]*e[2] - e[0]*e[3]) ],
        [2 * (e[0]*e[2] - e[1]*e[3])    , 2 * (e[1]*e[2] + e[0]*e[3])   , 1 - 2*e[0]**2 - 2*e[1]**2 ]
        ])
    PA=R.dot(PB)
    PA=PA+Translation_coordinates

    return PA
## Q7 done