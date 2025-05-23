
"""
This is my rubik's cube software for Engineering Optimisation ENEL445
This project will build upon a 2*2*2 rubik's cube and work up to a 3*3*3 cube 
if successful 

"""
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import time

#----------------------------------------------------------------------------#
# Variables
#----------------------------------------------------------------------------#

cube_x_pos = [2,3,2,3,0,1,0,1,2,3,2,3,4,5,4,5,2,3,2,3,2,3,2,3]
cube_y_pos = [7,7,6,6,5,5,4,4,5,5,4,4,5,5,4,4,3,3,2,2,1,1,0,0]

color_map_1 = {
    1: 'yellow', 
    2: 'blue',
    3: 'red',
    4: 'green',
    5: 'white',
    6: 'orange'
}

color_map_2 = {
    1: 'yellow', 
    2: 'yellow', 
    3: 'yellow', 
    4: 'yellow', 
    5: 'blue',
    6: 'blue',
    7: 'blue',
    8: 'blue',
    9: 'red',
    10: 'red',
    11: 'red',
    12: 'red',
    13: 'green',
    14: 'green',
    15: 'green',
    16: 'green',
    17: 'white',
    18: 'white',
    19: 'white',
    20: 'white',
    21: 'orange',
    22: 'orange',
    23: 'orange',
    24: 'orange'
    }

cube_mixed_1 = np.array([22,18,10,11,20,13,9,24,4,8,14,5,17,15,23,7,2,1,6,21,3,19,16,12])
# has scramble sequence ['bottomCW', 'backCW', 'backFT', 'backFT', 'leftCCW', 'frontCCW', 
#                        'topCW', 'leftFT', 'bottomCCW', 'bottomCCW', 'rightFT', 'leftCW', 
#                        'frontFT', 'leftCW', 'rightFT', 'bottomCCW', 'leftCCW', 'leftCW', 
#                        'rightCW', 'frontFT']

cube_mixed_2 = np.array([15,5,20,8,18,22,24,13,16,17,10,9,11,1,6,21,4,3,14,19,2,7,12,23])


cube_mixed_3 = np.array([1,8,3,4,5,6,7,2,9,10,24,12,13,17,15,16,14,18,19,20,21,22,23,11])


cube_solved = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]) # desired cube solution
    



#----------------------------------------------------------------------------#
# Cube plotting
#----------------------------------------------------------------------------#

fig, ax = None, None

def plot_cube(cube, itr=None):
    """This function plots the 2d unfolded layout of the 2*2*2 cube"""
    
    global fig, ax
    plt.ion()

    # Initialize figure and axis once
    if fig is None or ax is None:
        fig, ax = plt.subplots()
    else:
        ax.clear()
    
    
    for i in range(len(cube)):
        rectangle = patches.Rectangle((cube_x_pos[i] + 2, cube_y_pos[i]), 1, 1, linewidth=1, edgecolor='black', facecolor= color_map_2[cube[i]])
        ax.add_patch(rectangle)
        plt.annotate(str(cube[i]), xy=(cube_x_pos[i] + 2.25,cube_y_pos[i]+ 0.5), xytext=(cube_x_pos[i] + 2.25,cube_y_pos[i] + 0.5))
    
    # Set axis limits for better visualization
    ax.set_xlim(2, 8)
    ax.set_ylim(0, 9)
    
    plt.annotate('Top', xy=(4, 8.5), xytext=(4.5, 8.5))
    plt.annotate('Left', xy=(2, 6.5), xytext=(2.5, 6.5))
    plt.annotate('Front', xy=(6, 4), xytext=(6.5, 3), arrowprops=dict(facecolor='red', arrowstyle='->'))
    plt.annotate('Right', xy=(4, 9), xytext=(6.5, 6.5))
    plt.annotate('Bottom', xy=(4, 9), xytext=(2.5, 3))
    plt.annotate('Back', xy=(4, 9), xytext=(2.5, 1))
    plt.annotate(itr, xy=(7,1), xytext=(7,1))
    
    plt.tick_params(axis='x', labelbottom=False)  # Remove x-axis values
    plt.tick_params(axis='y', labelleft=False)    # Remove y-axis values
    
    # Show the plot
    fig.canvas.draw()
    plt.pause(0.01)


