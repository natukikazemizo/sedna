#!BPY
# -*- coding: UTF-8 -*-
#
# ReSetBoneNumbers
#
# 2016.01.12 Natukikazemizo
import bpy
import string

print("### START ###")

orgStr = "Pose."
destStr = ""

for x in bpy.context.selected_editable_bones:
    if x.name.startswith(orgStr):
        print(x.name)
        x.name = x.name.replace(orgStr, destStr)

print("### END ###")
