fs = 1e5;
t = 0:1/fs:0.1;

fc = 100;
kf = 30*pi;
fm = 5;
Am = 5;
m_t = Am*cos(2*pi*fm*t);

% FM modulation
s_t = cos(2*pi*fc*t + 2*pi*kf*cumsum(m_t)/fs);

% Add AWGN to the modulated signal
SNR = 20;
s_t_noisy = awgn(s_t, SNR, 'measured');

% Calculate Carson bandwidth and design bandpass filter
bw_carson = 2*(kf+fm);
Wn = [(fc-bw_carson/2)/(fs/2), (fc+bw_carson/2)/(fs/2)];
[b,a] = butter(5, Wn, 'bandpass');

% Filter the noisy modulated signal
s_t_filtered = filter(b, a, s_t_noisy);

% Perform FM demodulation using a linear demodulator
Kd = -1/(2*pi*kf);
m_t_demodulated = Kd*diff(s_t_filtered).*fs;

% Plot signals in the time domain
subplot(5,1,1);
plot(t(1:200),m_t(1:200),'r');
xlabel('Time(s)');
ylabel('Amplitude(V)');
title('Original Message Signal');
grid on;

subplot(5,1,2);
plot(t(1:200),s_t(1:200),'g');
xlabel('Time(s)');
ylabel('Amplitude(V)');
title('FM Modulated Signal');
grid on;

subplot(5,1,3);
plot(t(1:200),s_t_noisy(1:200),'b');
xlabel('Time(s)');
ylabel('Amplitude(V)');
title('Noisy Modulated Signal');
grid on;

subplot(5,1,4);
plot(t(1:200),s_t_filtered(1:200),'m');
xlabel('Time(s)');
ylabel('Amplitude(V)');
title('Filtered Modulated Signal');
grid on;

subplot(5,1,5);
plot(t(1:199),m_t_demodulated(1:199),'k');
xlabel('Time(s)');
ylabel('Amplitude(V)');
title('Demodulated Signal');
grid on;
