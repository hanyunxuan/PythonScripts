"""
author:hanyunxuan
date:2018.4.21
version:python27

matlab code:
function sum_AB = get_sum(a,b)
    sum_AB = double(a + b);
end

https://blog.csdn.net/houchaoqun_xmu/article/details/53948647?readlog
"""


from mlab.releases import latest_release as matlab
from numpy import mat, array

matlab.path(matlab.path(), r'E:/Algorithm')



a = int(1)
b = int(2)
c = array([[1, 1], [1, 1]])
array([[1,2], [1,3]])
d = array([[2, 2], [2, 2]])
result = matlab.get_sum(c, d)
print result


