% example ex 2
clf
% n = input('Nr of trials n = ');
% p = input('Probability of success p = ');
% x = 0 : n;
% px = binopdf(x, n, p);
% plot(x, px, 'r+')
% hold on
% xx = 0 : 0.01 : n;
% fx = binocdf(xx, n, p);
% plot(xx, fx, 'm')
% legend('pdf', 'cdf')

% a)
hold on
n = 3;
p = 0.5;
x1 = 0 : n;
px1 = binopdf(x1, n, p);
px1
plot(x1, px1, ':b')

% b)
x2 = 0 : 0.01 : n;
fx2 = binocdf(x2, n, p);
plot(x2, fx2)

% c)
p1 = binopdf(0, 3, 0.5);
p2 = 1 - binopdf(0, 3, 0.5);

fprintf('P(X=0) = %2.5f\n', p1)
fprintf('P(X<>0) = %2.5f\n', p2)

% d)
p3 = binocdf(2, 3, 0.5);
p4 = binocdf(1, 3, 0.5);
fprintf('P(X<=2) = %2.5f\n', p3)
fprintf('P(X<2) = %2.5f\n', p4)

% e)
p5 = 1 - binocdf(0, 3, 0.5);
p6 = 1 - binocdf(1, 3, 0.5);
fprintf('P(X>=1) = %2.5f\n', p5)
fprintf('P(X>2) = %2.5f\n', p6)

% f)
n = 3;
x = 0;
for i = 1 : n
    toss = rand;
    if toss > 0.5   
        x = x + 1;
    end
end
x
hold off