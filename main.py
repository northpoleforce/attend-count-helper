import pandas as pd
import numpy as np
import os
from datetime import datetime


current_directory = os.getcwd()
file_list = os.listdir(current_directory)
file_path = ""
for file_name in file_list:
    if file_name.endswith('.xlsx') and file_name.startswith('月度汇总'):
        file_path = os.path.join(current_directory, file_name)


df = pd.read_excel(file_path)
df_value = df.values


array_2d = np.zeros((1, 4))
for info in df_value[1:]:
    days_bigger2 = 0
    for data in info[3:]:
        time_list = data.split(",")
        list_len = len(time_list)
        total_time = 0
        if list_len > 1:
            for i in range(0, list_len, 2):
                time_in = datetime.strptime(time_list[i-1], '%H:%M')
                time_out = datetime.strptime(time_list[i], '%H:%M')
                total_time += -(time_out-time_in).total_seconds()/60/60
        if total_time >= 2:
            days_bigger2 += 1
    arr = np.array([info[0], info[1], info[2], days_bigger2])
    array_2d = np.vstack((array_2d, arr))
array_2d = array_2d[1:]


columns = ['姓名', '出勤天数', '出勤总时长', '出勤天数(2h+)']
new_df = pd.DataFrame(array_2d, columns=columns)
new_df.to_excel('output.xlsx', index=False)