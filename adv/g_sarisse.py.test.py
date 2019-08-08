import adv.adv_test
import adv
from adv import *
from slot import *

class test(WeaponBase):
    ele = ['flame']
    wt = 'bow'
    att = 534
    s3 = {
        "dmg"      : 9.49     ,
        "sp"       : 8075     ,
        "startup"  : 0.1      ,
        "recovery" : 2.25     ,
        }


def module():
    return G_Sarisse

class G_Sarisse(adv.Adv):
    a3 = ('bt',0.3)
    conf = {}
    #conf['mod'] = {'ex':('sp','passive',0.15)}
    conf['slot.w'] = test()

    def prerun(this):
        this.hits = 0
        this.bc = adv.Selfbuff()
        this.s2stance = 0
        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s3,s1.charged>=2803
                `s1
                `s2
                `fs, seq=4
                """

    def init(this):
        if this.condition('never lose combos'):
            this.dmg_proc = this.c_dmg_proc
        return 'never lose combos & c4+fs'

    def c_dmg_proc(this, name, amount):
        if name[:2] == 'x1':
            this.hits += 3
        elif name[:2] == 'x2':
            this.hits += 2
        elif name[:2] == 'x3':
            this.hits += 3
        elif name[:2] == 'x4':
            this.hits += 2
        elif name[:2] == 'x5':
            this.hits += 5
        elif name[:2] == 'fs':
            this.hits += 8
        if this.hits >= 20:
            this.hits -= 20
            adv.Selfbuff('sylvan strength',0.02,15).on()
            adv.Selfbuff('sylvan crit',0.01,15,'crit','chance').on()

    def s1_proc(this, e):
        buffcount = this.bc.buffcount()
        if buffcount > 7:
            buffcount = 7
        this.dmg_make('s1_missile*%d'%buffcount,0.95*buffcount)
        this.hits += 1 + buffcount
            

    def s2_proc(this, e):
        if this.s2stance == 0:
            adv.Teambuff('s2str',0.20,10).on()
            this.s2stance = 1
        elif this.s2stance == 1:
            adv.Teambuff('s2def',1,15,'defup').on()
            this.s2stance = 0


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s3,s1.charged>=2803
        `s1
        `s2
        """
    import slot
    conf['slots.d'] = slot.d.flame.Sakuya()

    adv_test.test(module(), conf, verbose=-2)

