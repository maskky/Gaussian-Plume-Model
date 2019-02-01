from cal_wind_type import cal_wind_type
from cal_sigma import cal_sigma
from cal_position_map import cal_position_map
def main(windSpeed, windDirection, distance, la, lg, Q, u, h):
    windType = cal_wind_type(windSpeed)
    print("WindType :", windType)
    
    sigma = cal_sigma(windType, distance)
    sigma_z = sigma[0]
    sigma_y = sigma[1]

    position = cal_position_map(la, lg, windDirection, sigma_z, sigma_y, distance, Q, u, h)

main(6, "E", 500, 13.729960, 100.778602, 10, 6, 50)