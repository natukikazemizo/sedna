#!BPY
# -*- coding: UTF-8 -*-
# Set F-Curve Interpola
#
# 2016.02.07 Natukikazemizo
import bpy
import math
import re

print("### START ###")a

targetNames = ["Albatrus_Pos", "Albatrus_Pose.Prottype"]

for objName in targetNames:
    for x in bpy.data.objects[objName].animation_data.action.fcurves:
        print(x.rna_type)
        for y in x.keyframe_points:
            # QUAD,CUBIC,BEZIER
            y.interpolation = 'BEZIER'
            #y.easing = 'AUTO'

print("### END ###")