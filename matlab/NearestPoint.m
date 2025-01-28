function np = NearestPoint(C, P)

% Quick and dirty find nearest point on cubic B�zier curve specfied by
% control points C to point P sing Geom2D toolkit

% Compute complete Bezier

##P e C chegando certo
Q = cubicBezierToPolyline(C, 128);
% Find nearest point on Bezier
ind = findClosestPoint(P, Q);
np  = Q(ind,:);

% % Test
% figure;plot(Q(:,1), Q(:,2), 'b.--', C(:,1), C(:,2), 'ks:');
% hold on;
% plot(P(1), P(2), 'rx', np(1), np(2), 'ro');
% axis equal; axis tight;
