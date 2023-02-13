% d)
clear ALL
n = input('nb of success = ');
p = input('p in (0, 1) = ');
for j = 1:n
    Y(j) = 0;
    while(rand >= p)
        Y(j) = Y(j)+1;
    end
end
X = sum(Y);

N = input('number of simulations = ');
for i = 1:N
    for j = 1:n
        Y(j) = 0;
        while(rand >= p)
            Y(j) = Y(j)+1;
        end
    end
    X(i) = sum(Y);
end

U_X = unique(X);
n_X = hist(X, length(U_X));
relative_freq = n_X / N

% nbinpdf
k = 0:n;
a =nbinpdf(k, n, p);
plot(k, a, 'o', U_X, relative_freq, 'x')