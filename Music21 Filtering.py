import music21
from music21 import *

# open up midi file, remove drums
"""
From https://inspiringpeople.github.io/data%20analysis/midi-music-data-extraction-using-music21/
"""
midi_path = "sample 1126.mid"
mf = midi.MidiFile()
mf.open(midi_path)
mf.read()

# isolate drums
for i in range(len(mf.tracks)):
            mf.tracks[i].events = [ev for ev in mf.tracks[i].events if ev.channel != 10]


# convert MIDI file to stream
midi_stream = midi.translate.midiFileToStream(mf)
components = []
print(midi_stream.classes)

# trying to open
part_1 = midi_stream[0]

# find piano part
instr = instrument.Piano
inst_parts = []
for part in instrument.partitionByInstrument(midi_stream):
    if isinstance(part.getInstrument(), instr):
        inst_parts.append(part)

print(inst_parts)

# convert piano part into chord progression
"""
We could probably just take a small sample of the chord progression, rather than using the whole song. 
Then we won't get all the repeated patterns, but would still get a useful progression.

There could be benefits of just taking piano parts. Then we know they are playable on the piano / sound good.

What if piano isn't playing chords?
What if notes also outline chords in the progression. For example 2 chords played as chords, and then two arpeggiated 
chords. If we just look at the chords we're not getting the proper progression.
What if piano only plays the bridge or some small random moments.
What if chord is split between instruments (root in the bass, higher notes in piano etc)  (chordify would fix this)


For repeated chords: just keep looking until see next chord?
"""


# # filter out everything but chords
# chords = []
# for element in midi_stream.getElementsByClass(note.Note):
#     chords.append(element)
#
#
# # chordify
# # chords = midi_stream.chordify()
#
# # print chords and remove notes
# for element in chords:
#     print(element.pitchedCommonName)
#     print(element)
#
# # chords.show()
# print(part_1.getInstrument)
#
# for element in part_1:
#     # atm this just takes the first piano part
#     # probably a cleaner way to do this
#     try:
#         if element.isChord:
#             name = element.pitchedCommonName
#             print(name)
#             print(element)
#     except AttributeError:
#         pass
#

# # find all instruments
# for part in instrument.partitionByInstrument(midi_stream):
#     print(part.getInstrument())


# finding duration
# print(billie.duration)
# finding time sig (could be useful for genre filter) (may be None tho lol)
# print(billie.timeSignature)\

