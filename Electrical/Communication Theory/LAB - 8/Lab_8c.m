clc

t = 0 : 0.001 : 0.999;
fim = 50;

gt = sin(2*pi*t) - sin(6*pi*t);

imp = zeros(1,length(t));
imp(1 : 20 : 1000) = 1;

ct = gt .* imp ;
q_val = 16;
delta = (max(ct) - min(ct))/q_val ;
start = max(ct) - delta/2;

q = zeros(1,q_val);
q(1,1) = start;

for i = 1:(q_val-1)
    q(1,i+1) = start - i*delta;
end

for i = 1:length(ct)
    for j = 1:length(q)
        if ct(i) >= q(j)
            ct(i) = q(j);
            break
        end
    end
end

pt_1c = (square(pi*t*fim , 25) +1)/2 ;
gpt_1c = pt_1c .* ct;

plot(t,gpt_1c,'color','red');