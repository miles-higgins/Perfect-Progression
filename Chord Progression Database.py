# add to git so I can start making commits
import music21
from music21 import *


def find_chord_progression(midi_filename):
    # open midi file
    mf = midi.MidiFile()
    mf.open(midi_filename)
    mf.read()
    # convert MIDI file to stream
    midi_stream = midi.translate.midiFileToStream(mf)

    # chordify the midi stream
    chords = midi_stream.chordify()

    # build up chord progression array
    progression = []
    for element in chords:
        if isinstance(element, music21.chord.Chord):
            progression.append(element.pitchedCommonName)

    return progression


print(find_chord_progression('sample 1126.mid'))
