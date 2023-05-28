fm = 10;
fc = 50;
kf = 2 * pi * 150;
am = 1;
ac = 1;
t = 0:0.000001:2 / fm;

m = am * square(2 * pi * fm * t);
phi = ac * cos(2 * pi * fc * t + kf * am * sawtooth(2 * pi * fm * t, 1/2) / (2 * pi * fm));
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