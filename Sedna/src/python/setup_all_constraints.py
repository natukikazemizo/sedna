#!BPY
# -*- coding: UTF-8 -*-
# Set up All Constraints of Seleted Armature's Bones
#
# 2017.08.06 Natukikazemizo

import bpy
import math
import re
import utils_log

# parameters
DELETE_IK = False

ARMATURE_NAME = "Loris.Armature"

TRANSFORMATION_NAME = "Rig Ctrl"

EXTRAPOLATE = True

# constants
PY_NAME = "SETUP ALL CONSTRAINTS"
CONSTRAINT_TYPE = "TRANSFORM"

# classes
class TF_Prm():
    """Parameters of Bone Constraints of Transformation"""
    def __init__(self, bone_name, target_bone_name, from_min_x, from_max_x, \
            from_min_y, from_max_y, from_min_z, from_max_z, \
            map_to_x_from, map_to_y_from, map_to_z_from, map_to, \
            to_min_x_rot, to_max_x_rot, to_min_y_rot, to_max_y_rot, to_min_z_rot, to_max_z_rot, \
            target_space, owner_space):
        self.bone_name = bone_name
        self.target_bone_name = target_bone_name
        self.from_min_x = from_min_x
        self.from_max_x = from_max_x
        self.from_min_y = from_min_y
        self.from_max_y = from_max_y
        self.from_min_z = from_min_z
        self.from_max_z = from_max_z
        self.map_to_x_from = map_to_x_from
        self.map_to_y_from = map_to_y_from
        self.map_to_z_from = map_to_z_from
        self.map_to = map_to
        self.to_min_x_rot = to_min_x_rot
        self.to_max_x_rot = to_max_x_rot
        self.to_min_y_rot = to_min_y_rot
        self.to_max_y_rot = to_max_y_rot
        self.to_min_z_rot = to_min_z_rot
        self.to_max_z_rot = to_max_z_rot
        self.target_space = target_space
        self.owner_space = owner_space

pi = math.pi

bone_transformations = {
 TF_Prm("BigToe.L.002", "BigToe_T.L", 0, 0.01, 0, 0, 0, 0.01, 'X', 'Y', 'Z', 'ROTATION', 0, pi/4, 0, 0, pi/4, 0, "LOCAL", "LOCAL")
#,TF_PRM()
}
utils_log.start(PY_NAME)

p_Left=re.compile(r"(.*\.L(\.|_).*|.*\.L\Z)")

for bone_transform in bone_transformations:
    bone = bpy.context.object.pose.bones[bone_transform.bone_name]
    if bone.constraints.find(TRANSFORMATION_NAME) == -1:
        newConstraint = bone.constraints.new(type=CONSTRAINT_TYPE)
        newConstraint.name = TRANSFORMATION_NAME
        
    constraint = bone.constraints[TRANSFORMATION_NAME]
    
    constraint.target = bpy.data.objects["Loris.Armature"]
    constraint.subtarget = bone_transform.target_bone_name
    constraint.use_motion_extrapolate = EXTRAPOLATE
    constraint.from_min_x = bone_transform.from_min_x
    constraint.from_min_x = bone_transform.from_min_x
    constraint.from_max_x = bone_transform.from_max_x
    constraint.from_min_y = bone_transform.from_min_y
    constraint.from_max_y = bone_transform.from_max_y
    constraint.from_min_z = bone_transform.from_min_z
    constraint.from_max_z = bone_transform.from_max_z
    constraint.map_to_x_from = bone_transform.map_to_x_from
    constraint.map_to_y_from = bone_transform.map_to_y_from
    constraint.map_to_z_from = bone_transform.map_to_z_from
    constraint.map_to = bone_transform.map_to
    constraint.to_min_x_rot = bone_transform.to_min_x_rot
    constraint.to_max_x_rot = bone_transform.to_max_x_rot
    constraint.to_min_y_rot = bone_transform.to_min_y_rot
    constraint.to_max_y_rot = bone_transform.to_max_y_rot
    constraint.to_min_z_rot = bone_transform.to_min_z_rot
    constraint.to_max_z_rot = bone_transform.to_max_z_rot
    constraint.target_space = bone_transform.target_space
    constraint.owner_space = bone_transform.owner_space


utils_log.end(PY_NAME)



