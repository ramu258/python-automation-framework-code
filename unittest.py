import unittester
def sum(a,b):
    return a+b
class sumtest(unittester.Testcase):
    def test_sumfun(self):
        a=10
        b=20
        result=sum(a,b)
        self.assertequal(result,a+b)
if __name__ == __main__:
    unittester.main()