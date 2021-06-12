import re
from app.utilities.generate_key import generate_key
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
    pass

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