from cal_gaussian_func import cal_gaussian_func
from cal_sigma import cal_sigma
import json

def cal_position_map(la, lg, windDirection, sigma_z, sigma_y, distance, Q, u, h):
    position = []

    gaussian = getGaussian(distance, Q, u, h, sigma_z, sigma_y)

    if (windDirection == "N"):
        plot_list = north(distance) 
    if (windDirection == "NE"):
        plot_list = north_east(distance) 
    if (windDirection == "E"):
        plot_list = east(distance) 
    if (windDirection == "SE"):
        plot_list = south_east(distance) 
    if (windDirection == "S"):
        plot_list = south(distance) 
    if (windDirection == "SW"):
        plot_list = south_west(distance)
    if (windDirection == "W"):
        plot_list = west(distance) 
    if (windDirection == "NW"):
        plot_list = north_west(distance) 

    for i in range(len(plot_list)):
        buffer = la + (plot_list[i][1]/111111), lg + (plot_list[i][0]/111111), gaussian[i]
        position.append(buffer)

    return position

def getGaussian(distance, Q, u, h, sigma_z, sigma_y):
        gassian = []
        for i in range(distance):
                for j in range(i+1):
                        gassian.append(cal_gaussian_func(i, j, Q, u, sigma_z, sigma_y, h))
                        if not (j == 0):
                                gassian.append(cal_gaussian_func(i, -j, Q, u, sigma_z, sigma_y, h))
        return gassian

def east(distance):
        alist = []
        for i in range(distance):
                for j in range(i + 1):
                        buffer = i, j
                        buffer_2 = i, -j
                        alist.append(buffer)
                        if not (j == 0):
                                alist.append(buffer_2)
        return alist

def north_east(distance):
        alist = []
        for i in range(distance):
                for j in range(distance):
                        buffer = i, j
                        alist.append(buffer)
        return alist

def north(distance):
        alist = []
        for i in range(distance):
                for j in range(i + 1):
                        buffer = j, i
                        buffer_2 = -j, i
                        alist.append(buffer)
                        if not (j == 0):
                                alist.append(buffer_2)
        return alist

def north_west(distance):
        alist = []
        for i in range(distance):
                for j in range(distance):
                        buffer = -i, j
                        alist.append(buffer)
        return alist

def west(distance):
        alist = []
        for i in range(distance):
                for j in range(i + 1):
                        buffer = -i, j
                        buffer_2 = -i, -j
                        alist.append(buffer)
                        if not (j == 0):
                                alist.append(buffer_2)
        return alist

def south_west(distance):
        alist = []
        for i in range(distance):
                for j in range(distance):
                        buffer = -i, -j
                        alist.append(buffer)
        return alist

def south(distance):
        alist = []
        for i in range(distance):
                for j in range(i + 1):
                        buffer = j, -i
                        buffer_2 = -j, -i
                        alist.append(buffer)
                        if not (j == 0):
                                alist.append(buffer_2)
        return alist

def south_east(distance):
        alist = []
        for i in range(distance):
                for j in range(distance):
                        buffer = i, -j
                        alist.append(buffer)
        return alist
    
# cal_position_map(13.729960, 100.778602, cal_sigma("D", 0.5)[0], cal_sigma("D", 0.5)[1])