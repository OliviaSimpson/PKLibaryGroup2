#
# Protocol class
#
import math
import numpy as np

class Protocol:
    """A class to describe the dosing protocol and method of administration for the pharmacokinetic model.

    Parameters
    :param d_g: the total quantity of drug to be administered over the entire protocol (ng)
    :type d_g: float
    :param plan: the duration of infusion (if continuous); the timings of each dose (if discrete)
    :type plan: list or tuple (if continuous); int or float (if discrete)
    """
    
    def __init__(self, d_g, plan):
        self.d_g = d_g
        self.plan = plan

    def dose(self):
        if isinstance(self.plan, list) or isinstance(self.plan, tuple): # discrete administration
            n_dose = len(self.plan)

            sig = 1 / ((self.d_g / n_dose) * math.sqrt(2 * math.pi))

            gaussian = sum((1 / sig * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((t - dose_time) ** 2 / (sig ** 2))for dose_time in self.plan)
            
            return gaussian

        elif isinstance(self.plan, int) or isinstance(self.plan, float): # continuous administration
            return self.d_g / self.plan

        else:
            raise TypeError('incorrect input format')

protocol = Protocol(5, [1,2,3])


        

