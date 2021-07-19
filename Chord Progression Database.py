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
    current_root_key = None
    for root, dirs, files in os.walk(root_directory, topdown=True):
        update_tags(root, current_tonality, current_genre,
                    current_song_section, current_root_key)  # updates genre, tonality etc. tags for current folder
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


def update_tags(root, tonality=None, genre=None, song_section=None, root_key=None):
    folder_history = root.split("\\")  # split directory path by backslash
    most_recent_folder = folder_history[-1]

    # if we're in a new genre folder (of the format 'Genre-X Templates Pack'
    if 'Templates' in most_recent_folder:
        most_recent_folder.split()
        genre = most_recent_folder[0]

    # if we're in a new key folder
    if 'Major' in most_recent_folder:
        tonality = 'Major'
        root_key = most_recent_folder.split()[0]  # update root_key  (not sure if this assignment will work)
    elif 'Minor' in most_recent_folder:
        tonality = 'Minor'
        root_key = most_recent_folder.split()[0]

    # find song section
    if 'Chord Progressions' in most_recent_folder:
        song_section_lst = most_recent_folder.split()
        song_section = ''
        # build up string of words describing the song section
        for i in range(len(song_section_lst) - 1):
            song_section_lst.append(song_section_lst[i])

        # if there was no song section
        if song_section is '':
            song_section = None

    return tonality, genre, song_section, root_key


# print(find_chord_progression('sample 116.mid'))
print(build_progression_tree('Compressed Chord Templates'))

# chord templates pack = genre
# chord progressions =
