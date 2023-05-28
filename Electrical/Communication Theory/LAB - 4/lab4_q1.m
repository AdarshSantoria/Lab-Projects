t = 0:1 / 100:1;
gt = sin(2 * pi * t) - sin(6 * pi * t);

subplot(2, 1, 1);
plot(t, gt);
xlabel('time (s)');
ylabel('g(t)');
title('Message signal in time domain');

fs = 1000;
Gf = fft(gt)/100;
f = linspace(-50, 50, length(Gf));
subplot(2, 1, 2);
stem(f, abs(fftshift(Gf)));
xlabel('frequency (Hz)');
ylabel('|g(f)|');
xlim([-4, 4]);
title('Message signal in frequency domain');