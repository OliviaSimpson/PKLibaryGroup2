#
# Solution class
#
import numpy as np
import scipy.integrate


class Solution:
    """Module that solves the Pharmokinetic differential equation model
    taking parameters passed to it from other scripts in the package

    Parameters
    ----------

    model: object, specifying the model to be used and the parameters for the
            central and any peripheral compartments
    protocol: object, specifies the dosing protocol used in the model
    timescale: list, specifies the timescale to solve the model for.

    """

    def __init__(self, model, protocol, timescale):
        self.model = model
        self.protocol = protocol
        self.timescale = timescale
        if type(self.timescale) != list:
            raise ValueError('Timescale must be a list')

    def rhs(self, y, t):
        v_ps = self.model.v_ps
        Q_ps = self.model.Q_ps
        v_c = self.model.v_c
        cl = self.model.cl
        transitions = []  # store the transitions

        if self.model.k_a == 0.0:
            dqc_dt = self.protocol.dose() - y[0] / v_c * cl  # define central compartment term
            for vi, Qi, i in v_ps, Q_ps, range(len(v_ps)):  # make a term for each peripheral
                transitions.append(Qi * (y[0] / v_c - y[i] / vi))
            for tr in transitions:
                dqc_dt -= tr # subtract the peripherals from the s.c. central compartment
            return transitions.insert(0, dqc_dt)

        else:
            dqp0_dt = self.protocol.dose() - self.model.k_a * y[1] # define subcutaneous term
            for vi, Qi, i in v_ps, Q_ps, range(len(v_ps)):  # make a term for each peripheral
                transitions.append(Qi * (y[0] / v_c - y[i + 1] / vi))
            dqc_dt = self.model.k_a * y[1] - y[0] / v_c * cl # define central compartment term
            for tr in transitions:
                dqc_dt -= tr  # subtract the peripherals from the s.c. central compartment
            transitions.insert(0, dqp0_dt)
            return transitions.insert(0, dqc_dt)

    def sol(self):
        if self.model.k_a == 0.0:
            y0 = np.zeros(len(self.model.v_ps) + 1)
        else:
            y0 = np.zeros(len(self.model.v_ps) + 2)
        t_eval = np.linspace(0,1,1000)
        sol = scipy.integrate.solve_ivp(
            fun=lambda y, t: self.rhs(y, t),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )
        return [sol.t, sol.y]