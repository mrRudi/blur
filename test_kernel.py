from lib import TestBasic, GAUS, CUSTOM, Y, X, run


class TestKernel(TestBasic):
    def compare_multiplication(self, name):
        kernel_xy = self.kernels[name]
        kernel_x = self.breakdowns[name][X]
        kernel_y = self.breakdowns[name][Y]

        dst_xy = TestKernel.step_filter("M**(XY)", self.matrix, kernel_xy)
        dst_x = TestKernel.step_filter("M**X", self.matrix, kernel_x)
        dst_x_y = TestKernel.step_filter("(M**X)**Y", dst_x, kernel_y)
        TestKernel.compare_arrays(dst_xy, dst_x_y)

    def test_Gaus(self):
        self.compare_multiplication(GAUS.g9)

    def test_Breakdown(self):
        self.compare_multiplication(CUSTOM.breakdown1)


if __name__ == '__main__':
    run()
