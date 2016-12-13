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

# Settings
START_FRAME = 19
END_FRAME = 36
ENABLE_KEY_LIST = [19, 21, 23, 25, 27, 29, 31, 33, 35]

print("### START ###")

i = START_FRAME
offset = END_FRAME - START_FRAME + 1

bpy.ops.pose.select_all(action='SELECT')

for i in range(START_FRAME, END_FRAME):
    if i in ENABLE_KEY_LIST:
        copy_pose(i, i - offset, True)
copy_pose(START_FRAME - offset, END_FRAME + 1, False)

print("### END ###")
