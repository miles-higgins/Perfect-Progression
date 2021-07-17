import music21

"""
Chord Identifier

Might be a good idea project wise to implement this as the minimum possible functional tool. Then work out 
more complex stuff later.
"""

# # read MIDI live with MIDO  (relies on me having installed RTMIDI, how will this work online?
import mido
import timeit
from music21 import chord


# initialise ports
print(mido.get_input_names())  # To list the input devices (could print these and let user select)
inport = mido.open_input('microKEY2 Air 1 KEYBOARD 1')
p = mido.parse_string_stream(inport)


def read_input(inport):
    # use timeit or something to contain individual chords (or we could use the note off midi message or smtn?)
    while True:
        chord_notes = []
        while len(chord_notes) < 7:  # client should get prompt saying ready
            msg = inport.receive()
            chord_notes.append(msg.note)  # add note to chord array  (need to deal with on off duplicate notes)
        played_chord = music21.chord.Chord(chord_notes)
        print(played_chord.pitchedCommonName)


# make this work with different input devices later


# suggest next chord


# learn how to set this up with django

read_input(inport)

