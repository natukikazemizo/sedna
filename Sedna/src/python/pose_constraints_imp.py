#!BPY
# -*- coding: UTF-8 -*-
# import pose bone constraints 
#
# 2017.10.22 Natukikazemizo

import bpy
import os
import utils_log
import utils_io_csv

# Constants
WORK_FILE_NAME = "pose_constraints_edit.csv"

BONE_NAME = 0 
CONSTRAINT_NAME = 1
MUTE = 2
TARGET = 3
SUBTARGET_BONE_NAME = 4
EXTRAPOLATE = 5
FROM_MIN_X = 6
FROM_MAX_X = 7
FROM_MIN_Y = 8
FROM_MAX_Y = 9
FROM_MIN_Z = 10
FROM_MAX_Z = 11
MAP_TO_X_FROM = 12
MAP_TO_Y_FROM = 13
MAP_TO_Z_FROM = 14
MAP_TO = 15
TO_MIN_X = 16
TO_MAX_X = 17
TO_MIN_Y = 18
TO_MAX_Y = 19
TO_MIN_Z = 20
TO_MAX_Z = 21
TARGET_SPACE = 22
OWNER_SPACE = 23

# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

header, data = utils_io_csv.read(WORK_FILE_NAME)

for row in data:
    if bpy.context.object.pose.bones.find(row[BONE_NAME]) == -1:
        logger.warn("Bone not found. Bone name is " + row[BONE_NAME])
        break
    if bpy.data.objects.find(row[TARGET]) == -1:
        logger.warn("Object not found. Object name is " + row[TARGET])
        break
    bone = bpy.context.object.pose.bones[row[BONE_NAME]]
    constraint = bone.constraints[row[CONSTRAINT_NAME]]
    
    print(bone.name + constraint.name)
    
    constraint.mute = row[MUTE] == "True"
    constraint.target = bpy.data.objects[row[TARGET]]
    constraint.subtarget = row[SUBTARGET_BONE_NAME]
    constraint.use_motion_extrapolate = row[EXTRAPOLATE] == "True"
    
    constraint.from_min_x = float(row[FROM_MIN_X])
    constraint.from_max_x = float(row[FROM_MAX_X])
    constraint.from_min_y = float(row[FROM_MIN_Y])
    constraint.from_max_y = float(row[FROM_MAX_Y])
    constraint.from_min_z = float(row[FROM_MIN_Z])
    constraint.from_max_z = float(row[FROM_MAX_Z])
    
    constraint.map_to_x_from = row[MAP_TO_X_FROM]
    constraint.map_to_y_from = row[MAP_TO_Y_FROM]
    constraint.map_to_z_from = row[MAP_TO_Z_FROM]
    constraint.map_to = row[MAP_TO]
    if constraint.map_to == "LOCATION":
        constraint.to_min_x = float(row[TO_MIN_X])
        constraint.to_max_x = float(row[TO_MAX_X])
        constraint.to_min_y = float(row[TO_MIN_Y])
        constraint.to_max_y = float(row[TO_MAX_Y])
        constraint.to_min_z = float(row[TO_MIN_Z])
        constraint.to_max_z = float(row[TO_MAX_Z])
    elif constraint.map_to == "ROTATION":
        constraint.to_min_x_rot = float(row[TO_MIN_X])
        constraint.to_max_x_rot = float(row[TO_MAX_X])
        constraint.to_min_y_rot = float(row[TO_MIN_Y])
        constraint.to_max_y_rot = float(row[TO_MAX_Y])
        constraint.to_min_z_rot = float(row[TO_MIN_Z])
        constraint.to_max_z_rot = float(row[TO_MAX_Z])
    else:
        # map_to:SCALE
        constraint.to_min_x_scale = float(row[TO_MIN_X])
        constraint.to_max_x_scale = float(row[TO_MAX_X])
        constraint.to_min_y_scale = float(row[TO_MIN_Y])
        constraint.to_max_y_scale = float(row[TO_MAX_Y])
        constraint.to_min_z_scale = float(row[TO_MIN_Z])
        constraint.to_max_z_scale = float(row[TO_MAX_Z])

    constraint.target_space = row[TARGET_SPACE]
    constraint.owner_space = row[OWNER_SPACE]

logger.end()

