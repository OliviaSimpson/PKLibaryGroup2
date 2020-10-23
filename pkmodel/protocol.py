#
# Protocol class
#

import math

class Protocol:
    """A class to describe the dosing protocol for the pharmacokinetic model.
    Creates a dose(t) function to be called in the Solution class.

    Parameters
    :param d_g: the total quantity of drug to be administered over the entire protocol (ng)
    :type d_g: float
    :param plan: the duration of infusion (if continuous); the timings of each dose (if discrete)
    :type plan: list or tuple (if continuous); int or float (if discrete)

    Raises
    :Type error: if the dosing plan is in an incorrect input format (i.e. not a list/tuple or int/float)
    """
    
    def __init__(self, d_g, plan):
        self.d_g = d_g
        self.plan = plan

    def discrete(self, t, dose_time):
        n_dose = len(self.plan)
        sig = 1 / ((self.d_g / n_dose) * math.sqrt(2 * math.pi))
        return (1 / sig * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((t - dose_time) ** 2 / (sig ** 2)))

    def dose(self, t):
        if isinstance(self.plan, list) or isinstance(self.plan, tuple):
            gaus = []
            for dose_time in self.plan:
                gaus.append(self.discrete(t, dose_time))
            return sum(gaus)

        elif isinstance(self.plan, int) or isinstance(self.plan, float):
            return self.d_g / self.plan

        else:
            raise TypeError('Incorrect input format')