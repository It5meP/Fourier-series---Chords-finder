Input an 1-2 seconds long audio file (.wav) of a chords that you want to know what the notes that made it up. Works best without noise

At line 17, put the audio's path inside quotation markers. (e.g. file_path = r"chords.wav")

It will output a graph of amplitude by frequency. Look out for frequency that spikes in amplitudes. Those are the notes that make up the chord. Terminal also output some, tho it only a "guess", better to look at the graph and try out every notes that shows up. Better than guessing 1 in 88 keys for 3/4 times per chord.
