# -*- coding: utf-8 -*-
from music21 import *
import numpy
import matplotlib
import scipy
import random



#乱数生成
random_num = [-1 for _ in range(8)]
random_num[0] = 0
for i in range(1,8):
    random_num[i] = random.randint(1, 7)
    if i >= 1: #前の音符と同じ音符がかぶらないようにする
        while True:
            if random_num[i] != random_num[i-1]:
                break
            else:
                random_num[i] = random.randint(1, 7)



#楽譜をかくよ

##なんか最初のおまじない
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

otos = ["C2", "D2", "E2", "F2", "G2", "A2", "B2", "C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5", "B5", "C6"]



##右手
for i in range(14):
    ###1小節目
    meas = stream.Measure()
    n0 = note.Note(otos[random_num[0] + 7 + i], quarterLength = 0.25)
    meas.append(n0)
    n1 = note.Note(otos[random_num[1] + 7 + i], quarterLength = 0.25)
    meas.append(n1)
    n2 = note.Note(otos[random_num[2] + 7 + i], quarterLength = 0.25)
    meas.append(n2)
    n3 = note.Note(otos[random_num[3] + 7 + i], quarterLength = 0.25)
    meas.append(n3)
    n4 = note.Note(otos[random_num[4] + 7 + i], quarterLength = 0.25)
    meas.append(n4)
    n5 = note.Note(otos[random_num[5] + 7 + i], quarterLength = 0.25)
    meas.append(n5)
    n6 = note.Note(otos[random_num[6] + 7 + i], quarterLength = 0.25)
    meas.append(n6)
    n7 = note.Note(otos[random_num[7] + 7 + i], quarterLength = 0.25)
    meas.append(n7)
    stream_right.append(meas)


##左手
for i in range(14):
    ###1小節目
    meas = stream.Measure()
    n0 = note.Note(otos[random_num[0] + i], quarterLength = 0.25)
    meas.append(n0)
    n1 = note.Note(otos[random_num[1] + i], quarterLength = 0.25)
    meas.append(n1)
    n2 = note.Note(otos[random_num[2] + i], quarterLength = 0.25)
    meas.append(n2)
    n3 = note.Note(otos[random_num[3] + i], quarterLength = 0.25)
    meas.append(n3)
    n4 = note.Note(otos[random_num[4] + i], quarterLength = 0.25)
    meas.append(n4)
    n5 = note.Note(otos[random_num[5] + i], quarterLength = 0.25)
    meas.append(n5)
    n6 = note.Note(otos[random_num[6] + i], quarterLength = 0.25)
    meas.append(n6)
    n7 = note.Note(otos[random_num[7] + i], quarterLength = 0.25)
    meas.append(n7)
    stream_left.append(meas)



##最後のおまじない
s = stream.Score()
s.append(stream_right)
s.append(stream_left)
s.show('musicxml')
