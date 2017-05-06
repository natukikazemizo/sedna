#!BPY
# -*- coding: UTF-8 -*-
# Set Finger Constraints
#
# 2017.05.03 Natukikazemizo

import bpy
import math
import re

print("Copy Bone Constraints START")


targetArmature = "Armature.Dorothy"

fromArmatureConstraintsDict = {}


LR_LIST = ("L", "R")
BONE_NAME_LIST = ("Little", "Ring", "Middle", "Index")
POSITION_LIST = ("Root", "", "001", "002")
THUMB_POSITION_LIST = {"002", "003"}

print("SET Finger Constraints")

for lr in LR_LIST:
    # SET UP Thumb
    for pos in THUMB_POSITION_LIST:
        ctrlBoneName = "Thumb.Ctrl_T_" + lr + "." + pos
        targetBoneName = "Thumb_" + lr + "." + pos
        constraint = bpy.context.object.pose.bones[targetBoneName].constraints["Transformation"]
        constraint.subtarget = ctrlBoneName
        constraint.from_min_x = -0.05
        constraint.from_max_x = 0.05
        constraint.map_to = 'ROTATION'
        constraint.map_to_x_from = 'Z'
        constraint.map_to_z_from = 'X'

        constraint.to_min_z_rot = -math.pi * 2 / 3
        constraint.to_max_z_rot = math.pi * 2 / 3
#        if lr == "R":
#            constraint.to_min_z_rot = math.pi * 2 / 3
#            constraint.to_max_z_rot = -math.pi * 2 / 3
#        else:
#            constraint.to_min_z_rot = -math.pi * 2 / 3
#            constraint.to_max_z_rot = math.pi * 2 / 3
        constraint.target_space = 'LOCAL'
        constraint.owner_space = 'LOCAL'
    
    # SET UP Index, Middle, Ring, Little
    for boneNameSheed in BONE_NAME_LIST:
        for pos in POSITION_LIST:
            # Create Bone Name
            
            if pos == "002":
                # SET COPY ROTATION
                ctrlBoneName = boneNameSheed + "_" + lr + ".001"
                targetBoneName = boneNameSheed + "_" + lr + "." + pos
                
                constraint = bpy.context.object.pose.bones[targetBoneName].constraints["Copy Rotation"]
                constraint.target = bpy.data.objects[targetArmature]
                constraint.subtarget = ctrlBoneName
                constraint.target_space = 'LOCAL'
                constraint.owner_space = 'LOCAL'

            else:
                # SET TRANSFORM
                
                if pos == "Root":
                    ctrlBoneName = boneNameSheed + ".Ctrl_T_" + lr
                    targetBoneName = boneNameSheed + "_" + pos + "_" + lr

                    constraint = bpy.context.object.pose.bones[targetBoneName].constraints["Transformation"]
                    constraint.map_to = 'ROTATION'
                    constraint.map_to_x_from = 'Z'
                    constraint.map_to_z_from = 'X'

                    constraint.subtarget = ctrlBoneName
                    constraint.from_min_x = -0.02
                    constraint.from_max_x = 0.02
                    constraint.from_min_z = -0.02
                    constraint.from_max_z = 0.02

                    constraint.to_min_x_rot = math.pi / 36
                    constraint.to_max_x_rot = -math.pi / 36
                    
                    constraint.to_min_z_rot = math.pi / 36
                    constraint.to_max_z_rot = -math.pi / 36
                elif pos == "":
                    ctrlBoneName = boneNameSheed + ".Ctrl_T_" + lr
                    targetBoneName = boneNameSheed + "_" + lr

                    constraint = bpy.context.object.pose.bones[targetBoneName].constraints["Transformation"]
                    constraint.map_to = 'ROTATION'
                    constraint.map_to_x_from = 'Z'
                    constraint.map_to_z_from = 'X'

                    constraint.subtarget = ctrlBoneName
                    constraint.from_min_x = -0.02
                    constraint.from_max_x = 0.02
                    constraint.from_min_z = -0.02
                    constraint.from_max_z = 0.02

                    constraint.to_min_x_rot = math.pi / 2
                    constraint.to_max_x_rot = -math.pi / 2
                    
                    constraint.to_min_z_rot = math.pi / 2
                    constraint.to_max_z_rot = -math.pi / 2

                elif pos == "001":
                    ctrlBoneName = boneNameSheed + ".Ctrl_T_" + lr + "." + pos
                    targetBoneName = boneNameSheed + "_" + lr + "." + pos

                    constraint = bpy.context.object.pose.bones[targetBoneName].constraints["Transformation"]
                    constraint.map_to = 'ROTATION'

                    constraint.subtarget = ctrlBoneName
                    constraint.from_min_x = -0.05
                    constraint.from_max_x = 0.05
                    constraint.to_min_x_rot = math.pi * 2 / 3
                    constraint.to_max_x_rot = -math.pi * 2 / 3
            
                if lr == "R":
                    constraint.to_min_x_rot *= -1
                    constraint.to_max_x_rot *= -1
                    constraint.to_min_z_rot *= -1
                    constraint.to_max_z_rot *= -1

                constraint.target_space = 'LOCAL'
                constraint.owner_space = 'LOCAL'

            print(targetBoneName)

print("SET Finger Constraints")

 