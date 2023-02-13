%PS-practic-ex2
clear
clc
close all

X1 = [46, 37, 39, 48, 47, 44, 35, 31, 44, 37];
X2 = [35, 33, 31, 35, 34, 30, 27, 32, 31, 31];

n1 = length(X1);
n2 = length(X2);
m1 = mean(X1);
m2 = mean(X2);
v1 = var(X1);
v2 = var(X2);

% a) At the 5% significance level, do the population variances seem to
% differ?

% H0 : population variances are equal
% H1 : population variances differ 

fprintf("POINT a)\n");
fprintf("The null hypothesis H0: population variances are equal\n");
fprintf("The alternative hypothesis H1: population variances differ\n");

% we must do a variances two-tailed test

alpha = input("Please input the significance level: ");

[H, P, CI, STATS] = vartest2(X1, X2, alpha, 0);

if H == 0
    fprintf("\nThe null hypothesis is not rejected!\n");
    fprintf("The population variances are equal!\n");
else
    fprintf("\nThe null hypothesis is rejected!\n");
    fprintf("The population variances differ!\n");
end

f1 = finv(alpha/2, n1-1, n2-1);
f2 = finv(1-alpha/2, n1-1, n2-1);

fprintf("For the variances test we have:\n");
fprintf("The rejection region is (%.4f, %.4f) U (%.4f, %.4f)\n", -inf, f1, f2, inf);
fprintf("The P-value is %.4f\n", P);
fprintf("The statistics test value is %.4f\n", STATS.fstat);
fprintf("The value of H is %1f", H);

% b) Find a 95% confidence interval for the difference of the average
% assembling times.

if H == 0
    n = n1+n2-2;
    t = tinv(1-alpha/2, n);
    sp = sqrt(((n1-1)*v1 + (n2-1)*v2)/n);
    left = m1 - m2 - t*sp*sqrt(1/n1+1/n2);
    right = m1 - m2 + t*sp*sqrt(1/n1+1/n2);
else 
    c = (v1/n1)/(v1/n1+v2/n2);
    n = c^2/(n1-1)+(1-c)^2/(n2-1);
    n = 1/n;
    t = tinv(1-alpha/2, n);
    left = m1-m2-t*sqrt(v1/n1+v2/n2);
    right = m1-m2+t*sqrt(v1/n1+v2/n2);
end
fprintf("\nb)\n");
fprintf("The 95 confidence interval is: (%.4f, %.4f)\n", left, right);