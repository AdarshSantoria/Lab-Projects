fm = 7;
fc = 30;
kp = 0.666 * pi;
am = 1;
ac = 1;
t = 0:0.001:2 / fm;

m = am * square(2 * pi * fm * t);
phi = ac * cos(2 * pi * fc * t + kp * m);
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