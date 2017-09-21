#!BPY
# -*- coding: UTF-8 -*-
# Remove Constraints from selected objects
#
# 2017.04.23 Natukikazemizo
import bpy
import math
import re

print("### START ###")

for x in bpy.context.selected_objects:
    for y in x.modifiers:
        if y.name == 'Wireframe':
            x.modifiers.remove(y)
print("### END ###")
