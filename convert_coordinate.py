from math import *


def deg_min_sec(degrees=0.0):
    if type(degrees) != 'float':
        try:
            degrees = float(degrees)
        except:
            print('\nERROR: Could not convert %s to float.' % (type(degrees)))
            return 0
    minutes = degrees % 1.0 * 60
    seconds = minutes % 1.0 * 60

    # return '\n%s°%s\'%s"\n' % (int(floor(degrees)), int(floor(minutes)), seconds)
    return int(floor(degrees)) * 10000 + int(floor(minutes)) * 100 + int(floor(seconds))

# def convert(longitude,latitude):
#     # if longitude>=1000: # degree minute second to degree
#     #
#     # else:
#         longitude_convert=deg_min_sec(longitude)
#         latitude_convert = deg_min_sec(latitude)
#     return longitude_convert,latitude_convert

