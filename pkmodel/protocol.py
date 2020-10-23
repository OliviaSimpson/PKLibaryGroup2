#
# Protocol class
#
import math

class Protocol:
    """A class to describe the dosing protocol and method of administration for the pharmacokinetic model.

    Parameters
    :param d_g: the total quantity of drug to be administered over the entire protocol (ng)
    :type d_g: float
    :param dur: the total duration of continuous infusion (hr)
    :type dur: float
    :param dose_times: the timing of administration of each bolus dose (hr)
    :type dose_times: tuple
    """
    def __init__(self, d_g, plan):
        self.d_g = d_g
        self.plan = plan

    def dose(self):
        if isinstance(self.plan,list) or isinstance(self.plan, tuple): # discrete administration
            n_dose = len(self.plan)
            gaussians = []
            a = n_dose / (self.d_g * math.sqrt(math.pi))
            for time in self.plan:
                gaussian = (1 / (a * math.sqrt(math.pi))) * math.exp(-(time / a) ** 2)
                gaussians.append(gaussian)
            return gaussians

        elif isinstance(self.plan, int) or isinstance(self.plan, float): # continuous administration
            return self.d_g / self.plan

        else:
            raise TypeError('incorrect input format')


protocol = Protocol(3,[3,4])
print(protocol.dose())