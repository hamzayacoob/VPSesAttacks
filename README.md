# VPSesAttacks
This is a repositity of 4 pertubtion techniques that expose the vunerabilites of Voice Processing Systems (VPSes).

# Prequisties
The use of the following attacks requires an extensive use of libraries and imports. Be sure to import all the 

# 1. Time Domain Inversion Attack (TDI)
Two completely different signals in the time domain can have similar spectra. This attack modifies audio in the time domain while preserving it's spectrum, by inverting the windows signal. Inverting small windows across the entire signal removes the smoothness and thus makes it more difficult for the human ear to interpret. 

# 2. Random Phase Generation (RPG)
Exploits the way magnitude is used in the phase for an audio signal. Magnitude is a one to many function. Two signals of different phases can have the same magnitude spectrum. This attack will output a new signal with a different phase yet with the same magnitude spectrum as the original signal. This attack will thus introduce discontinuities in the signal which will make it harder to interpret 

# 3. High Frequency Addition (HFA)
VPSes remove high frequencies from the audio signal during the preprocessing phase in order to improve accuracy. Spoken content is below 8000 Hz and and sampled at 16000 Hz. This attack creates high intensity sin waves and adds it to the real audio. By doing so we can mask the real audio and while still ensuring the VPSes understand it due to it's preprocessing. 

# 4. Time Scaling (TS)
This attack accelerates the voice commands to a point where they are still able to be properly transcribed but fast enough to make it harder to interpret by the human ear.
