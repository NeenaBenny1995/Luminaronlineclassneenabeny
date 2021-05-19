class Pycharm:
    def compile(self):
        print("compile using pycharm")
    def execute(self):
        print("execute using pycharm")
class Vscode:
    def compile(self):
        print("compile using vscode")
    def execute(self):
        print("execeute using vscode")
class Programmer:
    def coding(self,code):
        code.compile()
        code.execute()
p=Programmer()
py=Pycharm()
p.coding(py)