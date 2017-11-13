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
    "NR":[1, -2],
    "SL":[1, -1],
    "TN":[1, -1],
    "ST":[1, 2]
}

START_FRAME = 3048
END_FRAME = 3143
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

class NoteOnHand:
    def __init__(self, start_frame):
        self.start_frame = start_frame
        self.thumb = -1
        self.index = -1
        self.middle = -1
        self.ring = -1
        self.little = -1

    def set(self, bone_name, end_frame):
        if bone_name == "Thumb_T.L.001" or bone_name == "Thumb_T.R.001":
            self.thumb = end_frame
        elif bone_name == "Index_T.L.002" or bone_name == "Index_T.R.002":
            self.index = end_frame
        elif bone_name == "Middle_T.L.002" or bone_name == "Middle_T.R.002":
            self.middle = end_frame
        elif bone_name == "Ring_T.L.002" or bone_name == "Ring_T.R.002":
            self.ring = end_frame
        elif bone_name == "Little_T.L.002" or bone_name == "Little_T.R.002":
            self.little = end_frame



# PARAMETER
ARMATURE_NAME_LIST = ["Dorothy.Armature", "Loris.Armature"]

RH_ART = {
    "Dorothy.Armature":[
        Art(0.000, "NR"),
        Art(0.750, "ST"),
        Art(1.125, "NR"),
        Art(1.875, "ST"),
        Art(2.500, "NR"),
        Art(2.875, "ST"),
        Art(3.000, "NR"),
        Art(3.750, "TN"),
        Art(4.000, "NR"),
        Art(4.250, "ST"),
        Art(4.500, "NR"),
        Art(5.250, "ST"),
        Art(5.500, "NR"),
        Art(6.000, "ST"),
        Art(6.6875, "NR"),
        Art(6.875, "ST"),
        Art(7.6875, "NR"),
        Art(7.875, "ST"),
        Art(11.250, "NR"),
        Art(11.625, "ST"),
        Art(13.250, "NR"),
        Art(13.625, "ST"),
        Art(15.166, "NR"),
        Art(17.000, "ST"),
        Art(17.125, "NR"),
        Art(18.000, "ST"),
        Art(18.125, "NR"),
        Art(19.000, "ST"),
        Art(24.375, "NR"),
        Art(24.625, "ST"),
        Art(25.250, "SL"),
        Art(25.500, "NR"),
        Art(25.625, "ST"),
        Art(26.375, "NR"),
        Art(26.625, "ST"),
        Art(27.250, "SL"),
        Art(27.500, "NR"),
        Art(27.625, "ST"),
        Art(30.500, "NR"),
        Art(31.125, "ST"),
        Art(31.250, "NR"),
        Art(31.375, "ST"),
        Art(31.500, "NR"),
        Art(31.875, "ST"),
        Art(32.000, "NR"),
        Art(32.125, "ST"),
        Art(32.250, "NR"),
        Art(32.4375, "ST"),
        Art(36.500, "NR"),
        Art(37.000, "ST"),
        Art(38.000, "NR"),
        Art(39.000, "ST"),
        Art(39.125, "NR"),
        Art(40.000, "ST"),
        Art(40.125, "NR"),
        Art(52.000, "ST"),
        Art(57.375, "NR"),
        Art(57.625, "ST"),
        Art(58.250, "SL"),
        Art(58.500, "NR"),
        Art(58.625, "ST"),
        Art(59.375, "NR"),
        Art(59.625, "ST"),
        Art(60.250, "SL"),
        Art(60.500, "NR"),
        Art(60.625, "ST"),
        Art(63.500, "NR"),
        Art(64.125, "ST"),
        Art(64.250, "NR"),
        Art(64.375, "ST"),
        Art(64.500, "NR"),
        Art(64.875, "ST"),
        Art(65.000, "NR"),
        Art(65.125, "ST"),
        Art(65.250, "NR"),
        Art(65.4375, "ST"),
        Art(69.500, "NR"),
        Art(70.000, "ST"),
        Art(71.000, "NR"),
        Art(72.000, "ST"),
        Art(72.125, "NR"),
        Art(73.000, "ST"),
        Art(73.125, "NR"),
        Art(76.000, "ST"),
        Art(76.250, "NR"),
        Art(76.500, "ST")
    ],
    "Loris.Armature":[
        Art(0.000, "ST"),
        Art(1.625, "NR"),
        Art(2.375, "ST"),
        Art(3.000, "NR"),
        Art(3.375, "ST"),
        Art(3.750, "TN"),
        Art(4.000, "NR"),
        Art(4.250, "ST"),
        Art(4.500, "NR"),
        Art(5.250, "ST"),
        Art(5.500, "NR"),
        Art(6.125, "ST"),
        Art(6.250, "NR"),
        Art(6.375, "ST"),
        Art(6.500, "NR"),
        Art(6.875, "ST"),
        Art(7.000, "NR"),
        Art(7.125, "ST"),
        Art(7.250, "NR"),
        Art(7.375, "ST"),
        Art(7.500, "NR"),
        Art(7.875, "ST"),
        Art(8.000, "NR"),
        Art(32.4375, "ST"),
        Art(33.000, "NR"),
        Art(41.000, "ST"),
        Art(41.125, "NR"),
        Art(42.000, "ST"),
        Art(42.125, "NR"),
        Art(48.000, "ST"),
        Art(48.166, "NR"),
        Art(50.000, "ST"),
        Art(50.125, "NR"),
        Art(51.000, "ST"),
        Art(51.125, "NR"),
        Art(65.4375, "ST"),
        Art(66.000, "NR"),
        Art(76.000, "ST"),
        Art(76.250, "NR"),
        Art(76.500, "ST")
    ]
    }

