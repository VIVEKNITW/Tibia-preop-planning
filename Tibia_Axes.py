import bpy
from bpy.types import Operator
from .Tibia_helper_functions import copy_object, make_axis, unhide_list, move_to_collection, delete_obj, check_obj_list, check_create_collection

    
class TIBIA_OT_TibiaMechanicalAxis(Operator):
    """ """
    bl_label = "Tibia Mechanical Axis"
    bl_idname = "object.tibiamechanicalaxis"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks", "Tibia_Axes"])
        unhide_list(["Tibia Mechanical Axis", 'Ankle Center', 'Tibia Knee Center'])
        
        try:
            delete_obj(bpy.data.objects["Tibia Mechanical Axis"])
        except:
            pass
        
        check_list = check_obj_list(['Ankle Center', 'Tibia Knee Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Ankle Center'], "Ankle Center for mech axis")
            copy_object(bpy.data.objects['Tibia Knee Center'], "Tibia Knee Center for mech axis")
            make_axis([bpy.data.objects["Ankle Center for mech axis"], bpy.data.objects["Tibia Knee Center for mech axis"]], "Tibia Mechanical Axis")

            move_to_collection("Tibia_Axes", bpy.data.objects["Tibia Mechanical Axis"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))

        return {'FINISHED'}


class TIBIA_OT_TibiaAPAxis(Operator):
    """ """
    bl_label = "Tibia AP Axis"
    bl_idname = "object.tibiaapaxis"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):

        check_create_collection(["Tibia_Landmarks", "Tibia_Axes"])
        unhide_list(["Tibia AP Axis", 'PCL Insertion', 'Tibia Tuberosity'])

        try:
            delete_obj(bpy.data.objects["Tibia AP Axis"])
        except:
            pass

        check_list = check_obj_list(['PCL Insertion', 'Tibia Tuberosity'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['PCL Insertion'], "PCL Insertion for TibiaAPAxis")
            copy_object(bpy.data.objects['Tibia Tuberosity'], "Tibia Tuberosity for TibiaAPAxis")
            make_axis([bpy.data.objects["PCL Insertion for TibiaAPAxis"], bpy.data.objects["Tibia Tuberosity for TibiaAPAxis"]], "Tibia AP Axis")

            move_to_collection("Tibia_Axes", bpy.data.objects["Tibia AP Axis"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))

        return {'FINISHED'}


class TIBIA_OT_TransEpicondylarAxis(Operator):
    """ """
    bl_label = "Trans Epicondylar Axis"
    bl_idname = "object.transepicondylaraxis"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        check_create_collection(["Landmarks", "Axes"])
        unhide_list(["Trans Epicondylar Axis", 'Lateral Epicondyle', 'Medial Epicondyle'])

        try:
            delete_obj(bpy.data.objects["Trans Epicondylar Axis"])
        except:
            pass

        check_list = check_obj_list(['Lateral Epicondyle', 'Medial Epicondyle'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Lateral Epicondyle'], "Lateral Epicondyle for TEA")
            copy_object(bpy.data.objects['Medial Epicondyle'], "Medial Epicondyle for TEA")
            make_axis([bpy.data.objects['Lateral Epicondyle for TEA'], bpy.data.objects['Medial Epicondyle for TEA']], "Trans Epicondylar Axis")

            move_to_collection("Axes", bpy.data.objects["Trans Epicondylar Axis"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
      
        return {'FINISHED'}