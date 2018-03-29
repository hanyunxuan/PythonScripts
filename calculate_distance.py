"""
input:longitude1,latitude1,longitude2,latitude2
output:distance
"""
import numpy

def calculate(longitude1,latitude1,longitude2,latitude2):
    distance=numpy.sqrt(numpy.square(abs(longitude1-longitude2))+numpy.square(abs(latitude1-latitude2)))
    return distance

if __name__ == '__main__':
    longitude1=0
    latitude1=-3
    longitude2=-4
    latitude2=0
    distance=calculate(longitude1, latitude1, longitude2, latitude2)