import bpy
from bpy.types import Operator
from .Tibia_helper_functions import save_orientation_InEditMode, select_activate, cursor_to_obj, add_plane, copy_object, delete_obj, save_orientation_obj, unhide_list, move_to_collection, check_obj_list, check_create_collection

class Tibia_OT_SagittalPlane(Operator):
    """ """
    bl_label = "Tibia Sagittal Plane"
    bl_idname = "object.tibiasagittalplane"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes"])
        unhide_list(["Tibia Sagittal Plane", "Tibia Mechanical Axis", 'Tibia AP Axis', 'Tibia Knee Center'])
        
        try:
            delete_obj(bpy.data.objects["Sagittal Plane"])
        except:
            pass
        
        check_list = check_obj_list(["Tibia Mechanical Axis", 'Tibia AP Axis', 'Tibia Knee Center'])
        if len(check_list) == 0:
            save_orientation_InEditMode(bpy.data.objects["Tibia Mechanical Axis"], "EDGE")
            copy_object(bpy.data.objects['Tibia AP Axis'], 'Tibia AP Axis for Sagittal Plane')
        
            select_activate(bpy.data.objects['Tibia AP Axis for Sagittal Plane'])
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_mode(type="EDGE")
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, -120, 0), "constraint_axis":(False, True, False)})
            bpy.ops.mesh.select_mode(type="FACE")
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.transform.create_orientation(use=True)
            bpy.ops.object.editmode_toggle()

            cursor_to_obj(bpy.data.objects['Tibia Knee Center'])
        
            add_plane("Tibia Sagittal Plane")
            delete_obj(bpy.data.objects['Tibia AP Axis for Sagittal Plane'])

            move_to_collection("Tibia_Planes", bpy.data.objects["Tibia Sagittal Plane"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class TIBIA_OT_CoronalPlane(Operator):
    """ """
    bl_label = "Tibia Coronal Plane"
    bl_idname = "object.tibiacoronalplane"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):

        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes"])
        unhide_list(["Tibia Coronal Plane", 'Tibia Knee Center', 'Tibia Sagittal Plane'])
        
        try:
            delete_obj(bpy.data.objects["Tibia Coronal Plane"])
        except:
            pass
        
        check_list = check_obj_list(['Tibia Sagittal Plane', 'Tibia Knee Center'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects['Tibia Sagittal Plane'])
            cursor_to_obj(bpy.data.objects['Tibia Knee Center'])
            add_plane("Tibia Coronal Plane")
            bpy.ops.transform.transform(mode='ALIGN')
            bpy.ops.transform.rotate(value=1.5708, orient_axis='Y',  constraint_axis=(False, True, False))

            move_to_collection("Tibia_Planes", bpy.data.objects["Tibia Coronal Plane"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class Tibia_OT_DistalPlane(Operator):
    """ """
    bl_label = "Tibia Distal Plane"
    bl_idname = "object.tibiadistalplane"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):

        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes"])
        unhide_list(["Tibia Distal Plane" , "Tibia Sagittal Plane", 'Tibia Knee Center'])

        try:
            delete_obj(bpy.data.objects["Tibia Distal Plane"])
        except:
            pass
        
        check_list = check_obj_list(["Tibia Sagittal Plane", 'Tibia Knee Center'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects["Tibia Sagittal Plane"])
            cursor_to_obj(bpy.data.objects['Tibia Knee Center'])
            add_plane("Tibia Distal Plane")
            bpy.ops.transform.transform(mode='ALIGN')
            bpy.ops.transform.rotate(value=1.5708, orient_axis='X', constraint_axis=(False, True, False))

            move_to_collection("Tibia_Planes", bpy.data.objects["Tibia Distal Plane"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}