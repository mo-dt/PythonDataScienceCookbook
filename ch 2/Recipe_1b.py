import numpy as np


# Creating matrices
from Display_Shape import display_shape

a_listoflist = [[1,2,3],[5,6,7],[8,9,10]]
a_matrix = np.matrix(a_listoflist,dtype=float)
display_shape(a_matrix)
