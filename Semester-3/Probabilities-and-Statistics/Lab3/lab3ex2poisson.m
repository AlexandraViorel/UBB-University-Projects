p = input("p=");
n = input("n=");
if p <= 0.05 && n >= 30
    k = 0 : n;
    plot(k, binopdf(k, n, p), 'm', k, poisspdf(k, n*p), 'b');
end