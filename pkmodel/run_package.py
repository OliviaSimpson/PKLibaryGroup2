import numpy as np
import matplotlib.pylab as ply
import scipy.integrate

from PKLibaryGroup2.pkmodel.model import Model
from PKLibaryGroup2.pkmodel.solve_arbitrary import Solution

class Protocol:
    def __init__(self):

    def dose(self, t, X):


model = Model([[0,1], [2,4], [3,5]])
solution = Solution(model,)