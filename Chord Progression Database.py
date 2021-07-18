import music21
import os
from music21 import *
from anytree import Node, RenderTree


class Chord:
    def __init__(self, name, progression):
        self.chord_name = name  # music 21 pitched common name of chord
        self.progression = progression  # progression object which stores filterable details


class Progression:
    def __init__(self, progression_array, genre, tonality, song_section=None):
        self.progression_array = progression_array
        self.song_section = song_section
        self.tonality = tonality
        self.genre = genre


def build_progression_tree(root_directory):
    current_genre = None
    current_tonality = None
    current_song_section = None
    for root, dirs, files in os.walk(root_directory, topdown=True):
        print(dirs)
        for name in files:
            progression = Progression(find_chord_progression(os.path.join(root, name)), current_genre,
                                                             current_tonality, current_song_section)
            # if first chord isn't a pre-exiting tree, create it
            # if subsequent chord isn't in tree yet, add to tree
            # if reach end of progression, add tags

    return


def find_chord_progression(midi_filename):
    # open midi file
    mf = midi.MidiFile()
    mf.open(midi_filename)
    mf.read()
    # convert MIDI file to stream
    try:
        midi_stream = midi.translate.midiFileToStream(mf)
    except:  # fixme
        print('incorrect midi file')

    # chordify the midi stream
    chords = midi_stream.chordify()

    # build up chord progression array
    progression = []
    for element in chords:
        if isinstance(element, music21.chord.Chord):
            progression.append(element.pitchedCommonName)

    return progression


# print(find_chord_progression('sample 116.mid'))
print(build_progression_tree('Compressed Chord Templates'))
