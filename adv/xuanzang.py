import adv.adv_test
from adv import *
from slot.a import *
import random

def module():
    return Xuanzang

class Xuanzang(Adv):
    a3 = ('cc',0.06,'hp70')

    def s1_proc(this, e):
        if this.mod('def')!= 1:
            this.dmg_make('o_s1_boost',2.51*3*0.2*0.91)

    def s2_proc(this, e):
        Debuff('s2_defdown',0.1,20,0.7).on()





if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2
        `s3
        `fs, seq=5
        """
    adv_test.test(module(), conf, verbose=0, mass=0)

