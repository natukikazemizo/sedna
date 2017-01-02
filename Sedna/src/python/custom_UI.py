#!BPY
# -*- coding: UTF-8 -*-
# Set UI 
#
# 2017.01.02 Natukikazemizo

import bpy
from bpy.props import *
import flip_next_paste_pose as next_paste
import custom_constants as cst_c

#
#    Store properties in the active scene
#
def initSceneProperties(scn):
    bpy.types.Scene.CopyStartFrame = IntProperty(
        name="Start Frame", 
        min = cst_c.FRAME_MIN, max = cst_c.FRAME_MAX,
        default = 1)
#    scn['CopyStartFrame'] = 1
    bpy.types.Scene.CopyEndFrame = IntProperty(
        name="End Frame", 
        min = cst_c.FRAME_MIN, max = cst_c.FRAME_MAX,
        default = 8)
#    scn['CopyEndFrame'] = 8
    bpy.types.Scene.CopyStep = IntProperty(
        name="Step", 
        min = -9999, max = 9999,
        default = 1)
#    scn['CopyStep'] = 1
    return

initSceneProperties(bpy.context.scene)

class UI(bpy.types.Panel):
  bl_label = "Flip Copy Pose"
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
 
#############################################
  def draw(self, context):
    layout = self.layout
    scn = context.scene
    layout.prop(scn, 'CopyStartFrame', icon='BLENDER', toggle=True)
    layout.prop(scn, 'CopyEndFrame', icon='BLENDER', toggle=True)
    layout.prop(scn, 'CopyStep', icon='BLENDER', toggle=True)
    row = layout.row(align=True)
    row.alignment = 'EXPAND'
    row.operator("my.button", text="Flip Next Copy")
#############################################

class MyButton(bpy.types.Operator):
  bl_idname = "my.button"
  bl_label = "text"
  def execute(self, context):
      print("pushed")
      scn = context.scene
      next_paste.flip_next_copy(scn['CopyStartFrame'],
        scn['CopyEndFrame'], scn['CopyStep'])
      return{'FINISHED'}

bpy.utils.register_module(__name__)
