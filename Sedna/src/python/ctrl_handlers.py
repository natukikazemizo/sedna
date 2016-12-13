#!BPY
# -*- coding: UTF-8 -*-
# Copy Bone Limits from Armature to another Armature
#
# 2016.09.05 Natukikazemizo

import bpy
import math

targetTextObjectName = "Text0" 
cursorText0 = "|"
cursorText1 = ""
textParFrame = 1
frameParMeter = 100
ctrlObjectName = "Text_C"
ctrlCursorObjectName = "Text_Cursor_C"

sentence = '''Gallia est omnis divisa in partes tres, 
quarum unam incolunt Belgae, aliam Aquitani, 
tertiam qui ipsorum lingua Celtae, nostra
Galli appellantur. 
'''

def handler(scene):
    #frame = scene.frame_current 
    pos = math.floor(bpy.data.objects[ctrlObjectName].location[0] * \
            frameParMeter)
    posCursor = bpy.data.objects[ctrlCursorObjectName].location[2] * \
            frameParMeter
    cursor = cursorText1;
    #print(posCursor)
    if posCursor == 0:
        cursor = cursorText0
    if pos == 0:
        pass
    elif pos < 0:
        #print(cursor)
        bpy.data.objects[targetTextObjectName].data.body = cursor
    else: 
        bpy.data.objects[targetTextObjectName].data.body = \
            sentence[:pos * textParFrame] + cursor

bpy.app.handlers.frame_change_pre.clear()
bpy.app.handlers.frame_change_pre.append(handler)
