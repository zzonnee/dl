from core.advbase import *
from slot.a import *

def module():
    return Renelle

class Renelle(Adv):
    a1 = ('cc',0.15,'hit15')
    
    conf = {}
    conf['slots.a'] = Twinfold_Bonds()+Me_and_My_Bestie()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s1, fsc
        `s2, fsc
        `s4, fsc
        `fs, x=5
        """
    conf['afflict_res.burn'] = 0
    coab = ['Blade', 'Marth', 'Serena']
    share = ['Ranzal']

    def s1_proc(self, e):
        self.afflics.burn(e.name,100,0.803)
    
    def s2_proc(self, e):
        self.afflics.burn(e.name,100,0.803)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
