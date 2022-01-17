%% Collision Avoidance Initialization
clear all;
clc;
% Vehicle 1
% preferred velocity
v_ref = 1.0 ;
% target position
p1x_goal = 100 ;
p1y_goal = 200 ;
% initial position 1
p1x_ini    = 100;
p1y_ini    = 0;
% initial velocity 1
v1x_ini = v_ref * (p1x_goal - p1x_ini) / (sqrt( (p1x_goal - p1x_ini)^2 + (p1y_goal - p1y_ini)^2) ) ;
v1y_ini = v_ref * (p1y_goal - p1y_ini) / (sqrt( (p1x_goal - p1x_ini)^2 + (p1y_goal - p1y_ini)^2) ) ;

% Vehicle 2
% initial velocity 2
v2x_ini = 1.0;
v2y_ini = 0.0;
% initial position 2
p2x_ini    = 0;
p2y_ini    = 100;

% Collision constraints
r1  = 10; % radius of vehicle 1
r2  = 10; % radius of vehicle 2

% Done
% Save Workspace
save("simin.mat")