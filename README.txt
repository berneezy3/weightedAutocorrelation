Weighted Autocorrelation function for pitch detection

Pros: 

- robust against noise
- good for speech 

Cons:

- inaccurate for high frequencies

Dependencies:

scipy
numpy
pyaudio
matplotlib
scipy
wave

* to install these, run commands "pip scipy", "pip numpy" or "pip pyaudio" etc.


Inputs:

wavFile:  wavFile object in python, either mono or stereo
mmin: minimum pitch you expect in hertz
mmax: maximum pitch you expect in hertz
N: size of sliding window
threshold:  threshold to categorize as pitch point (play around with this to achieve better results)

Output:

Array object containing the pitches as floats


