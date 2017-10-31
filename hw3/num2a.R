# 2.a
X = array(dim = 10)
ones = array(dim = 11, data = 1)
X[1] = -1
for(i in 2:11){ X[i] = X[i-1] + 1.0/5.0}
X_s = X ^ 2
f = exp(X)
A <- matrix(data = c(ones, X, X_s), nrow = 11, ncol = 3, byrow = FALSE)
At <- t(A)
At_A <- At %*% A
At_f = At %*% f
ans = solve(At_A, At_f)
ans
g <- function(x){ans[1] + ans[2]*x + ans[3]*x*x}
plot.function(g, from = -1.5, to = 2.5)
err_val = (f - g(X))
err_val_s = err_val ^ 2
err = sum(err_val_s)
err