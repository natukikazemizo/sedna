#!BPY
# -*- coding: UTF-8 -*-
# Set Finger Constraints
#
# 2017.04.09 Natukikazemizo
import bpy
import math
import re

print("Set Bone Constraints START")


fromArmature = "Jody_Armature"
toArmature = "Jody_Armature"

fromArmatureConstraintsDict = {}


LR_LIST = ("L", "R")
BONE_NAME_LIST = ("2ndToe", "3rdToe", "4thToe", "LittleToe")
POSITION_LIST = ("", "001", "002","003")

print("Copy Finger Bone Constraints START")

for lr in LR_LIST:
    for boneNameSheed in BONE_NAME_LIST:
        fromBoneName = boneNameSheed + "_T_" + lr
        print(fromBoneName)
        for pos in POSITION_LIST:
            # Create Bone Name
            rotMax = math.pi / 3 * 2
            if pos == "":
                toBoneName = boneNameSheed + "_" + lr
            else:
                toBoneName = boneNameSheed + "_" + lr + "." + pos
                
            if pos == "003":
                rotMax = math.pi / 180 * 5

            rotMin = rotMax * -1
            print(toBoneName)
            
            x = bpy.context.object.pose.bones[toBoneName]
            
            if x.constraints.find("Transformation") < 0:
                transConstraint = x.constraints.new(type="TRANSFORM")
                transConstraint.name = "Transformation"

            # SET Transformation
            x.constraints["Transformation"].target = bpy.data.objects[fromArmature]
            x.constraints["Transformation"].subtarget = fromBoneName
            x.constraints["Transformation"].from_min_x = -0.01
            x.constraints["Transformation"].from_max_x = 0.01
            x.constraints["Transformation"].from_min_z = -0.01
            x.constraints["Transformation"].from_max_z = 0.01
            x.constraints["Transformation"].map_to_x_from = 'Z'
            x.constraints["Transformation"].map_to_z_from = 'X'
            x.constraints["Transformation"].map_to = 'ROTATION'
            x.constraints["Transformation"].to_min_x_rot = rotMin
            x.constraints["Transformation"].to_max_x_rot = rotMax
            x.constraints["Transformation"].to_min_z_rot = rotMin
            x.constraints["Transformation"].to_max_z_rot = rotMax
            x.constraints["Transformation"].target_space = 'LOCAL'
            x.constraints["Transformation"].owner_space = 'LOCAL'




print("Set Bone Constraints END")

 