def iteration_cost(cost_list, n):
        axes = plt.axes()
        nS = np.arange(n)
        axes.plot(nS, np.array(cost_list))
        axes.set_xlabel("Iterations (n)")
        axes.set_ylabel("Cost f(cube, cube*)")
        axes.set_ybound(lower=0, upper=25)
        axes.grid()
        plt.show()

    
#----------------------------------------------------------------------------#
# Cube Operations
#----------------------------------------------------------------------------#
                     #1,2,3,4,5,6,7,8,9,1,1,2,3,4,5,6,7,8,9,1,1,2,3,4
TOP_CW = np.array(  [[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#1 TOP
                     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#2 
                     [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#3
                     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#4
                     [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#5 LEFT
                     [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#6
                     [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#7
                     [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#8
                     [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],#9 FRONT
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],#10
                     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],#11
                     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],#12
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],#13 RIGHT
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],#14
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],#15
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],#16
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],#17 BOTTOM
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],#18
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],#19
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],#20 BACK
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],#21
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],#22
                     [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#23
                     [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],])#24
    
                     #1,2,3,4,5,6,7,8,9,1,1,2,3,4,5,6,7,8,9,1,1,2,3,4
LEFT_CW = np.array([ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],#1 TOP
                     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#2 
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],#3
                     [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#4
                     [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#5 LEFT
                     [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#6
                     [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#7
                     [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#8
                     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#9 FRONT
                     [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#10
                     [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#11
                     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],#12
                     [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],#13 RIGHT
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],#14
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],#15
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],#16
                     [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#17 BOTTOM
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],#18
                     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],#19
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],#20 BACK
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],#21
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],#22
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],#23
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],])#24

                     #1,2,3,4,5,6,7,8,9,1,1,2,3,4,5,6,7,8,9,1,1,2,3,4
FRONT_CW = np.array([[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#1 TOP
                     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#2 
                     [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#3
                     [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#4
                     [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#5 LEFT
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],#6
                     [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#7
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],#8
                     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],#9 FRONT
                     [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#10
                     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],#11
                     [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#12
                     [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#13 RIGHT
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],#14
                     [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#15
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],#16
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],#17 BOTTOM
                     [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],#18
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],#19
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],#20 BACK
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],#21
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],#22
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],#23
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],])#24

                      #1,2,3,4,5,6,7,8,9,1,1,2,3,4,5,6,7,8,9,1,1,2,3,4
RIGHT_CW = np.array([ [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#1 TOP
                      [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#2 
                      [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#3
                      [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],#4
                      [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#5 LEFT
                      [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#6
                      [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#7
                      [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#8
                      [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#9 FRONT
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],#10
                      [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],#11
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],#12
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],#13 RIGHT
                      [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],#14
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],#15
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],#16
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],#17 BOTTOM
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],#18
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],#19
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],#20 BACK
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],#21
                      [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#22
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],#23
                      [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],])#24

                      #1,2,3,4,5,6,7,8,9,1,1,2,3,4,5,6,7,8,9,1,1,2,3,4
BOTTOM_CW = np.array([[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#1 TOP
                      [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#2 
                      [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#3
                      [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#4
                      [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#5 LEFT
                      [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#6
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],#7
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],#8
                      [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#9 FRONT
                      [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#10
                      [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#11
                      [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#12
                      [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],#13 RIGHT
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],#14
                      [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],#15
                      [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],#16
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],#17 BOTTOM
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],#18
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],#19
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],#20 BACK
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],#21
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],#22
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],#23
                      [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],])#24

                     #1,2,3,4,5,6,7,8,9,1,1,2,3,4,5,6,7,8,9,1,1,2,3,4
