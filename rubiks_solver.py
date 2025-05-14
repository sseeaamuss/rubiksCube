
"""
This is my rubik's cube software for Engineering Optimisation ENEL445
This project will build upon a 2*2*2 rubik's cube and work up to a 3*3*3 cube 
if successful 

"""
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

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

#----------------------------------------------------------------------------#
# Cube plotting
#----------------------------------------------------------------------------#



def plot_cube(cube, itr=None):
    """This function plots the 2d unfolded layout of the 2*2*2 cube"""
    fig, ax = plt.subplots()
    
    for i in range(len(cube)):
        rectangle = patches.Rectangle((cube_x_pos[i] + 2, cube_y_pos[i]), 1, 1, linewidth=1, edgecolor='black', facecolor= color_map_2[cube[i]])
        ax.add_patch(rectangle)
        plt.annotate(str(cube[i]), xy=(cube_x_pos[i] + 2.25,cube_y_pos[i]+ 0.5), xytext=(cube_x_pos[i] + 2.25,cube_y_pos[i] + 0.5))
    
    # Set axis limits for better visualization
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    
    plt.annotate('Top', xy=(4, 8.5), xytext=(4.5, 8.5))
    plt.annotate('Left', xy=(2, 6.5), xytext=(2.5, 6.5))
    plt.annotate('Front', xy=(6, 4), xytext=(6.5, 3), arrowprops=dict(facecolor='red', arrowstyle='->'))
    plt.annotate('Right', xy=(4, 9), xytext=(6.5, 6.5))
    plt.annotate('Bottom', xy=(4, 9), xytext=(2.5, 3))
    plt.annotate('Back', xy=(4, 9), xytext=(2.5, 1))
    plt.annotate(itr, xy=(1,1), xytext=(1,1))
    
    plt.tick_params(axis='x', labelbottom=False)  # Remove x-axis values
    plt.tick_params(axis='y', labelleft=False)    # Remove y-axis values
    
    # Show the plot
    plt.show()


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
topCCW = lambda cube: TOP_CW @ TOP_CW @ TOP_CW @ cube

leftCW = lambda cube: LEFT_CW @ cube
leftFT = lambda cube: LEFT_CW @ LEFT_CW @ cube
leftCCW = lambda cube: LEFT_CW @ LEFT_CW @ LEFT_CW @ cube

frontCW = lambda cube: FRONT_CW @ cube
frontFT = lambda cube: FRONT_CW @ FRONT_CW @ cube
frontCCW = lambda cube: FRONT_CW @ FRONT_CW @ FRONT_CW @ cube

rightCW = lambda cube: RIGHT_CW @ cube
rightFT = lambda cube: RIGHT_CW @ RIGHT_CW @ cube
rightCCW = lambda cube: RIGHT_CW @ RIGHT_CW @ RIGHT_CW @ cube

bottomCW = lambda cube: BOTTOM_CW @ cube
bottomFT = lambda cube: BOTTOM_CW @ BOTTOM_CW @ cube
bottomCCW = lambda cube: BOTTOM_CW @ BOTTOM_CW @ BOTTOM_CW @ cube

backCW = lambda cube: BACK_CW @ cube
backFT = lambda cube: BACK_CW @ BACK_CW @ cube
backCCW = lambda cube: BACK_CW @ BACK_CW @ BACK_CW @ cube

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
    
    
    print()
    print("minimum cost after 3 moves:",min_value)
    print("optimal moves", moveset)
    print("moveset", operations_str)
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
    
    
    print()
    print("minimum cost after 3 moves:",min_value)
    print("optimal moves", moveset)
    print("moveset", operations_str)
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
    
    print()
    print("minimum cost after 5 moves:",min_value)
    print("optimal moves", moveset)
    print("moveset", operations_str)
    # print("inverted moveset", reverse_operations)
    
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
        moveset = solve_planning_prob_3(current_cube, desired_cube, previous_cube)
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
        
        if (stagnation > 3):
            current_cube, _ = scramble_cube(current_cube, scramble_length=20)
        
        #Solving Planning Problem
        moveset = solve_planning_prob_3(current_cube, desired_cube, previous_cube)
        previous_cube = current_cube
        previous_cost = cost
        
        #Performing Planning Problem Moves
        for i in range(len(moveset)):
            n+=1
            current_cube = cube_operations[moveset[i]](current_cube)
            plot_cube(current_cube, itr = n)
            cost = calculate_obj(current_cube, desired_cube)
            cost_list.append(cost) 
        # Check for convergence or timeout        
        if (cost == 0) or (n >= nMax):
            loop = False
        
        if (cost >= previous_cost):
            stagnation += 1
        else:
            stagnation = 0
        

    if plot_cost:
        iteration_cost(cost_list,n)
       
        

#----------------------------------------------------------------------------#
# Main Function
#----------------------------------------------------------------------------#

cube_mixed_1 = np.array([22, 18, 10, 11, 20, 13, 9, 24, 4, 8, 14, 5, 17, 15, 23, 7, 2, 1, 6, 21, 3, 19, 16, 12])
# has scramble sequence ['bottomCW', 'backCW', 'backFT', 'backFT', 'leftCCW', 'frontCCW', 
#                        'topCW', 'leftFT', 'bottomCCW', 'bottomCCW', 'rightFT', 'leftCW', 
#                        'frontFT', 'leftCW', 'rightFT', 'bottomCCW', 'leftCCW', 'leftCW', 
#                        'rightCW', 'frontFT']

cube_mixed_2 = np.array([15, 5, 20, 8, 18, 22, 24, 13, 16, 17, 10, 9, 11, 1, 6, 21, 4, 3, 14, 19, 2, 7, 12, 23])


cube_mixed_3 = np.array([1,8,3,4,5,6,7,2,9,10,24,12,13,17,15,16,14,18,19,20,21,22,23,11])


solved_cube = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]) # desired cube solution
    




def main():
    

    cube_solve_algorithm_random(cube_mixed_3, solved_cube, 300, plot_cost = True)
        


main()