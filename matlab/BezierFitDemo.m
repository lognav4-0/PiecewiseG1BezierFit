function BezierFitDemo
% BezierFitDemo.m  Fitting Data using Picecewire G1 Cubic B�zier Curves
%
% Demonstration of MATLAB code from:
% Lane, Edward J. Fitting Data Using Piecewise G1 Cubic Bezier Curves.
% Thesis, NAVAL POSTGRADUATE SCHOOL MONTEREY CA, 1995.
%
% This code depends on the geom2D Toolbox which requires MATLAB R2014b or
% later.
% https://www.mathworks.com/matlabcentral/fileexchange/7844-geom2d


% Demonstrate two different Bezier curve fits
% Array Q is the set of data points to which we want to fit
% a piecewise G1 continuous cubic Bezier curve
% (Replace Q with your data.  You will need to adjust n = number of knots)
clear all;
demo = 1;

switch demo
    case 1
        % In this example, we generate a cubic B�zier with four control points.
        % Then we try to fit it with n knot points, leading to n-1 cubic B�zier
        % sections or 3*(n-1)+1 control points in all.
        % Define control points to generate data.  The control points
        % define a Bezier curve defined in:
        % "Solving the Nearest Point-on-Curve Problem" and
        % "A Bezier Curve-Based Root-Finder", both by Philip J. Schneider
        % from "Graphics Gems", Academic Press, 1990
        % http://www.realtimerendering.com/resources/GraphicsGems/gems/NearestPoint.c

        Q = [-1.72690252  -0.60320651;
             -1.24897493  -0.62118553;
             -0.95691139  -0.82453109;
             -0.54693039  -1.2073633;
             -0.29682866  -1.37491497;
             -0.07528416  -1.41953392;
             0.04932819   -1.41626638;
             0.32158605   -1.35978003;
             0.43495913   -1.26875526;
             0.46268872   -1.21207157;
             0.45620099   -0.99347741;
             0.39856247   -0.78108789;
             0.46167742   -0.37008614;
             0.49065901   -0.12820093;
             0.4293792    0.10799786;
             0.36700556   0.31922918;
             0.39913502   0.45092671;
             0.45062568   0.51972223;
             0.60943489   0.60025459;
             0.79160628   0.61508022;
             1.16497901   0.66786697;
             1.31335563   0.64628676;
             1.42801164   0.5450193;
             1.46717999   0.39541395;
             1.41809855   0.15004509;
             1.39170192   -0.23027283;
             1.28265079   -0.42013758;
             1.20794485   -0.45379492;
             1.19367788   -0.45363579;
             1.22633365   -0.52443446;
             1.00658826   -0.37020543;
             0.82064844   -0.10291448;
             0.41806804   0.16256904;
             0.18311442   0.37252653;
             -0.02908209  0.49855851;
             -0.16199967  0.52701975];
        
        % Generate a cubice B�zier polyline data with these control points
        % Q = cubicBezierToPolyline(C, 65);
        n = 4;  % Starting number of knot points
    case 2
        % Or, try a Lissajous figure:
        theta = 0:0.05:2*pi;
        x = sin(2*theta); y = cos(theta);
        Q(:,1) = x;  Q(:,2) = y;
        n = 3;  % Starting number of knot points
    case 3
        % Or two cycles of a sine wave
        theta = 0:0.05:4*pi;
        x = theta; y = cos(theta);
        Q(:,1) = x;  Q(:,2) = y;
        n = 5;  % Starting number of knot points
end

% Now try to do a piecewise cubic B�zier fit to Q starting with n knot points
% This computes the globally optimized only (GOO) curvve.
% (The plotting of the IG curve in iguess0.m can be commented out.)
Qt = Q';
[IG, k] = iguess0(Qt, n);
% Improve the fit: Segmentally Optimum Only Curve (SOO)
SOC = segop(k, Qt, IG);
disp("SOC");
disp(SOC);

% Improve it again: Segmentally then Globally Optimized Curve (SGO)
GOC = globop(SOC, Qt, 0, k);

% plot SGO curve using internal routine
figure;
hp = poplt(GOC, Qt);
title('Plot of SGO curve')

% This section of code simply repeats the plot above (poplt) in a
% manner that makes it easier to see the piecewise cubic Beizier sections

% Get the B�zier control points of the curve fit
Cnew = cpoints(GOC)';
P    = knots(Qt, k)';
disp("Cnew");
disp(Cnew');
disp("P");
disp(P');

% Plot fitted, segment by segment using Geom2D toolkit
figure; 
hold on;
for i = 1:3:length(Cnew)-3
    drawBezierCurve(Cnew(i:i+3,:));      % Fitted cubic bezier segment
end
hc = plot(Cnew(:,1), Cnew(:,2), 'o-');   % Control points
ho = plot(Q(:,1), Q(:,2), 'k.');           % Original data
hn = plot(P(:,1), P(:,2), 'kx', 'markerSize', 10);   % Original knot points
legend([ho hn hc], 'Original data', ...
    sprintf('Original guess n = %d knots',n), ...
    'New control points');
set(gcf, 'color', 'w');