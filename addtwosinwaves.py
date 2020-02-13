#program to add two sinosoidal signals of frequency 1khz and 10khz
#and plot all the three signals uing subplot command





import numpy as np
import matplotlib.pyplot as plot

orbitperiod = .36
lumorbitperiod = 3.25
synodicperiod = 1/abs((1/orbitperiod)-(1/lumorbitperiod))
highesthigh = 13500
lowesthigh = 3500
highestlow = 3000
lowestlow = 2000
halfofhighrange = abs(highesthigh-highestlow)/2
halfoflowrange = abs(highestlow-lowestlow)/2
lowmean = (highestlow+lowestlow)/2

time = np.arange(0, 2, 0.01) ;

sine_one = np.sin(time*np.pi*2 / orbitperiod)*halfoflowrange+lowmean
plot.plot(time * 365, sine_one, label='first Sine wave')

sine_two = np.sin(time*np.pi*2 / synodicperiod)*halfofhighrange+halfofhighrange
plot.plot(time * 365, sine_two, label='Second Sine wave')

sine_sum = sine_one + sine_two
plot.plot(time * 365 , sine_sum, label='Sum of both the Sine waves')
plot.legend();
plot.show()



#Lucciffer
