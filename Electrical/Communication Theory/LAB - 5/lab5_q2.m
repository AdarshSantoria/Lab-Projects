K = 10000; % number of realizations
N = 200; % length of each realization

% generate random variables
U = (rand(K, N) > p) * 2 - 1;


% compute random walk process
X = cumsum(U, 2);

% plot three realizations
plot(X(1,:), 'b');
hold on;
plot(X(2,:), 'g');
plot(X(3,:), 'r');
xlabel('Time');
ylabel('X[n]');
legend('Realization 1', 'Realization 2', 'Realization 3');
