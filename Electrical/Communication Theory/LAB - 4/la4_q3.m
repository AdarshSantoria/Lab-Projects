t = linspace(0, 1, 1001); 
gt = sin(2*pi*t) - sin(6*pi*t);

fs = 50; 
imptrain = zeros(1, length(t));
imptrain(1:fs:end) = 1;

gsk = gt .* imptrain;

quant_levels = linspace(min(gsk), max(gsk), 16);
gk = zeros(1, length(gsk));
for i = 1:length(gk)
    [~, idx] = min(abs(quant_levels - gsk(i)));
    gk(i) = quant_levels(idx);
end

figure;
plot(t, gt, 'LineWidth', 2, 'DisplayName', 'g(t)');
hold on;
stem(t, gsk, 'LineWidth', 2, 'DisplayName', 'g_s(kT_s)');
stem(t, gk, 'LineWidth', 2, 'DisplayName', 'g_k(kT_s)');
ylabel('Amplitude');
xlabel('Time (s)');
grid on;
title('Message signal and its sampled and quantized versions');
legend('Location', 'southwest');
ylim([-2, 2]);

yline(quant_levels, '--', {'Quantization levels'}, 'LineWidth', 1.5);
xticks(0:1/fs:1);
xticklabels({'0', '0.02', '0.04', '0.06', '0.08', '0.1', '0.12', '0.14', '0.16', '0.18', '0.2', '0.22', '0.24', '0.26', '0.28', '0.3', '0.32', '0.34', '0.36', '0.38', '0.4', '0.42', '0.44', '0.46', '0.48', '0.5', '0.52', '0.54', '0.56', '0.58', '0.6', '0.62', '0.64', '0.66', '0.68', '0.7', '0.72', '0.74', '0.76', '0.78', '0.8', '0.82', '0.84', '0.86', '0.88', '0.9', '0.92', '0.94', '0.96', '0.98', '1'});
title('Message signal, Sampled and Quantized signals with grid lines');