#!BPY
# -*- coding: UTF-8 -*-
# MoveKeys By Name
#
# 2016.02.11 Natukikazemizo
import bpy
import math
import re

print("### START ###")

#targetNames = ["0300_01_Ryujo_Tall_T.002", "RJ_Armature", "0300_SD_RJ_T.002", "0300_SD_RJ_Bone", "EB0010_Nothern_T", "EB0010_Nothern_Armature"]
targetNames = ["RJ_Armature","0300_01_Ryujo_Tall_T.002"]
weightDic = {
"Pelvis_T":0,
"ThighHead_T_L":1,
"Thigh_T_L":2,
"Knee_T_L":3,
"Heel_T_L":4,
"Foot_T_L":5,
"BigToe_T_L":6,
"2ndToe_T_L":7,
"3rdToe_T_L":8,
"4thToe_T_L":9,
"LittleToe_T_L":10,
"ThighHead_T_R":1,
"Thigh_T_R":2,
"Knee_T_R":3,
"Heel_T_R":4,
"Foot_T_R":5,
"BigToe_T_R":6,
"2ndToe_T_R":7,
"3rdToe_T_R":8,
"4thToe_T_R":9,
"LittleToe_T_R":10,
"Waist_T":1,
"Waist_P":2,
"Rib_T":3,
"Neck_T":4,
"Neck_P":5,
"Head_T":6,
"Gaze_T_R":7,
"Gaze_T_L":8,
"Shoulder_T_L":4,
"Elbo_T_L":5,
"Arm_T_L":6,
"Arm_P_L":7,
"Hand_T_L":8,
"Thumb_T_L":9,
"Index_T_L":10,
"Middle_T_L":11,
"Ring_T_L":12,
"Little_T_L":13,
"Index_T_L.001":14,
"Middle_T_L.001":15,
"Ring_T_L.001":16,
"Little_T_L.001":17,
"Shoulder_T_R":4,
"Elbo_T_R":5,
"Arm_T_R":6,
"Arm_P_R":7,
"Hand_T_R":8,
"Thumb_T_R":9,
"Index_T_R":10,
"Middle_T_R":11,
"Ring_T_R":12,
"Little_T_R":13,
"Index_T_R.001":14,
"Middle_T_R.001":15,
"Ring_T_R.001":16,
"Little_T_R.001":17
}

span = max(weightDic.values()) + 1

for objName in targetNames:
    for x in bpy.data.objects[objName].animation_data.action.fcurves:
        print(x.data_path)
        dicIndex = x.data_path.replace("pose.bones[\"", "").replace("\"].location", "")
        print(dicIndex in weightDic)
        for y in x.keyframe_points:
            if dicIndex in weightDic:
                y.co[0] = math.floor(y.co[0]) + weightDic[dicIndex] * 0 / span
            # QUAD,CUBIC,BEZIER
            y.interpolation = 'BEZIER'
            # y.easing = 'AUTO'

print("### END ###")