BACK_CW = np.array([ [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],#1 TOP
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],#2 
                     [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#3
                     [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#4
                     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#5 LEFT
                     [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#6
                     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#7
                     [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#8
                     [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#9 FRONT
                     [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#10
                     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],#11
                     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],#12
                     [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],#13 RIGHT
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],#14
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],#15
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],#16
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],#17 BOTTOM
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],#18
                     [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#19
                     [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#20 BACK
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],#21
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],#22
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],#23
                     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],])#24
#----------------------------------------------------------------------------#
# Cube Operation Functions
#----------------------------------------------------------------------------#
topCW = lambda cube: TOP_CW @ cube
topFT = lambda cube: TOP_CW @ TOP_CW @ cube
topCCW = lambda cube: TOP_CW.T @ cube

leftCW = lambda cube: LEFT_CW @ cube
leftFT = lambda cube: LEFT_CW @ LEFT_CW @ cube
leftCCW = lambda cube: LEFT_CW.T @ cube

frontCW = lambda cube: FRONT_CW @ cube
frontFT = lambda cube: FRONT_CW @ FRONT_CW @ cube
frontCCW = lambda cube: FRONT_CW.T @ cube

rightCW = lambda cube: RIGHT_CW @ cube
rightFT = lambda cube: RIGHT_CW @ RIGHT_CW @ cube
rightCCW = lambda cube: RIGHT_CW.T @ cube

bottomCW = lambda cube: BOTTOM_CW @ cube
bottomFT = lambda cube: BOTTOM_CW @ BOTTOM_CW @ cube
bottomCCW = lambda cube: BOTTOM_CW.T @ cube

backCW = lambda cube: BACK_CW @ cube
backFT = lambda cube: BACK_CW @ BACK_CW @ cube
backCCW = lambda cube: BACK_CW.T @ cube

noturn = lambda cube: cube

cube_operations = {
    0: topCW,
    1: topFT,
    2: topCCW,
    3: leftCW,
    4: leftFT,
    5: leftCCW,
    6: frontCW,
    7: frontFT,
    8: frontCCW,
    9: rightCW,
    10: rightFT,
    11: rightCCW,
    12: bottomCW,
    13: bottomFT,
    14: bottomCCW,
    15: backCW,
    16: backFT,
    17: backCCW,
    18: noturn
}

cube_operations_reduced = {
    0: topCW,
    1: topFT,
    2: leftCW,
    3: leftFT,
    4: frontCW,
    5: frontFT,
    6: rightCW,
    7: rightFT,
    8: bottomCW,
    9: bottomFT,
    10: backCW,
    11: backFT,
    12: noturn
}


cube_operations_str = {
    0: 'topCW',
    1: 'topFT',
    2: 'topCCW',
    3: 'leftCW',
    4: 'leftFT',
    5: 'leftCCW',
    6: 'frontCW',
    7: 'frontFT',
    8: 'frontCCW',
    9: 'rightCW',
    10: 'rightFT',
    11: 'rightCCW',
    12: 'bottomCW',
    13: 'bottomFT',
    14: 'bottomCCW',
    15: 'backCW',
    16: 'backFT',
    17: 'backCCW',
    18: 'noturn'
}

inverse_operations = {
    0: 2,
    1: 1,
    2: 0,
    3: 5,
    4: 4,
    5: 3,
    6: 8,
    7: 7,
    8: 6,
    9: 11,
    10: 10,
    11: 9,
    12: 14,
    13: 13,
    14: 12,
    15: 17,
    16: 16,
    17: 15,
    18: 18
    }

#----------------------------------------------------------------------------#
# Print Operations Function
#----------------------------------------------------------------------------#

def return_operations(operations):
    
    operations_str = len(operations) * [0]
    for i in range(len(operations)):
        operations_str[i] = cube_operations_str[operations[i]]
        
    return operations_str
 
#----------------------------------------------------------------------------#
# Return Inverted Operations Function
#----------------------------------------------------------------------------#
def return_inverted_operations(operations):
    
    inverted_operations = np.zeros(len(operations))
    for i in range(len(operations)):
        inverted_operations[-1-i] = inverse_operations[operations[i]]
    
    return inverted_operations

#----------------------------------------------------------------------------#
# Scramble Function
#----------------------------------------------------------------------------#


