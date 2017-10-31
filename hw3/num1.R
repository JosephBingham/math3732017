a <- c(1.0, 1.1, 1.3, 1.5, 1.9, 2.1)
ones <- array(data = 1, dim = 6)
a_s <- a ^ 2
A <- matrix(data = c(ones, a, a_s), nrow = 6, ncol = 3, byrow = FALSE)
At <- t(A)
At_A <- At %*% A
b <-c(1.84, 1.96, 2.21, 2.45, 2.94, 3.18)
At_b = At %*% b
ans = solve(At_A, At_b)
ans
f <- function(x){ans[1] + ans[2]*x + ans[3]*x*x}
plot.function(f, from = .5, to = 2.5)
err_val = (b - f(a))
err_val_s = err_val ^ 2
err = sum(err_val_s)
err
