from tester_tool import Test,Tester
from number_prettier_tool import number_prettier


def full_test():
    tester = Tester(
        func = number_prettier,
        func_args = list(),
        func_kwargs = dict(split_digit=True,simplefy=True),
    )

    tester.add_test(Test('0','0'))
    tester.add_test(Test('0.0','0'))
    tester.add_test(Test('0.001','0.001'))
    tester.add_test(Test('0.00001','0.00001'))

    tester.add_test(Test('-0','0'))
    tester.add_test(Test('-0.0','0'))
    tester.add_test(Test('-0.001','-0.001'))
    tester.add_test(Test('-0.00001','-0.00001'))

    tester.add_test(Test('1000','1 T'))
    tester.add_test(Test('1000000','1 M'))
    tester.add_test(Test('1000000000','1 B'))
    tester.add_test(Test('1200000000','1.2 B'))
    tester.add_test(Test('1000000000000','1,000 B'))
    tester.add_test(Test('1200000000000','1,200 B'))
    tester.add_test(Test('1234567890123','1,234.567890123 B'))

    tester.add_test(Test('-1000','-1 T'))
    tester.add_test(Test('-1000000','-1 M'))
    tester.add_test(Test('-1000000000','-1 B'))
    tester.add_test(Test('-1200000000','-1.2 B'))
    tester.add_test(Test('-1000000000000','-1,000 B'))

    tester.add_test(Test('-1200.43234 stoks','-1.2 T stoks'))
    tester.add_test(Test('-1234000.765456 stoks','-1.234 M stoks'))

    tester.run()


def only_split_digit_test():
    tester = Tester(
        func = number_prettier,
        func_args = list(),
        func_kwargs = dict(split_digit=True,simplefy=False),
    )

    tester.add_test(Test('0','0'))
    tester.add_test(Test('0.0','0'))
    tester.add_test(Test('0.001','0.001'))


    tester.add_test(Test('1234','1,234'))
    tester.add_test(Test('1234.6544356','1,234.6544356'))

    tester.run()


def only_simplefy_test():
    tester = Tester(
        func = number_prettier,
        func_args = list(),
        func_kwargs = dict(split_digit=False,simplefy=True),
    )

    tester.add_test(Test('0','0'))
    tester.add_test(Test('0.0','0'))
    tester.add_test(Test('0.001','0.001'))


    tester.add_test(Test('1234','1.234 T'))
    tester.add_test(Test('1234.6544356','1.234 T'))

    tester.run()


only_split_digit_test()
only_simplefy_test()
full_test()