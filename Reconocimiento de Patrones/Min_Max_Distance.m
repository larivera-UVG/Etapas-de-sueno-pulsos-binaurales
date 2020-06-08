function [mmd,a,b,c,d,e] = MMD (x)

L = length(x);

subwind = 30;
lista = zeros(1,subwind);
l_indmax = zeros(1,subwind);
l_indmin = zeros(1,subwind);
l_max = zeros(1,subwind);
l_min = zeros(1,subwind);
for i = 1:subwind
    [maximum,Indmax] = max(x(((i-1)*(L/subwind)+1):i*(L/subwind)));
    [minimum,Indmin] = min(x(((i-1)*(L/subwind)+1):i*(L/subwind)));
    l_indmax(1,i) = Indmax;
    l_indmin(1,i) = Indmin;
    l_max(1,i) = maximum;
    l_min(1,i) = minimum;
    lista(1,i) = sqrt ((Indmax - Indmin)^2 + (maximum - minimum)^2);
end 

%mmd = sum(abs(list)) / subwind;
mmd = mean(lista);
a = l_indmax;
b = l_indmin;
c = l_max;
d = l_min;
e = lista;