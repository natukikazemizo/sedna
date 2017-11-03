#!BPY
# -*- coding: UTF-8 -*-
# Auto BreakDown on Piano
#
# 2017.10.29 Natukikazemizo

import bpy
import os
import utils_log

# CONSTANTS
SCENE_NAME = "Root.DorothyLoris"

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

LH_NOTE_CTRLS = ["Thumb_T.L.001",
        "Index_T.L.001",
        "Middle_T.L.001",
        "Ring_T.L.001",
        "Little_T.L.001"]
RH_NOTE_CTRLS = ["Thumb_T.R.001",
        "Index_T.R.001",
        "Middle_T.R.001",
        "Ring_T.R.001",
        "Little_T.R.001"]

AUTO_BONE_LIST = LH_NOTE_CTRLS + RH_NOTE_CTRLS

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

#functions
def find_data_path(bone_name_list, data_path):
    for x in bone_name_list:
        if data_path == 'pose.bones["' + x + '"].location':
            return True, x
    return False, ""

def get_bone_name(data_path):
    if "].location" in data_path:
        index = data_path.find('"')
        str = data_path[index + 1:]
        index = str.find('"')
        str = str[:index]
        return str
    else:
        return ""

def get_art(art_dic, frame):
    art = ""
    for key, value in art_dic.items():
        if key * FRAME_PAR_MEASURE + START_FRAME > frame:
            break
        art = value
    return art

def add_keyframe_point(keyframe_points, frame, value):
    keyframe_points.add(1)
    index = len(keyframe_points) - 1
    keyframe_points[index].type =  "BREAKDOWN"
    keyframe_points[index].co =  frame, value
    keyframe_points[index].handle_left = frame - 0.5, 0
    keyframe_points[index].handle_right = frame + 0.5, 0

def is_play(bone_name, x, y, z):
    if bone_name in ["Thumb_T.L.001", "Thumb_T.R.001"]:
        if z < - 0.015:
            return True
        else:
            return False
    elif bone_name in ["Index_T.L.001", "Middle_T.L.001", "Ring_T.L.001", "Little_T.L.001"]:
        if x > - 0.001:
            return True
        else:
            return False
    elif bone_name in ["Index_T.R.001", "Middle_T.R.001", "Ring_T.R.001", "Little_T.R.001"]:
        if x < 0.001:
            return True
        else:
            return False
    else:
        return False

def get_note_start_frame(art, frame):
    return frame - ART_DIC[art][0]

def get_note_end_frame(art, frame, next_frame):
    note_end = 0
    if ART_DIC[art][1] > 0:
        note_end = frame + ART_DIC[art][1]
    else:
        note_end = next_frame - ART_DIC[art][1]
    return note_end

def add_note(fcurves, fcurve_index_dic, bone_name, art, frame, next_frame, pre, post):
    note_start = get_note_start_frame(art, frame)
    note_end = get_note_end_frame(art, frame, next_frame)

    for i, index in enumerate(fcurve_index_dic[bone_name]):
        add_keyframe_point(fcurves[index].keyframe_points, note_start, pre[i])
        add_keyframe_point(fcurves[index].keyframe_points, note_end, post[i])
        fcurves[index].update()

def create_breakdown(fcurves, fcurve_index_dic, bone_name, frame, next_frame):
    if frame >= START_FRAME:
        newBreakdownList = []
        art = ""
        if bone_name in LH_NOTE_CTRLS:
            art = get_art(D_LH_ART, frame)
        else:
            art = get_art(D_RH_ART, frame)
        if bone_name == "Middle_T.L.001":
            print("frame:" + str(frame) + ",bone_name:" + bone_name + ",art:" + art)

        bpy.context.scene.frame_set(frame)
        bones = bpy.data.objects[ARMATURE_NAME].pose.bones

        if bone_name == "Middle_T.L.001":
            loc = bones["Middle_T.L.001"].location
            pre =[loc[0] * 4, loc[1], loc[2]]
            post = [loc[0] * 3, loc[1], loc[2]]

            add_note(fcurves, fcurve_index_dic, bone_name, art, frame, next_frame, pre, post)

            loc = bones["Middle_T.L"].location
            pre = [loc[0] / 3, loc[1], loc[2]]
            post = [loc[0] / 2, loc[1], loc[2]]
            add_note(fcurves, fcurve_index_dic, "Middle_T.L", art, frame, next_frame, pre, post)

global logger

# init logger
logger = utils_log.Util_Log(os.path.basename(__file__))


logger.start()
cnt = 0
axis = ""
keyframeDic = {}
fcurveList = []
fcurve_index_dic = {}

act = bpy.data.objects[ARMATURE_NAME].animation_data.action


# delete all old breakdowns and create fcurve_index_dictionary
for fcurve_index, x in enumerate(act.fcurves):
    oldBreakdownList = []

    bone_name = get_bone_name(x.data_path)

    if bone_name != "":
        if bone_name in fcurve_index_dic:
            fcurve_index_dic[bone_name].append(fcurve_index)
        else:
            fcurve_index_dic.update({bone_name:[fcurve_index]})

    for i, y in enumerate(x.keyframe_points):
        if y.type == "BREAKDOWN":
            oldBreakdownList.append(i)

    if len(oldBreakdownList) > 0:
        oldBreakdownList.reverse()
        for y in oldBreakdownList:
            x.keyframe_points.remove(x.keyframe_points[y])
        x.update()



# create breakdown
for fcurve_index, x in enumerate(act.fcurves):
    if cnt == 0:
        keyframeDic = {}
        fcurveIndexList = []

    isFind, bone_name = find_data_path(AUTO_BONE_LIST, x.data_path)
    if isFind:
        keyframeList = []

        fcurveList.append(fcurve_index)

        cnt += 1
        if cnt == 1:
            axis = "X"
        if cnt == 2:
            axis = "Y"
        if cnt == 3:
            axis = "Z"
            cnt = 0

        # read all keyframe of ONE f-curve
        for i, y in enumerate(x.keyframe_points):
            if y.type == "KEYFRAME":
                keyframeList.append([y.co[0], y.co[1]])

        # add keyframes on dic
        keyframeDic.update({axis:keyframeList})

        if axis == "Z":
            if bone_name in LH_NOTE_CTRLS or bone_name in RH_NOTE_CTRLS:
                for i, y in enumerate(keyframeDic["X"]):
                    #SKIP LAST ELEMENT
                    if i == len(keyframeList) - 1:
                        break

                    frame = y[0]
                    loc_x = y[1]
                    loc_y = keyframeDic["Y"][i][1]
                    loc_z = keyframeDic["Z"][i][1]

                    if is_play(bone_name, loc_x, loc_y, loc_z):
                        create_breakdown(act.fcurves, fcurve_index_dic, bone_name, frame, \
                                      keyframeDic["X"][i + 1][0])


logger.end()

