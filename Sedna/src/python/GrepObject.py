#!BPY
# -*- coding: UTF-8 -*-
# Set IK Limits
#
# 2016.01.17 Natukikazemizo
import bpy
import math
import re

# Using Regular expression
#"[0]"	1文字が0
#"[0-9]"	1文字が0,1,2,3,4,5,6,7,8,9のいずれか
#"[02468]"	1文字が偶数
#"[BCD]"	1文字がB,C,Dのいずれか
#"[B-D]"	1文字がB,C,Dのいずれか
#"[0-2A-C]"	1文字が0,1,2,A,B,Cのいずれか
#"[^12]"	1文字が1,2以外
#"\w"	1文字が英数字
#"\W"	1文字が英数字以外
#"\d"	1文字が数字
#"\D"	1文字が数字以外
#"\s"	1文字が空白
#"\S"	1文字が空白以外
#"."	1文字が任意の1文字（改行文字以外の）
#"\t"	1文字がタブ
#"\n"	1文字が改行
#"A*"	Aが連続で0個以上
#"A+"	Aが連続で1個以上
#/AB?/	BがAの次に0個または1個あるか
#/z{4}$/	zが連続で4個あって、データ末尾か？
#/z{3,}/	zが連続で3個以上あるか？
#/(ABC){2,4}	2回以上4回以下のABCの繰り返しになっているか？
#"(?:.)"	()を記憶しない
#/(?:a.b){1,3}/	a.b a.ba.b a.ba.ba.b いずれかに一致
#/\bABC\b/	ABCが単語単位か？
#"\."	.があるか？
#"\\"	\があるか？
#"\*"	*があるか？
#"\?"	?があるか？
#"\+"	+があるか？
#"\^"	^があるか？
#"(HELLO).*\1"	HELLOが行中にもう1回出現するか？
#"(HELLO)(SEEU).*\2"	SEEUが行中にもう1回出現するか？

# At pose mode Selected bones: bpy.context.selected_pose_bones:

# Way of selecting objects is Description in here
# https://sites.google.com/site/matosus304blendernotes/home/blender-python-script

##選択しているボーンに対して
#for x in bpy.context.selected_bones:

#選択しているボーンに対して（エディットモードで使用）
#for x in bpy.context.selected_editable_bones:

#選択しているボーンに対して（ポーズモードで使用）
#for x in bpy.context.selected_pose_bones:

#選択しているオブジェクトのすべてのボーンに対して
#for x in bpy.context.active_object.pose.bones:

#選択オブジェクトのボーングループに対して
#obj = bpy.context.active_object.pose


#ボーン関連のコードです。
#Blenderのボーンデータには、ボーンそのものを表すデータ(bones)と、エディットモードで編集できるのと同等の操作ができるエディットボーン、ボーンのポーズを表すデータ(pose)とがあります。混同しやすいので注意してください。
#なお、ポーズからは".bone"でボーンデータにアクセスできるのに対して、逆にボーンデータからポーズにそのままアクセスはできない様です。

#ボーンに対して
##選択しているボーンに対して
#for x in bpy.context.selected_bones:
#    print(x.name)                                        #ボーン名を表示
#    x.use_deform = False                           #ボーンによる変形を行わない
#    x.hide = True                                       #非表示にする

##選択しているオブジェクトのすべてのボーンに対して
#for x in bpy.context.active_object.data.bones:
#    print(x.name)                                        #ボーン名を表示

#エディットボーンに対して
##選択しているボーンに対して（エディットモードで使用）
#for x in bpy.context.selected_editable_bones:
#    print(x.name)                                        #ボーン名を表示
#    x.head = (0,0,0)                                    #ボーンのヘッド位置を変更
#    x.tail = (0,0,1)                                       #ボーンのテール位置を変更

##選択しているオブジェクトのすべてのボーンに対して
#for x in bpy.context.active_object.data.edit_bones:
#    print(x.name)                                        #ボーン名を表示

#ポーズに対して
##選択しているボーンに対して（ポーズモードで使用）
#for x in bpy.context.selected_pose_bones:
#    print(x.name)                                       #ボーン名を表示
#    x.location = (0,0,0)                               #位置をセット
#    x.rotation_quaternion = (1,0,0,0)            #クオータニオン回転をセット
#    x.custom_shape                                  #カスタムシェイプ
#    x.bone_group = bpy.context.active_object.pose.bone_groups["Group"]    #ボーングループを設定する
#    x.bone                                                #ボーンデータにアクセス

##選択しているオブジェクトのすべてのボーンに対して
#for x in bpy.context.active_object.pose.bones:
#    print(x.name)                                        #ボーン名を表示
#    if x.bone_group != None and x.bone_group.name == "Group":    #指定したボーングループに属するボーンに対して
#        print(x.name)

##選択オブジェクトのボーングループに対して
#obj = bpy.context.active_object.pose
#obj.bone_groups[0].color_set = "CUSTOM"    #カラーセットをカスタム（任意のカラーに設定）に変更

##bpy.ops.pose
#bpy.ops.pose.group_add()                        #ボーングループを追加


#コンストレインに対して
##選択しているボーンに対して（ポーズモードで使用）
#pose_bone = bpy.context.active_pose_bone
#pose_bone.constraints[0]    #コンストレイントにアクセス
#new_constraint = pose_bone.constraints.new(type="COPY_SCALE")    #新しいコンストレインを追加

from . import debug

if __name__ == "__main__":
    debug.startdebug()

print("##### START #####")
p=re.compile(r".*(0).*\1")
for x in bpy.context.selected_pose_bones:
    if p.match(x.name):
        print(x.name)
print("##### END #####")
    
