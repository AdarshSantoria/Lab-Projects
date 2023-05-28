K = 1e4; % initialize K to 10^4
SNR = 10; % set the SNR in dB

% Step 1: Generate binary message symbols with equal probability
s = 2*randi([0,1],1,K)-1;

% Step 2: Generate AWGN noise
sigma_n = sqrt(1/(SNR));
n = sigma_n*randn(1,K);

% Step 3: Received signal
y = s + n;

% Step 4: Decoding
s_hat = sign(y);

% Step 5: Compute errors
num_errors = sum(s_hat ~= s);

% Step 6: Repeat steps 1-5 K times and compute Pe
Pe = num_errors/K;

% Step 7: Repeat step 6 for different SNR values
SNR_dB = 0:1:10;
SNR = 10.^(SNR_dB/10);
Pe_sim = zeros(size(SNR));
for i=1:length(SNR)
    sigma_n = sqrt(1/(SNR(i)));
    n = sigma_n*randn(1,K);
    y = s + n;
    s_hat = sign(y);
    num_errors = sum(s_hat ~= s);
    Pe_sim(i) = num_errors/K;
end

% Step 8: Plot results
Pe_theory = qfunc(sqrt(SNR));
semilogy(SNR_dB, Pe_sim, 'b-*', SNR_dB, Pe_theory, 'r--');
xlabel('SNR (dB)'); ylabel('Pe'); grid on;
legend('Simulated', 'Theoretical');
axis([0 15 1e-5 1]);
