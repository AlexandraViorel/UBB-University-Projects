% b)
clear ALL
n = input('number of trials = ');
p = input('p in (0, 1) = ');

U = rand(n, 1);
X = sum(U < p);

N = input('number of simulations= ');
for i = 1 : N
    U = rand(n, 1);
    X(i) = sum(U < p);
end

U_X = unique(X);
n_X = hist(X, length(U_X));
relative_freq = n_X / N

k = 0:n;
a = binopdf(k, n, p);
plot(k, a, 'o', U_X, relative_freq, 'x')