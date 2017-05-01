#!BPY
# -*- coding: UTF-8 -*-
# Set up Seleted Ctrl Bones properties
#
# 2017.04.23 Natukikazemizo
import bpy
import re

print("### START ###")

for x in bpy.context.selected_pose_bones:
    print(x.name)
    bpy.context.object.data.bones[x.name].show_wire = True 
print("### END ###")
