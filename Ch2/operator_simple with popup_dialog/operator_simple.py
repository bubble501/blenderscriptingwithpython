﻿import bpy


def main(context):
    for ob in context.scene.objects:
        print(ob)


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    
    def draw(self, context):
        layout = self.layout
        col0 = layout.column()
        box0 = col0.box()

        # Display the names of the current scene objects.
        box0.label("Scene Objects:", icon="OBJECT_DATA")
        for ob in context.scene.objects:
            r = box0.row(align=True)
            r.label(text=str(ob.name))
    

def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text="Simple Operator", icon="OBJECT_DATA")


def register():
    bpy.utils.register_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.prepend(menu_func)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.simple_operator()
