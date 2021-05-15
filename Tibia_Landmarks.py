import bpy 
from bpy.types import Operator
from .Tibia_helper_functions import unhide, move_to_collection, delete_obj, check_create_collection, create_ankle_point, check_obj_list, add_single_vert

class TIBIA_OT_TibiaKneeCenter(Operator):
    """ """
    bl_label = "Tibia Knee Center"
    bl_idname = "object.tibiakneecenter"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):    
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Tibia Knee Center"])
            delete_obj(bpy.data.objects["Tibia Knee Center"])
        except:
            pass
        
        add_single_vert("Tibia Knee Center")
        
        move_to_collection("Tibia_Landmarks", bpy.data.objects["Tibia Knee Center"])
        return {'FINISHED'}


class TIBIA_OT_ProximalLateralTibialPlateau(Operator):
    """ """
    bl_label = "Proximal Lateral Tibial Plateau"
    bl_idname = "object.proximallateraltibialplateau"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Proximal Lateral Tibial Plateau"])
            delete_obj(bpy.data.objects["Proximal Lateral Tibial Plateau"])
        except:
            pass
        
        add_single_vert("Proximal Lateral Tibial Plateau")

        move_to_collection("Tibia_Landmarks", bpy.data.objects["Proximal Lateral Tibial Plateau"])
        return {'FINISHED'}


class TIBIA_OT_ProximalMedialTibialPlateau(Operator):
    """ """
    bl_label = "Proximal Medial Tibial Plateau"
    bl_idname = "object.proximalmedialtibialplateau"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Proximal Medial Tibial Plateau"])
            delete_obj(bpy.data.objects["Proximal Medial Tibial Plateau"])
        except:
            pass
        
        add_single_vert("Proximal Medial Tibial Plateau")

        move_to_collection("Tibia_Landmarks", bpy.data.objects["Proximal Medial Tibial Plateau"])
        return {'FINISHED'}


class TIBIA_OT_PosteriorMedialTibialPlateau(Operator):
    """ """
    bl_label = "Posterior Medial Tibial Plateau"
    bl_idname = "object.posteriormedialtibialplateau"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Posterior Medial Tibial Plateau"])
            delete_obj(bpy.data.objects["Posterior Medial Tibial Plateau"])
        except:
            pass
        
        add_single_vert("Posterior Medial Tibial Plateau")

        move_to_collection("Tibia_Landmarks", bpy.data.objects["Posterior Medial Tibial Plateau"])
        return {'FINISHED'}


class TIBIA_OT_PosteriorLateralTibialPlateau(Operator):
    """ """
    bl_label = "Posterior Lateral Tibial Plateau"
    bl_idname = "object.posteriorlateraltibialplateau"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Posterior Lateral Tibial Plateau"])
            delete_obj(bpy.data.objects["Posterior Lateral Tibial Plateau"])
        except:
            pass
        
        add_single_vert("Posterior Lateral Tibial Plateau")

        move_to_collection("Tibia_Landmarks", bpy.data.objects["Posterior Lateral Tibial Plateau"])
        return {'FINISHED'}


class TIBIA_OT_MedialMedialTibialPlateau(Operator):
    """ """
    bl_label = "Medial Medial Tibial Plateau"
    bl_idname = "object.medialmedialtibialplateau"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Medial Medial Tibial Plateau"])
            delete_obj(bpy.data.objects["Medial Medial Tibial Plateau"])
        except:
            pass
        
        add_single_vert("Medial Medial Tibial Plateau")

        move_to_collection("Tibia_Landmarks", bpy.data.objects["Medial Medial Tibial Plateau"])
        return {'FINISHED'}

    
class TIBIA_OT_LateralLateralTibialPlateau(Operator):
    """ """
    bl_label = "Lateral Lateral Tibial Plateau"
    bl_idname = "object.laterallateraltibialplateau"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Lateral Lateral Tibial Plateau"])
            delete_obj(bpy.data.objects["Lateral Lateral Tibial Plateau"])
        except:
            pass
        
        add_single_vert("Lateral Lateral Tibial Plateau")
       
        move_to_collection("Tibia_Landmarks", bpy.data.objects["Lateral Lateral Tibial Plateau"])
        return {'FINISHED'}

    
