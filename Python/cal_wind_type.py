def cal_wind_type():

    # WindSpeed need to be m/s unit and must be positive number
    windSpeed = 3.05556
    # WindDirection (N, NE, E, SE, S, SW, W, NW) Example NE:North-East
    windDirection = "NE"
    # Default WindType
    windType = ""

    # Calculate the type of wind by this solution
    if (windSpeed < 2):
        windType = "A"
    elif (windSpeed >= 2 and windSpeed < 3):
        windType = "B"
    elif (windSpeed >= 3 and windSpeed < 5):
        windType = "C"
    elif (windSpeed >= 5 and windSpeed < 6):
        windType = "D"
    else:
        windType = "E"
    
    return (windType, windDirection)