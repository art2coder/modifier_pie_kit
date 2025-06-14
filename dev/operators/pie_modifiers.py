import bpy

class PIE_MT_modifiers_pie(bpy.types.Menu):
    bl_label = "Modifier Pie Menu"
    bl_idname = "PIE_MT_modifiers_pie"

    def draw(self, context):
        pie = self.layout.menu_pie()
    
        # ↗ Top-Right
        pie.operator("modifier_pie.add_bevel_popup",           text="Bevel",        icon='MOD_BEVEL')

        # ↑ Top
        pie.operator("modifier_pie.add_boolean_popup", text="Boolean", icon='MOD_BOOLEAN')
  
        # → Right
        pie.operator("modifier_pie.mirror_live_popup",         text="Mirror",       icon='MOD_MIRROR')
   
        # ↘ Bottom-Right
        pie.operator("modifier_pi.move_bottom_to_z0",         text="Move Bottom",  icon='TRIA_DOWN')

        # ← Left
        pie.operator("modifier_pie.rotational_array", text="Rot Array", icon='MOD_ARRAY')

         # ↖ Top-Left
        pie.operator("view3d.toggle_overlay",            text="Toggle Overlay", icon='OVERLAY')
        
         # ↙ Bottom-Left
        pie.operator("modifier_pie.apply_all_common_modifiers", text="Apply All",   icon='FILE_TICK')

        # ↓ Bottom
        pie.operator("modifier_pie.add_subsurf_popup",         text="Subsurf",      icon='MOD_SUBSURF')




# 🔧 등록/해제
classes = (
    PIE_MT_modifiers_pie,
)



def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
