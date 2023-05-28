% Define the carrier signal parameters
fc = 1000;      % Carrier frequency
Ac = 4;         % Carrier amplitude
fs = 100000;       % Sampling frequency
fm = 10;         % Message frequency
Am = 2;          % Message amplitude
T = 1/fm;        % Duration of one cycle
t = 0:1/fs:T-1/fs;   % Time vector

% Generate the message signal
m = Am*sin(2*pi*fm*t);

% Modulate the message signal using DSB-SC modulation
s = m.*cos(2*pi*fc*t);

% Plot the modulated signal in time domain
figure;
plot(t,s);
xlabel('Time (s)');
ylabel('Amplitude (V)');
title('Modulated Signal s(t)');
