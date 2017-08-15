#!BPY
# -*- coding: UTF-8 -*-
# Set up All Constraints of Seleted Armature's Bones
#
# 2017.08.06 Natukikazemizo

import bpy
import math
import os
import re

import importlib

import utils_converter
import utils_judge
import utils_log

#reload all user pythons
importlib.reload(utils_converter)
importlib.reload(utils_judge)
importlib.reload(utils_log)

# parameters
DELETE_IK = False

ARMATURE_NAME = "Loris.Armature"

TRANSFORMATION_NAME = "Rig Ctrl"

EXTRAPOLATE = True

# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))

# constants
CONSTRAINT_TYPE = "TRANSFORM"

# class definition
class TF_Prm():
    """Parameters of Bone Constraints of Transformation"""
    def __init__(self, bone_name, subtarget_bone_name, from_min_x, from_max_x, \
            from_min_y, from_max_y, from_min_z, from_max_z, \
            map_to_x_from, map_to_y_from, map_to_z_from, map_to, \
            to_min_x_rot, to_max_x_rot, to_min_y_rot, to_max_y_rot, to_min_z_rot, to_max_z_rot, \
            target_space, owner_space):
        self.bone_name = bone_name
        self.subtarget_bone_name = subtarget_bone_name
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


# class definition
pi = math.pi

bone_transformations = [
 TF_Prm("Invarid_BoneNameTest", "BigToe_T.L",   0, 0.01, 0, 0.01, 0, 0, 'Y', 'Z', 'X', 'ROTATION', 0, -pi/4,  0, 0, 0, pi/4 , "LOCAL", "LOCAL")

# Legs
,TF_Prm("Knee.L.001",           "Knee_T.L",      0, 0.01, 0, 0.01, 0, 0, 'Y', 'Z', 'X', 'ROTATION', 0, pi/4, 0, 0, 0, -pi/4 , "LOCAL", "LOCAL")


# Foot
,TF_Prm("Shanks.L.005",         "Foot_P.L",      0, 0.01, 0, 0.01, 0, 0, 'Y', 'Z', 'X', 'ROTATION', 0, pi/4, 0, 0, 0, -pi/4 , "LOCAL", "LOCAL")
,TF_Prm("Shanks.L.006",         "Heel_T.L.001",  0, 0.01, 0, 0.01, 0, 0, 'Y', 'Z', 'X', 'ROTATION', 0, 0,     0, 0, 0, -pi/4 , "LOCAL", "LOCAL")
,TF_Prm("Foot.L",               "Heel_T.L.001",  0, 0.01, 0, 0.01, 0, 0, 'Y', 'Z', 'X', 'ROTATION', 0, pi/4 , 0, 0, 0, -pi/4 , "LOCAL", "LOCAL")

# Toe
,TF_Prm("BigToe.L",             "Toe_T.L",      0, 0.01, 0, 0.01, 0, 0, 'Y', 'Z', 'X', 'ROTATION', 0, -pi/4 , 0, 0, 0, pi/4 , "LOCAL", "LOCAL")
,TF_Prm("BigToe.L.001",         "BigToe_T.L",   0, 0.01, 0, 0.01, 0, 0, 'Y', 'Z', 'X', 'ROTATION', 0, -pi/4 , 0, 0, 0, pi/4 , "LOCAL", "LOCAL")
,TF_Prm("BigToe.L.002",         "BigToe_T.L",   0, 0.01, 0, 0.01, 0, 0, 'Y', 'Z', 'X', 'ROTATION', 0, -pi/4 , 0, 0, 0, pi/4 , "LOCAL", "LOCAL")

#,TF_PRM()
]



# FUNCTIONS
def setup_transform(bone_name, subtarget_bone_name, bone_transform):
    logger.info(bone_name + " ctrl bone is " + subtarget_bone_name)

    if bpy.context.object.pose.bones.find(bone_name) == -1:
        logger.warn("Bone not found. Bone name is " + bone_name)
        return
    
    bone = bpy.context.object.pose.bones[bone_name]
    if bone.constraints.find(TRANSFORMATION_NAME) == -1:
        newConstraint = bone.constraints.new(type=CONSTRAINT_TYPE)
        newConstraint.name = TRANSFORMATION_NAME
        
    constraint = bone.constraints[TRANSFORMATION_NAME]
    constraint.target = bpy.data.objects[ARMATURE_NAME]
    constraint.subtarget = subtarget_bone_name
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


# MAIN
logger.start()

for bone_transform in bone_transformations:
    setup_transform(bone_transform.bone_name, bone_transform.subtarget_bone_name, bone_transform)
    
    # IF .L Bone FOUND. Setup .R Bone
    if utils_judge.is_include_l(bone_transform.bone_name):
        r_bone_name = utils_converter.cnv_l_2_r(bone_transform.bone_name)
        r_target_bone_name = utils_converter.cnv_l_2_r(bone_transform.subtarget_bone_name)
        setup_transform(r_bone_name, r_target_bone_name, bone_transform)

logger.end()



