#need to translate [0,2] to [-1,1] using t = (2x-(a+b))/(b-a) -> (2x-2)/2 -> x-1, whose inverse is x+1
tr <- function(x){x + 1}
X <- tr(c(-0.3826, 0.3826, -0.92388, 0.92388))
ones <- c(1, 1, 1, 1)
X_new <- (X ^ 2)
f <- exp(X)
A <- matrix(data = c(ones, X, X_new), nrow = 4, ncol = 3, byrow = FALSE)
At <- t(A)
At_A <- At %*% A
At_f <- At %*% f
ans <- solve(At_A, At_f)
ans
g <- function(x){ans[1] + ans[2]*x + ans[3]*x*x}
plot.function(g, from <- -.25, to = 2.5)
err_val <- (f - g(X))
err_val_s <- err_val ^ 2
err <- sum(err_val_s)
err