import re
from app.utilities.generate_key import generate_key
from app.utilities.generate_regression import generate_regression
from app.utilities.vet_precision import vet_precision
from app.utilities.vet_data_set import vet_data_set

class TestGenerateKeyUtility:
    def test_generate_key_set_length(self):
        new_key = generate_key()
        assert len(new_key) == 32
    
    def test_generate_key_set_characters(self):
        new_key = generate_key()
        pattern = r'[^\.a-zA-Z0-9]'
        problems = re.search(pattern, new_key)
        assert not problems

class TestGenerateRegressionUtility:
    def test_generate_regression_creates_collection(self):
        data_set = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12],
            [13, 14],
            [15, 16],
            [17, 18],
            [19, 20]
        ]
        precision = 4
        new_collection = generate_regression(data_set, precision)
        assert new_collection['linear_coefficients'] == [1.0, 1.0]
        assert new_collection['linear_points'] == {'roots': [[-1.0, 0.0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}
        assert new_collection['linear_correlation'] == 1.0
        assert new_collection['quadratic_coefficients'] == [-0.0001, 1.0, 1.0]
        assert new_collection['quadratic_points'] == {'roots': [[-0.9999, 0.0], [10000.9999, 0.0]], 'maxima': [[5000.0, 2501.0]], 'minima': [None], 'inflections': [None]}
        assert new_collection['quadratic_correlation'] == 1.0
        assert new_collection['cubic_coefficients'] == [-0.0001, 0.0001, 1.0, 1.0]
        assert new_collection['cubic_points'] == {'roots': [[-98.9949, 0.0], [-1.0002, 0.0], [100.9951, 0.0]], 'maxima': [[58.0693, 39.8253]], 'minima': [[-57.4027, -37.1586]], 'inflections': [[0.3333, 1.3333]]}
        assert new_collection['cubic_correlation'] == 0.9988
        assert new_collection['hyperbolic_coefficients'] == [-15.037, 14.2078]
        assert new_collection['hyperbolic_points'] == {'roots': [[1.0584, 0.0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}
        assert new_collection['hyperbolic_correlation'] == 0.7186
        assert new_collection['exponential_coefficients'] == [2.8622, 1.1221]
        assert new_collection['exponential_points'] == {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [None]}
        assert new_collection['exponential_correlation'] == 0.9222
        assert new_collection['logarithmic_coefficients'] == [6.1078, -1.3987]
        assert new_collection['logarithmic_points'] == {'roots': [[1.2573, 0.0]], 'maxima': [None], 'minima': [None], 'inflections': [None]}
        assert new_collection['logarithmic_correlation'] == 0.9246
        assert new_collection['logistic_coefficients'] == [23.2346, 0.201, 10.6583]
        assert new_collection['logistic_points'] == {'roots': [None], 'maxima': [None], 'minima': [None], 'inflections': [[10.6583, 11.6173]]}
        assert new_collection['logistic_correlation'] == 0.9974
        assert new_collection['sinusoidal_coefficients'] == [-2.4629, 0.9381, -0.047, 11.0]
        assert new_collection['sinusoidal_points'] == {'roots': [None], 'maxima': [[4.9763, 13.4629], [11.6741, 13.4629], [18.3719, 13.4629], ['4.9763 + 6.6978k', 13.4629]], 'minima': [[1.6274, 8.5371], [8.3252, 8.5371], [15.023, 8.5371], ['1.6274 + 6.6978k', 8.5371]], 'inflections': [[3.3019, 11.0], [6.6508, 11.0], [9.9997, 11.0], [13.3486, 11.0], [16.6975, 11.0], ['3.3019 + 3.3489k', 11.0]]}
        assert new_collection['sinusoidal_correlation'] == 0.3046
        assert new_collection['best_fit'] == 'linear'
    
    def test_generate_regression_rejects_bad_precision(self):
        data_set = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12],
            [13, 14],
            [15, 16],
            [17, 18],
            [19, 20]
        ]
        precision = 4.5
        new_collection = generate_regression(data_set, precision)
        assert new_collection[0] == 'Precision must be a positive integer'
        assert new_collection[1] == 403
    
    def test_generate_regression_rejects_bad_set(self):
        data_set = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        precision = 4
        new_collection = generate_regression(data_set, precision)
        assert new_collection[0] == 'Data set must contain at least 10 points'
        assert new_collection[1] == 403

class TestRequestQueryUtility:
    pass

class TestRequestSubmissionUtility:
    pass

class TestRequireKeyUtility:
    pass

class TestUniqueKeyUtility:
    pass

class TestVetDataSetUtility:
    def test_vet_data_set_accepts_full_list(self):
        initial_data_set = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12],
            [13, 14],
            [15, 16],
            [17, 18],
            [19, 20]
        ]
        checked_input = vet_data_set(initial_data_set)
        assert checked_input == initial_data_set
    
    def test_vet_data_set_rejects_short_list(self):
        initial_data_set = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        checked_input = vet_data_set(initial_data_set)
        assert checked_input != initial_data_set
        assert checked_input[0] == 'Data set must contain at least 10 points'
        assert checked_input[1] == 403
    
    def test_vet_data_set_rejects_nonlist_set(self):
        initial_data_set = {
            'first_point': [1, 2],
            'second_point': [3, 4],
            'third_point': [5, 6]
        }
        checked_input = vet_data_set(initial_data_set)
        assert checked_input != initial_data_set
        assert checked_input[0] == 'Data set must be a list'
        assert checked_input[1] == 403
    
    def test_vet_data_set_rejects_nonlist_points(self):
        initial_data_set = [
            {'x': 1, 'y': 2},
            {'x': 3, 'y': 4},
            {'x': 5, 'y': 6}
        ]
        checked_input = vet_data_set(initial_data_set)
        assert checked_input != initial_data_set
        assert checked_input[0] == 'Each coordinate pair within data set must be a list'
        assert checked_input[1] == 403
    
    def test_vet_data_set_rejects_long_points(self):
        initial_data_set = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        checked_input = vet_data_set(initial_data_set)
        assert checked_input != initial_data_set
        assert checked_input[0] == 'Each coordinate pair within data set must contain exactly 2 numbers'
        assert checked_input[1] == 403
    
    def test_vet_data_set_rejects_string_points(self):
        initial_data_set = [
            [1, 2],
            ['3', 4],
            [5, 6]
        ]
        checked_input = vet_data_set(initial_data_set)
        assert checked_input != initial_data_set
        assert checked_input[0] == 'All numbers within coordinate pairs within data set must be integers or floats'
        assert checked_input[1] == 403

class TestVetPrecisionUtility:
    def test_vet_precision_accepts_positive_integer(self):
        checked_input = vet_precision(4)
        assert checked_input == 4
    
    def test_vet_precision_rejects_negative(self):
        checked_input = vet_precision(-4)
        assert checked_input != -4
        assert checked_input[0] == 'Precision must be a positive integer'
        assert checked_input[1] == 403
    
    def test_vet_precision_rejects_float(self):
        checked_input = vet_precision(4.5)
        assert checked_input != 4.5
        assert checked_input[0] == 'Precision must be a positive integer'
        assert checked_input[1] == 403
    
    def test_vet_precision_rejects_string(self):
        checked_input = vet_precision('4')
        assert checked_input != '4'
        assert checked_input[0] == 'Precision must be a positive integer'
        assert checked_input[1] == 403