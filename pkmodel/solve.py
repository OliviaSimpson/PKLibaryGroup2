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
        self.q_c = None
        self.q_p = None
        if type(self.timescale) != list:
             print('Timescale must be a list')
             
        
        if self.protocol.type == 'intravenous':
            if self.protocol.method == 'discrete':
                self.y0 = np.array([self.protocol.d_g, 0.0])
    #This sets up the initial conditions for the ODE such that the amount of drug 
    #in the central compartment at t=0 is the first dose
    
    def rhs(self, y):
        self.q_c, self.q_p1 = y
        transition = self.model.Q_p1 * (self.q_c / self.model.v_c - self.q_p1 / self.model.v_p1)           #determines the transition rate (in ng/h)
        dqc_dt = - self.q_c / self.model.v_c * self.model.cl - transition       #Rate of change of qc (in ng/h)
        dqp1_dt = transition                                    #Rate of change of qp1 (in ng/h) aka the quantity of drug in peripheral compartment
        return [dqc_dt, dqp1_dt]
    
    def sol(self):
        t_eval = np.linspace(self.timescale)
        scipy.integrate.solve_ivp(
            fun=lambda y: self.rhs(y),
            t_span=[t_eval[0], t_eval[-1]],
            y0=self.y0, t_eval=t_eval
            )
        return [sol.t, sol.y]
        
        

