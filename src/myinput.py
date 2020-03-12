import sys
import os
class Input:
    def __init__(self, question, error, *args):
        self.question = question
        self.error = error
        if args:
            self.options = args
        else:
            self.options = []

    def run(self):
        value = input(f'{self.question}')
        return value

    def check_input(self, option):
        ## NOT WORKING
        if option is 'q':
            os.system('clear')
            sys.exit()
        elif not option:
            return False
        elif not self.options:
            return True
        elif option not in self.options:
            return False
        return True


    @staticmethod
    def quit_console(self,option):
        os.system('clear')
        print("Goodbye")
        sys.exit()
    

