function zc = ZC_v2(y,thr)

L = length(y);
y_fixed = y;
zc = 0;     % initialize counter
pivot = 0;
pivotsign = 0;

for l = 1:L
    if(((y(l) > 0) && (y(l) <= thr)) || ((y(l) < 0) && (y(l) >= -thr)))
        y_fixed(l) = 0;
    else
        y_fixed(l) = y(l);  % only necessary in the C version, since y_fixed
                            % would not be initialized.
    end
    
    % determine where the first nonzero value is
    if(pivotsign == 0)
        if(y_fixed(l) > 0)
            pivot = l;
            pivotsign = 1;
        elseif(y_fixed(l) < 0)
            pivot = l;
            pivotsign = -1;
        end
    end
end

% Count how many sign changes there are. A zero is considered the same sign
% as the previous one.
for j = (pivot+1):L
   if((y_fixed(j) > 0) && (pivotsign == -1))
       zc = zc + 1;
       pivotsign = 1;
   elseif((y_fixed(j) < 0) && (pivotsign == 1))
       zc = zc + 1;
       pivotsign = -1;
   end
end

end
