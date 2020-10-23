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

    :param model: Specifying the model to be used and the parameters for the central and any peripheral compartments
    :type model: Model object
    :param protocol: Specifies the dosing protocol used in the model
    :type protocol: Protocol object
    :param timescale: Specifies the timescale to solve the model for in the format [start, stop, increment]
    :type timescale: list
    """

    def __init__(self, model, protocol, timescale):
        self.model = model
        self.protocol = protocol
        self.timescale = timescale
        if type(self.timescale) != list:
            raise ValueError('Timescale must be a list')

    def rhs(self, t, y):
        """Calculates the Right Hand Side of the equation for the numerical solution of the model. Accommodates an
        arbitrary number of peripheral compartments (transitions) by storing them as a list.

        :param v_ps: A list of the volumes for the peripheral compartments
        :type v_ps: list of floats
        :param Q_ps: A list of the Q_pi values (the transition rates between the given peripheral compartments and the
        central compartment
        :type Q_ps: list of floats
        :param v_c: The volume of the central compartment
        :type v_c: Float
        :param cl: The clearance rate from the central compartment
        :type cl: Float
        """
        v_ps = self.model.v_ps
        Q_ps = self.model.Q_ps
        v_c = self.model.v_c
        cl = self.model.cl
        transitions = []  # store the transitions

        if self.model.k_a == 0.0:
            dqc_dt = self.protocol.dose() - y[0] / v_c * cl  # define central compartment term
            for i in range(len(v_ps)):  # make a term for each peripheral
                transitions.append(Q_ps[i] * (y[0] / v_c - y[i + 1] / v_ps[i]))
            for tr in transitions:
                dqc_dt -= tr  # subtract the peripherals from the s.c. central compartment
            return transitions.insert(0, dqc_dt)

        else:
            dqp0_dt = self.protocol.dose() - self.model.k_a * y[1]  # define subcutaneous term
            for i in range(len(v_ps)):  # make a term for each peripheral
                transitions.append(Q_ps[i] * (y[0] / v_c - y[i + 1] / v_ps[i]))
            dqc_dt = self.model.k_a * y[1] - y[0] / v_c * cl  # define central compartment term
            for tr in transitions:
                dqc_dt -= tr  # subtract the peripherals from the s.c. central compartment
            transitions.insert(0, dqp0_dt)
            return transitions.insert(0, dqc_dt)

    def sol(self):
        """Calculates a numerical solution for the specified model system given starting conditions, y0.
        """
        if self.model.k_a == 0.0:
            y0 = np.zeros(len(self.model.v_ps) + 1)
        else:
            y0 = np.zeros(len(self.model.v_ps) + 2)
        t_eval = np.linspace(0, 1, 1000)
        sol = scipy.integrate.solve_ivp(
            fun=lambda t, y: self.rhs(t, y),
            t_span=[t_eval[0], t_eval[-1]],
            y0=y0, t_eval=t_eval
        )
        return [sol.t, sol.y]
