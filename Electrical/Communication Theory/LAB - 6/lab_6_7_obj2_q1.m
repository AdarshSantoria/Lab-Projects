% Define the parameters
fs = 100000;       % Sampling frequency
fm = 10;         % Message frequency
Am = 2;          % Message amplitude
T = 1/fm;        % Duration of one cycle
t = 0:1/fs:T-1/fs;   % Time vector

% Generate the message signal
m = Am*sin(2*pi*fm*t);

% Plot the message signal in time domain
figure;
plot(t,m);
xlabel('Time (s)');
ylabel('Amplitude (V)');
title('Message Signal m(t)');
