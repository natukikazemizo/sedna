#!BPY
# -*- coding: UTF-8 -*-
# Set Copy Rotation Constraints For Prototype SelectedBones
#
# 2016.10.06 Natukikazemizo
import bpy
import re

print("### START ###")

keyPhrase = ".Ctrl"
newConstraintName = "Copy Hand Rotation"

for x in bpy.context.selected_pose_bones:
    if keyPhrase in x.name :
        targetName = x.name.replace(keyPhrase, "")
        if targetName in bpy.context.object.pose.bones:
            targetBone = bpy.context.object.pose.bones[targetName]
            if newConstraintName in targetBone.constraints:
                targetBone.constraints.remove(targetBone.constraints[newConstraintName])
            newConstraint = targetBone.constraints.new(type="COPY_ROTATION")
            newConstraint.name = newConstraintName
            newConstraint.target = bpy.data.objects["Jody_Armature.BodyControl"]
            newConstraint.subtarget = x.name
            newConstraint.target_space = 'LOCAL'
            newConstraint.owner_space = 'LOCAL'
            print(x.name)
print("### END ###")
