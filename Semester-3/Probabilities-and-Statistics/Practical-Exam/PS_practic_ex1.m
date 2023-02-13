% PS-practic-ex1
clear
clc
close all

X1 = [4.6, 0.7, 4.2, 1.9, 4.8, 6.1, 4.7, 5.5, 5.4]; % steel
X2 = [2.5, 1.3, 2.0, 1.8, 2.7, 3.2, 3.0, 3.5, 3.4]; % glass

n1 = length(X1);
n2 = length(X2);
m1 = mean(X1);
m2 = mean(X2);
v1 = var(X1);
v2 = var(X2);

% a) At the 5% significance level, do the population variances seem to
% differ?

% H0 = population variances are equal
% H1 = population variances differ
fprintf('a)\n');
fprintf("The null hypothesis H0: population variances are equal\n");
fprintf("The alternative hypothesis H1: population variances differ\n");

% because we must test if the variances differ and we have 2 populations => we
% will use "vartest2"

alpha = input("Please input the significance level: ");

[H, P, CI, STATS] = vartest2(X1, X2, alpha, 0);

f1 = finv(alpha/2, n1-1, n2-1);
f2 = finv(1-alpha/2, n1-1, n2-1);

fprintf("The value of the variances test vartest2 is %.4f\n", STATS.fstat);
fprintf("The rejection region of the variances test is (%.4f, %.4f) U (%.4f, %.4f)\n", -inf, f1, f2, inf);
fprintf("The P-value of the variances test is %.4f\n",P);
fprintf("The value of H of the variances test is %.4f", H);

if H == 0
    fprintf("\nThe null hypothesis is not rejected!\n");
    fprintf("The population variances are equal!\n");
else
    fprintf("\nThe null hypothesis is rejected!\n");
    fprintf("The population variances seem to differ!\n");
end

% b) At the same significance level, does it seem that on average, steel
% pipes lose more heat than glass pipes?

% H0: on average, they lose the same heat (the means are equal)
% H1: on average, steel lose more heat than glass (mean(X1) > mean(X2))
fprintf("b)\n");
fprintf("The null hypothesis H0 is: steel and glass lose the same amount of heat\n");
fprintf("The alternative hypothesis H1 is: steel lose more heat than glass\n");

% because the test is on average => we must test the means
% we have to test the means of 2 populations => ttest2

% if H from point a) is 0 => the variances are equal
% if H from point a) is 1 => the variances differ

if H == 0
    n = n1 + n2 - 2;
    t1 = tinv(1 - alpha, n);
    [H1, P1, CI1, STATS1] = ttest2(X1, X2, alpha, 1, "equal");
    if H1 == 0
        fprintf("\nThe null hypothesis is not rejected!\n");
        fprintf("On average, steel and glass lose the same heat!\n");
    else
        fprintf("\nThe null hypothesis is rejected!\n");
        fprintf("On average, steel lose more heat than glass!\n");
    end
    fprintf("The rejection region for the mean test is (%.4f, %.4f)\n", t1, inf);
    fprintf("The mean test statistic is %.4f\n", STATS1.tstat);
    fprintf("The P-value of the mean test is %.4f\n", P1);
    fprintf("The value of H for the mean test is %.4f", H1);
else 
    c = (v1/n1)/(v1/n1+v2/n2);
    n = c^2/(n1-1)+(1-c)^2/(n2-1);
    n = 1/n;
    t1 = tinv(1-alpha, n);
        [H1, P1, CI1, STATS1] = ttest2(X1, X2, alpha, 1, "unequal");
    if H1 == 0
        fprintf("\nThe null hypothesis is not rejected!\n");
        fprintf("On average, steel and glass lose the same heat!\n");
    else
        fprintf("\nThe null hypothesis is rejected!\n");
        fprintf("On average, steel lose more heat than glass!\n");
    end
    fprintf("The rejection region for the mean test is (%.4f, %.4f)\n", t1, inf);
    fprintf("The mean test statistic is %.4f\n", STATS1.tstat);
    fprintf("The P-value of the mean test is %.4f\n", P1);
    fprintf("The value of H for the mean test is %.4f", H1);
end