LH_ART = {
    "Dorothy.Armature":[
        Art(0.000, "ST"),
        Art(3.750, "TN"),
        Art(4.000, "NR"),
        Art(4.250, "ST"),
        Art(4.500, "NR"),
        Art(5.250, "ST"),
        Art(5.500, "NR"),
        Art(8.000, "TN"),
        Art(15.000, "ST"),
        Art(15.166, "TN"),
        Art(16.000, "NR"),
        Art(17.000, "SL"),
        Art(17.125, "ST"),
        Art(17.250, "SL"),
        Art(17.375, "ST"),
        Art(17.500, "SL"),
        Art(17.625, "ST"),
        Art(17.750, "SL"),
        Art(17.875, "ST"),
        Art(18.000, "SL"),
        Art(18.125, "ST"),
        Art(18.250, "SL"),
        Art(18.375, "ST"),
        Art(18.500, "SL"),
        Art(18.625, "ST"),
        Art(18.750, "SL"),
        Art(18.875, "ST"),
        Art(19.000, "TN"),
        Art(30.500, "NR"),
        Art(31.000, "ST"),
        Art(31.6875, "NR"),
        Art(31.875, "ST"),
        Art(33.000, "TN"),
        Art(37.000, "ST"),
        Art(38.000, "TN"),
        Art(39.000, "SL"),
        Art(39.125, "ST"),
        Art(39.250, "SL"),
        Art(39.375, "ST"),
        Art(39.500, "SL"),
        Art(39.625, "ST"),
        Art(39.750, "SL"),
        Art(39.875, "ST"),
        Art(40.000, "SL"),
        Art(40.125, "ST"),
        Art(40.250, "SL"),
        Art(40.375, "ST"),
        Art(40.500, "SL"),
        Art(40.625, "ST"),
        Art(40.750, "SL"),
        Art(40.875, "ST"),
        Art(41.000, "NR"),
        Art(48.000, "ST"),
        Art(48.166, "TN"),
        Art(49.000, "NR"),
        Art(52.000, "TN"),
        Art(63.500, "NR"),
        Art(64.000, "ST"),
        Art(64.6875, "NR"),
        Art(64.875, "ST"),
        Art(66.000, "TN"),
        Art(70.000, "ST"),
        Art(71.000, "TN"),
        Art(72.000, "SL"),
        Art(72.125, "ST"),
        Art(72.250, "SL"),
        Art(72.375, "ST"),
        Art(72.500, "SL"),
        Art(72.625, "ST"),
        Art(72.750, "SL"),
        Art(72.875, "ST"),
        Art(73.000, "SL"),
        Art(73.125, "ST"),
        Art(73.250, "SL"),
        Art(73.375, "ST"),
        Art(73.500, "SL"),
        Art(73.625, "ST"),
        Art(73.750, "SL"),
        Art(73.875, "ST"),
        Art(74.000, "TN"),
        Art(76.000, "ST"),
        Art(76.250, "NR"),
        Art(76.500, "ST")
    ],
    "Loris.Armature":[
        Art(0.000, "TN"),
        Art(4.000, "NR"),
        Art(4.250, "ST"),
        Art(4.500, "NR"),
        Art(5.250, "ST"),
        Art(5.500, "NR"),
        Art(6.000, "ST"),
        Art(6.625, "NR"),
        Art(6.875, "ST"),
        Art(7.625, "NR"),
        Art(7.875, "ST"),
        Art(8.000, "NR"),
        Art(32.4375, "ST"),
        Art(33.000, "NR"),
        Art(48.000, "ST"),
        Art(48.166, "NR"),
        Art(50.000, "ST"),
        Art(50.125, "NR"),
        Art(51.000, "ST"),
        Art(51.125, "NR"),
        Art(65.4375, "ST"),
        Art(66.000, "NR"),
        Art(75.000, "TN"),
        Art(75.250, "NR"),
        Art(76.000, "ST"),
        Art(76.250, "NR"),
        Art(76.500, "ST")
    ]
}

