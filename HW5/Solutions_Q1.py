import matplotlib.pyplot as plt
import numpy as np



def on_segment (p, q, r):
    # check if r lies on (p,q)
    if r[0] <= max (p[0], q[0]) and r[0] >= min (p[0], q[0]) and r[1] <= max (p[1], q[1]) and r[1] >= min (p[1], q[1]):
        return True
    return False


def orientation (p, q, r):
    # return 0/1/-1 for colinear / clockwise / counterclockwise
    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
    if val == 0 : return 0
    return 1 if val > 0 else -1


def intersects (seg1 , seg2 ):
    # check if seg1 and seg2 intersect
    p1 , q1 = seg1
    p2 , q2 = seg2
    o1 = orientation (p1 , q1 , p2)
    # find all orientations
    o2 = orientation (p1 , q1 , q2)
    o3 = orientation (p2 , q2 , p1)
    o4 = orientation (p2 , q2 , q1)
    if o1 != o2 and o3 != o4:
        # check general case
        return True
    if o1 == 0 and on_segment (p1 , q1 , p2) : return True
    

def manipulatorSegment(start_point, length, angle):
    return (start_point , (start_point[0] + length * np.cos(np.radians(angle)), start_point[1] + length * np.sin(np.radians(angle))))


""" Main Code """
L1 = 3
L2 = 2
seg_obstacle = ((-1, 1), (-0.8, 1.2))

c_space = np.zeros((360, 360), dtype=bool)
for Theta1 in range(0,181,1):
    seg_1 = manipulatorSegment((0,0), L1, Theta1)
    #print(f'L1 segment is {seg_1[0]}, {seg_1[1]}')
    if not intersects ( seg_1 , seg_obstacle ):
        for Theta2 in range(0,360,1):
            seg_2 = manipulatorSegment(seg_1[1], L2, Theta2)
            if intersects(seg_2,seg_obstacle):
                # nothing
                pass
            else:
                c_space[Theta1][Theta2]=True


plt.imshow(c_space)
plt.title('C-Space')
plt.ylabel("Theta 1")
plt.xlabel("Theta 2")
plt.show()