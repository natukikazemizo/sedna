#!BPY
# -*- coding: UTF-8 -*-
# Copy Bone Limits from Armature to another Armature
#
# 2016.01.31 Natukikazemizo

import bpy
import math
import re

fromArmature = "Albatrus_Armature"
#toArmature = "SD_Albatrus_Armature"
toArmature = "Nothern_Armature"

pi = math.pi

for x in bpy.data.objects[toArmature].pose.bones:
    if x.name in bpy.data.objects[fromArmature].pose.bones:
        fromBone = bpy.data.objects[fromArmature].pose.bones[x.name]
        x.ik_min_x = fromBone.ik_min_x
        x.ik_min_y = fromBone.ik_min_y
        x.ik_min_z = fromBone.ik_min_z
        x.ik_max_x = fromBone.ik_max_x
        x.ik_max_y = fromBone.ik_max_y
        x.ik_max_z = fromBone.ik_max_z
        x.use_ik_limit_x = fromBone.use_ik_limit_x
        x.use_ik_limit_y = fromBone.use_ik_limit_y
        x.use_ik_limit_z = fromBone.use_ik_limit_z
        x.ik_stretch = fromBone.ik_stretch
        x.lock_ik_x = fromBone.lock_ik_x
        x.lock_ik_y = fromBone.lock_ik_y
        x.lock_ik_z = fromBone.lock_ik_z
    