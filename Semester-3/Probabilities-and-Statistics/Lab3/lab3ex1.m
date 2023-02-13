%normal distributions
x = input('Select normal, student, chi2, fischer: ', 's');

% a) P(X<=0), P(X>=0)

switch x
    case 'normal'
        % a) 
        mu = input('mu: ');
        sigma = input('sigma: ');
        pa1 = normcdf(0, mu, sigma);
        pa2 = 1 - normcdf(0, mu, sigma);
        % b)
        pb1 = normcdf(1, mu, sigma) - normcdf(-1, mu, sigma);
        pb2 = 1 - pb1;
        % c)
        alpha = input('alpha: ');
        answc = norminv(alpha, mu, sigma);
        % d)
        beta = input('beta: ');
        answd = norminv(1-beta, mu, sigma);
    case 'student'
        % a)
        n = input('n: ');
        pa1 = tcdf(0, n);
        pa2 = 1 - tcdf(0, n);
        % b)
        pb1 = tcdf(1, n) - tcdf(-1, n);
        pb2 = 1 - pb1;
        % c)
        alpha = input('alpha: ');
        answc = tinv(alpha, n);
        % d)
        beta = input('beta: ');
        answd = tinv(1-beta, n); 
    case 'chi2'
        % a)
        n = input('n: ');
        pa1 = chi2cdf(0, n);
        pa2 = 1 - chi2cdf(0, n);
        % b)
        pb1 = chi2cdf(1, n) - chi2cdf(-1, n);
        pb2 = 1 - pb1;
        % c)
        alpha = input('alpha: ');
        answc = chi2inv(alpha, n);
        % d)
        beta = input('beta: ');
        answd = chi2inv(1-beta, n);
    case 'fischer'
        % a)
        m = input('m: ');
        n = input('n: ');
        pa1=fcdf(0, m, n);
        pa2=1 - fcfd(0, m, n);
        % b)
        pb1 = fcdf(1, m, n) - fcdf(-1, m, n);
        pb2 = 1 - pb1;
        % c)
        alpha = input('alpha: ');
        answc = finv(alpha, m, n);
        % d)
        beta = input('beta: ');
        answd = finv(1-beta, m, n);
    otherwise
        fprintf('Wrong option!');
end

fprintf('a.1) P(X<=0)= %5.4f\n', pa1);
fprintf('a.2) P(X>=0)= %5.4f\n', pa2);
fprintf('b.1) P(-1<=X<=1)= %6.4f\n', pb1);
fprintf('b.2) P(X<=-1 or X>=1)= %6.4f\n', pb2);
fprintf('c) P(X < x alpha)= %6.4f\n', answc);
fprintf('d) P(X > x beta)= %6.4f\n', answd);



