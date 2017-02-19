#!BPY
# -*- coding: UTF-8 -*-
# Set Finger Constraints
#
# 2016.02.19 Natukikazemizo
import bpy
import math
import re

print("Copy Bone Constraints START")


fromArmature = "Jody_Armature"
toArmature = "Jody_Armature"

fromArmatureConstraintsDict = {}


LR_LIST = ("L", "R")
BONE_NAME_LIST = ("Little", "Ring", "Middle", "Index")
POSITION_LIST = ("Root", "", "001", "002")

print("Copy Finger Bone Constraints START")

for lr in LR_LIST:
    for boneNameSheed in BONE_NAME_LIST:
        for pos in POSITION_LIST:
            # Create Bone Name
            if pos == "Root":
                fromBoneName = boneNameSheed + "_" + pos + ".Ctrl_" + lr
                toBoneName = boneNameSheed + "_" + pos + "_" + lr
            elif pos == "":
                fromBoneName = boneNameSheed + ".Ctrl_" + lr
                toBoneName = boneNameSheed + "_" + lr
            else:
                fromBoneName = boneNameSheed + ".Ctrl_" + lr + "." + pos
                toBoneName = boneNameSheed + "_" + lr + "." + pos
            print(toBoneName)
            # SET Copy Rotation
            bpy.context.object.pose.bones[toBoneName].constraints["Copy Rotation"].subtarget = fromBoneName
            bpy.context.object.pose.bones[toBoneName].constraints["Copy Rotation"].target_space = 'LOCAL'
            bpy.context.object.pose.bones[toBoneName].constraints["Copy Rotation"].owner_space = 'LOCAL'


print("Copy Bone Constraints END")

 