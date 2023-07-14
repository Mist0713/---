# simple code to implement Runs 
# test of randomnes
  
import random
import math
import statistics
import csv
  
def runsTest(l, l_median):
  
    runs, n1, n2 = 0, 0, 0
      
    # Checking for start of new run
    for i in range(len(l)):
          
        # no. of runs
        if (l[i] >= l_median and l[i-1] < l_median) or (l[i] < l_median and l[i-1] >= l_median):
            runs += 1  
        # no. of positive values
        if(l[i]) >= l_median:
            n1 += 1     
        # no. of negative values
        else:
            n2 += 1   
    runs_exp = ((2*n1*n2)/(n1+n2))+1
    stan_dev = math.sqrt((2*n1*n2*(2*n1*n2-n1-n2))/(((n1+n2)**2)*(n1+n2-1)))
    z = (runs-runs_exp)/stan_dev
    return z
    
# Making a list of 100 random numbers 
l = []
for i in range(100):
    l.append(random.random())
# f = open('source.csv','r')
# rdr = csv.reader(f)

# for line in rdr:
#     l.append(line[4])

l_median= statistics.median(l)
  
Z = abs(runsTest(l, l_median))
  
print('Z-statistic= ', Z)