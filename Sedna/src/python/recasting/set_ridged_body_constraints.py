#!BPY
# -*- coding: UTF-8 -*-
# Set Ridged Body Constraints
#
# 2017.06.25 Natukikazemizo

import bpy
import math
import re

# constants
PY_NAME = "SET RIDGED BODY CONSTRAINTS"

print(PY_NAME + " START")

# parameters
targetParentName = "Cubes"

for child in bpy.data.objects[targetParentName].children:
    if child.rigid_body.type == 'ACTIVE':
        print(child.name)
        child.rigid_body.friction = 0.5
        child.rigid_body.restitution = 0
        # Mass in kiro grams
        child.rigid_body.mass = 0.1
        child.rigid_body.collision_shape = 'CONVEX_HULL'

print(PY_NAME + " END")

 