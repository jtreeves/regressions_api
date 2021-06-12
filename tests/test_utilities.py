import re
from app.utilities.generate_key import generate_key

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
    pass