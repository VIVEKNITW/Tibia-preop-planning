from bpy.types import Panel

class TIBIA_PT_Landmark_assignment(Panel):
    """ """
    bl_label = "Landmarks & axes"
    bl_idname = "tibia_PT_landmarkassignment"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tibia"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.tibiakneecenter")
        row = layout.row()
        row.operator("object.proximallateraltibialplateau")
        row = layout.row()
        row.operator("object.proximalmedialtibialplateau")
        row = layout.row()
        row.operator("object.posteriormedialtibialplateau")
        row = layout.row()
        row.operator("object.posteriorlateraltibialplateau")
        row = layout.row()
        row.operator("object.medialmedialtibialplateau")
        row = layout.row()
        row.operator("object.laterallateraltibialplateau")
        row = layout.row()
        row.operator("object.pclinsertion")
        row = layout.row()
        row.operator("object.tibiatuberosity")
        row = layout.row()
        row.operator("object.fibulahead")
        row = layout.row()
        row.label(text="Ankle center by directly selecting location")
        row = layout.row()
        row.operator("object.anklecenter")
        row = layout.row()
        row.label(text="Ankle center by selecting 2 reference points")
        row = layout.row()
        row.operator("object.point1anklecenter")
        row = layout.row()
        row.operator("object.point2anklecenter")
        row = layout.row()
        row.operator("object.medialepicondyle")
        row = layout.row()
        row.operator("object.lateralepicondyle")
        row = layout.row()
        row.operator("object.transepicondylaraxis")
        row = layout.row()
        row.operator("object.tibiamechanicalaxis")
        row = layout.row()
        row.operator("object.tibiaapaxis")
        row = layout.row()
        row.operator("object.tibiasagittalplane")
        row = layout.row()
        row.operator("object.tibiacoronalplane")
        row = layout.row()
        row.operator("object.tibiadistalplane")