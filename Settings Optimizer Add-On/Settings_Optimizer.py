bl_info = {
    'name': 'Settings Optimizer',
    'category': 'Side Menu',
    'version': (1, 0, 0),
    'blender': (4, 0, 0),
    'location': "Side Menu; Shortcut: N",
    'author': 'Chris Nendick',
    'description': "Optimizes settings for eevee and cycles",
}

import bpy
#I have no fingers and I must code.

#setting up labels and id names. 
class CustomPanel(bpy.types.Panel):
    bl_icon = "SETTINGS"
    bl_label = "Settings Optimizer"
    bl_idname = "PT_CustomPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Auto settings'
#creating the buttons for the sidebar tool
    def draw(self, context):
        layout = self.layout
        layout.operator("object.simple_operator", text="Cartoon Renders",icon="RENDER_ANIMATION")
        layout.operator("object.simple_operator2", text="Realistic Renders", icon="RENDER_ANIMATION")
    
#realistic render class 
class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator2"
    bl_label = "Simple Operator"

    def execute(self, context):
        
#Changing the render settings so that cycles doesn't take 4 millenniums to render a rotating apple.
        render_settings = bpy.context.scene.render
        render_settings.resolution_x = 1920
        render_settings.resolution_y = 1080
        render_settings.engine = 'CYCLES'
        render_settings.image_settings.file_format = 'PNG'
        bpy.data.scenes["Scene"].cycles.samples = 100
        bpy.data.scenes["Scene"].cycles.preview_samples = 100
        bpy.data.scenes["Scene"].cycles.preview_adaptive_threshold = 0.5
        bpy.data.scenes["Scene"].cycles.adaptive_threshold = 0.5
        bpy.data.scenes["Scene"].cycles.device = 'GPU'
        bpy.data.scenes["Scene"].cycles.max_bounces = 6
        

        return {'FINISHED'}
    
#cartoon renders class 
class CartoonOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Cartoon Operator"

    def execute(self, context):
        
        
#Eevee is already fast. Still has garbage lighting tho. 
#This just turns on bloom and sets up basic output settings.
        render_settings = bpy.context.scene.render
        render_settings.resolution_x = 1920
        render_settings.resolution_y = 1080
        render_settings.engine = 'BLENDER_EEVEE'
        render_settings.image_settings.file_format = 'PNG'
        bpy.data.scenes["Scene"].eevee.use_bloom = True
        
        return {'FINISHED'}
        
#registers the classes that are present 
def register():
    bpy.utils.register_class(CustomPanel)
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(CartoonOperator)

#unregisters the classes
def unregister():
    bpy.utils.unregister_class(CustomPanel)
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.register_class(CartoonOperator)

if __name__ == "__main__":
    register()
    
