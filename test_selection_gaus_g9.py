
from lib import TestBasic, GAUS, RIDGE_DETECTION, run, SHARPEN, pp


class TestGausSelection(TestBasic):

    def compare_multiplication(self, title,  title_reverse):
        kernel = self.kernels[title]
        kernel_reverse = self.kernels[title_reverse]
        print("\noriginal")
        pp(self.matrix)
        changed = TestGausSelection.step_filter("changed", self.matrix, kernel)
        reverse = TestGausSelection.step_filter(
            "reverse", changed, kernel_reverse)
        print("diff")
        TestGausSelection.deviation(self.matrix, reverse)

    # def test_Filter1(self):
    #     self.compare_multiplication(GAUS.g9, SHARPEN.center4)

    def test_Filter2(self):
        self.compare_multiplication(GAUS.g9, SHARPEN.center5)

    # def test_Filter3(self):
    #     self.compare_multiplication(GAUS.g9, RIDGE_DETECTION.rd_mns1_7)

    # def test_Filter4(self):
    #     self.compare_multiplication(GAUS.g9, RIDGE_DETECTION.rd_mns1_8)

    # def test_Filter5(self):
    #     self.compare_multiplication(GAUS.g9, RIDGE_DETECTION.rd_mns1_9)

    # def test_Filter6(self):
    #     self.compare_multiplication(GAUS.g9, RIDGE_DETECTION.rd_mns1div9_10)

    # def test_Filter7(self):
    #     self.compare_multiplication(GAUS.g9, RIDGE_DETECTION.rd_mns2_10)


if __name__ == '__main__':
    run()
