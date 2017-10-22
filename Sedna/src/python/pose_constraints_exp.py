#!BPY
# -*- coding: UTF-8 -*-
# Export Custome Shape Settings
#
# 2017.10.22 Natukikazemizo

import bpy
import os
import utils_log
import utils_io_csv

# Constants
WORK_FILE_NAME = "pose_constraints.csv"

# init logger
global logger
logger = utils_log.Util_Log(os.path.basename(__file__))

logger.start()

bone_data = []
header = [
        "bone_name", 
        "constraint_name",
        "mute",
        "target",
        "subtarget_bone_name",
        "from_min_x",
        "from_max_x",
        "from_min_y",
        "from_max_y",
        "from_min_z",
        "from_max_z",
        "map_to_x_from",
        "map_to_y_from",
        "map_to_z_from",
        "map_to",
        "to_min_x",
        "to_max_x",
        "to_min_y",
        "to_max_y",
        "to_min_z",
        "to_max_z",
        "target_space",
        "owner_space"
          ]
bone_data.append(header)

for x in bpy.context.selected_pose_bones:
    for y in x.constraints:
        if y.type == "TRANSFORM":
            print(x.name + ", " + y.name)
            data_row = []
            data_row.append(x.name)
            data_row.append(y.name)
            data_row.append(y.mute)
            data_row.append(y.target.name)
            data_row.append(y.subtarget)
            data_row.append(y.from_min_x)
            data_row.append(y.from_max_x)
            data_row.append(y.from_min_y)
            data_row.append(y.from_max_y)
            data_row.append(y.from_min_z)
            data_row.append(y.from_max_z)
            data_row.append(y.map_to_x_from)
            data_row.append(y.map_to_y_from)
            data_row.append(y.map_to_z_from)
            data_row.append(y.map_to)
            if y.map_to == "LOCATION":
                data_row.append(y.to_min_x)
                data_row.append(y.to_max_x)
                data_row.append(y.to_min_y)
                data_row.append(y.to_max_y)
                data_row.append(y.to_min_z)
                data_row.append(y.to_max_z)
            elif y.map_to == "ROTATION":
                data_row.append(y.to_min_x_rot)
                data_row.append(y.to_max_x_rot)
                data_row.append(y.to_min_y_rot)
                data_row.append(y.to_max_y_rot)
                data_row.append(y.to_min_z_rot)
                data_row.append(y.to_max_z_rot)
            else:
                # map_to:SCALE
                data_row.append(y.to_min_x_scale)
                data_row.append(y.to_max_x_scale)
                data_row.append(y.to_min_y_scale)
                data_row.append(y.to_max_y_scale)
                data_row.append(y.to_min_z_scale)
                data_row.append(y.to_max_z_scale)
            data_row.append(y.target_space)
            data_row.append(y.owner_space)
            bone_data.append(data_row)

utils_io_csv.write(WORK_FILE_NAME, bone_data)

logger.end()

