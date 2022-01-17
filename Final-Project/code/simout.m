%% Get simulation outputs
t = out.tout ;
p1x = out.p1x ;
p1y = out.p1y ;
p2x = out.p2x ;
p2y = out.p2y ;

%% Illustrate
i=1;
figure;
title("Collision avoidance Illustration")

hold on;
% xlim([-5 25]);
% ylim([-5 25]);
% pxlimit = (1.5 * max(abs(p1x),abs(p2x))) ;
% pylimit = (1.5 * max(abs(p1y),abs(p2y))) ;
pxlimit = (1.5 * 200) ;
pylimit = (1.5 * 200) ;
xlim([ -pxlimit pxlimit ]) ;
ylim([ -pylimit pylimit ]) ;

% draw goal and initial positions
len = 10 ;
color1 = 'r' ;
color2 = 'b' ;

rectangle("position",[p1x_goal-len/2,p1y_goal-len/2,len,len],"FaceColor",[0, 1, 0])
[hPlotData1,hPlotData2] = draw_vehicle(p1x(i),p1y(i),r1,color1);
[hPlotData3,hPlotData4] = draw_vehicle(p2x(i),p2y(i),r2,color2);
% prev_position=[hPlotData1,hPlotData2,hPlotData3,hPlotData4];
% demonstrate
while (i<length(t))
  hold on;
  delete([hPlotData1,hPlotData2,hPlotData3,hPlotData4]);
  [hPlotData1,hPlotData2] = draw_vehicle(p1x(i),p1y(i),r1,color1);
  [hPlotData3,hPlotData4] = draw_vehicle(p2x(i),p2y(i),r2,color2);
%  hold off;
  pause( (t(i+1) - t(i)) / 10)
  
%   delete(prev_position);
%   prev_position=[hPlotData1,hPlotData2,hPlotData3,hPlotData4];
  i=i+1;
end