def scramble_cube(cube, scramble_length=6, seed=None, plot = False):
    if seed is not None:
        random.seed(seed)

    scramble_sequence = random.choices(range(18), k=scramble_length)
    for move in scramble_sequence:
        cube = cube_operations[move](cube)
        if plot:
            plot_cube(cube)

    return cube, scramble_sequence

#----------------------------------------------------------------------------#
# Objective Function
#----------------------------------------------------------------------------#

def calculate_obj(current_cube, obj_cube):
    """Calculates the objective function of the current cube configuration vs 
    the desired cube configuration"""
    matches = current_cube == obj_cube  # This gives a boolean array of True/False
    match_count = np.sum(matches)  # Count of True values (i.e., matches)

    # Return match count or process it however you want
    obj =  (24 - match_count)
    
    return obj
#----------------------------------------------------------------------------#
# Cube Solving algorithms
#----------------------------------------------------------------------------#
def cube_move_from_moveset(cube, desired_cube, moves, plot = False):
    """plots an input cube for different input operations provided"""
    cost_list = [0] * (len(moves) + 1)
    cost_list[0] = calculate_obj(cube, solved_cube)
    # plot_cube(cube)
    i = 0
    for move in moves:
        i+=1
        cube = cube_operations[move](cube)
        cost_list[i] = calculate_obj(cube, solved_cube)
        if plot:
            plot_cube(cube)
        
    
    # print (cost_list)
    if plot:
        iteration_cost(cost_list, len(cost_list))
    return cube
        
def solve_local_min(cube, cube_desired):
    """checks for local minima and solves """
    min_1 = cube_move_from_moveset(cube_desired, cube_desired, [1,10,8,11,0,8,1,6,2,11])
    min_2 = cube_move_from_moveset(cube_desired, cube_desired, [7,10,2,11,0,11,7,9,8,11])
    
    if (calculate_obj(cube, min_1) == 0):
        cube = cube_move_from_moveset(cube, cube_desired,[1,10,8,11,0,8,1,6,2,11])
    elif (calculate_obj(cube, min_2) == 0):
        cube = cube_move_from_moveset(cube, cube_desired,[7,10,2,11,0,11,7,9,8,11])
    else:
        print("no match :(")
    
    return cube

def solve_planning_prob_3(current_cube, cube_desired, cube_previous):
    

    n = 0
    min_value = 24
    moveset = np.zeros(3)

    for i in range(len(cube_operations)):
        for j in range(len(cube_operations)):
            for k in range(len(cube_operations)):
                n += 1
                
                cube_update = cube_operations[i](current_cube)
                cube_update = cube_operations[j](cube_update)
                cube_update = cube_operations[k](cube_update) 
                cost = calculate_obj(cube_update, cube_desired)
                
                cube_difference_current = calculate_obj(cube_update, current_cube)
                cube_difference_previous = calculate_obj(cube_update, cube_previous)
                
                if (cost != 0) and (cube_difference_current == 0):
                    continue
                elif (cost !=0) and (cube_difference_previous == 0):
                    continue
                else:
                    if cost < min_value:
                        min_value = cost
                        moveset[0] = i
                        moveset[1] = j
                        moveset[2] = k
                    
                
                # print("calculating",n, "out of", 19**3, "moves    move(" ,i,",",j,",",k,")  cost: ",cost)

    operations_str = return_operations(moveset)
    reverse_operations = return_operations(return_inverted_operations(moveset))
    
    
    # print()
    # print("minimum cost after 3 moves:",min_value)
    # print("optimal moves", moveset)
    # print("moveset", operations_str)
    # print("inverted moveset", reverse_operations)
    
    return moveset
    
