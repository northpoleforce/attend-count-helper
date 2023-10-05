import pandas as pd
import numpy as np
import os
from datetime import datetime


current_directory = os.getcwd()
file_list = os.listdir(current_directory)
# print(file_list)

file_path = ""

for file_name in file_list:
    if file_name.endswith('.xlsx') and file_name.startswith('月度汇总'):
        file_path = os.path.join(current_directory, file_name)
        # df = pd.read_excel(file_path)
        # print(f"文件名: {file_name}")
        # print(df)  # 打印读取的 Excel 内容

# 指定Excel文件的路径
# excel_file_path = '月度汇总.xlsx'

# 使用pandas读取Excel文件
df = pd.read_excel(file_path)

# 打印读取的数据框（DataFrame）
# print(df)
# print(type(df))
df_value = df.values
# print(type(df_value))
# print(df_value)
# print(df_value[1])
# array_2d = np.empty((len(df_value)-1, 4))
array_2d = np.zeros((1, 4))
# print(array_2d, type(array_2d))
for info in df_value[1:]:
    # print(info)
    # print(type(info))
    days_bigger2 = 0
    for data in info[3:]:
        # print(data, type(data))
        # data = str(data)
        time_list = data.split(",")
        # print(time_list, type(time_list), len(time_list))
        list_len = len(time_list)
        total_time = 0
        if list_len > 1:
            for time_value in time_list:
                # time_str = '2023-10-05 14:30:00'
                # time_obj = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
                time_obj = datetime.strptime(time_value, '%H:%M')
                # print(time_obj)
            for i in range(0, list_len, 2):
                time_in = datetime.strptime(time_list[i-1], '%H:%M')
                time_out = datetime.strptime(time_list[i], '%H:%M')
                total_time += -(time_out-time_in).total_seconds()/60/60
        # print("total_time", total_time)
        if total_time >= 2:
            days_bigger2 += 1
    # print(info[0], days_bigger2)
    arr = np.array([info[0], info[1], info[2], days_bigger2])
    # print(arr, type(arr))
    array_2d = np.vstack((array_2d, arr))
# print(array_2d)
array_2d = array_2d[1:]
# print(array_2d)
# array_2d = np.array([[1, 2, 3],
#                      [4, 5, 6]])
# array_1d = np.array([7, 8, 9])
# 使用 vstack 垂直堆叠将一维数组添加到二维数组中
# result = np.vstack((array_2d, array_1d))
columns = ['姓名', '出勤天数', '出勤总时长', '出勤天数(2h+)']
new_df = pd.DataFrame(array_2d, columns=columns, index=None)
# print(new_df)
new_df.to_excel('output.xlsx', index=False)