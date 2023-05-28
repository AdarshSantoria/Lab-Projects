fm = 1000;
fc = 10 * 10 ^ 6;
am = 1;
ac = 1;
kf = 2 * pi * 5000;
t = 0:0.000001:2 / fm;

m = am * sin(2 * pi * fm * t);
phi = ac * cos(2 * pi * fc * t + kf * am * (1 - cos(2 * pi * fm * t)) / (2 * pi * fm));
subplot(2, 1, 1);
plot(t, m);
title('Message Signal');
xlabel('Time (s)')
ylabel('Amplitude (V)');
subplot(2, 1, 2);
plot(t, phi);
title('Modulated Signal');
xlabel('Time (s)')
ylabel('Amplitude (V)');