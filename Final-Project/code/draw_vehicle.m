function [hPlotData1,hPlotData2] = draw_vehicle(x,y,r,color)
  t = linspace(0,2*pi,100)'; 
  circsx = r.*cos(t) + x; 
  circsy = r.*sin(t) + y;
  hPlotData1 = plot(x,y,'r*');
  hPlotData2 = plot(circsx,circsy,color);
  end