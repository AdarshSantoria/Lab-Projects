T = 1;     
fs = 50;   
Ts = 1/fs;  

t = 0:0.001:T;
g = sin(2*pi*t) - sin(6*pi*t);
ts = 0:Ts:T;
gs = sin(2*pi*ts) - sin(6*pi*ts);

Amp = max(abs(g));
Delta = 2*Amp/16;
levels = -Amp+(Delta/2):Delta:Amp-(Delta/2);
gq = interp1(levels, levels, gs, 'nearest');

figure;
hold on;
grid on;

for k = 1:16
    plot([0 T], [levels(k) levels(k)], 'k:');
end

plot(t, g, 'b', 'LineWidth', 2);
stem(ts, gq, 'r', 'LineWidth', 2, 'MarkerSize', 4);

xlim([0 T]);
ylim([-Amp Amp]);
xlabel('Time (s)');
ylabel('Amplitude');
grid on;
grid minor;
ax = gca;
ax.GridColor = [0.5 0.5 0.5];
ax.GridAlpha = 0.5;
ax.GridLineStyle = ':';
legend('Quantization levels', 'Message signal g(t)', 'Quantized signal gq(t)');