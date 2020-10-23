#
# Protocol class
#

class Protocol:
    """A class to describe the dosing protocol and method of administration for the pharmacokinetic model.

    Parameters
    :param d_g: the total quantity of drug to be administered over the entire protocol (ng)
    :type d_g: float
    :param dur: the total duration of continuous infusion (hr)
    :type dur: float
    :param n_dose: the number of doses to be administered in a discrete bolus protocol
    :type n_dose: int
    :param method: the method of administration (intravenous or subcutaneous)
    :type method: string
    """
    
    def __init__(self, d_g, dur, plan, method):
        self.d_g = d_g # total quantity of drug
        self.dur = dur # continuous: duration of infusion
        self.n_dose = n_dose # discrete: number of repeated doses
        self.method = method # method of administration

    def continuous(self):
        return self.d_g / self.dur

    def discrete(self):
        a = self.n_dose / (self.d_g * math.sqrt(math.pi))
        return (1 / (a * math.sqrt(math.pi))) * math.exp(-(t / a) ** 2)












































