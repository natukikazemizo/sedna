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
    "NR":[1, -3],
    "SL":[1, -2],
    "TN":[1, -1],
    "ST":[1, 2]
}

START_FRAME = 3048
FRAME_PAR_MEASURE = 48
MEASURE = 2

LH_NOTE_THUMB = ["Thumb_T.L.001"]

LH_NOTE_INDEX_2_LITTLE = [
    "Index_T.L.002",
    "Middle_T.L.002",
    "Ring_T.L.002",
    "Little_T.L.002"]

LH_NOTE_CTRLS = LH_NOTE_THUMB + LH_NOTE_INDEX_2_LITTLE

RH_NOTE_THUMB = ["Thumb_T.R.001"]

RH_NOTE_INDEX_2_LITTLE = [
    "Index_T.R.002",
    "Middle_T.R.002",
    "Ring_T.R.002",
    "Little_T.R.002"]

RH_NOTE_CTRLS = RH_NOTE_THUMB + RH_NOTE_INDEX_2_LITTLE

AUTO_BONE_LIST = LH_NOTE_CTRLS + RH_NOTE_CTRLS

#Classes
class Note:
    loc = [[],[],[],]
    def __init__(self, art, frame, next_frame):
        self.art = art
        self.frame = frame
        self.next_frame = next_frame

class Art:
    def __init__(self, measure, art):
        self.measure = measure
        self.art = art


# PARAMETER
ARMATURE_NAME = "Dorothy.Armature"

D_RH_ART = [
Art(0.000, "NR"),
Art(0.750, "ST"),
Art(1.125, "NR"),
Art(1.875, "ST"),
Art(2.500, "NR"),
Art(2.875, "ST"),
Art(3.000, "NR"),
Art(3.750, "TN")
]

## MAY UNUSE
#D_RH_REST = {
#1.125:0.625,
#3.5:0.25
#}

D_LH_ART = [
Art(0.000, "ST"),
Art(3.750, "TN")
]

## MAY UNUSE
#D_LH_REST = {
#0:0
#}

#globals
global logger
global bones
global bodyModionDic




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

def get_art(art_list, frame):
    art = ""
    for x in art_list:
        if x.measure * FRAME_PAR_MEASURE + START_FRAME > frame:
            break
        art = x.art
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
    elif bone_name in LH_NOTE_INDEX_2_LITTLE:
        if x > - 0.001:
            return True
        else:
            return False
    elif bone_name in RH_NOTE_INDEX_2_LITTLE:
        if x < 0.001:
            return True
        else:
            return False
    else:
        return False

def get_note_frames(note):
    frames = []
    start = 0
    leave = 0
    end = 0
    
    start =  note.frame - ART_DIC[note.art][0]
    
    if ART_DIC[note.art][1] > 0:
        end = note.frame + ART_DIC[note.art][1]
    else:
        end = note.next_frame + ART_DIC[note.art][1]
    
    if start + 2 > end:
        end = start + 2
    
    leave = end - 1

    return [start, leave, end]

def add_note(fcurves, fcurve_index_dic, bone_name, note):
    locs = [[],[],[]]

    frames = get_note_frames(note)
    add_keyframes_fcurve(fcurves, fcurve_index_dic, bone_name, note.art, frames, note.loc)
    
    # logging
    print(str(note.frame)+ " art:" + note.art + " " + bone_name)

    # get left or right and sign
    lr = "L"
    sign = 1
    if bone_name in RH_NOTE_CTRLS:
        lr = "R"
        sign = -1

    # add motion on Hand
    t_name = "Hand_T." + lr
    if update_breakdown_dic(t_name, frames[0]):
        loc = bones[t_name].location
        locs[0] = [loc[0], loc[1] + 0.0008, loc[2]]
        locs[1] = [loc[0], loc[1], loc[2]]
        locs[2] = [loc[0], loc[1] + 0.0008, loc[2]]
        frames_hand = [frames[0] - 1, frames[1], frames[2] - 1]
        
        add_keyframes_fcurve(fcurves, fcurve_index_dic, t_name, note.art, frames_hand, locs)

    # add motion on Arm
    t_name = "Arm_T." + lr
    if update_breakdown_dic(t_name, frames[0]):
        loc = bones[t_name].location
        locs[0] = [loc[0] - sign * 0.010, loc[1], loc[2]]
        locs[1] = [loc[0], loc[1], loc[2]]
        locs[2] = [loc[0] - sign * 0.008, loc[1], loc[2]]
        frames_arm = [frames[0] - 2, frames[1], frames[2]]

        add_keyframes_fcurve(fcurves, fcurve_index_dic, t_name, note.art, frames_arm, locs)

    # add motion on Elbo
    t_name = "Elbo_T." + lr
    if update_breakdown_dic(t_name, frames[0]):
        loc = bones[t_name].location
        locs[0] = [loc[0] -sign * 0.005, loc[1] - 0.01, loc[2] + sign * 0.01]
        locs[1] = [loc[0], loc[1], loc[2]]
        locs[2] = [loc[0] -sign * 0.005, loc[1] - 0.01, loc[2] + sign * 0.01]
        frames_arm = [frames[0] - 1, frames[1], frames[2]]

        add_keyframes_fcurve(fcurves, fcurve_index_dic, t_name, note.art, frames_arm, locs)

    # add motion on Shoulder_
    t_name = "Shoulder_T." + lr
    if update_breakdown_dic(t_name, frames[0]):
        loc = bones[t_name].location
        locs[0] = [loc[0], loc[1] + 0.0010, loc[2]]
        locs[1] = [loc[0], loc[1], loc[2]]
        locs[2] = [loc[0], loc[1] + 0.0008, loc[2]]
        frames_arm = [frames[0] - 1, frames[1], frames[2]]

        add_keyframes_fcurve(fcurves, fcurve_index_dic, t_name, note.art, frames_arm, locs)



