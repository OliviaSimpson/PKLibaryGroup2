class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    :param params: A 2D list containing the parameters for the compartments, with the first list being
    the central compartment and the rest being the peripherals. Must be specified in the order [rate, volume].
    :type params: list
    :param k_a": If modelling subcutaneous dosing this is the absorption rate
    :type k_a: float, optional
    """

    def __init__(self, params, k_a=0):
        # check that input is suitable
        if not any(isinstance(i, list) for i in params):
            raise TypeError('input must be supplied as a 2D list')
        for p in params:
            if len(p) != 2:
                raise ValueError('incorrect number of parameters provided')

        # make central compartment
        self.central = Compartment(params[0], type='central')  # make central compartment
        self.cl = self.central.rate
        self.v_c = self.central.volume

        # make peripherals
        self.peripherals = []
        self.Q_ps = []  # store the Q_p values for each peripheral
        self.v_ps = []  # store the v_p values for each peripheral
        for p in params[1:]:  # make peripheral compartments and store in a list
            peripheral = Compartment(p, type='peripheral')
            self.peripherals.append(peripheral)
            self.Q_ps.append(peripheral.rate)
            self.v_ps.append(peripheral.volume)
        self.k_a = k_a  # absorption rate for subcutaneous dosing (defaults to 0)


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


model = Model([[0, 1]])
print(model.v_c)

v_ps = [1,2,3]
q_ps = [4,5,6]

def make_equation(v_ps, q_ps):
    peris = []
    for vi, qi in v_ps, q_ps:
        peris.append(qi * ())

def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    transitions = [] # store the transitions
    for vi, qi, i in v_ps, q_ps, range(len(v_ps)):
        transitions.append(qi * (y[0] / V_c - y[i] / vi))
    dqc_dt = dose(t, X) - q_c / V_c * CL
    for t in transitions:
        dqc_dt -= t
    return transitions.insert(0, dqc_dt)


