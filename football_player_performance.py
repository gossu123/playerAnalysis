"""Performance Analysis of Football Player"""
import math
import pandas as pd
A = pd.read_csv('football_player.csv', sep=";", header=1)
X = A['LINEAR ACCELERATION X (m/s²)']
Y = A['LINEAR ACCELERATION Y (m/s²)']
Z = A['LINEAR ACCELERATION Z (m/s²)']
T = A['Time since start in ms ']
P = (X*X)+(Y*Y)+(Z*Z)
ACC = P.apply(math.sqrt)
ACC = (ACC-ACC.mean())/ACC.std()
ACC = pd.Series(ACC)
TI = []
TI.append((T[0]-0)/1000)
for j in range(len(T)-1):
    TI.append((T[j+1]-T[j])/1000)
TI = pd.Series(TI)


def peaks(axl):
    """For count of peaks"""
    peak = 0
    for k in range(1, len(axl)-1):
        if axl[k-1] < axl[k] and axl[k] > axl[k+1]:
            peak += 1
    return peak


STEPS = peaks(-1*ACC) + peaks(ACC)
print("Number of steps: ", STEPS)
STRIDE_LENGTH = 0.85  # using Sanket's analysis
DISTANCE = (STEPS*STRIDE_LENGTH)/1000
print("Total Distance Covered: ", DISTANCE, "KM")
AVR_SPEED = DISTANCE*1000*3600/T[len(T)-1]
print("Average speed of player: ", AVR_SPEED, "KMPH")
INST_IMPULSE = []
for i in range(len(ACC)-1):
    INST_IMPULSE.append(ACC[i]*TI[i]*0.43)
INST_IMPULSE = pd.Series(INST_IMPULSE)
print("Maximum impulse applied on ball: ", INST_IMPULSE.max(), "N-s")
