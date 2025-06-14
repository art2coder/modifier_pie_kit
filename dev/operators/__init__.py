# operators/__init__.py

from .grouping           import register as register_group,        unregister as unregister_group
from .popup_modifiers    import register as register_mods,         unregister as unregister_mods
from .pie_modifiers      import register as register_pie,          unregister as unregister_pie
from .popup_pivot        import register as register_pivot_ops,    unregister as unregister_pivot_ops
from .pie_pivot          import register as register_pivot,        unregister as unregister_pivot
from .tools_extra import register as register_select, unregister as unregister_select
from . import auto_sorter
from . import clean_view
from . import camera_quick_settings
from . import lineart_extras

def register():
    register_group()
    register_mods()
    register_pie()
    register_pivot_ops()   
    register_pivot()
    register_select()
    auto_sorter.register()
    clean_view.register()
    camera_quick_settings.register()
    lineart_extras.register()

def unregister():
    lineart_extras.unregister()
    camera_quick_settings.unregister()
    clean_view.unregister()
    auto_sorter.unregister()
    unregister_select()
    unregister_pivot()
    unregister_pivot_ops()  
    unregister_pie()
    unregister_mods()
    unregister_group()
