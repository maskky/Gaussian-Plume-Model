from cal_wind_type import cal_wind_type
from cal_sigma import cal_sigma
from cal_position_map import cal_position_map
def main(windDirection, distance, la, lg, Q, u, h):

    position = cal_position_map(la, lg, windDirection, distance, Q, u, h)
main(47.26369829, 1000, 13.729960, 100.778602, 40, 1.5, 20)