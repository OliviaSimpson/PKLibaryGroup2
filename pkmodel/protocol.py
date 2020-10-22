#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    value: numeric, optional
        an example paramter

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












































