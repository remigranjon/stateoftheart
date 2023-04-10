from django.db.models.deletion import CASCADE

DO_CASCADE = object()

def SET_WITH(func):
    def set_on_delete(collector, field, sub_objs, using):
        cascades = []
        for obj in sub_objs:
            result = func(obj)
            if result is DO_CASCADE:
                cascades.append(obj)
            else:
                collector.add_field_update(field, result, [obj])
        if cascades:
            CASCADE(collector, field, cascades, using)
    set_on_delete.deconstruct = lambda: ('blog.deletion.SET_WITH', (func,), {})
    return set_on_delete