def solve_planning_prob_4(current_cube, cube_desired, cube_previous):
    
   
    n = 0
    min_value = 24
    moveset = np.zeros(4)

    for i in range(len(cube_operations)):
        for j in range(len(cube_operations)):
            for k in range(len(cube_operations)):
                for l in range(len(cube_operations)):
                    n += 1
                    
                    cube_update = cube_operations[i](current_cube)
                    cube_update = cube_operations[j](cube_update)
                    cube_update = cube_operations[k](cube_update) 
                    cube_update = cube_operations[l](cube_update)
                    cost = calculate_obj(cube_update, cube_desired)
                    
                    cube_difference_current = calculate_obj(cube_update, current_cube)
                    cube_difference_previous = calculate_obj(cube_update, cube_previous)
                    
                    if (cost != 0) and (cube_difference_current == 0):
                        continue
                    elif (cost !=0) and (cube_difference_previous == 0):
                        continue
                    else:
                        if cost < min_value:
                            min_value = cost
                            moveset[0] = i
                            moveset[1] = j
                            moveset[2] = k
                            moveset[3] = l
                    
                
                # print("calculating",n, "out of", 19**3, "moves    move(" ,i,",",j,",",k,")  cost: ",cost)

    operations_str = return_operations(moveset)
    reverse_operations = return_operations(return_inverted_operations(moveset))
    
    
    # print()
    # print("minimum cost after 3 moves:",min_value)
    # print("optimal moves", moveset)
    # print("moveset", operations_str)
    # print("inverted moveset", reverse_operations)
    
    return moveset
    
def solve_planning_prob_5(current_cube, cube_desired, cube_previous):
    
    n = 0
    min_value = 24
    moveset = np.zeros(5)

    for i in range(len(cube_operations)):
        for j in range(len(cube_operations)):
            for k in range(len(cube_operations)):
                for l in range(len(cube_operations)):
                    for m in range(len(cube_operations)):
                        n += 1
                        
                        cube_update = cube_operations[i](current_cube)
                        cube_update = cube_operations[j](cube_update)
                        cube_update = cube_operations[k](cube_update) 
                        cube_update = cube_operations[l](cube_update)
                        cube_update = cube_operations[m](cube_update)
                        cost = calculate_obj(cube_update, cube_desired)
                        
                        cube_difference_current = calculate_obj(cube_update, current_cube)
                        cube_difference_previous = calculate_obj(cube_update, cube_previous)
                        
                        if (cost != 0) and (cube_difference_current == 0):
                            continue
                        elif (cost !=0) and (cube_difference_previous == 0):
                            continue
                        else:
                            if cost < min_value:
                                min_value = cost
                                moveset[0] = i
                                moveset[1] = j
                                moveset[2] = k
                                moveset[3] = l
                                moveset[4] = m
                         
                # print("calculating",n, "out of", 19**3, "moves    move(" ,i,",",j,",",k,")  cost: ",cost)

    operations_str = return_operations(moveset)
    reverse_operations = return_operations(return_inverted_operations(moveset))
    
    # print()
    # print("minimum cost after 5 moves:",min_value)
    # print("optimal moves", moveset)
    # print("moveset", operations_str)
    # print("inverted moveset", reverse_operations)
    
    return moveset

def solve_planning_prob_5_reduced(current_cube, cube_desired, cube_previous):
    
    n = 0
    min_value = 24
    moveset = np.zeros(5)

    for i in range(len(cube_operations_reduced)):
        for j in range(len(cube_operations_reduced)):
            for k in range(len(cube_operations_reduced)):
                for l in range(len(cube_operations_reduced)):
                    for m in range(len(cube_operations_reduced)):
                        n += 1
                        
                        cube_update = cube_operations_reduced[i](current_cube)
                        cube_update = cube_operations_reduced[j](cube_update)
                        cube_update = cube_operations_reduced[k](cube_update) 
                        cube_update = cube_operations_reduced[l](cube_update)
                        cube_update = cube_operations_reduced[m](cube_update)
                        cost = calculate_obj(cube_update, cube_desired)
                        
                        cube_difference_current = calculate_obj(cube_update, current_cube)
                        cube_difference_previous = calculate_obj(cube_update, cube_previous)
                        
                        if (cost != 0) and (cube_difference_current == 0):
                            continue
                        elif (cost !=0) and (cube_difference_previous == 0):
                            continue
                        else:
                            if cost < min_value:
                                min_value = cost
                                moveset[0] = i
                                moveset[1] = j
                                moveset[2] = k
                                moveset[3] = l
                                moveset[4] = m
                         
                # print("calculating",n, "out of", 19**3, "moves    move(" ,i,",",j,",",k,")  cost: ",cost)

    operations_str = return_operations(moveset)
    reverse_operations = return_operations(return_inverted_operations(moveset))
    
    return moveset

  
