# """
# https://matplotlib.org/users/pyplot_tutorial.html
# """
# import matplotlib.pyplot as plt
#
# # line
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# # point
# # plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'yo')
# plt.scatter([1, 2, 3, 4], [1, 4, 9, 16])
# # other
# plt.ylabel('some numbers')
# plt.axis([0, 6, 0, 20])
# plt.show()

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()