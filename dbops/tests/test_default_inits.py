from dbops import WhereLives
from dbops import PatchExpander
from dbops import CommandMultiRun

def test_wherelives_default_init():
    wl = WhereLives()

def test_patchexpander_default_init():
    pe = PatchExpander()

def test_commandmultirun_default_init():
    text_file = open("food.pmr", "w")
    text_file.write("echo {0} {1}")
    text_file.close()
    cm = CommandMultiRun()
