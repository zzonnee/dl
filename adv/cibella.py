from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Cibella

class Cibella(Adv):
    conf = {}
    conf['slots.frostbite.a'] = Primal_Crisis()+His_Clever_Brother()
    conf['slots.d'] = Leviathan()
    conf['acl'] = """
        `dragon
        `s3
        `s2
        `s4
        `fs, seq=5
        """
    coab = ['Tiki', 'Xander', 'Dagger']
    share = ['Gala_Elisanne', 'Ranzal']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
