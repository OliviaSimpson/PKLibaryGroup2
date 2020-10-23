import matplotlib.pylab as plt
import numpy as np
import scipy.integrate

def dose(t, X):
    return X
# Dose function - X is dose in nanograms, t indicates that the dosing protocol could involve more than one dose at various timepoints, or a continuous application
# will need to modify this function to take this into account 
def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    q_c, q_p1 = y                                           #sets the initial drug quantity in the central and peripheral compartments
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)           #determines the transition rate (in ng/h)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition       #Rate of change of qc (in ng/h)
    dqp1_dt = transition                                    #Rate of change of qp1 (in ng/h) aka the quantity of drug in peripheral compartment
    return [dqc_dt, dqp1_dt]

model1_args = {                                             #These are both libraries of parameters for the model, changing the transition rate between model 1 and 2
    'name': 'model1',
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
}

model2_args = {
    'name': 'model2',
    'Q_p1': 2.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
}

t_eval = np.linspace(0, 1, 1000)                        #generating the time points to evaluate the model at
y0 = np.array([0.0, 0.0])                               

fig = plt.figure()
for model in [model1_args, model2_args]:
    args = [
        model['Q_p1'], model['V_c'], model['V_p1'], model['CL'], model['X']
    ]
    sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: rhs(t, y, *args),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
    )
    plt.plot(sol.t, sol.y[0, :], label=model['name'] + '- q_c')
    plt.plot(sol.t, sol.y[1, :], label=model['name'] + '- q_p1')

plt.legend()
plt.ylabel('drug mass [ng]')
plt.xlabel('time [h]')
plt.show()
return [sol.t, sol.y]