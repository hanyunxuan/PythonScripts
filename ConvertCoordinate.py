from math import *


def deg2deg_min_sec(input_number=0.0):
    if type(input_number) != 'float':
        try:
            input_number = float(input_number)
        except:
            print('\nERROR: Could not convert %s to float.' % (type(input_number)))
            return 0
    minutes = input_number % 1.0 * 60
    seconds = minutes % 1.0 * 60

    # return '\n%s°%s\'%s"\n' % (int(floor(input_number)), int(floor(minutes)), seconds)
    output_number=int(floor(input_number)) * 10000 + int(floor(minutes)) * 100 + int(floor(seconds))
    return output_number

def deg_min_sec2deg(input_number=0):
    if type(input_number) != 'int':
        try:
            input_number = int(input_number)
        except:
            print('\nERROR: Could not convert %s to int.' % (type(input_number)))
            return 0
    tem = str(input_number)
    second = int(tem[-2] + tem[-1])
    minute = int(tem[-4] + tem[-3])
    degress = int(tem[:-4])
    output_number = degress + minute / 60 + second / 3600
    return output_number
