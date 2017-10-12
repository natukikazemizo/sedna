#!BPY
# -*- coding: UTF-8 -*-
# Read MIDI File
#
# 2017.10.12 Natukikazemizo
#

import bpy
import os
import utils_log
import utils_io_csv
import pretty_midi
import math

# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

midi_data = pretty_midi.PrettyMIDI(bpy.path.abspath("//") + "data/MIDI/yamato_piano_rendan.mid")

# GET 1ST TEMPO
tempo = math.floor(midi_data.get_tempo_changes()[1][0])

print("tempo:" + str(tempo))

for index in range(4):
    print(midi_data.instruments[index])
    for note in midi_data.instruments[index].notes:
        print(note)

logger.end()

