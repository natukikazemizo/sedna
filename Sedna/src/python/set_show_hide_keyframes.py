#!BPY
# -*- coding: UTF-8 -*-
# Set Show Hide KeyFrames
# 2017.07.11 Natukikazemizo

import bpy
import math
import re

# constants
PY_NAME = "SET SHOW HIDE KEY FRAMES"

print(PY_NAME + " START")

# parameters
targetParentName = "Pos.Loris"
hideFrame = 1364
showFrame = 1363

# Add Show or Hide Key Frame On Child Objects
def addDispKeyChildren(obj, frame, hide):
    for child in obj.children:
        child.hide = hide
        child.hide_render = hide
        child.keyframe_insert('hide', frame = frame)
        child.keyframe_insert('hide_render', frame = frame)
        addDispKeyChildren(child, frame, hide)

# set current frame
print("HIDE " + targetParentName + " DESCENDANTS AT FRAME:" + str(hideFrame))
bpy.data.scenes['Root.DorothyLoris'].frame_set(hideFrame)
addDispKeyChildren(bpy.data.objects[targetParentName], hideFrame, True)

# set current frame
print("SHOW " + targetParentName + " DESCENDANTS AT FRAME:" + str(showFrame))
bpy.data.scenes['Root.DorothyLoris'].frame_set(showFrame)
addDispKeyChildren(bpy.data.objects[targetParentName], showFrame, False)

print(PY_NAME + " END")

