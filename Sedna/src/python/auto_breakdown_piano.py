#!BPY
# -*- coding: UTF-8 -*-
# Auto BreakDown on Piano
#
# 2017.10.29 Natukikazemizo

import bpy
import os
import utils_log

# CONSTANTS
# Articulation Dictionary
ART_DIC = {
    "NR":[1, -7],
    "SL":[1, -5],
    "TN":[1, -3],
    "ST":[1, 1]
}

START_FRAME = 3048
FRAME_PAR_MEASURE = 48
MEASURE = 2

AUTO_BONE_LIST = ["Middle_T.L", "Middle_T.L.001"]
#AUTO_BONE_LIST = ["Middle_T.L"]

# PARAMETER
ARMATURE_NAME = "Dorothy.Armature"

D_RH_ART = {
0:"NR",
0.75:"ST",
1.125:"NR",
1.875:"ST",
2.5:"NR",
2.875:"ST",
3:"NR",
3.75:"TN",
}

# MAY UNUSE
D_RH_REST = {
1.125:0.625,
3.5:0.25
}

D_LH_ART = {
0:"ST",
3.75:"TN",
}

# MAY UNUSE
D_LH_REST = {
0:0
}

def find_data_path(bone_name_list, data_path):
    for x in bone_name_list:
        if data_path == 'pose.bones["' + x + '"].location':
            return True, x
    return False, ""

def get_art(art_dic, frame):
    art = ""
    for key, value in art_dic.items():
        art = value
        if key * FRAME_PAR_MEASURE + START_FRAME >= frame:
            break
    return art

def add_keyframe_point(keyframe_points, frame, value):
    keyframe_points.add(1)
    index = len(keyframe_points) - 1
    keyframe_points[index].type =  "BREAKDOWN"
    keyframe_points[index].co =  frame, value
    keyframe_points[index].handle_left = frame - 0.5, 0
    keyframe_points[index].handle_right = frame + 0.5, 0


# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))


logger.start()
cnt = 0
axis = ""

for x in bpy.data.objects[ARMATURE_NAME].animation_data.action.fcurves:
    oldBreakdownList = []
    keyframeList = []
    isFind, bone_name = find_data_path(AUTO_BONE_LIST, x.data_path)
    if isFind:
        cnt += 1
        if cnt == 1:
            axis = "X"
        if cnt == 2:
            axis = "Y"
        if cnt == 3:
            axis = "Z"
            cnt = 0

        if axis == "X":
            for i, y in enumerate(x.keyframe_points):
                if y.type == "BREAKDOWN":
                    oldBreakdownList.append(i)
                elif y.type == "KEYFRAME":
                    keyframeList.append([y.co[0], y.co[1]])
            
            # delete breakdown
            oldBreakdownList.reverse()
            for y in oldBreakdownList:
                x.keyframe_points.remove(x.keyframe_points[y])

            if len(oldBreakdownList) > 0:
                x.update()

            # create breakdown
            newBreakdownList = []
            for i, y in enumerate(keyframeList):
                # skip last keyframe
                if i == len(keyframeList) - 1:
                    break
                
                if y[0] >= START_FRAME:
                    art = get_art(D_LH_ART, y[0])
                    
                    value = 0
                    if bone_name == "Middle_T.L":
                        value = y[1] / 2
                    elif bone_name == "Middle_T.L.001":
                        value = y[1] * 3

                    add_keyframe_point(x.keyframe_points, y[0] - ART_DIC[art][0], value)
                    
                    note_end = 0
                    if ART_DIC[art][1] > 0:
                        note_end = y[0] + ART_DIC[art][1]
                    else:
                        note_end = keyframeList[i + 1][0] - ART_DIC[art][1]
                    
                    add_keyframe_point(x.keyframe_points, note_end, value)

            if len(keyframeList) > 0:
                x.update()

# bpy.data.objects[ARMATURE_NAME].pose.bones


logger.end()

