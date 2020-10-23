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
        self.q_p0 = None
        self.q_p1 = None
        self.q_p2 = None
        print(self.timescale)
        if type(self.timescale) != list:
             print('Timescale must be a list')
        
        
    #test to see if subcutaneous or intravenous
    def rhsetup(self):
        if self.model.k_a == 0.0:
            
            if len(self.model.peripherals) == 0:
                self.y0 = np.array([0.0])
                def rhs(self, y, t):               #Set up the right hand side of the ODE
                    self.q_c = y
                    dqc_dt = self.protocol.dose(t) - self.q_c / self.model.v_c * self.model.cl     #Rate of change of qc (in ng/h)
                    return [dqc_dt]
                
            elif len(self.model.peripherals) == 1:
                self.y0 = np.array([0.0,0.0])
                def rhs(self, y, t):               #Set up the right hand side of the ODE
                    self.q_c, self.q_p1 = y
                    transition = self.model.Q_ps[0] * (self.q_c / self.model.v_c - self.q_p1 / self.model.v_ps[0])           #determines the transition rate (in ng/h)
                    dqc_dt = self.protocol.dose(t) - self.q_c / self.model.v_c * self.model.cl - transition       #Rate of change of qc (in ng/h)
                    dqp1_dt = transition                                    #Rate of change of qp1 (in ng/h) aka the quantity of drug in peripheral compartment
                    return [dqc_dt, dqp1_dt]
                
            elif len(self.model.peripherals) == 2:
                self.y0 = np.array([0,0,0])
                print(self.y0)
                def rhs(self, y, t):               #Set up the right hand side of the ODE
                    self.q_c, self.q_p1, self.q_p2 = y
                    transition1 = self.model.Q_ps[0] * (self.q_c / self.model.v_c - self.q_p1 / self.model.v_ps[0])           #determines the transition rate (in ng/h)
                    transition2 = self.model.Q_ps[1] * (self.q_c/self.model.v_c - self.q_p2 / self.model.v_ps[1])
                    dqc_dt = self.protocol.dose(t) - self.q_c / self.model.v_c * self.model.cl - transition1 - transition2       #Rate of change of qc (in ng/h)
                    dqp1_dt = transition1                                     #Rate of change of qp1 (in ng/h) aka the quantity of drug in peripheral compartment
                    dqp2_dt = transition2
                    return [dqc_dt, dqp1_dt, dqp2_dt]
                
                
        elif self.model.k_a != 0:
            if len(self.model.peripherals) == 0:
                self.y0 = np.array([0.0, 0.0])
                def rhs(self, y, t):               #Set up the right hand side of the ODE
                    self.q_c, self.q_p0 = y
                    dqp0_dt = self.protocol.dose(t) - self.model.k_a * self.q_p0
                    dqc_dt = self.model.k_a * self.q_p0 - self.q_c / self.model.v_c * self.model.cl     #Rate of change of qc (in ng/h)
                    return [dqc_dt, dqp0_dt]
                
            elif len(self.model.peripherals) == 1:
                self.y0 = np.array([0.0, 0.0,  0.0])
                def rhs(self, y, t):               #Set up the right hand side of the ODE
                    self.q_c, self.q_p0, self.q_p1 = y
                    dqp0_dt = self.protocol.dose(t) - self.model.k_a * self.q_p0
                    transition = self.model.Q_ps[0] * (self.q_c / self.model.v_c - self.q_p1 / self.model.v_ps[0])           #determines the transition rate (in ng/h)
                    dqc_dt = self.model.k_a * self.q_p0 - self.q_c / self.model.v_c * self.model.cl - transition       #Rate of change of qc (in ng/h)
                    dqp1_dt = transition                                    #Rate of change of qp1 (in ng/h) aka the quantity of drug in peripheral compartment
                    return [dqc_dt, dqp0_dt, dqp1_dt]
                
            elif len(self.model.peripherals) == 2:
                self.y0 = np.array([0.0, 0.0, 0.0, 0.0])
                def rhs(self, y, t):               #Set up the right hand side of the ODE
                    self.q_c, self.q_p0, self.q_p1, self.q_p2 = y
                    dqp0_dt = self.protocol.dose(t) - self.model.k_a * self.q_p0
                    transition1 = self.model.Q_ps[0] * (self.q_c / self.model.v_c - self.q_p1 / self.model.v_ps[0])           #determines the transition rate (in ng/h)
                    transition2 = self.model.Q_ps[1] * (self.q_c/self.model.v_c - self.q_p2 / self.model.v_ps[1])
                    dqc_dt = self.model.k_a * self.q_p0 - self.q_c / self.model.v_c * self.model.cl - transition1 - transition2       #Rate of change of qc (in ng/h)
                    dqp1_dt = transition1                                     #Rate of change of qp1 (in ng/h) aka the quantity of drug in peripheral compartment
                    dqp2_dt = transition2
                    return [dqc_dt, dqp0_dt, dqp1_dt, dqp2_dt], 
        return lambda t, y: rhs(self, y, t)
    
#print(self.y0)   
    def sol(self):
        f = self.rhsetup()
        #print(f(3,4))
        print(self.y0)
        t_eval = np.linspace(self.timescale[0], self.timescale[1], self.timescale[2])
        #print(t_eval)
        sol = scipy.integrate.solve_ivp(
            fun= f,
            t_span=[t_eval[0], t_eval[-1]],
            y0=self.y0, t_eval=t_eval
            )
        return [sol.t, sol.y]
        
