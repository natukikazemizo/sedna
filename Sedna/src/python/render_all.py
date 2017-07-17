#!BPY
# -*- coding: UTF-8 -*-
# Render All of Secne & Frame which need to render.
#
# 2017.07.17 Natukikazemizo
import utils_log
import bpy

# constants
PY_NAME = "RENDER ALL"

utils_log.start(PY_NAME)

# classes
class RenderScope():
    def __init__(self, name, scene, startFrame, endFrame, camera, filepath):
        self.name = name
        self.scene = scene
        self.startFrame = startFrame
        self.endFrame = endFrame
        self.camera = camera
        self.filepath = filepath

# constants
RESOLUTION_X = 1920
RESOLUTION_Y = 1080
RESOLUTION_PERCENTAGE = 25
FILE_FORMAT = 'PNG'
FRAME_PER_SECOND = 24
FRAME_STEP = 2

# parameters
renderScopes = {RenderScope("Loris at Loris's Room", "Root.Loris", 1, 4, "Camera.Main.Loris", "//textures\\loris\\")}

# rendering renderScopes
bpy.context.window.screen = bpy.data.screens['Render']

for scope in renderScopes:
    print(scope.name + " RENDER START")
    bpy.context.screen.scene = bpy.data.scenes[scope.scene]
    bpy.context.scene.render.resolution_x = RESOLUTION_X
    bpy.context.scene.render.resolution_y = RESOLUTION_Y 
    bpy.context.scene.render.resolution_percentage = RESOLUTION_PERCENTAGE
    bpy.context.scene.render.image_settings.file_format = FILE_FORMAT
    bpy.context.scene.frame_start = scope.startFrame
    bpy.context.scene.frame_end = scope.endFrame
    bpy.context.scene.frame_step = FRAME_STEP
    bpy.context.scene.render.fps = FRAME_PER_SECOND
    bpy.context.scene.camera = bpy.data.objects[scope.camera]
    bpy.data.scenes[scope.scene].render.filepath = scope.filepath
    bpy.ops.render.render(animation=True)
    print(scope.name + " RENDER END")

utils_log.end(PY_NAME)