def add_keyframes_fcurve(fcurves, fcurve_index_dic, bone_name, art, frames, locs):
    for i, index in enumerate(fcurve_index_dic[bone_name]):
        add_keyframe_point(fcurves[index].keyframe_points, frames[0], locs[0][i])
        add_keyframe_point(fcurves[index].keyframe_points, frames[1], locs[1][i])
        add_keyframe_point(fcurves[index].keyframe_points, frames[2], locs[2][i])
        fcurves[index].update()


def update_breakdown_dic(bone_name, frame):
    ret = False
    if bone_name not in bodyModionDic:
        bodyModionDic.update({bone_name:[]})
        ret = True
    if frame not in bodyModionDic[bone_name]:
        bodyModionDic[bone_name].append(frame)
        ret = True
    return ret
    

def create_breakdown(fcurves, fcurve_index_dic, bone_name, frame, next_frame):
    if frame >= START_FRAME:
        newBreakdownList = []
        art = ""
        if bone_name in LH_NOTE_CTRLS:
            art = get_art(D_LH_ART, frame)
        else:
            art = get_art(D_RH_ART, frame)
            
        note = Note(art, frame, next_frame)

        bpy.context.scene.frame_set(frame)

        loc = bones[bone_name].location
        note.loc[1] = [loc[0], loc[1], loc[2]]

        if bone_name in LH_NOTE_THUMB + RH_NOTE_THUMB:
            # Add Thumb joints Motion
            note.loc[0] =[note.loc[1][0], note.loc[1][1], note.loc[1][2] + 0.020]
            note.loc[2] = [note.loc[1][0], note.loc[1][1], note.loc[1][2] + 0.015]
            add_note(fcurves, fcurve_index_dic, bone_name, note)
        elif bone_name in LH_NOTE_INDEX_2_LITTLE + RH_NOTE_INDEX_2_LITTLE:
            sign = 1
            if bone_name in RH_NOTE_INDEX_2_LITTLE:
                sign = -1
            
            # Add Finger 1st joints Motion
            note.loc[0] =[note.loc[1][0] - 0.003 * sign, note.loc[1][1], note.loc[1][2]]
            note.loc[2] = [note.loc[1][0] - 0.002 * sign, note.loc[1][1], note.loc[1][2]]
            add_note(fcurves, fcurve_index_dic, bone_name, note)

            # Add Finger 2nd joints Motion
            note.loc[0] =[note.loc[1][0] - 0.003 * sign, note.loc[1][1], note.loc[1][2]]
            note.loc[2] = [note.loc[1][0] - 0.002 * sign, note.loc[1][1], note.loc[1][2]]
            add_note(fcurves, fcurve_index_dic, bone_name[:-4] + ".001", note)
            
            # Add Finger 3rd joints Motion
            loc = bones[bone_name[:-4]].location
            note.loc[1] = [loc[0], loc[1], loc[2]]
            note.loc[0] = [note.loc[1][0] + 0.002 * sign, note.loc[1][1], note.loc[1][2]]
            note.loc[2] = [note.loc[1][0] + 0.0025 * sign, note.loc[1][1], note.loc[1][2]]
            add_note(fcurves, fcurve_index_dic, bone_name[:-4], note)


# init logger
logger = utils_log.Util_Log(os.path.basename(__file__))
bones = bpy.data.objects[ARMATURE_NAME].pose.bones
bodyModionDic = {}

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