def cube_solve_algorithm_1(initial_cube, desired_cube, nMax, plot_cost = False):
    """The first iteration of the cube solving algorithm with simple greedy horizon look ahead approach"""
    n = 1 # number of iterations
    loop = True # while loop condition
    current_cube = initial_cube
    previous_cube = initial_cube
    plot_cube(current_cube, itr = n)
    cost_list = [calculate_obj(current_cube, desired_cube)] 
    
    while loop:
        
        #Solving Planning Problem
        moveset = solve_planning_prob_5_reduced(current_cube, desired_cube, previous_cube)
        previous_cube = current_cube
        
        #Performing Planning Problem Moves
        for i in range(len(moveset)):
            n+=1
            current_cube = cube_operations[moveset[i]](current_cube)
            plot_cube(current_cube, itr = n)
            cost = calculate_obj(current_cube, desired_cube)
            cost_list.append(cost) 
        # Check for convergence or timeout        
        if (calculate_obj(current_cube, desired_cube) == 0) or (n >= nMax):
            loop = False

    if plot_cost:
        iteration_cost(cost_list,n)


def cube_solve_algorithm_2(initial_cube, desired_cube, nMax, plot_cost = False):
    """"""
    n = 1 # number of iterations
    loop = True # while loop condition
    current_cube = initial_cube
    previous_cube = initial_cube
    plot_cube(current_cube, itr = n)
    cost_list = [calculate_obj(current_cube, desired_cube)] 
    
    
    while loop:
        
        #Solving Planning Problem
        moveset = solve_planning_prob_5(current_cube, desired_cube, previous_cube)
        previous_cube = current_cube
        
        #Performing Planning Problem Moves
        for i in range(len(moveset)):
            n+=1
            current_cube = cube_operations[moveset[i]](current_cube)
            # plot_cube(current_cube, itr = n)
            cost = calculate_obj(current_cube, desired_cube)
            cost_list.append(cost)
            
        
        if (calculate_obj(current_cube, desired_cube) == 0) or (n >= nMax):
            loop = False

    if plot_cost:
        iteration_cost(cost_list,n)
        
             
def cube_solve_algorithm_random(initial_cube, desired_cube, nMax, plot_cost = False):
    """This solver implements random moves if solution has stagnated"""
    
    n = 1 # number of iterations
    loop = True # while loop condition
    current_cube = initial_cube
    previous_cube = initial_cube
    plot_cube(current_cube, itr = n)
    
    cost = calculate_obj(current_cube, desired_cube)
    cost_list = [cost] 
    stagnation = 0
    
    while loop:
        
        if (stagnation > 5):
            current_cube, _ = scramble_cube(current_cube, scramble_length=20)
        
        #Solving Planning Problem
        moveset = solve_planning_prob_3(current_cube, desired_cube, previous_cube)
        previous_cube = current_cube
        previous_cost = cost
        
        #Performing Planning Problem Moves
        for i in range(len(moveset)):
            n+=1
            current_cube = cube_operations[moveset[i]](current_cube)
            cost = calculate_obj(current_cube, desired_cube)
            plot_cube(current_cube, itr = cost)
            cost_list.append(cost) 
        # Check for convergence or timeout 
        current_cube = solve_local_min(current_cube, desired_cube)
        
        if (cost == 0) or (n >= nMax):
            loop = False
        
        if (cost >= previous_cost):
            stagnation += 1
        else:
            stagnation = 0
        

    if plot_cost:
        iteration_cost(cost_list,n)
        
