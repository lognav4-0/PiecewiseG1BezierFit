function Q = cubicBezierToPolyline(C, n)
% Generate polyline data from a cubic Bezier curve defined by its control points
t = linspace(0, 1, n)';
Q = (1-t).^3*C(1,:) + 3*t.*(1-t).^2*C(2,:) + 3*t.^2.*(1-t)*C(3,:) + t.^3*C(4,:);
end