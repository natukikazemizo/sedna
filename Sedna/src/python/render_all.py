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
FRAME_STEP = 1

# parameters
renderScopes = {RenderScope("Loris at Loris's Room", "Root.Loris", 1, 199, "Camera.Main.Loris", "//textures\\loris\\")
,RenderScope("Intro_Sub", "Root.DorothyLoris", 1520, 1723, "Camera.Main.Dorothy.004", "//..\\renderResults_004\\")
,RenderScope("Intro_Main", "Root.DorothyLoris", 1520, 2098, "Camera.Main.Dorothy", "//..\\renderResults\\")
#,RenderScope("Loris WARP", "Root.DorothyLoris", 1, 265, "Camera.Main.Dorothy", "//..\\renderResults\\")
#,RenderScope("GetUp Dorothy", "Root.DorothyLoris", 280, 324, "Camera.Main.Dorothy", "//..\\renderResults\\")
#,RenderScope("Swing Dorothy Shoulder", "Root.DorothyLoris", 340, 388, "Camera.Main.Dorothy", "//..\r\enderResults\\")
#,RenderScope("Pull Dorothy Cheek", "Root.DorothyLoris", 390, 430, "Camera.Main.Dorothy", "//..\\renderResults\\")
#,RenderScope("Loris Think", "Root.DorothyLoris", 430,580 , "Camera.Main.Dorothy", "//..\\renderResults\\")
#,RenderScope("Sting", "Root.DorothyLoris", 590, 598, "Camera.Main.Dorothy", "//..\\renderResults\\")
#,RenderScope("Pumping", "Root.DorothyLoris", 600, 740, "Camera.Main.Dorothy", "//..\\renderResults\\")
#,RenderScope("Burst", "Root.DorothyLoris", 741, 1000, "Camera.Main.Dorothy", "//..\\renderResults\\")
#,RenderScope("Loris Run", "Root.DorothyLoris", 1001, 1092, "Camera.Main.Dorothy", "//..\\renderResults\\")
#,RenderScope("MoveCube-Ending", "Root.DorothyLoris", 1093, 1519, "Camera.Main.Dorothy", "//..\\renderResults\\")
}

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

