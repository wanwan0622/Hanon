# -*- coding: utf-8 -*-
from music21 import *
import numpy
import matplotlib
import scipy
import random

#難易度調整
## E => 簡単, D => 難しい
print("難易度を入力してください")
print("簡単ならEを、難しいならDを入力してください")
diff = str(input())


#乱数生成
random_num = [-1 for _ in range(8)]
random_num[0] = 0
if diff == 'E':
    for i in range(1,8):
        random_num[i] = random.randint(1, 3)
        if i >= 1: #前の音符と同じ音符がかぶらないようにする
            while True:
                if random_num[i] != random_num[i-1]:
                    break
                else:
                    random_num[i] = random.randint(1, 3)
        if i == 7: #小節の最後の音が次の小節の最初の音とかぶらないようにする
            while random_num[i] == random_num[0] + 1:
                random_num[i] = random.randint(1, 3)
if diff == 'D':
    for i in range(1,8):
        random_num[i] = random.randint(4, 7)
        if i >= 1: #前の音符と同じ音符がかぶらないようにする
            while True:
                if random_num[i] != random_num[i-1]:
                    break
                else:
                    random_num[i] = random.randint(4, 7)
        if i == 7: #小節の最後の音が次の小節の最初の音とかぶらないようにする
            while random_num[i] == random_num[0] + 1:
                random_num[i] = random.randint(4, 7)


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

sounds = ["C1", "D1", "E1", "F1", "G1", "A1", "B1", "C2", "D2", "E2", "F2", "G2", "A2", "B2", "C3", "D3", "E3", "F3", "G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5", "B5", "C6"]



##右手
for i in range(14): #のぼり
    ###1小節目
    meas = stream.Measure()
    for j in range(8):
        n_right_up = note.Note(sounds[random_num[j] + 14 + i], quarterLength = 0.25)
        meas.append(n_right_up)
    stream_right.append(meas)

for i in range(14): #くだり
    ###1小節目
    meas = stream.Measure()
    x = 18
    for j in range(8):
        if j == 0:
            n_right_down = note.Note(sounds[x + 14 - i], quarterLength = 0.25)
        else:
            n_right_down = note.Note(sounds[x - random_num[j] + 14 - i], quarterLength = 0.25)
        meas.append(n_right_down)
    stream_right.append(meas)

###最後の小節
meas = stream.Measure()
n = note.Note("C3", quarterLength = 2)
meas.append(n)
stream_right.append(meas)


##左手
for i in range(14): #のぼり
    ###1小節目
    meas = stream.Measure()
    for j in range(8):
        n_left_up = note.Note(sounds[random_num[j] + 7 + i], quarterLength = 0.25)
        meas.append(n_left_up)
    stream_left.append(meas)

for i in range(14): #くだり
    ###1小節目
    meas = stream.Measure()
    x = 18
    for j in range(8):
        if j == 0:
            n_left_down = note.Note(sounds[x + 7 - i], quarterLength = 0.25)
        else:
            n_left_down = note.Note(sounds[x - random_num[j] + 7 - i], quarterLength = 0.25)
        meas.append(n_left_down)
    stream_left.append(meas)

###最後の小節
meas = stream.Measure()
n = note.Note("C2", quarterLength = 2)
meas.append(n)
stream_left.append(meas)


##最後のおまじない
s = stream.Score()
s.append(stream_right)
s.append(stream_left)
s.show('musicxml')
