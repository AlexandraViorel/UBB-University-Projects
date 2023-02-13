% PS-practic-ex4
clear 
clc


X1 = [1021, 980, 1017, 988, 1005, 998, 1014, 985, 995, 1004, 1030, 1015, 995, 1023];
X2 = [1070, 970, 993, 1013, 1006, 1002, 1014, 997, 1002, 1010, 975];

n1 = length(X1);
n2 = length(X2);
m1 = mean(X1);
m2 = mean(X2);
v1 = var(X1);
v2 = var(X2);

% a) At the 5% significance level, do the population variances seem to
% differ?

% H0 : the population variances are equal
% H1 : the population variances differ

fprintf("a)\n");

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

fprintf("The rejection region is: (%.4f, %.4f) U (%.4f, %.4f)\n", -inf, f1, f2, inf);
fprintf("The test statistics value is: %.4f\n", STATS.fstat);
fprintf("The P-value of the test is: %.4f\n", P);

% b) At the same significance level, on average, does Supplier A seem to be more reliable?

% H0 : the means are equal
% H1 : the mean of Supplier A is greater than the mean of Supplier B
% we have to perform a right-tailed test

fprintf("\nb)\n");

if H == 0
    type = "equal";
    n = n1+n2-2;
else 
    type = "unequal";
    c = (v1/n1)/(v1/n1+v2/n2);
    n = c^2/(n1-1) + (1-c)^2/(n2-1);
    n = 1/n;
end

[H1, P1, CI1, STATS1] = ttest2(X1, X2, alpha, 1, type);

if H1 == 0
    fprintf("\nThe null hypothesis is not rejected!\n");
    fprintf("The means are equal, so Supplier A is not more reliable!\n");
else 
    fprintf("\nThe null hypothesis is rejected!\n");
    fprintf("The mean of Supplier A is greater than the mean of Supplier B, so Supplier A is more reliable!\n");
end

t = tinv(1-alpha, n);
fprintf("The rejection region is: (%.4f, %.4f)\n", t, inf);
fprintf("The P-value of the test is: %.4f\n", P1);
fprintf("The value of the test statistics is: %.4f\n", STATS1.tstat);
fprintf("The value of H is: %1.0f\n", H);