#globals
global logger
global bones
global bodyModionDic
global lhNoteDic
global rhNoteDic




#functions
"""find bone_name from from data_path"""
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
    art = art_list[0].art
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
        if z < 0.002:
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
        locs[0] = [loc[0], loc[1] + 0.00005, loc[2]]
        locs[1] = [loc[0], loc[1], loc[2]]
        locs[2] = [loc[0], loc[1] + 0.00005, loc[2]]
        frames_hand = [frames[0], frames[1], frames[2]]

        add_keyframes_fcurve(fcurves, fcurve_index_dic, t_name, note.art, frames_hand, locs)

    # add motion on Arm
    t_name = "Arm_T." + lr
    if update_breakdown_dic(t_name, frames[0]):
        loc = bones[t_name].location
        locs[0] = [loc[0] - sign * 0.010, loc[1], loc[2]]
        locs[1] = [loc[0], loc[1], loc[2]]
        locs[2] = [loc[0] - sign * 0.008, loc[1], loc[2]]
        frames_arm = [frames[0], frames[1], frames[2]]

        add_keyframes_fcurve(fcurves, fcurve_index_dic, t_name, note.art, frames_arm, locs)

    # add motion on Elbo
    t_name = "Elbo_T." + lr
    if update_breakdown_dic(t_name, frames[0]):
        loc = bones[t_name].location
        locs[0] = [loc[0] -sign * 0.005, loc[1] - 0.01, loc[2] + sign * 0.01]
        locs[1] = [loc[0], loc[1], loc[2]]
        locs[2] = [loc[0] -sign * 0.005, loc[1] - 0.01, loc[2] + sign * 0.01]
        frames_arm = [frames[0] - 1, frames[1] - 1, frames[2] - 1]

        add_keyframes_fcurve(fcurves, fcurve_index_dic, t_name, note.art, frames_arm, locs)

    # add motion on Shoulder_
    t_name = "Shoulder_T." + lr
    if update_breakdown_dic(t_name, frames[0]):
        loc = bones[t_name].location
        locs[0] = [loc[0], loc[1] + 0.0010, loc[2]]
        locs[1] = [loc[0], loc[1], loc[2]]
        locs[2] = [loc[0], loc[1] + 0.0008, loc[2]]
        frames_arm = [frames[0] - 2, frames[1] - 2, frames[2] -2]

        add_keyframes_fcurve(fcurves, fcurve_index_dic, t_name, note.art, frames_arm, locs)



