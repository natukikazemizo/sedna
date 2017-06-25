#!BPY
# -*- coding: UTF-8 -*-
# Set Show Hide KeyFrames
# 2017.06.25 Natukikazemizo

import bpy
import math
import re

# constants
PY_NAME = "SET SHOW HIDE KEY FRAMES"

print(PY_NAME + " START")

# parameters
targetParentName = "Cubes"

# set current frame
bpy.data.scenes['Root.DorothyLoris'].frame_set(739)

for child in bpy.data.objects[targetParentName].children:
    child.hide = True
    child.hide_render = True
    child.keyframe_insert('hide', frame=739)
    child.keyframe_insert('hide_render', frame=739)

bpy.data.scenes['Root.DorothyLoris'].frame_set(740)

for child in bpy.data.objects[targetParentName].children:
    child.hide = False
    child.hide_render = False
    child.keyframe_insert('hide', frame=740)
    child.keyframe_insert('hide_render', frame=740)

print(PY_NAME + " END")

 