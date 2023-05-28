K = [100, 1000, 10000];
N = 200;
p=0.5;

mu_theo = zeros(1,N);

mu_sample = zeros(length(K), N);
for i = 1:length(K)
    U = (rand(K(i), N)>p)*2-1;
    X = cumsum(U, 2);
    mu_sample(i,:) = mean(X(1:K(i),:), 1);
end

figure;
hold on;
plot(0:N-1,mu_theo,'k--','LineWidth',2);
plot(0:N-1,mu_sample(1,:),'b');
plot(0:N-1,mu_sample(2,:),'g');
plot(0:N-1,mu_sample(3,:),'r');
hold off;
xlabel('n'); ylabel('\mu_X[n]');
legend('Theoretical','K=100','K=1000','K=10000');