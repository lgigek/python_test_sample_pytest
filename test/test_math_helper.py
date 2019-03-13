from python_test_sample.math_helper import MathHelper
from pytest import fixture


class TestMathHelper:
    math_helper: MathHelper

    @fixture
    def setup(self):
        """
        Setup before the test
        """

        self.math_helper = MathHelper()

    def test_add(self, mocker, setup):
        """
        It should return the result of operation and should call method "_add"
        """

        spy_add = mocker.spy(self.math_helper, '_add')

        assert self.math_helper.calc('addition', 1, 1) == 2
        spy_add.assert_called_with(1, 1)

    def test_sub(self, mocker, setup):
        """
        It should return the result of operation and should call method "_sub"
        """

        spy_sub = mocker.spy(self.math_helper, '_sub')

        assert self.math_helper.calc('subtraction', 2, 1) == 1
        spy_sub.assert_called_with(2, 1)

    def test_mul(self, mocker, setup):
        """
        It should return the result of operation and should call method "_mul"
        """

        spy_mul = mocker.spy(self.math_helper, '_mul')

        assert self.math_helper.calc('multiplication', 2, 2) == 4
        spy_mul.assert_called_with(2, 2)

    def test_div(self, mocker, setup):
        """
        It should return the result of operation and should call method "_div"
        """

        spy_div = mocker.spy(self.math_helper, '_div')

        assert self.math_helper.calc('division', 4, 2) == 2
        spy_div.assert_called_with(4, 2)

    def test_incorrect_operation(self, setup):
        """
        It should return "None" if the first parameter is incorrect
        """

        assert self.math_helper.calc('incorrect', 1, 1) is None
