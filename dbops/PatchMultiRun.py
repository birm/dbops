import os

class CommandMultiRun(object):
    """Neat Patch Looping."""
    def __init__(self, list=[["dog","cat"],"lemon"], command="food.pmr",
                 mode ="print"):
        """Take in input."""
        self.list = list
        with open(command, 'r') as cmf:
            self.command=cmf.read().replace('\n', '')

        self.mode = mode

    def replace(self, inputs):
        """ Replace {x} with a list of inputs. """
        return self.command.format(*inputs)

    def output(self, result, mode="print"):
        """Do what is expected with the commands as they come."""
        if mode = "print":
            print result
        if mode = "bash":
            os.system(result)


    def run(self):
        """ Run through the list and format and run commands. """
