from flask_restful import fields, marshal



class Obj:
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2


def test_base():
    mfields = {
        # test different options: Raw, String, Integer
        'f1': fields.Raw,
        'f2': fields.String,
    }
    d = dict(f1='text', f2=123)
    marshalled_d = marshal(d, mfields)
    obj = Obj(f1='text', f2=123)
    marshalled_obj = marshal(obj, mfields)

    # list of objects
    obj_list = [d for _ in range(10)]
    marshalled_obj_list = marshal(obj_list, mfields)

    # envelope
    marshalled_obj_with_env = marshal(obj, mfields, envelope='object')
    marshalled_obj_list_with_env = marshal(marshalled_obj_list, mfields, envelope='objects')

    # nested
    master_fields = {
        'f1': fields.Raw,
        'f2': fields.Nested(mfields),
    }
    master_obj = Obj(f1=123, f2=obj)
    marshalled_master = marshal(master_obj, master_fields)

    # nested list
    master_fields = {
        'f1': fields.Raw,
        'f2': fields.Nested(mfields),  # simple list
    }
    master_obj = Obj(f1=123, f2=[obj, obj])
    marshalled_master = marshal(master_obj, master_fields)

    # nested list 2 the same?
    master_fields = {
        'f1': fields.Raw,
        'f2': fields.List(fields.Nested(mfields)),  # simple list
    }
    master_obj = Obj(f1=123, f2=[obj, obj])
    marshalled_master2 = marshal(master_obj, master_fields)
    print('ok')


if __name__ == '__main__':
    test_base()
