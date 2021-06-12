import re
from app.utilities.generate_key import generate_key
from app.utilities.vet_precision import vet_precision

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

class TestVetDataSourceUtility:
    pass

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