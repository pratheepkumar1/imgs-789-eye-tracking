import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gaze_data = pd.read_csv('gaze_positions.csv')
gaze_data.sort_values(["gaze_timestamp"], 
                    ascending=[True], 
                    inplace=True)
plTime_fr = np.array((gaze_data['gaze_timestamp'] - gaze_data['gaze_timestamp'].iloc[0])/60)
print(plTime_fr)

def getFrameNum(time_sec):
    frame = (time_sec*60) + gaze_data['gaze_timestamp'].iloc[0]
    return frame

calibration_values = gaze_data.iloc[gaze_data['gaze_timestamp'] == getFrameNum(0):gaze_data['gaze_timestamp'] == getFrameNum(1.88)]
print(calibration_values)