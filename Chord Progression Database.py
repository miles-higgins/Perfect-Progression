# add to git so I can start making commits
import music21
import os
from music21 import *


def build_progression_tree(root_directory):
    # want to supply the program with a folder, traverse through and build up the trees
    # this has subfolders sorted by genre
    # these subfolders have subfolders sorted by song section (exceptnot all do)
    # these subfolders have subfolders sorted by major or minor (except not all do)
    # these subfolders have subfolders have subfolders sorted by key
    for root, dirs, files in os.walk(root_directory, topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

    return


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


# print(find_chord_progression('sample 1126.mid'))
print(build_progression_tree('Compressed Chord Templates'))
