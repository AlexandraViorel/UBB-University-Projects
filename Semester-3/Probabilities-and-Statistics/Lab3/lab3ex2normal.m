p = input("p=");
if p <= 0.95 && p >= 0.05
    for n = 1 : 3 : 100
      k = 0 : n;
      plot(k, binopdf(k, n, p));
      pause(0.5);
    end
end
