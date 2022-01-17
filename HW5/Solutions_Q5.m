close all; clear all; clc;
% Step 0: Initialization
est_err = 0.3;
est_pos = 0.1;
est_vel = 0.0064*rand();

noise = 0.05;

t = [1,10 ,22 ,35 ,40 ,51 ,59 ,72 ,85 ,90 , 100 ];
y = [0.18 ,0.22 ,0.29 ,0.39 ,0.48 ,0.16 ,0.56 ,0.61 ,0.68 ,0.75 ,0.81];

out_pos = [est_pos];
out_err = [est_err];
out_Kn = [];
state = 1;
meas_t = 0;
while(state<12)
%     Step 1: Measurement
    meas_val = y(state);
    meas_err = 0.05;
%     Step 2: State update
    [est_pos, est_err, Kn] = state_update(meas_val, meas_err, est_pos, est_err);
%     OUTPUTS
    out_Kn = [out_Kn, Kn];
    out_pos = [out_pos, est_pos];
    out_err = [out_err, est_err];
%     print(f"system state estimate: {est_pos}")
%     print(f"uncertainty estimate : {est_err}")
%     Step 3: Prediction
    if state==11 % predict 5 seconds after
        est_pos = est_pos + (t(state)+5-t(state))*est_vel;
        est_err = est_err * noise;
    else        
        est_pos = est_pos + (t(state+1)-t(state))*est_vel;
        est_err = est_err * noise;
    end
    state = state + 1;

end

figure;
hold on;
ylim([0 1])
xlim([0 t(end)])
scatter(t,y,'r');
plot(t,y,'r');
scatter([t, t(end)+5],out_pos,'b');
plot([t, t(end)+5],out_pos,'b');
xlabel("time [s]");
ylabel("position [m]");
legend("measured values","true values (estimated)")

figure;
hold on;
ylim([0 1e-6])
scatter(t,out_Kn,'r');
plot(t,out_Kn,'r');
xlabel("time [s]");
ylabel("Kalman Filter Gain ");
legend("Kn")


function [est_pos_curr, est_err_curr, Kn] = state_update(meas_val, meas_err, est_pos_prev, est_err_prev)
    Kn = est_err_prev / (est_err_prev + meas_err);
    est_pos_curr = est_pos_prev + Kn * (meas_val - est_pos_prev);
    est_err_curr = (1 - Kn) * est_err_prev;
end