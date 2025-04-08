# -*- coding: utf-8 -*-
"""
This is my rubik's cube software for Engineering Optimisation ENEL445
This project will build upon a 2*2*2 rubik's cube and work up to a 3*3*3 cube 
if successful 

"""

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as patches

cube = np.array([1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6])
cube_x_pos = [2,3,2,3,0,1,0,1,2,3,2,3,4,5,4,5,2,3,2,3,2,3,2,3]
cube_y_pos = [7,7,6,6,5,5,4,4,5,5,4,4,5,5,4,4,3,3,2,2,1,1,0,0]

color_map = {
    1: 'yellow',
    2: 'blue',
    3: 'red',
    4: 'green',
    5: 'white',
    6: 'orange'
}


def plot_cube(cube):
    """This function plots the 2d unfolded layout of the 2*2*2 cube"""
    fig, ax = plt.subplots()
    
    for i in range(len(cube)):
        rectangle = patches.Rectangle((cube_x_pos[i], cube_y_pos[i]), 1, 1, linewidth=1, edgecolor='black', facecolor= color_map[cube[i]])
        ax.add_patch(rectangle)
    
    # Set axis limits for better visualization
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    
    # Show the plot
    plt.show()
    

plot_cube(cube)