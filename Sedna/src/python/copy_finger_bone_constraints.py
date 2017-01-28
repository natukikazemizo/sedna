#!BPY
# -*- coding: UTF-8 -*-
# Create Finger Control Bones
#
# 2017.01.22 Natukikazemizo
import bpy
import math
import re

LR_LIST = ("L", "R")
BONE_NAME_LIST = ("Little.Ctrl", "Ring.Ctrl", "Middle.Ctrl", "Index.Ctrl")

print("Copy Finger Bone Constraints START")

for lr in LR_LIST:
    for boneNameSheed in BONE_NAME_LIST:
        # Create Bone Names
        middleBoneName = boneNameSheed + "_" + lr + ".001"
        topBoneName = boneNameSheed + "_" + lr + ".002"
        targetBoneName = boneNameSheed + "_T_" + lr + ".001"

        # SET TRANSFORM
        bpy.context.object.pose.bones[middleBoneName].constraints["Transformation"].subtarget = targetBoneName
        bpy.context.object.pose.bones[middleBoneName].constraints["Transformation"].from_min_x = -0.05
        bpy.context.object.pose.bones[middleBoneName].constraints["Transformation"].from_max_x = 0.05
        bpy.context.object.pose.bones[middleBoneName].constraints["Transformation"].map_to = 'ROTATION'
        if lr == "R":
            bpy.context.object.pose.bones[middleBoneName].constraints["Transformation"].to_min_x_rot = 2.0944
            bpy.context.object.pose.bones[middleBoneName].constraints["Transformation"].to_max_x_rot = -2.0944
        else:
            bpy.context.object.pose.bones[middleBoneName].constraints["Transformation"].to_min_x_rot = -2.0944
            bpy.context.object.pose.bones[middleBoneName].constraints["Transformation"].to_max_x_rot = 2.0944
        bpy.context.object.pose.bones[middleBoneName].constraints["Transformation"].target_space = 'LOCAL'
        bpy.context.object.pose.bones[middleBoneName].constraints["Transformation"].owner_space = 'LOCAL'
        
        # SET COPY ROTATION
        bpy.context.object.pose.bones[topBoneName].constraints["Copy Rotation"].target = bpy.data.objects["Jody_Armature.BodyControl"]
        bpy.context.object.pose.bones[topBoneName].constraints["Copy Rotation"].target_space = 'LOCAL'
        bpy.context.object.pose.bones[topBoneName].constraints["Copy Rotation"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones[topBoneName].constraints["Copy Rotation"].subtarget = middleBoneName



print("Copy Finger Bone Constraints END")

 