def add_keyframes_fcurve(fcurves, fcurve_index_dic, bone_name, art, frames, locs):
    for i, index in enumerate(fcurve_index_dic[bone_name]):
        add_keyframe_point(fcurves[index].keyframe_points, frames[0], locs[0][i])
        add_keyframe_point(fcurves[index].keyframe_points, frames[1], locs[1][i])
        add_keyframe_point(fcurves[index].keyframe_points, frames[2], locs[2][i])
        fcurves[index].update()


def update_breakdown_dic(bone_name, frame):
    global bodyModionDic
    ret = False
    if bone_name not in bodyModionDic:
        bodyModionDic.update({bone_name:[]})
        ret = True
    if frame not in bodyModionDic[bone_name]:
        bodyModionDic[bone_name].append(frame)
        ret = True
    return ret


def create_breakdown(armature_name, fcurves, fcurve_index_dic, bone_name, frame, next_frame):
    if frame >= START_FRAME and frame <= END_FRAME:
        newBreakdownList = []
        art = ""
        if bone_name in LH_NOTE_CTRLS:
            art = get_art(LH_ART[armature_name], frame)
        else:
            art = get_art(RH_ART[armature_name], frame)

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
            note.loc[0] =[note.loc[1][0] - 0.0015 * sign, note.loc[1][1], note.loc[1][2]]
            note.loc[2] = [note.loc[1][0] - 0.001 * sign, note.loc[1][1], note.loc[1][2]]
            add_note(fcurves, fcurve_index_dic, bone_name, note)

            # Add Finger 2nd joints Motion
            loc = bones[bone_name[:-4] + ".001"].location
            note.loc[1] = [loc[0], loc[1], loc[2]]
            note.loc[0] =[note.loc[1][0] - 0.0015 * sign, note.loc[1][1], note.loc[1][2]]
            note.loc[2] = [note.loc[1][0] - 0.001 * sign, note.loc[1][1], note.loc[1][2]]
            add_note(fcurves, fcurve_index_dic, bone_name[:-4] + ".001", note)

            # Add Finger 3rd joints Motion
            loc = bones[bone_name[:-4]].location
            note.loc[1] = [loc[0], loc[1], loc[2]]
            note.loc[0] = [note.loc[1][0] + 0.001 * sign, note.loc[1][1], note.loc[1][2]]
            note.loc[2] = [note.loc[1][0] + 0.00125 * sign, note.loc[1][1], note.loc[1][2]]
            add_note(fcurves, fcurve_index_dic, bone_name[:-4], note)


def auto_breakdown(armature_name):
    global bones
    global bodyModionDic
    global lhNoteDic
    global rhNoteDic
    bones = bpy.data.objects[armature_name].pose.bones
    bodyModionDic = {}
    lhNoteDic = {}
    rhNoteDic = {}


    cnt = 0
    axis = ""
    keyframeDic = {}
    fcurveList = []
    fcurve_index_dic = {}

    act = bpy.data.objects[armature_name].animation_data.action

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
                            create_breakdown(armature_name, act.fcurves, fcurve_index_dic, bone_name, frame, \
                                          keyframeDic["X"][i + 1][0])

                        # create Note on hand dic
                        handDic = {}
                        if bone_name in LH_NOTE_CTRLS:
                            handDic = lhNoteDic
                        else:
                            handDic = rhNoteDic

                        if frame not in handDic:
                            handDic.update({frame:NoteOnHand(frame)})

                        note_end_frame = 0
                        if is_play(bone_name, loc_x, loc_y, loc_z):
                            art = ""
                            if bone_name in LH_NOTE_CTRLS:
                                art = get_art(LH_ART[armature_name], frame)
                            else:
                                art = get_art(RH_ART[armature_name], frame)
                            note = Note(art, frame, keyframeDic["X"][i + 1][0])
                            frames = get_note_frames(note)
                            note_end_frame = frames[2]

                        handDic[frame].set(bone_name, note_end_frame)

# init logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

for x in ARMATURE_NAME_LIST:
    print(x)
    auto_breakdown(x)

sorted(lhNoteDic.keys())
print(sorted(lhNoteDic.keys()))

logger.end()

