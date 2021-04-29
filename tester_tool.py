class Test():
    def __init__(self,inpute,expect): 
        self.inpute = inpute
        self.expect = expect

class InputeTestInstanceException(Exception):
    pass

class Tester():
    def __init__(self,func,func_args=None,func_kwargs=None,tests=None): 
        
        if func_args is None:
            func_args = list()

        if func_kwargs is None:
            func_kwargs = {}

        if tests is None:
            tests = list()

        self.func = func
        self.func_args = func_args
        self.func_kwargs = func_kwargs
        self.tests = tests

    def add_test(self,test):
        if not isinstance(test,Test):
            raise InputeTestInstanceException('test must be instance of Test class')

        self.tests.append(test)

    def run(self):
        for test in self.tests:
            result = self.func(test.inpute,*self.func_args,**self.func_kwargs)
            succcess_test = result == test.expect

            if succcess_test :
                print(f'successfully test with {test.inpute} and result {test.expect}')

            else:
                print(f'faild test with {test.inpute} and result {result} != expect {test.expect}')