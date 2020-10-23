#
# Protocol class
#
import math

class Protocol2:
    """A class to describe the dosing protocol and method of administration for the pharmacokinetic model.

    Parameters
    :param d_g: the total quantity of drug to be administered over the entire protocol (ng)
    :type d_g: float
    :param dur: the total duration of continuous infusion (hr)
    :type dur: float
    :param dose_times: the timing of administration of each bolus dose (hr)
    :type dose_times: tuple
    """
    
    def __init__(self, d_g, dur=0, dose_times=None):
        self.d_g = d_g # total quantity of drug
        self.dur = dur # continuous: duration of infusion
        self.dose_times = dose_times # discrete: number of repeated doses - tuple
        # assumes that the dose of drug with each discrete bolus is equal

    def continuous(self):
        if self.dur == 0:
            raise ValueError('continuous dose must have a duration')
        else:
            return self.d_g / self.dur

    def discrete(self):
        if self.dose_times == None:
            return 0

        else:
            n_dose = len(self.dose_times)
            gaussians = []
            a = n_dose / (self.d_g * math.sqrt(math.pi))
            for time in self.dose_times:
                gaussian = (1 / (a * math.sqrt(math.pi))) * math.exp(-(time / a) ** 2)
                gaussians.append(gaussian)
            return gaussians

    def dose(self, t):
        if self.discrete != 0:
            return self.discrete
        else:
            return self.continous

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