import os
import pandas as pd
import csv
import cv2
from load_save_model import read_model
from numpy import load
import numpy as np
path = r"D:\MTCNNPro\inforuser/infor.csv"
# data = {"StudentCode": ["100", "101","102","103","104","105","106"],
#         "Name":["Colin_Powell", "Donald_Rumsfeld", "George_W_Bush", "Gerhard_Schroeder", "LeVu", "TranNhan", "Tony_Blair"]}
# df_data = pd.DataFrame(data)
# df_data.to_csv(path, index=False)
# with open(path) as f:
#         user = []
#         data = csv.reader(f)
#         rows = [r for r in data]
#         i = 0
#         for row in rows:
#                 if "TranNhan" == row[1]:
#                         user.append(row[0])
#                         user.append(row[1])
#
#         print (type(user[1]))

