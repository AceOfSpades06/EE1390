
import numpy as np
import os
path = os.getcwd()
print path
filenames = os.listdir(path)
i=0
for f in filenames:
	if f[0]=='f':
		a = "forward"+str(i)+".wav"
		os.rename(f,a)
		i = i+1
		print a