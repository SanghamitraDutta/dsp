[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

```  
import numpy as np

import nsfg

def CohenEffectSize(group1, group2):
    
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

print('Difference in totalwgt_lb relative to mean (Percentage points)', 
          (firsts.totalwgt_lb.mean() - others.totalwgt_lb.mean()) / live.totalwgt_lb.mean() * 100)

print('Difference in prglngth relative to mean (Percentage points)', 
          (firsts.prglngth.mean() - others.prglngth.mean())/ live.prglngth.mean() * 100)

d = CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb)
print('Difference in totalwgt_lb, Cohen\'s d:', d)

d = CohenEffectSize(firsts.prglngth,others.prglngth)
print('Difference in prglngth, Cohen\'s d:', d)
```
