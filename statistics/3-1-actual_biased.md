[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

### Code
```
import nsfg
import thinkstats2
import thinkplot


def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

resp = nsfg.ReadFemResp()

actual_pmf=thinkstats2.Pmf(resp.numkdhh,label='Actual')
biased_pmf=BiasPmf(actual_pmf,label='Biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([actual_pmf, biased_pmf])
thinkplot.Show(xlabel='No. of children in a Household', ylabel='PMF')

print('Actual Mean: ',actual_pmf.Mean(),'\nBiased/Observed Mean: ', biased_pmf.Mean())
```
### Result
Actual mean no. of children under 18years in a household are 1.02420515504    
Observed/Biased mean no. of children under 18years in a household are 2.40367910066

### Analysis
If you ask children about the no. of children in the household as observed by them you will find the observed mean of the no. of children in a household to be approximately 1.38 more than the actual mean no. of children in a household
