% Define the SNR and calculate the noise power
SNR = 10;               % Signal-to-noise ratio in dB
Ps = mean(s.^2);        % Signal power
Pn = Ps / (10^(SNR/10)); % Noise power

% Generate the noise signal and add it to the modulated signal
noise = sqrt(Pn) * randn(1,length(s));
r = s + noise;

% Plot the noisy signal in time domain
figure;
plot(t,r);
xlabel('Time (s)');
ylabel('Amplitude (V)');
title('Noisy Signal r(t)');
