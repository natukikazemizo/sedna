#!BPY
# -*- coding: UTF-8 -*-
# Auto BreakDown on Piano
#
# 2017.10.29 Natukikazemizo

import bpy
import os
import utils_log

# CONSTANTS
ART_NORMAL = "NR"
ART_SLUR = "SL"
ART_TENUTO = "TN"
ART_STACCATO = "ST"

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
D_RH_REST = {
1.125:0.625,
3.5:0.25
}

D_LH_ART = {
0:"ST",
3.75:"TN",
}
D_LH_REST = {
0:0
}

def find_data_path(bone_name_list, data_path):
    for x in bone_name_list:
        if data_path == 'pose.bones["' + x + '"].location':
            return True, x
    return False, ""

# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))


logger.start()
cnt = 0
axis = ""
newBreakdownList = []

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
            print(x.data_path + " " + axis)
            
            for i, y in enumerate(x.keyframe_points):
                if y.type == "BREAKDOWN":
                    oldBreakdownList.append(i)
                elif y.type == "KEYFRAME":
                    keyframeList.append([y.co[0], y.co[1]])
            print(oldBreakdownList)
            print(keyframeList)
            
            # delete breakdown
            print("delete from" + bone_name)
            bone = bpy.data.objects[ARMATURE_NAME].pose.bones[bone_name]
            
            oldBreakdownList.reverse()
            for y in oldBreakdownList:
                #bone.keyframe_delete(data_path = "location", frame = y)
                x.keyframe_points.remove(x.keyframe_points[y])

            if len(keyframeList) > 0:
                x.keyframe_points.update()

            # create breakdown
            newBreakdownList = []
            for y in keyframeList:
                if y[0] >= START_FRAME:
                    print(y)
                    x.keyframe_points.add(1)
                    index = len(x.keyframe_points) - 1
                    x.keyframe_points[index].type =  "BREAKDOWN"
                    if bone_name == "Middle_T.L":
                        x.keyframe_points[index].co =  y[0] + 1, y[1] / 2
                        #x.keyframe_points[index].co =  y[0] + 3, -0.1
                        x.keyframe_points[index].handle_left = y[0] + 0.5, 0
                        x.keyframe_points[index].handle_right = y[0] + 1.5, 0
                        #print("x.keyframe_points[index - 1].co[0]" + str(x.keyframe_points[index - 1].co[0]) )
                        #print("handle_left:" + str(x.keyframe_points[index - 1].handle_left) + "," +  str(x.keyframe_points[index].handle_left))
                        #print("handle_right:" + str(x.keyframe_points[index - 1].handle_right) + "," + str(x.keyframe_points[index].handle_right))
                        #bone.location = 0, bone.location[1], bone.location[2]
                        #bone.keyframe_insert(data_path = "location", frame = y[0] + 1)
                    else:
                        x.keyframe_points[index].co =  y[0] + 1, y[1] * 3
                        x.keyframe_points[index].handle_left = y[0] + 0.5, 0
                        x.keyframe_points[index].handle_right = y[0] + 1.5, 0
                        #bone.location = bone.location[0] * 2, bone.location[1], bone.location[2]
                        #bone.keyframe_insert(data_path = "location", frame = y[0] + 1)
                    newBreakdownList.append(y[0] + 1)

            if len(keyframeList) > 0:
                #x.keyframe_points.update()
                x.update()
            
            for y in x.keyframe_points:
                if y.co[0] in newBreakdownList:
                    y.type = "BREAKDOWN"
#        elif axis == "Y" or axis == "Z":
#            for y in x.keyframe_points:
#                if y.co[0] in newBreakdownList:
#                    y.type = "BREAKDOWN"
#            x.keyframe_points.update()

# bpy.data.objects[ARMATURE_NAME].pose.bones


logger.end()

