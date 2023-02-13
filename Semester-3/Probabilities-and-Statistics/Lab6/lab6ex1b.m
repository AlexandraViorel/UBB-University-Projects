% exercise 1
clear
x = [7 7 4 5 9 9 4 12 8 1 8 7 3 13 2 1 17 7 12 5 6 2 1 13 14 10 2 4 9 11 3 5 12 6 10 7];
n = length(x);
 
% b) sigma unknown 
alpha = input('alpha = ');
sigma = std(x);
m0 = input('m0= ');
[H, P, CI, STATS] = ttest(x, m0, alpha, 1);
RR = [tinv(1-alpha, n-1), inf];

fprintf('The value of the test statistic z is %.4f\n', STATS.tstat)
fprintf('The rejection region is (%.4f, %.4f)\n', RR)
fprintf('The P-value of the test is %.4f\n', P)

% result of the test, H = 0, if H0 is NOT rejected, H = 1, if H0 IS rejected
if H == 1 
    fprintf('\nThe null hypothesis is rejected.\n') 
    fprintf('The data suggests that the average exceeds 5.5.\n')
else
    fprintf('\nThe null hypothesis is not rejected.\n')
    fprintf('The data suggests that the average DOES NOT exceed 5.5.\n')
end