import numpy as np


def state_update(meas_val, meas_err, est_pos_prev, est_err_prev):
    Kn = est_err_prev / (est_err_prev + meas_err)
    pos_est_curr = est_pos_prev + Kn * (meas_val - est_pos_prev)
    est_err_curr = (1 - Kn) * est_err_prev

    return pos_est_curr, est_err_curr, Kn

""" Step 0: Initialization """
est_err = 0.3
est_pos = 0.1

noise = 0.05

t = [1,10 ,22 ,35 ,40 ,51 ,59 ,72 ,85 ,90 , 100 ]
y = [0.18 ,0.22 ,0.29 ,0.39 ,0.48 ,0.16 ,0.56 ,0.61 ,0.68 ,0.75 ,0.81]

out_pos = [est_pos]
out_err = [est_err]
state = 0
while state<11:
    print(state)
    # Step 1: Measurement
    meas_val = y[state]
    meas_err = 0.05
    # Step 2: Measurement
    est_pos, est_err, Kn = state_update(meas_val, meas_err, est_pos, est_err)
    #est_vel = est_pos / t[]
    # OUTPUTS
    out_pos.append(est_pos)
    out_err.append(est_err)
    print(f"system state estimate: {est_pos}")
    print(f"uncertainty estimate : {est_err}")
    # Step 3: Prediction
    est_pos = est_pos
    est_err = est_err * noise

    state += 1


print(out_pos)
print(out_err)