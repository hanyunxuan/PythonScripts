"""
https://matplotlib.org/users/pyplot_tutorial.html
"""
import matplotlib.pyplot as plt
# line
plt.plot([1,2,3,4], [1,4,9,16])
# point
plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'yo')

# other
plt.ylabel('some numbers')
plt.axis([0, 6, 0, 20])
plt.show()