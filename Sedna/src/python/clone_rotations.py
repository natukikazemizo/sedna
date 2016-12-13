#!BPY
# -*- coding: UTF-8 -*-
# Set Copy Rotation Constraints For Prototype SelectedBones
#
# 2016.01.31 Natukikazemizo
import bpy
import math
import re

print("### START ###")

for x in bpy.context.selected_pose_bones:
    for y in x.constraints:
        x.constraints.remove(y)
    else:
        newConstraint = x.constraints.new(type="COPY_ROTATION")
        newConstraint.name = "Copy Rotation"
        newConstraint.target = bpy.data.objects["SD_Albatrus_Armature"]
        print("Pose." + x.name)
        newConstraint.subtarget = "Pose." + x.name
        print(x.name)
print("### END ###")
