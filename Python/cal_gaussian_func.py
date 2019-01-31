from cal_sigma import cal_sigma
import numpy as np

def cal_gaussian_func(x, y, z, Q, u, sigma_z, sigma_y, h):
    solution_1 = Q/(2 * np.pi * u * sigma_y * sigma_z)
    exp_1 = np.exp(((-1) * (z - h)**2) / (2 * (sigma_z**2)))
    exp_2 = np.exp(((-1) * (z + h)**2) / (2 * (sigma_z**2)))
    exp_3 = np.exp((-1) * (y**2) / (2 * (sigma_y**2)))

    result = solution_1 * (exp_1 + exp_2) * exp_3

    formatted = '{0:.10f}'.format(result)
    print(formatted)

cal_gaussian_func(500, 0, 0, 10, 6, 18.3, 36.1, 50)
    