class TIBIA_OT_PCLInsertion(Operator):
    """ """
    bl_label = "PCL Insertion"
    bl_idname = "object.pclinsertion"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["PCL Insertion"])
            delete_obj(bpy.data.objects["PCL Insertion"])
        except:
            pass
        
        add_single_vert("PCL Insertion")

        move_to_collection("Tibia_Landmarks", bpy.data.objects["PCL Insertion"])
        return {'FINISHED'}


class TIBIA_OT_TibiaTuberosity(Operator):
    """ """
    bl_label = "Tibia Tuberosity"
    bl_idname = "object.tibiatuberosity"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Tibia Tuberosity"])
            delete_obj(bpy.data.objects["Tibia Tuberosity"])
        except:
            pass
        
        add_single_vert("Tibia Tuberosity")

        move_to_collection("Tibia_Landmarks", bpy.data.objects["Tibia Tuberosity"])
        return {'FINISHED'}


class TIBIA_OT_FibulaHead(Operator):
    """ """
    bl_label = "Fibula Head"
    bl_idname = "object.fibulahead"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Fibula Head"])
            delete_obj(bpy.data.objects["Fibula Head"])
        except:
            pass
        
        add_single_vert("Fibula Head")

        move_to_collection("Tibia_Landmarks", bpy.data.objects["Fibula Head"])
        return {'FINISHED'}


class TIBIA_OT_AnkleCenter(Operator):
    """ """
    bl_label = "Ankle Center"
    bl_idname = "object.anklecenter"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Ankle Center"])
            delete_obj(bpy.data.objects["Ankle Center"])
        except:
            pass
        
        add_single_vert("Ankle Center")
        
        move_to_collection("Tibia_Landmarks", bpy.data.objects["Ankle Center"])
        return {'FINISHED'}


class TIBIA_OT_Point1AnkleCenter(Operator):
    """ """
    bl_label = "Point1 (Ankle Center)"
    bl_idname = "object.point1anklecenter"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Point1 (Ankle Center)"])
            delete_obj(bpy.data.objects["Point1 (Ankle Center)"])
        except:
            pass
        
        add_single_vert("Point1 (Ankle Center)")
        
        move_to_collection("Tibia_Landmarks", bpy.data.objects["Point1 (Ankle Center)"])

        check_list = check_obj_list(["Point1 (Ankle Center)", "Point2 (Ankle Center)"])
        if len(check_list) == 0:
            create_ankle_point()

        return {'FINISHED'}


class TIBIA_OT_Point2AnkleCenter(Operator):
    """ """
    bl_label = "Point2 (Ankle Center)"
    bl_idname = "object.point2anklecenter"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Point2 (Ankle Center)"])
            delete_obj(bpy.data.objects["Point2 (Ankle Center)"])
        except:
            pass
        
        add_single_vert("Point2 (Ankle Center)")

        move_to_collection("Tibia_Landmarks", bpy.data.objects["Point2 (Ankle Center)"])

        check_list = check_obj_list(["Point1 (Ankle Center)", "Point2 (Ankle Center)"])
        if len(check_list) == 0:
            create_ankle_point()

        return {'FINISHED'}

    
class TIBIA_OT_LateralEpicondyle(Operator):
    """ """
    bl_label = "Lateral Epicondyle"
    bl_idname = "object.lateralepicondyle"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Lateral Epicondyle"])
            delete_obj(bpy.data.objects["Lateral Epicondyle"])
        except:
            pass
        
        add_single_vert("Lateral Epicondyle")

        move_to_collection("Tibia_Landmarks", bpy.data.objects["Lateral Epicondyle"])
        return {'FINISHED'}


class TIBIA_OT_MedialEpicondyle(Operator):
    """ """
    bl_label = "Medial Epicondyle"
    bl_idname = "object.medialepicondyle"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks"])
        try:
            unhide(bpy.data.objects["Medial Epicondyle"])
            delete_obj(bpy.data.objects["Medial Epicondyle"])
        except:
            pass
        
        add_single_vert("Medial Epicondyle")
        
        move_to_collection("Tibia_Landmarks", bpy.data.objects["Medial Epicondyle"])
        return {'FINISHED'}