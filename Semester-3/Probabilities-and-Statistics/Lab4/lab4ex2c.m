% c)
clear ALL
p = input('p in (0, 1) = ');
X = 0;
while (X >= p)
    X = X + 1;
end

N = input('number of simulations= ');
for i = 1 : N
    X(i) = 0;
    while (rand >= p)
        X(i) = X(i) + 1;
    end
end

U_X = unique(X);
n_X = hist(X, length(U_X));
relative_freq = n_X / N

% geopdf
k = 0:20;
a =geopdf(k, p);
plot(k, a, 'o', U_X, relative_freq, 'x')