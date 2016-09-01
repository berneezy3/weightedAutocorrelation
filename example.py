import pyaudio
import wave
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavf
from weightedAutoCor import *


# Open recording and plot pitch
dataArr = wavf.read('example.wav')
rate = dataArr[0]
soundArr = np.mean(dataArr[1], axis=1)
WACFpitchArr = pitchByWACF(dataArr)
time=np.arange(0,len(WACFpitchArr),1);


#pitch contour plot
f = plt.figure(1)
plt.subplot(211)
plt.scatter(time, WACFpitchArr)
plt.xlabel('time (s)')
#plt.yscale('log')
plt.ylabel('frequency(Hz)')
plt.xlim([-20,140])
plt.title('pitch contour')
plt.grid(True)
plt.subplot(212)
plt.plot(soundArr)

plt.show()