t = linspace(0, 1, 1000);
gt = sin(2 * pi * t) - sin(6 * pi * t);
fs = 50;
imptrain = zeros(1, length(t));
imptrain(1: 1000 / fs: end) = 1;
imptrain(imptrain == 0) = nan;

gsk = gt .* imptrain;

figure;
subplot(3, 1, 1);
plot(t, gt);
xlabel('time (s)');
ylabel('g(t)');
title('Message signal g(t) in time domain');
xlim([0, 1]);
grid on;

subplot(3, 1, 2);
stem(t, imptrain);
xlabel('time (s)');
ylabel('p(t)');
title('impulse train p(t) in time domain');
xlim([0, 1]);
grid on;

subplot(3, 1, 3);
stem(t, gsk);
xlabel('time (s)');
ylabel('g_s(kT_s)');
title('Sampled signal g_s(kT_s) in time domain');
xlim([0, 1]);
grid on;