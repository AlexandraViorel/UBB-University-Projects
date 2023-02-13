x=0:0.01:3;
f1=x.^5/10;
f2=x.*sin(x);
f3=cos(x);
plot(x,f1,x,f2,':b',x,f3,'-.m')
title('My plot')
legend('f1=x^5/10','f2=x*sin(x)','f3=cos(x)')

