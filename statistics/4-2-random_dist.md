[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

### Code
```
import numpy as np

import nsfg
import first
import thinkstats2
import thinkplot


sample = np.random.random(1000)
hist = thinkstats2.Hist(sample)
thinkplot.Hist(hist)
thinkplot.Show(xlabel='Random Nos.', ylabel='Frequency')

#Distribution is uniform with equal probability of occurance for each Random No.

pmf = thinkstats2.Pmf(sample)
thinkplot.Pmf(pmf,linewidth=0.1)
thinkplot.Show(xlabel='Random Nos.', ylabel='PMF')

#Distribution is uniform as cdf of the sample values is linear

sample_cdf = thinkstats2.Cdf(sample, label='Random Nos.')
thinkplot.Cdf(sample_cdf)
thinkplot.Show(xlabel='Random Nos.', ylabel='CDF')
```

### Analysis
The sample of random numbers has a uniform distribution as:
  * The PMF plot shows equal probability of occurance for all the random values in the sample
  * The CDF plot of the sample of random values is linear which again indicates it's a uniform distribution
