theta_0 = 5
theta_v = 15
theta_g = 40
tf  = 1

a10 = theta_0
a11 = 0
a12 = (12*theta_v - 3*theta_g - 9*theta_0) / (4*tf^2)
a13 = (-8*theta_v + 3*theta_g + 5*theta_0) / (4*tf^3)

a20 = theta_v
a21 = (0*theta_v + 3*theta_g - 3*theta_0) / (4*tf)
a22 = (-12*theta_v + 6*theta_g + 6*theta_0) / (4*tf^2)
a23 = (+8*theta_v - 5*theta_g - 3*theta_0) / (4*tf^3)

t1=linspace(0,1,1000);
theta1=a10+a11*t1+a12*t1.^2+a13*t1.^3;
theta1_dot=a11+2*a12*t1+3*a13*t1.^2;
theta1_dotdot=2*a12+6*a13*t1;

t2=linspace(0,1,1000);
theta2=a20+a21*t2+a22*t2.^2+a23*t2.^3;
theta2_dot=a21+2*a22*t2+3*a23*t2.^2;
theta2_dotdot=2*a22+6*a23*t2;

figure;
title("Single link robot motion with via point 1")
plot(t1,theta1,'r');
hold on;
plot(t1,theta1_dot,'b')
plot(t1,theta1_dotdot,'g')
legend({'position[\deg]','velocity[\deg/s]','acceleration[\deg/s^2]'},'location','northwest')

figure;
title("Single link robot motion with via point 2")
plot(t2,theta2,'r');
hold on;
plot(t2,theta2_dot,'b')
plot(t2,theta2_dotdot,'g')
legend({'position[\deg]','velocity[\deg/s]','acceleration[\deg/s^2]'},'location','northwest')

t=[t1 t2+1]
theta=[theta1 theta2]
theta_dot=[theta1_dot theta2_dot]
theta_dotdot=[theta1_dotdot theta2_dotdot]

figure;
title("Single link robot motion with via point")
plot(t,theta,'r');
hold on;
plot(t,theta_dot,'b')
plot(t,theta_dotdot,'g')
legend({'position[\deg]','velocity[\deg/s]','acceleration[\deg/s^2]'},'location','northwest')
