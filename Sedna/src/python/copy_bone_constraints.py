#!BPY
# -*- coding: UTF-8 -*-
# Copy Bone Constraints from Armature to another Armature
#
# 2016.01.31 Natukikazemizo
import bpy
import math
import re

print("Copy Bone Constraints START")


fromArmature = "Albatrus_Armature"
#toArmature = "SD_Albatrus_Armature"
toArmature = "Nothern_Armature"

fromArmatureConstraintsDict = {}

# Get Constraints from FROM ARMATURE
bpy.data.objects[fromArmature].select = True
for x in bpy.data.objects[fromArmature].pose.bones:
    if len(x.constraints) > 0:
        constraints = []
        for y in x.constraints:
            print(y)
            constraints.append(y)
        else:
            fromArmatureConstraintsDict.update({x.name:constraints})
else:
    bpy.data.objects[fromArmature].select = False

bpy.data.objects[toArmature].select = True
for x in bpy.data.objects[toArmature].pose.bones:
    print(x.name)
    if x.name in fromArmatureConstraintsDict:
        for z in x.constraints:
            x.constraints.remove(z)
        else:
            for y in fromArmatureConstraintsDict[x.name]:
                print(y.type)
                newConstraint = x.constraints.new(type=y.type)
                newConstraint.target = bpy.data.objects[toArmature]
                newConstraint.name=y.name
                newConstraint.subtarget = y.subtarget
                newConstraint.influence = y.influence
                if y.type == "IK":
                    print("CopyIK")
                    if y.pole_target is not None:
                        newConstraint.pole_target = bpy.data.objects[toArmature]
                        newConstraint.pole_subtarget = y.pole_subtarget
                    newConstraint.pole_angle = y.pole_angle
                    newConstraint.iterations = y.iterations
                    newConstraint.chain_count = y.chain_count
                    newConstraint.use_tail = y.use_tail
                    newConstraint.use_stretch = y.use_stretch
                    newConstraint.use_location = y.use_location
                    newConstraint.use_rotation = y.use_rotation
                    newConstraint.weight = y.weight
                    newConstraint.orient_weight = y.orient_weight
                    
                elif y.type == "COPY_ROTATION":
                    print("Copy Rotation");
                    newConstraint.target_space = y.target_space
                    newConstraint.owner_space = y.owner_space
                    newConstraint.use_x = y.use_x
                    newConstraint.use_y = y.use_y
                    newConstraint.use_z = y.use_z
                    newConstraint.invert_x = y.invert_x
                    newConstraint.invert_y = y.invert_y
                    newConstraint.invert_z = y.invert_z
                    newConstraint.use_offset = y.use_offset       
                    

bpy.data.objects[toArmature].select = False

print("Copy Bone Constraints END")

 