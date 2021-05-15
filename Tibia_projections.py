import bpy
from bpy.types import Operator
from .Tibia_helper_functions import copy_object, shrinkwrap_obj, unhide_list, move_to_collection, delete_obj, check_create_collection, check_obj_list

class TIBIA_OT_Projections(Operator):
    """ """
    bl_label = "Projections"
    bl_idname = "object.tibiaprojections"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        
        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes", "Tibia_Projections"])
        unhide_list(["Proximal Lateral Tibial Plateau P:Cor", "Proximal Lateral Tibial Plateau P:Cor.Sag","Proximal Medial Tibial Plateau P:Cor","Proximal Medial Tibial Plateau P:Cor.Sag", "PCL Insertion P:Cor","PCL Insertion P:Cor.Sag", "Fibula Head P:Cor", "Fibula Head P:Cor.Sag", "Medial Medial Tibial Plateau P:Cor", "Lateral Lateral Tibial Plateau P:Cor","PCL Insertion P:Dis","Tibia Tuberosity P:Dis", "Posterior Lateral Tibial Plateau P:Dis", "Posterior Medial Tibial Plateau P:Dis", "Lateral Epicondyle P:TIB_Dis", "Medial Epicondyle P:TIB_Dis"])
        unhide_list(['Medial Epicondyle', 'Lateral Epicondyle', 'Posterior Medial Tibial Plateau', 'Posterior Lateral Tibial Plateau', 'PCL Insertion', "Tibia Distal Plane", 'Tibia Tuberosity', 'Lateral Lateral Tibial Plateau', 'Medial Medial Tibial Plateau', "Fibula Head P:Cor", 'Fibula Head', 'PCL Insertion P:Cor', 'PCL Insertion', 'Proximal Medial Tibial Plateau P:Cor', 'Proximal Medial Tibial Plateau', 'Proximal Lateral Tibial Plateau P:Cor', 'Proximal Lateral Tibial Plateau', "Tibia Coronal Plane", "Tibia Sagittal Plane"])

        try:
            delete_obj(bpy.data.objects["Proximal Lateral Tibial Plateau P:Cor"])
        except:
            pass
        
        if (len(check_obj_list(['Proximal Lateral Tibial Plateau', "Tibia Coronal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Proximal Lateral Tibial Plateau'], "Proximal Lateral Tibial Plateau P:Cor")
                shrinkwrap_obj(bpy.data.objects["Proximal Lateral Tibial Plateau P:Cor"], bpy.data.objects["Tibia Coronal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Proximal Lateral Tibial Plateau P:Cor"])        
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Proximal Lateral Tibial Plateau P:Cor.Sag"])
        except:
            pass
        
        if (len(check_obj_list(['Proximal Lateral Tibial Plateau P:Cor', "Tibia Sagittal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Proximal Lateral Tibial Plateau P:Cor'], "Proximal Lateral Tibial Plateau P:Cor.Sag")
                shrinkwrap_obj(bpy.data.objects["Proximal Lateral Tibial Plateau P:Cor.Sag"], bpy.data.objects["Tibia Sagittal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Proximal Lateral Tibial Plateau P:Cor.Sag"])        
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Proximal Medial Tibial Plateau P:Cor"])
        except:
            pass
        
        if (len(check_obj_list(['Proximal Medial Tibial Plateau', "Tibia Coronal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Proximal Medial Tibial Plateau'], "Proximal Medial Tibial Plateau P:Cor")
                shrinkwrap_obj(bpy.data.objects["Proximal Medial Tibial Plateau P:Cor"], bpy.data.objects["Tibia Coronal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Proximal Medial Tibial Plateau P:Cor"])        
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Proximal Medial Tibial Plateau P:Cor.Sag"])
        except:
            pass
        
        if (len(check_obj_list(['Proximal Medial Tibial Plateau P:Cor', "Tibia Sagittal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Proximal Medial Tibial Plateau P:Cor'], "Proximal Medial Tibial Plateau P:Cor.Sag")
                shrinkwrap_obj(bpy.data.objects["Proximal Medial Tibial Plateau P:Cor.Sag"], bpy.data.objects["Tibia Sagittal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Proximal Medial Tibial Plateau P:Cor.Sag"])        
            except:
                pass


        try:
            delete_obj(bpy.data.objects["PCL Insertion P:Cor"])
        except:
            pass
        
        if (len(check_obj_list(['PCL Insertion', "Tibia Coronal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['PCL Insertion'], "PCL Insertion P:Cor")
                shrinkwrap_obj(bpy.data.objects["PCL Insertion P:Cor"], bpy.data.objects["Tibia Coronal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["PCL Insertion P:Cor"])        
            except:
                pass


        try:
            delete_obj(bpy.data.objects["PCL Insertion P:Cor.Sag"])
        except:
            pass
        
        if (len(check_obj_list(['PCL Insertion P:Cor', "Tibia Coronal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['PCL Insertion P:Cor'], "PCL Insertion P:Cor.Sag")
                shrinkwrap_obj(bpy.data.objects["PCL Insertion P:Cor.Sag"], bpy.data.objects["Tibia Sagittal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["PCL Insertion P:Cor.Sag"])        
            except:
                pass

        
        try:
            delete_obj(bpy.data.objects["Fibula Head P:Cor"])
        except:
            pass
        
        if (len(check_obj_list(['Fibula Head', "Tibia Coronal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Fibula Head'], "Fibula Head P:Cor")
                shrinkwrap_obj(bpy.data.objects["Fibula Head P:Cor"], bpy.data.objects["Tibia Coronal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Fibula Head P:Cor"])        
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Fibula Head P:Cor.Sag"])
        except:
            pass
        
        if (len(check_obj_list(["Fibula Head P:Cor", "Tibia Sagittal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects["Fibula Head P:Cor"], "Fibula Head P:Cor.Sag")
                shrinkwrap_obj(bpy.data.objects["Fibula Head P:Cor.Sag"], bpy.data.objects["Tibia Sagittal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Fibula Head P:Cor.Sag"])        
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Medial Medial Tibial Plateau P:Cor"])
        except:
            pass
        
        if (len(check_obj_list(['Medial Medial Tibial Plateau', "Tibia Coronal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Medial Medial Tibial Plateau'], "Medial Medial Tibial Plateau P:Cor")
                shrinkwrap_obj(bpy.data.objects["Medial Medial Tibial Plateau P:Cor"], bpy.data.objects["Tibia Coronal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Medial Medial Tibial Plateau P:Cor"])        
            except:
                pass

        
        try:
            delete_obj(bpy.data.objects["Lateral Lateral Tibial Plateau P:Cor"])
        except:
            pass
        
        if (len(check_obj_list(['Lateral Lateral Tibial Plateau', "Tibia Coronal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Lateral Lateral Tibial Plateau'], "Lateral Lateral Tibial Plateau P:Cor")
                shrinkwrap_obj(bpy.data.objects["Lateral Lateral Tibial Plateau P:Cor"], bpy.data.objects["Tibia Coronal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Lateral Lateral Tibial Plateau P:Cor"])        
            except:
                pass
        

        try:
            delete_obj(bpy.data.objects["PCL Insertion P:Dis"])
        except:
            pass
        
        if (len(check_obj_list(['PCL Insertion', "Tibia Distal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['PCL Insertion'], "PCL Insertion P:Dis")
                shrinkwrap_obj(bpy.data.objects["PCL Insertion P:Dis"], bpy.data.objects["Tibia Distal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["PCL Insertion P:Dis"])        
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Tibia Tuberosity P:Dis"])
        except:
            pass
        
        if (len(check_obj_list(['Tibia Tuberosity', "Tibia Distal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Tibia Tuberosity'], "Tibia Tuberosity P:Dis")
                shrinkwrap_obj(bpy.data.objects["Tibia Tuberosity P:Dis"], bpy.data.objects["Tibia Distal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Tibia Tuberosity P:Dis"])        
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Posterior Lateral Tibial Plateau P:Dis"])
        except:
            pass
        
        if (len(check_obj_list(['Posterior Lateral Tibial Plateau', "Tibia Distal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Posterior Lateral Tibial Plateau'], "Posterior Lateral Tibial Plateau P:Dis")
                shrinkwrap_obj(bpy.data.objects["Posterior Lateral Tibial Plateau P:Dis"], bpy.data.objects["Tibia Distal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Posterior Lateral Tibial Plateau P:Dis"])        
            except:
                pass

        
        try:
            delete_obj(bpy.data.objects["Posterior Medial Tibial Plateau P:Dis"])
        except:
            pass
        
        if (len(check_obj_list(['Posterior Medial Tibial Plateau', "Tibia Distal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Posterior Medial Tibial Plateau'], "Posterior Medial Tibial Plateau P:Dis")
                shrinkwrap_obj(bpy.data.objects["Posterior Medial Tibial Plateau P:Dis"], bpy.data.objects["Tibia Distal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Posterior Medial Tibial Plateau P:Dis"])        
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Lateral Epicondyle P:TIB_Dis"])
        except:
            pass
        
        if (len(check_obj_list(['Lateral Epicondyle', "Tibia Distal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Lateral Epicondyle'], "Lateral Epicondyle P:TIB_Dis")
                shrinkwrap_obj(bpy.data.objects["Lateral Epicondyle P:TIB_Dis"], bpy.data.objects["Tibia Distal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Lateral Epicondyle P:TIB_Dis"])        
            except:
                pass


        try:
            delete_obj(bpy.data.objects["Medial Epicondyle P:TIB_Dis"])
        except:
            pass
        
        if (len(check_obj_list(['Medial Epicondyle', "Tibia Distal Plane"])) == 0):
            try:
                copy_object(bpy.data.objects['Medial Epicondyle'], "Medial Epicondyle P:TIB_Dis")
                shrinkwrap_obj(bpy.data.objects["Medial Epicondyle P:TIB_Dis"], bpy.data.objects["Tibia Distal Plane"])
                move_to_collection("Tibia_Projections", bpy.data.objects["Medial Epicondyle P:TIB_Dis"])        
            except:
                pass
        
        return {'FINISHED'}