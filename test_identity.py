from lib import TestBasic, run, IDENTITY, pp


class TestIdentity(TestBasic):

    def setUp(self):
        super(TestIdentity, self).setUp()
        self.identity = self.kernels[IDENTITY.identity1]

    def compare_multiplication(self, kernel,  kernel_reverse):
        print("\noriginal")
        pp(self.matrix)
        changed = TestIdentity.step_filter("changed", self.matrix, kernel)
        reverse = TestIdentity.step_filter("reverse", changed, kernel_reverse)
        TestIdentity.compare_arrays(self.matrix, reverse)

    def test_1(self):
        self.compare_multiplication(self.identity, self.identity)

    def test_Reverse(self):
        self.compare_multiplication(self.identity * 2, self.identity / 2)


if __name__ == '__main__':
    run()
