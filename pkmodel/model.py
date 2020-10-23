class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    :param params: A 2D list or tuple containing the parameters for the compartments, with the first list/tuple being
    the central compartment and the rest being the peripherals
    :type params: list or tuple
    """

    def __init__(self, params):
        # check that input is suitable
        if len(params) < 2:
            raise ValueError('not enough compartments specified')
        for p in params:
            if len(p) != 2:
                raise ValueError('incorrect number of parameters provided')

        # make the model
        self.central = Compartment(params[0], type='central')  # make central compartment
        self.peripherals = []
        for p in params[1:]:  # make peripheral compartments and store in a list
            self.peripherals.append(Compartment(p, type='peripheral'))


class Compartment:
    """A compartment model

    Parameters
    ----------

    :param volume: Specifies the volume of the compartment
    :type volume: float
    :param rate: Speicifies the clearance rate if a central compartment, otherwise the transition rate
    :type rate: float
    :param type: The type of compartment, either central or peripheral
    :type type: str
    """

    def __init__(self, params, type):
        self.rate = float(params[0])
        self.volume = float(params[1])
        self.type = str(type)


model = Model([[0, 1], [2, 4], [3, 5]])
print(model.central)
