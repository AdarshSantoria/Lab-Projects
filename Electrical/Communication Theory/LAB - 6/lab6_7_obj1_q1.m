% Define the parameters
fs = 100000;          % Sampling frequency
fm = 1000;           % Message frequency
Am = 1.5;            % Message amplitude
T = 2/fm;            % Duration of one cycle
t = 0:1/fs:T-1/fs;   % Time vector

% Generate the message signal
m = Am*sin(2*pi*fm*t);

% Plot the message signal in time domain
subplot(2,1,1);
plot(t,m);
xlabel('Time (s)');
ylabel('Amplitude (V)');
title('Message Signal m(t)');

% Plot the message signal in frequency domain
N = length(m);
f = (-fs/2:fs/N:fs/2-fs/N);   % Frequency vector
M = abs(fftshift(fft(m,N)));
subplot(2,1,2);
plot(f,M);
xlim([-2000 2000]);
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('Frequency Domain of Message Signal m(t)');
