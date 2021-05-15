import bpy
from bpy.types import Operator
from .Tibia_helper_functions import copy_object, join_obj, make_axis, join_obj, save_orientation_obj, vertex_group, cursor_to_obj, add_plane, delete_obj, move_to_collection, unhide_list, check_obj_list, check_create_collection, remove_doubles, boolean_objects, hide_obj, change_dimension


class TIBIA_OT_CondylarDifferenceofTibialPlateau(Operator):
    """ """
    bl_label = "Condylar Difference of Tibial Plateau"
    bl_idname = "object.condylardifferenceoftibialplateau"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context): 
        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes", "Tibia_Projections", "Tibia_Measurements"])
        unhide_list(["Condylar Difference of Tibial Plateau", "Tibia Distal Plane", 'Proximal Lateral Tibial Plateau P:Cor.Sag', 'Proximal Medial Tibial Plateau P:Cor.Sag'])

        try:
            delete_obj(bpy.data.objects["Condylar Difference of Tibial Plateau"])
        except:
            pass
        
        check_list = check_obj_list(["Tibia Distal Plane", 'Proximal Lateral Tibial Plateau P:Cor.Sag', 'Proximal Medial Tibial Plateau P:Cor.Sag'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects["Tibia Distal Plane"])
            cursor_to_obj(bpy.data.objects['Proximal Lateral Tibial Plateau P:Cor.Sag'])
            add_plane("Condylar Difference of Tibial Plateau P1")

            cursor_to_obj(bpy.data.objects['Proximal Medial Tibial Plateau P:Cor.Sag'])
            add_plane("Condylar Difference of Tibial Plateau P2")

            join_obj([bpy.data.objects["Condylar Difference of Tibial Plateau P1"], bpy.data.objects["Condylar Difference of Tibial Plateau P2"]], "Condylar Difference of Tibial Plateau")

            move_to_collection("Tibia_Measurements", bpy.data.objects["Condylar Difference of Tibial Plateau"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class TIBIA_OT_HeadFibTibialJointLine(Operator):
    """ """
    bl_label = "Head Fib-Tibial Joint Line"
    bl_idname = "object.headfibtibialjointline"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes", "Tibia_Projections", "Tibia_Measurements"])
        unhide_list(["Head Fib-Tibial Joint Line", "Tibia Distal Plane", 'PCL Insertion P:Cor.Sag', 'Fibula Head P:Cor.Sag'])

        try:
            delete_obj(bpy.data.objects["Head Fib-Tibial Joint Line"])
        except:
            pass
        
        check_list = check_obj_list(["Tibia Distal Plane", 'PCL Insertion P:Cor.Sag', 'Fibula Head P:Cor.Sag'])
        if len(check_list) == 0:
            save_orientation_obj(bpy.data.objects["Tibia Distal Plane"])
            cursor_to_obj(bpy.data.objects['PCL Insertion P:Cor.Sag'])
            add_plane("Head Fib-Tibial Joint Line P1")

            cursor_to_obj(bpy.data.objects['Fibula Head P:Cor.Sag'])
            add_plane("Head Fib-Tibial Joint Line P2")
        
        
            join_obj([bpy.data.objects["Head Fib-Tibial Joint Line P1"], bpy.data.objects["Head Fib-Tibial Joint Line P2"]], "Head Fib-Tibial Joint Line")
            
            move_to_collection("Tibia_Measurements", bpy.data.objects["Head Fib-Tibial Joint Line"])

        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))

        return {'FINISHED'}

    
class TIBIA_OT_ProxTibiaVarus(Operator):
    """ """
    bl_label = "Prox tibia varus"
    bl_idname = "object.proxtibiavarus"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes", "Tibia_Projections", "Tibia_Measurements"])
        unhide_list(["Prox tibia varus", "Tibia Mechanical Axis", 'Medial Medial Tibial Plateau P:Cor', 'Lateral Lateral Tibial Plateau P:Cor', 'Ankle Center'])

        try:
            delete_obj(bpy.data.objects["Prox tibia varus"])
        except:
            pass
        
        check_list = check_obj_list(["Tibia Mechanical Axis", 'Medial Medial Tibial Plateau P:Cor', 'Lateral Lateral Tibial Plateau P:Cor', 'Ankle Center'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects["Tibia Mechanical Axis"], "Tibia Mechanical Axis ProxTibiaVarus")
            copy_object(bpy.data.objects['Medial Medial Tibial Plateau P:Cor'], 'Medial Medial Plateau P:Cor ProxTibiaVarus L2')
            copy_object(bpy.data.objects['Lateral Lateral Tibial Plateau P:Cor'], 'Lateral Lateral Plateau P:Cor ProxTibiaVarus L2')
            make_axis([bpy.data.objects['Medial Medial Plateau P:Cor ProxTibiaVarus L2'], bpy.data.objects['Lateral Lateral Plateau P:Cor ProxTibiaVarus L2']], "ProxTibiaVarus L2")
            join_obj([bpy.data.objects["Tibia Mechanical Axis ProxTibiaVarus"], bpy.data.objects["ProxTibiaVarus L2"]], "Prox tibia varus point")
        
            vertex_group(bpy.data.objects["Prox tibia varus point"])
            copy_object(bpy.data.objects["Prox tibia varus point"], "Prox tibia varus point copy")
            copy_object(bpy.data.objects["Prox tibia varus point"], "Prox tibia varus point copy1")
        
            copy_object(bpy.data.objects['Ankle Center'], 'Ankle Center for ProxTibiaVarus')
            copy_object(bpy.data.objects['Lateral Lateral Tibial Plateau'], "Lateral Lateral Tibial Plateau for ProxTibiaVarus")
            copy_object(bpy.data.objects['Medial Medial Tibial Plateau P:Cor'], "Medial Medial Tibial Plateau for ProxTibiaVarus")
            make_axis([bpy.data.objects["Prox tibia varus point"], bpy.data.objects['Ankle Center for ProxTibiaVarus']], "Prox tibia varus 1")
            make_axis([bpy.data.objects["Prox tibia varus point copy"],bpy.data.objects["Lateral Lateral Tibial Plateau for ProxTibiaVarus"]], "Prox tibia varus 2")
            make_axis([bpy.data.objects["Prox tibia varus point copy1"],bpy.data.objects[ "Medial Medial Tibial Plateau for ProxTibiaVarus"]], "Prox tibia varus 3")
            join_obj([bpy.data.objects["Prox tibia varus 1"], bpy.data.objects["Prox tibia varus 2"], bpy.data.objects["Prox tibia varus 3"]], "Prox tibia varus")
            remove_doubles(bpy.data.objects["Prox tibia varus"])
            move_to_collection("Tibia_Measurements", bpy.data.objects["Prox tibia varus"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))

        return {'FINISHED'}


class TIBIA_OT_ProxMedialTibiaVarus(Operator):
    """ """
    bl_label = "Prox Medial Tibia Varus"
    bl_idname = "object.proxmedialtibiavarus"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes", "Tibia_Projections", "Tibia_Measurements"])
        unhide_list(["Prox Medial Tibia Varus", "Tibia Mechanical Axis", 'Medial Medial Tibial Plateau P:Cor', 'Lateral Lateral Tibial Plateau P:Cor', 'Ankle Center',"Tibia Knee Center"])

        try:
            delete_obj(bpy.data.objects["Prox Medial Tibia Varus"])
        except:
            pass
        
        check_list = check_obj_list(["Tibia Mechanical Axis", 'Medial Medial Tibial Plateau P:Cor', 'Lateral Lateral Tibial Plateau P:Cor', 'Ankle Center',"Tibia Knee Center"])
        if len(check_list) == 0:
            copy_object(bpy.data.objects["Tibia Mechanical Axis"], "Tibia Mechanical Axis ProxMedialTibiaVarus L1")
            copy_object(bpy.data.objects['Medial Medial Tibial Plateau P:Cor'], 'Medial Medial Plateau ProxMedialTibiaVarus L2')
            copy_object(bpy.data.objects["Tibia Knee Center"], "Tibia Knee Center ProxMedialTibiaVarus L2")
            make_axis([bpy.data.objects['Medial Medial Plateau ProxMedialTibiaVarus L2'], bpy.data.objects["Tibia Knee Center ProxMedialTibiaVarus L2"]], "ProxMedialTibiaVarus L2")
            join_obj([bpy.data.objects["Tibia Mechanical Axis ProxMedialTibiaVarus L1"], bpy.data.objects["ProxMedialTibiaVarus L2"]],"Prox Medial Tibia Varus")
            remove_doubles(bpy.data.objects["Prox Medial Tibia Varus"])
            move_to_collection("Tibia_Measurements", bpy.data.objects["Prox Medial Tibia Varus"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        
        return {'FINISHED'}

    
class TIBIA_OT_ProxLateralTibiaVarus(Operator):
    """ """
    bl_label = "Prox Lateral Tibia Varus"
    bl_idname = "object.proxlateraltibiavarus"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes", "Tibia_Projections", "Tibia_Measurements"])
        unhide_list(["Prox Lateral Tibia Varus", "Tibia Mechanical Axis", 'Lateral Lateral Tibial Plateau P:Cor', "Tibia Knee Center"])

        try:
            delete_obj(bpy.data.objects["Prox Lateral Tibia Varus"])
        except:
            pass
        
        check_list = check_obj_list(["Tibia Mechanical Axis", 'Lateral Lateral Tibial Plateau P:Cor', "Tibia Knee Center"])
        if len(check_list) == 0:
            copy_object(bpy.data.objects["Tibia Mechanical Axis"], "Tibia Mechanical Axis for ProxLateralTibiaVarus L1")
            copy_object(bpy.data.objects['Lateral Lateral Tibial Plateau P:Cor'], 'Lateral Lateral Plateau ProxLateralTibiaVarus L2')
            copy_object(bpy.data.objects["Tibia Knee Center"], "Tibia Knee Center ProxLateralTibiaVarus L2")
            make_axis([bpy.data.objects['Lateral Lateral Plateau ProxLateralTibiaVarus L2'], bpy.data.objects["Tibia Knee Center ProxLateralTibiaVarus L2"]], "ProxLateralTibiaVarus L2")
            join_obj([bpy.data.objects["Tibia Mechanical Axis for ProxLateralTibiaVarus L1"], bpy.data.objects["ProxLateralTibiaVarus L2"]], "Prox Lateral Tibia Varus")
            remove_doubles(bpy.data.objects["Prox Lateral Tibia Varus"])
            move_to_collection("Tibia_Measurements", bpy.data.objects["Prox Lateral Tibia Varus"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))

        return {'FINISHED'}

    
class TIBIA_OT_ProxTibiaICVarus(Operator):
    """ """
    bl_label = "Prox tibia i/c varus"
    bl_idname = "object.proxtibiaicvarus"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes", "Tibia_Projections", "Tibia_Measurements"])
        unhide_list(["Prox tibia i/c varus", 'Tibia Knee Center', 'Medial Medial Tibial Plateau P:Cor', 'Lateral Lateral Tibial Plateau P:Cor'])

        try:
            delete_obj(bpy.data.objects["Prox tibia i/c varus"])
        except:
            pass
        
        check_list = check_obj_list(['Tibia Knee Center', 'Medial Medial Tibial Plateau P:Cor', 'Lateral Lateral Tibial Plateau P:Cor'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['Tibia Knee Center'], 'Tibia Knee Center ProxTibiaICVarus L1')
            copy_object(bpy.data.objects['Tibia Knee Center'], 'Tibia Knee Center ProxTibiaICVarus L2')
            copy_object(bpy.data.objects['Medial Medial Tibial Plateau P:Cor'], 'Medial Medial Tibial Plateau ProxTibiaICVarus L1')
            copy_object(bpy.data.objects['Lateral Lateral Tibial Plateau P:Cor'], 'Lateral Lateral Tibial Plateau ProxTibiaICVarus L2')

            make_axis([bpy.data.objects['Tibia Knee Center ProxTibiaICVarus L1'], bpy.data.objects['Medial Medial Tibial Plateau ProxTibiaICVarus L1']], "ProxTibiaICVarus L1")
            make_axis([bpy.data.objects['Tibia Knee Center ProxTibiaICVarus L2'], bpy.data.objects['Lateral Lateral Tibial Plateau ProxTibiaICVarus L2']], "ProxTibiaICVarus L2")
            join_obj([bpy.data.objects["ProxTibiaICVarus L1"], bpy.data.objects["ProxTibiaICVarus L2"]], "ProxTibiaICVarus")
            
            remove_doubles(bpy.data.objects["ProxTibiaICVarus"])
            move_to_collection("Tibia_Measurements", bpy.data.objects["ProxTibiaICVarus"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class TIBIA_OT_PCATibiatoTibAPAxis(Operator):
    """ """
    bl_label = "PCA tibia to Tib AP axis"
    bl_idname = "object.pcatibiatotibiaapaxis"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes", "Tibia_Projections", "Tibia_Measurements"])
        unhide_list(["PCA tibia to Tib AP axis", 'PCL Insertion P:Dis', 'Tibia Tuberosity P:Dis', 'Posterior Lateral Tibial Plateau P:Dis','Posterior Medial Tibial Plateau P:Dis'])

        try:
            delete_obj(bpy.data.objects["PCA tibia to Tib AP axis"])
        except:
            pass
        
        check_list = check_obj_list(['PCL Insertion P:Dis', 'Tibia Tuberosity P:Dis', 'Posterior Lateral Tibial Plateau P:Dis','Posterior Medial Tibial Plateau P:Dis'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects['PCL Insertion P:Dis'], 'PCL Insertion P:Dis for PCATibiatoTibAPAxis L1')
            copy_object(bpy.data.objects['Tibia Tuberosity P:Dis'], 'Tibia Tuberosity P:Dis for PCATibiatoTibAPAxis L1')
            copy_object(bpy.data.objects['Posterior Lateral Tibial Plateau P:Dis'], 'Posterior Lateral Plateau PCATibiatoTibAPAxis L2')
            copy_object(bpy.data.objects['Posterior Medial Tibial Plateau P:Dis'], 'Posterior Medial Plateau PCATibiatoTibAPAxis L2')

            make_axis([bpy.data.objects['PCL Insertion P:Dis for PCATibiatoTibAPAxis L1'], bpy.data.objects['Tibia Tuberosity P:Dis for PCATibiatoTibAPAxis L1']], "PCATibiatoTibAPAxis L1")
            make_axis([bpy.data.objects['Posterior Lateral Plateau PCATibiatoTibAPAxis L2'], bpy.data.objects['Posterior Medial Plateau PCATibiatoTibAPAxis L2']], "PCATibiatoTibAPAxis L2")
        
            join_obj([bpy.data.objects["PCATibiatoTibAPAxis L1"], bpy.data.objects["PCATibiatoTibAPAxis L2"]], "PCATibiatoTibAPAxis point")
     
            vertex_group(bpy.data.objects["PCATibiatoTibAPAxis point"])
            copy_object(bpy.data.objects["PCATibiatoTibAPAxis point"], "PCATibiatoTibAPAxis point copy1")
            copy_object(bpy.data.objects["PCATibiatoTibAPAxis point"], "PCATibiatoTibAPAxis point copy2")
        
            copy_object(bpy.data.objects['Tibia Tuberosity P:Dis'], 'Tibia Tuberosity P:Dis for PCATibiatoTibAPAxis')
            copy_object(bpy.data.objects['Posterior Medial Tibial Plateau P:Dis'], 'Posterior Medial Plateau PCATibiatoTibAPAxis')
            copy_object(bpy.data.objects['Posterior Lateral Tibial Plateau P:Dis'], 'Posterior Lateral Plateau PCATibiatoTibAPAxis')
        
            make_axis([bpy.data.objects["PCATibiatoTibAPAxis point"], bpy.data.objects['Tibia Tuberosity P:Dis for PCATibiatoTibAPAxis']], "PCATibiatoTibAPAxis L1")
            make_axis([bpy.data.objects["PCATibiatoTibAPAxis point copy1"], bpy.data.objects['Posterior Medial Plateau PCATibiatoTibAPAxis']], "PCATibiatoTibAPAxis L2")
            make_axis([bpy.data.objects["PCATibiatoTibAPAxis point copy2"], bpy.data.objects['Posterior Lateral Plateau PCATibiatoTibAPAxis']], "PCATibiatoTibAPAxis L3")
            join_obj([bpy.data.objects["PCATibiatoTibAPAxis L1"], bpy.data.objects["PCATibiatoTibAPAxis L2"], bpy.data.objects["PCATibiatoTibAPAxis L3"]], "PCA tibia to Tib AP axis")
            remove_doubles(bpy.data.objects["PCA tibia to Tib AP axis"])
            move_to_collection("Tibia_Measurements", bpy.data.objects["PCA tibia to Tib AP axis"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}


class TIBIA_OT_ProxTibiaSlope(Operator):
    """ """
    bl_label = "Prox tibia slope"
    bl_idname = "object.proxtibiaslope"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes", "Tibia_Projections", "Tibia_Measurements"])
        unhide_list(["Prox tibia slope", "Tibia Distal Plane", "Tibia Sagittal Plane"])

        try:
            delete_obj(bpy.data.objects["Prox tibia slope"])
        except:
            pass
        
        check_list = check_obj_list(["Tibia Distal Plane", "Tibia Sagittal Plane"])
        if len(check_list) == 0:
            bpy.ops.transform.create_orientation(use=True)
            bpy.ops.object.editmode_toggle()
            cursor_to_obj(bpy.data.objects['Tibia Knee Center'])
            add_plane("Fit Plane")
            copy_object(bpy.data.objects['Fit Plane'], "Prox tibia slope")
            copy_object(bpy.data.objects["Tibia Distal Plane"], "Tibia Distal Plane for ProxTibiaSlope")
            copy_object(bpy.data.objects["Tibia Sagittal Plane"], "Tibia Sagittal Plane for ProxTibiaSlope")

            change_dimension(bpy.data.objects["Tibia Distal Plane for ProxTibiaSlope"], (118, 118, 0))
            change_dimension(bpy.data.objects["Tibia Sagittal Plane for ProxTibiaSlope"], (116, 116, 0))
            
            boolean_objects(bpy.data.objects["Prox tibia slope"], bpy.data.objects["Tibia Distal Plane for ProxTibiaSlope"])
            boolean_objects(bpy.data.objects["Prox tibia slope"], bpy.data.objects["Tibia Sagittal Plane for ProxTibiaSlope"])
            move_to_collection("Tibia_Measurements", bpy.data.objects["Prox tibia slope"])
            delete_obj(bpy.data.objects["Tibia Distal Plane for ProxTibiaSlope"])
            delete_obj(bpy.data.objects["Tibia Sagittal Plane for ProxTibiaSlope"])
            
            hide_obj('Fit Plane')
            hide_obj("Tibia Distal Plane")
            hide_obj("Tibia Sagittal Plane")
            hide_obj("Tibia Coronal Plane")
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        return {'FINISHED'}
        


class TIBIA_OT_AngleTEA_TibiaAPAxis(Operator):
    """ """
    bl_label = "Angle TEA & Tibia AP axis"
    bl_idname = "object.angleteatibiaapaxis"
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        check_create_collection(["Tibia_Landmarks", "Tibia_Axes", "Tibia_Planes", "Tibia_Projections", "Tibia_Measurements"])
        unhide_list(["Angle TEA & Tibia AP axis", "Lateral Epicondyle P:TIB_Dis", "Medial Epicondyle P:TIB_Dis",'PCL Insertion P:Dis', 'Tibia Tuberosity P:Dis'])

        try:
            delete_obj(bpy.data.objects["Angle TEA & Tibia AP axis"])
        except:
            pass
        
        check_list = check_obj_list(["Lateral Epicondyle P:TIB_Dis", "Medial Epicondyle P:TIB_Dis",'PCL Insertion P:Dis', 'Tibia Tuberosity P:Dis'])
        if len(check_list) == 0:
            copy_object(bpy.data.objects["Lateral Epicondyle P:TIB_Dis"], 'Lateral Epicondyle AngleTEA_TibiaAPAxis L1')
            copy_object(bpy.data.objects["Medial Epicondyle P:TIB_Dis"], 'Medial Epicondyle AngleTEA_TibiaAPAxis L1')
            copy_object(bpy.data.objects['PCL Insertion P:Dis'], 'PCL Insertion AngleTEA_TibiaAPAxis L2')
            copy_object(bpy.data.objects['Tibia Tuberosity P:Dis'], 'Tibia Tuberosity AngleTEA_TibiaAPAxis L2')

            make_axis([bpy.data.objects['Lateral Epicondyle AngleTEA_TibiaAPAxis L1'], bpy.data.objects['Medial Epicondyle AngleTEA_TibiaAPAxis L1']], "AngleTEA_TibiaAPAxis L1")
            make_axis([bpy.data.objects['PCL Insertion AngleTEA_TibiaAPAxis L2'], bpy.data.objects['Tibia Tuberosity AngleTEA_TibiaAPAxis L2']], "AngleTEA_TibiaAPAxis L2")
        
            join_obj([bpy.data.objects["AngleTEA_TibiaAPAxis L1"], bpy.data.objects["AngleTEA_TibiaAPAxis L2"]], "Angle TEA & Tibia AP axis point")

            vertex_group(bpy.data.objects["Angle TEA & Tibia AP axis point"])
            copy_object(bpy.data.objects["Angle TEA & Tibia AP axis point"], "Angle TEA & Tibia AP axis point copy")
        
            copy_object(bpy.data.objects["Lateral Epicondyle P:TIB_Dis"], 'Lateral Epicondyle P:Dis AngleTEA_TibiaAPAxis')
            copy_object(bpy.data.objects['PCL Insertion P:Dis'], 'PCL Insertion P:Dis AngleTEA_TibiaAPAxis')
            
            make_axis([bpy.data.objects["Angle TEA & Tibia AP axis point"], bpy.data.objects['Lateral Epicondyle P:Dis AngleTEA_TibiaAPAxis']], "AngleTEA_TibiaAPAxis 1")
            make_axis([bpy.data.objects["Angle TEA & Tibia AP axis point copy"], bpy.data.objects['PCL Insertion P:Dis AngleTEA_TibiaAPAxis']], "AngleTEA_TibiaAPAxis 2")
            join_obj([bpy.data.objects["AngleTEA_TibiaAPAxis 1"], bpy.data.objects["AngleTEA_TibiaAPAxis 2"]], "Angle TEA & Tibia AP axis")
            remove_doubles(bpy.data.objects["Angle TEA & Tibia AP axis"])
            move_to_collection("Tibia_Measurements", bpy.data.objects["Angle TEA & Tibia AP axis"])
        else:
            self.report({'ERROR'}, "missing items:" + ", ".join(check_list))
        
        return {'FINISHED'}