def bi_directional_search(initial_cube, desired_cube, nMax, plot_cost = False):

    #initialising the beginning and end cube positions
    forward_cube = initial_cube
    previous_forward_cube = initial_cube
    back_cube = desired_cube
    previous_back_cube = desired_cube
    n = 0
    

    loop = True
    while(loop):

    #forward search
        #calculate forward move set from planning problem
        moveset_forward = solve_planning_prob_5(forward_cube, back_cube, cube_previous=previous_forward_cube)
        previous_forward_cube = forward_cube

        for i in range(len(moveset_forward)):
            n+=1
            forward_cube = cube_operations[moveset_forward[i]](forward_cube)
            plot_cube(forward_cube, itr = n)

        print(f"Moveset Forward: {moveset_forward}, Cost Function between forward & back: {calculate_obj(forward_cube, back_cube)}")
    #back search

        #calculate back move set from planning problem
        moveset_back = solve_planning_prob_5(back_cube, forward_cube, cube_previous = previous_back_cube)
        previous_back_cube = back_cube

        for i in range(len(moveset_back)):
            n+=1
            back_cube = cube_operations[moveset_back[i]](back_cube)
            plot_cube(back_cube, itr = n)

        print(f"Moveset Back {moveset_back}, Cost Function between forward & back: {calculate_obj(forward_cube, back_cube)}")

        if (calculate_obj(forward_cube, back_cube) == 0):
            print("Pathway Found!")
            loop = False
        
        if (n >= nMax):
            print(f"Reached nMax = {n}")
            loop = False


def bi_directional_search_random(initial_cube, desired_cube, nMax, plot_cost = False):

    #initialising the beginning and end cube positions
    forward_cube = initial_cube
    previous_forward_cube = initial_cube
    back_cube = desired_cube
    previous_back_cube = desired_cube
    n = 0
    stagnation = 0
    
    forward_moves = np.array([])
    reverse_moves = np.array([])


    loop = True
    while(loop):

    #forward search
        #calculate forward move set from planning problem
        moveset_forward = solve_planning_prob_4(forward_cube, back_cube, cube_previous=previous_forward_cube)
        forward_moves = np.append(forward_moves, moveset_forward)
        previous_forward_cube = forward_cube

        for i in range(len(moveset_forward)):
            n+=1
            forward_cube = cube_operations[moveset_forward[i]](forward_cube)
            plot_cube(forward_cube, itr = n)

        print(f"Moveset Forward: {moveset_forward}, Cost Function between forward & back: {calculate_obj(forward_cube, back_cube)}")
    #back search

        
        if (stagnation > 2):
            stagnation = 0
            print("lets mix things up!")
            __, moveset_back = scramble_cube(back_cube, scramble_length = 8)
            reverse_moves = np.append(reverse_moves, moveset_back)
            previous_back_cube = back_cube
            for i in range(len(moveset_back)):
                n+=1
                back_cube = cube_operations[moveset_back[i]](back_cube)
                plot_cube(back_cube, itr = n)

        #calculate back move set from planning problem
        moveset_back = solve_planning_prob_4(back_cube, forward_cube, cube_previous = previous_back_cube)
        reverse_moves = np.append(reverse_moves, moveset_back)
        previous_back_cube = back_cube

        for i in range(len(moveset_back)):
            n+=1
            back_cube = cube_operations[moveset_back[i]](back_cube)
            plot_cube(back_cube, itr = n)

        print(f"Moveset Back {moveset_back}, Cost Function between forward & back: {calculate_obj(forward_cube, back_cube)}")


        stagnation += 1


        if (calculate_obj(forward_cube, back_cube) == 0):
            print("Pathway Found!")
            loop = False
        
        if (n >= nMax):
            print(f"Reached nMax = {n}")
            loop = False

    moveset = np.append(forward_moves, return_inverted_operations(reverse_moves))

    print(f"The full moveset for solving the cube: {moveset}")
        





#----------------------------------------------------------------------------#
# Main Function
#----------------------------------------------------------------------------#




def main():
    

    cube_mixed_4 = [17,10,16,12,8,20,6,19,22,18,21,14,15,13,2,1,7,24,3,23,9,5,11,4] # solvable



    bi_directional_search_random(cube_mixed_3, cube_solved, 10000)

main()