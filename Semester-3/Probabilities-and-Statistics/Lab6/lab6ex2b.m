% exercise 2, b)

X1 = [22.4 21.7 24.5 23.4 21.6 23.3 22.4 21.6 24.8 20.0];
X2 = [17.7 14.8 19.6 19.6 12.1 14.8 15.4 12.6 14.0 12.2];

n1 = length(X1);
n2 = length(X2);

alpha = input('alpha= ');

[H, P, CI, STATS] = vartest2(X1, X2, alpha);

f1 = finv(alpha/2, n1-1, n2-1);
f2 = finv(1-alpha/2, n1-1, n2-1);

fprintf('The rejection region for F is (%6.4f, %6.4f) U (%6.4f, %6.4f)\n', -inf, f1, f2, inf)
fprintf('The value of the test statistic F is %6.4f\n', STATS.fstat)
fprintf('The P-value for the variances test is %6.4f\n', P)

if H == 1 
    fprintf('\nThe null hypothesis is rejected.\n') 
else
    fprintf('\nThe null hypothesis is not rejected.\n')

    n = n1 + n2 - 2;
    t2 = tinv(1 - alpha, n); %quantile for right-tailed test
    [H2, P2, CI2, STATS2] = ttest2(X1, X2)
end
