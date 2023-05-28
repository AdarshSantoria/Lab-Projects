K = [100, 1000, 10000]; % number of realizations
N = 200; % length of each realization

% generate random variables
U = zeros(length(K), N);
for i = 1:length(K)
    u = (rand(K(i), N)>p)*2-1;
    X = cumsum(u, 2);
    U(i,:) = mean(X(1:K(i),:), 1);
end


% compute sample autocorrelation for different K
RX_sample = zeros(length(K), N-1);
for i = 1:length(K)
    for n = 1:N-1
        RX_sample(i,n) = mean(X(1:K(i),n).*X(1:K(i),n+1));
        disp( RX_sample(i,n) );
    end
end

% compute theoretical autocorrelation
RX_theoretical = zeros(1, N-1);
for n = 1:N-1
    RX_theoretical(n) = n/4;
    disp(RX_theoretical(n));
end

% plot autocorrelation
plot(RX_theoretical, 'k');
hold on;
plot(RX_sample(1,:), 'b');
plot(RX_sample(2,:), 'g');
plot(RX_sample(3,:), 'r');
xlabel('Time lag');
ylabel('Autocorrelation');
legend('Theoretical', 'K = 100', 'K = 1000', 'K = 10000');
