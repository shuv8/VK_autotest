import pytest
class TestSet:
    def test_set_1(self):
        test_set = set()
        test_set.add(123)
        for a in test_set:
            assert a == 123


    @pytest.mark.parametrize("test_input, test_expected", [(3+5, 8), (2+4, 6), (6*7, 42)])
    def test_set_2(self, test_input, test_expected):
        test_set = {test_input}
        for a in test_set:
            assert a == test_expected


    def test_set_3(self):
        test_set = {123}
        try:
            assert test_set[0] == 123
        except TypeError:
            pass



class TestFloat:
    def test_float_1(self):
        a = 2.0
        b = -2.0
        assert a+b == 0.0


    @pytest.mark.parametrize("test_input_a, test_input_b, test_expected", [(3.0, 5.5, 8.5), (2.0, 4.3, 6.3), (6.0, 7.0, 13.0)])
    def test_float_2(self, test_input_a, test_input_b, test_expected):
        a = test_input_a
        b = test_input_b
        assert a+b == test_expected


    def test_float_3(self):
        a = 'a'
        try:
            assert type(float(a)) == float
        except ValueError:
            pass
