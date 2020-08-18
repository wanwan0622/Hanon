# -*- coding: utf-8 -*-
from music21 import *
import numpy
import matplotlib
import scipy
import random

#乱数生成
random_num = [-1 for _ in range(7)]
for i in range(7):
    random_num[i] = random.randint(0, 6)
    if i >= 1: #前の音符と同じ音符がかぶらないようにする
        while True:
            if random_num[i] != random_num[i-1]:
                break
            else:
                random_num[i] = random.randint(0, 6)



#楽譜をかくよ


stream_right = stream.Part()
stream_left = stream.Part()

inst1 = instrument.Instrument()
inst2 = instrument.Instrument()

stream_right.append(inst1)
stream_left.append(inst2)

tc = clef.TrebleClef() #ト音記号
bc = clef.BassClef() #ヘ音記号

stream_right.append(tc)
stream_left.append(bc)

otos_right = ["D3", "E3", "F3", "G3", "A3", "B3", "C4"]
otos_left = ["D2", "E2", "F2", "G2", "A2", "B2", "C3"]

##右手
###最初のド
meas = stream.Measure()
n = note.Note("C3", quarterLength = 0.25)
meas.append(n)
###1小節目の残りの音
for i in range(7):
    oto = note.Note(otos_right[random_num[i]], quarterLength = 0.25)
    meas.append(oto)
stream_right.append(meas)

##左手
###最初のド
meas = stream.Measure()
n = note.Note("C2", quarterLength = 0.25)
meas.append(n)
###1小節目の残りの音
for i in range(7):
    oto = note.Note(otos_left[random_num[i]], quarterLength = 0.25)
    meas.append(oto)
stream_left.append(meas)

"""
##最初のド
n = note.Note("C4", quarterLength = 0.25)
noteList.append(n)
##1小節目の残りの音
otos = ["D4", "E4", "F4", "G4", "A4", "B4", "C5"]
for i in range(7):
    #r = random.randint(0, 6)
    oto = note.Note(otos[random_num[i]], quarterLength = 0.25)
    noteList.append(oto)
"""

s = stream.Score()
s.append(stream_right)
s.append(stream_left)
s.show('musicxml')

"""
meas = stream.Measure()
meas.append(noteList)
meas.show('musicxml')
"""