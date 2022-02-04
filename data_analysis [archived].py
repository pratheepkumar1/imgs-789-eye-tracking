import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gaze_data = pd.read_csv('gaze_positions.csv')
print(gaze_data.head(5))
gaze_data.sort_values(["gaze_timestamp"], 
                    ascending=[True], 
                    inplace=True)

# print(gaze_data.filter(gaze_data['gaze_timestamp'] <= 2251.088394))

# def getFrameNum(time_sec):
#     frame = (time_sec*60) + gaze_data['gaze_timestamp'].iloc[0]
#     gaze_data['gaze_timestamp'].sub(frame).abs().idxmin()
#     return     

# print(gaze_data.loc[(gaze_data['gaze_timestamp'] == getFrameNum(2))])


# Getting the calibrated time sequence
plTime_fr = np.array((gaze_data['gaze_timestamp'] - gaze_data['gaze_timestamp'].iloc[0])/60)
print(plTime_fr)



# calibration_values = gaze_data.iloc[gaze_data['gaze_timestamp'] == getFrameNum(0):gaze_data['gaze_timestamp'] == getFrameNum(1.88)]
# print(calibration_values)

#Converting cartesan to spherical coordinates


