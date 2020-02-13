#program to create a sine wave of amplitude 2 volts with fundamental
#frequency 2khz and plot the signal




import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

frequency = 2000
num_samples = 48000

sampling_rate = 48000.0

sine_wave = [np.sin(2 * np.pi * frequency * x1 / sampling_rate) for x1 in range(num_samples)]
sine_wave = np.array(sine_wave)

plt.subplot(3,1,1)
plt.title("sine wave")

plt.subplots_adjust(hspace=.5)
plt.plot(sine_wave[:100])
plt.show()



#Lucciffer
