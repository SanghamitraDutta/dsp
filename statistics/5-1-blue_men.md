[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

### Code
```
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

print(dist.mean(), dist.std())
print(dist.cdf(mu-sigma))  # 15% below mu-sigma in the distribution

#How many people are between 5'10" and 6'1"?
H1= 177.8
H2= 185.4
PercentageH2_H1= dist.cdf(H2) - dist.cdf(H1)
print(PercentageH2_H1)
```
### Analysis 
34.21% of US male population is in the range of 5'10" and 6'1" of height.

