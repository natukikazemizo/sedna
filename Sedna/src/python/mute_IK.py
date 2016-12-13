#!BPY
# -*- coding: UTF-8 -*-
# Mute IK of SelectedBones with Pose Mode
#
# 2016.10.08 Natukikazemizo
import bpy
import datetime

print(datetime.datetime.today().\
strftime("%Y/%m/%d(%A) %H:%M:%S.%f") + "### START ###")

for x in bpy.context.selected_pose_bones:
    if "IK" in x.constraints:
        x.constraints["IK"].mute = True
        print(x.name + "IK muted")
print(datetime.datetime.today().\
strftime("%Y/%m/%d(%A) %H:%M:%S.%f") + "### END ###")
