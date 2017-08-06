#!BPY
# -*- coding: UTF-8 -*-
# Flip & Paste For SelectedBones And Setted Flame
#
# 2016.10.22 Natukikazemizo
import bpy

#Copy Pose Function
def copy_pose(srcFrame, destFrame, flip):
    bpy.context.scene.frame_set(srcFrame)
    bpy.ops.pose.copy()
    bpy.context.scene.frame_set(destFrame)
    bpy.ops.pose.paste(flipped=flip)
    bpy.ops.anim.keyframe_insert_menu(\
        type='__ACTIVE__', confirm_success=True)

def flip_next_copy(startFrame, endFrame, step):
    # Settings
    START_FRAME = startFrame
    END_FRAME = endFrame
    # ENABLE_KEY_LIST = [1, 2, 3, 4, 5, 6, 7, 8]
    STEP = step
    print("START:%s END:%s STEP:%s" %(START_FRAME, END_FRAME, STEP))
    print("### COPY START ###")

    i = START_FRAME
    offset = END_FRAME - START_FRAME + 1

    bpy.ops.pose.select_all(action='SELECT')

    for i in range(START_FRAME, END_FRAME + 1):
        #if i in ENABLE_KEY_LIST:
        if i % STEP == 1 or STEP == 1:
            copy_pose(i, i + offset, True)
            print("i:" + str(i) )
    copy_pose(START_FRAME, START_FRAME + offset * 2, False)

    print("### COPY END ###")
