from filters.file import *

class echo(file):
    def __init__(self):
        print("formats echo fun __init fun....");
        file.__init__(file)
    def test(self):
        print("formats echo class test fun....");
    
    def show(self):
        print("echo show() fun ...");
        file.show(file)
