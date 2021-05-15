# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Tibia preop-planning",
    "author" : "Vivekanand Shanbhag",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from .Tibia_Landmarks_Panel import TIBIA_PT_Landmark_assignment
from .Tibia_Projections_panel import TIBIA_PT_Projections
from .Tibia_angles_panel import TIBIA_PT_Angles
from .Tibia_measureIt_panel import MyProperty_Tibia, TIBIA_PT_MeasureIt
from .Tibia_measureIt import TIBIA_OT_EnableOrDisableMeasureIt
from .Tibia_Landmarks import TIBIA_OT_TibiaKneeCenter, TIBIA_OT_ProximalLateralTibialPlateau, TIBIA_OT_ProximalMedialTibialPlateau, TIBIA_OT_PosteriorLateralTibialPlateau, TIBIA_OT_PosteriorMedialTibialPlateau, TIBIA_OT_MedialMedialTibialPlateau, TIBIA_OT_LateralLateralTibialPlateau, TIBIA_OT_PCLInsertion, TIBIA_OT_TibiaTuberosity, TIBIA_OT_FibulaHead, TIBIA_OT_AnkleCenter, TIBIA_OT_Point1AnkleCenter, TIBIA_OT_Point2AnkleCenter, TIBIA_OT_MedialEpicondyle, TIBIA_OT_LateralEpicondyle
from .Tibia_Axes import TIBIA_OT_TibiaMechanicalAxis, TIBIA_OT_TibiaAPAxis, TIBIA_OT_TransEpicondylarAxis
from .Tibia_Planes import TIBIA_OT_CoronalPlane, Tibia_OT_SagittalPlane, Tibia_OT_DistalPlane
from .Tibia_Angles import TIBIA_OT_CondylarDifferenceofTibialPlateau, TIBIA_OT_HeadFibTibialJointLine, TIBIA_OT_ProxTibiaVarus, TIBIA_OT_ProxMedialTibiaVarus, TIBIA_OT_ProxLateralTibiaVarus, TIBIA_OT_ProxTibiaICVarus, TIBIA_OT_PCATibiatoTibAPAxis, TIBIA_OT_AngleTEA_TibiaAPAxis, TIBIA_OT_ProxTibiaSlope
from .Tibia_projections import TIBIA_OT_Projections

classes = (TIBIA_PT_Landmark_assignment, TIBIA_OT_TibiaKneeCenter, TIBIA_OT_ProximalLateralTibialPlateau, TIBIA_OT_ProximalMedialTibialPlateau, TIBIA_OT_PosteriorLateralTibialPlateau, TIBIA_OT_PosteriorMedialTibialPlateau, TIBIA_OT_MedialMedialTibialPlateau, TIBIA_OT_LateralLateralTibialPlateau, TIBIA_OT_PCLInsertion, TIBIA_OT_TibiaTuberosity, TIBIA_OT_FibulaHead, TIBIA_OT_AnkleCenter, TIBIA_OT_Point1AnkleCenter, TIBIA_OT_Point2AnkleCenter,  TIBIA_PT_Projections, TIBIA_OT_Projections, TIBIA_PT_Angles, TIBIA_OT_CoronalPlane, Tibia_OT_SagittalPlane, Tibia_OT_DistalPlane,TIBIA_OT_TibiaMechanicalAxis, TIBIA_OT_TibiaAPAxis, TIBIA_OT_TransEpicondylarAxis, TIBIA_OT_CondylarDifferenceofTibialPlateau, TIBIA_OT_HeadFibTibialJointLine, TIBIA_OT_ProxTibiaVarus, TIBIA_OT_ProxMedialTibiaVarus, TIBIA_OT_ProxLateralTibiaVarus, TIBIA_OT_ProxTibiaICVarus, TIBIA_OT_PCATibiatoTibAPAxis, TIBIA_OT_AngleTEA_TibiaAPAxis,  MyProperty_Tibia, TIBIA_PT_MeasureIt, TIBIA_OT_EnableOrDisableMeasureIt, TIBIA_OT_MedialEpicondyle, TIBIA_OT_LateralEpicondyle, TIBIA_OT_ProxTibiaSlope)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=MyProperty_Tibia)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()