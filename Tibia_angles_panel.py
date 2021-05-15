from bpy.types import Panel

class TIBIA_PT_Angles(Panel):
    """ """
    bl_label = "Angles"
    bl_idname = "tibia_PT_angles"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tibia"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.condylardifferenceoftibialplateau")
        row = layout.row()
        row.operator("object.headfibtibialjointline")
        row = layout.row()
        row.operator("object.proxtibiavarus")
        row = layout.row()
        row.operator("object.proxmedialtibiavarus")
        row = layout.row()
        row.operator("object.proxlateraltibiavarus")
        row = layout.row()
        row.operator("object.proxtibiaicvarus")
        row = layout.row()
        row.operator("object.pcatibiatotibiaapaxis")
        row = layout.row()
        row.label(text = "Go into edit mode and select flat surface")
        row = layout.row()
        row.operator("object.proxtibiaslope")
        row = layout.row()
        row.operator("object.angleteatibiaapaxis")