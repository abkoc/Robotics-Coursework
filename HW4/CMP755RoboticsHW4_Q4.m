# cubic polynomial coefficients found by hand
t=linspace(0,4,1000)
a0 = -5
a1 = 0
a2 = 85*3/16
a3 = -85/32

theta=a0+a1*t+a2*t.^2+a3*t.^3;
theta_dot=a1+2*a2*t+3*a3*t.^2;
theta_dotdot=2*a2+6*a3*t;
figure;
title("Single link robot motion")
plot(t,theta,'r');
hold on;
plot(t,theta_dot,'b')
plot(t,theta_dotdot,'g')
legend({'position[\deg]','velocity[\deg/s]','acceleration[\deg/s^2]'},'location','northwest')