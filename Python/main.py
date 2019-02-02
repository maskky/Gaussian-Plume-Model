from cal_wind_type import cal_wind_type
from cal_sigma import cal_sigma
from cal_position_map import cal_position_map
def main(windDirection, distance, la, lg, Q, u, h):

    # You need to understand the "Gaussian plume function" before read this project
    # Source : http://courses.washington.edu/cewa567/Plumes.PDF
    
    # ------------ Variable Description ------------
    # Q = Mass emission rate
    # u = Wind speed evaluated at “effective” release height
    # h = “Effective” stack height, including rise of the hot plume near the source
    # windDirection = Direction of wind, examples N(Nort), E(East)

    windType = cal_wind_type(u)
    
    sigma = cal_sigma(windType, distance)
    sigma_z = sigma[0]
    sigma_y = sigma[1]

    position = cal_position_map(la, lg, windDirection, sigma_z, sigma_y, distance, Q, u, h)
    print(position)
main("E", 100, 13.729960, 100.778602, 10, 6, 50)