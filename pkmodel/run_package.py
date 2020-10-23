import numpy as np
import matplotlib.pylab as plt
import scipy.integrate

from PKLibaryGroup2.pkmodel.model import Model
from PKLibaryGroup2.pkmodel.solve import Solution
from PKLibaryGroup2.pkmodel.protocol import Protocol

model = Model([[0, 1], [2, 4], [3, 5]],k_a=0)
protocol = Protocol(3, 4)
solution = Solution(model, protocol, [0, 1, 1000])

plt.plot(solution.sol()[0], solution.sol[1], label=model['name'] + '- q_c')
