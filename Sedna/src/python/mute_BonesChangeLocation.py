#!BPY
# -*- coding: UTF-8 -*-
# Lock Location of SelectedBones with Pose Mode
#
# 2017.02.05 Natukikazemizo
import bpy
import datetime

print(datetime.datetime.today().\
strftime("%Y/%m/%d(%A) %H:%M:%S.%f") + "### START ###")

for x in bpy.context.selected_pose_bones:
    x.lock_location[0]=True
    x.lock_location[1]=True
    x.lock_location[2]=True
    print(x.name + "Lock Location")
print(datetime.datetime.today().\
strftime("%Y/%m/%d(%A) %H:%M:%S.%f") + "### END ###")
