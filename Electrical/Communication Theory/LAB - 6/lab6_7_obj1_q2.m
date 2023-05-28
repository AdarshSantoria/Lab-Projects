% Define the noise parameters
SNR = 20;              % Signal-to-Noise Ratio in dB
Pm = mean(m.^2);       % Power of the message signal
Pn = Pm/10^(SNR/10);   % Power of the noise signal
noise = sqrt(Pn)*randn(size(m));   % Generate Gaussian white noise with the desired power

% Add noise to the message signal
m_noisy = m + noise;

% Plot the noisy message signal in time domain
subplot(2,1,1);
plot(t,m_noisy);
xlabel('Time (s)');
ylabel('Amplitude (V)');
title('Noisy Message Signal m(t) with AWGN, SNR = 20 dB');

% Plot the noisy message signal in frequency domain
N = length(m_noisy);
f = (-fs/2:fs/N:fs/2-fs/N); % Frequency vector
M_noisy = abs(fftshift(fft(m_noisy,N)));
subplot(2,1,2);
plot(f,M_noisy);
xlim([-10000 10000]);
xlabel('Frequency (Hz)');
ylabel('Magnitude');
title('Frequency Domain of Noisy Message Signal m(t) with AWGN, SNR = 20 dB');
