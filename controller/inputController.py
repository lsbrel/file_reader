import sys

class InputController:

    # REGRAS
    num_args = 3
    exec_type = ["--service", '--users', '--insert']
    file_type = ["--type-d", '--type-e', '--type-f']
    # REGRAS

    def __init__(self):
        self.numArgs()
        self.validateExecType()
        pass


    def numArgs(self):

        if(len(sys.argv) < self.num_args):
            print(f"must be at least {self.num_args}")
            sys.exit()

    def validateExecType(self):

        if(sys.argv[3] not in self.exec_type):
            print(f"type of exec must be {self.exec_type}")
            sys.exit()

    def validateFileType(self):

        if(sys.argv[2] not in self.file_type):
            print(f"type of file must be {self.file_type}")