class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    :param params: a 2D list or tuple containing the parameters for the compartments, with the first list/tuple being
    the central compartment and the rest being the peripherals
    """

    def __init__(self, params):
        self.central = Compartment(params[0], type='central') # make central compartment
        self.peripherals = []
        for p in params[1:]: # make peripheral compartments and store in a list
            self.peripherals.append(Compartment(p, type='peripheral'))


class Compartment:
    """A compartment model

    Parameters
    ----------

    :param volume: float, specifies the volume of the compartment
    :param rate: float, speicifies the clearance rate if a central compartment, otherwise the transition rate
    :param type: str, either central or peripheral
    """

    def __init__(self, params, type):
        self.rate = float(params[0])
        self.volume = float(params[1])
        self.type = str(type)