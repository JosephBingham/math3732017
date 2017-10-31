n <- 8
f <- function(x){exp(x)}
pi <- acos(-1)

x <- array(dim = 17, data = 0)
for(i in 0:16){x[i+1] <- -pi + i/8*pi}
y <- f(x)
a <- array(dim = 8, data = 0)
b <- array(dim = 8, data = 0)
for(i in 1:8){
  temp_x <- i*x
  temp_cos <- cos(temp_x)
  temp_sin <- sin(temp_x)
  temp_cos_y <- y %*% temp_cos
  temp_sin_y <- y %*% temp_sin
  overm_cos <- temp_cos_y/8
  overm_sin <- temp_sin_y/8
  a[i] <- overm_cos
  b[i] <- overm_sin
  }
a0 <- sum(y)/n
x <- seq(-pi, pi, length = n)
k <- 1:(n)
s1 <- cos(n*x)
s2 <- a[n]/2*s1
s3 <- a0/2 + s2 #split at sum
s4 <- x %*% k
s5 <- cos(s4)
s6 <- s5 %*% a[1:n] #split at sum
s7 <- x %*% k
s8 <- sin(s7)
s9 <- s8 %*% b
s <- s3 + s6 + s9
c <- fft(y)*16
cc_s <- array(dim = 9, data = 0)
for(i in 0:n){cc_s[i+1] = ((-1)^i)*(1/8)}
cc <- cc_s %*% c[1:9]
aa <- Re(cc)
bb <- Im(cc)
aa0 <- aa[1]
aa <- aa[2:length(aa)]
bb <- bb[2:length(bb)]
ss1 = aa0/2 #splitting at sum
ss2 = 8%*%x
ss2_2 = cos(ss2)
ss2_3 = (aa[8]/2)%*%ss2_2
ss3 = cos(x%*%k[1:n])%*%aa[1:n] 
ss4 = sin(x%*%k[1:n])%*%bb[1:n]
ss = ss1 + ss2 + ss3 + ss4

plot.function(ss, from = -pi, to = pi)