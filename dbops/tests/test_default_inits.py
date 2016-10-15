import sys, os
sys.path.append(os.path.abspath('../'))

from dbops.WhereLives import WhereLives
from dbops.PatchExpander import PatchExpander

def test_wherelives_default_init():
    wl = WhereLives()
    
def test_patchexpander_default_init():
    pe = PatchExpander()
