import re
import json
from datetime import datetime
from app import db
from app.models import User
from app.utilities.generate_key import generate_key
from app.utilities.generate_regression import generate_regression
from app.utilities.vet_precision import vet_precision
from app.utilities.vet_data_set import vet_data_set
from app.utilities.unique_key import unique_key
from app.utilities.request_query import request_query
from app.utilities.request_submission import request_submission
from app.utilities.require_key import require_key

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
    def test_request_query_accesses_params(self, app, client):
        @app.route("/query", methods=["POST"])
        def query_route():
            query = request_query()
            return query

        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        found_user_id = found_user.id

        res = client.post("/query?key=ABC123&source=TestQuerySource")
        query_values = json.loads(res.data.decode())
        assert query_values['source'] == 'TestQuerySource'
        assert query_values['user_id'] == found_user_id
        
        db.session.delete(found_user)
        db.session.commit()
    
    def test_request_query_fails_without_params(self, app, client):
        @app.route("/query_fails", methods=["POST"])
        def query_fails_route():
            query = request_query()
            return query

        res = client.post("/query_fails")
        assert res.status_code == 500

class TestRequestSubmissionUtility:
    def test_request_submission_accesses_json(self, app, client):
        @app.route("/submission", methods=["POST"])
        def submission_route():
            submission = request_submission()
            return submission
        
        title = 'Test Submission Title'
        independent = 'Test Submission Independent'
        dependent = 'Test Submission Dependent'
        precision = 4
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

        res = client.post(
            "/submission",
            json = {
                'title': title,
                'independent': independent,
                'dependent': dependent,
                'precision': precision,
                'data_set': data_set
            }
        )

        submission_values = json.loads(res.data.decode())
        assert submission_values['title'] == title
        assert submission_values['independent'] == independent
        assert submission_values['dependent'] == dependent
        assert submission_values['precision'] == precision
        assert submission_values['data_set'] == data_set
    
    def test_request_submission_fails_empty_fields(self, app, client):
        @app.route("/submission_empty_fails", methods=["POST"])
        def submission_empty_fails_route():
            submission = request_submission()
            return submission

        res = client.post(
            "/submission_empty_fails",
            json = {
                'title': '',
                'independent': '',
                'dependent': '',
                'precision': '',
                'data_set': ''
            }
        )

        assert res.status_code == 403
        assert b'Title, independent, dependent, data set, and precision fields must all be provided' in res.data
    
    def test_request_submission_fails_partial_fields(self, app, client):
        @app.route("/submission_partial_fails", methods=["POST"])
        def submission_partial_fails_route():
            submission = request_submission()
            return submission

        res = client.post(
            "/submission_partial_fails",
            json = {
                'precision': 4,
                'data_set': [[1, 2], [3, 4]]
            }
        )

        assert res.status_code == 403
        assert b'Title, independent, dependent, data set, and precision fields must all be provided' in res.data
    
    def test_request_submission_fails_without_json(self, app, client):
        @app.route("/submission_without_json_fails", methods=["POST"])
        def submission_without_json_fails_route():
            submission = request_submission()
            return submission

        res = client.post("/submission_without_json_fails")
        assert res.status_code == 500

class TestRequireKeyUtility:
    def test_require_key_returns_function(self, app, client):
        @app.route("/requirements", methods=["POST"])
        @require_key
        def requirements_route():
            return 'Valid key provided; all requirements met'

        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = 'ABC123',
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        res = client.post("/requirements?key=ABC123")
        assert b'Valid key provided; all requirements met' in res.data

        db.session.delete(found_user)
        db.session.commit()
    
    def test_require_key_fails_without_key(self, app, client):
        @app.route("/requirements_without_key", methods=["POST"])
        @require_key
        def requirements_without_key_route():
            return 'Valid key provided; all requirements met'

        res = client.post("/requirements_without_key")
        assert res.status_code == 403
        assert b'Key must be provided' in res.data
    
    def test_require_key_fails_with_bad_key(self, app, client):
        @app.route("/requirements_bad_key", methods=["POST"])
        @require_key
        def requirements_bad_key_route():
            return 'Valid key provided; all requirements met'

        res = client.post("/requirements_bad_key?key=ABC123")
        assert res.status_code == 401
        assert b'User not authenticated' in res.data

class TestUniqueKeyUtility:
    def test_unique_key_creates_standard_key(self):
        new_key = unique_key()
        pattern = r'[^\.a-zA-Z0-9]'
        problems = re.search(pattern, new_key)
        assert len(new_key) == 32
        assert not problems
    
    def test_unique_key_creates_unused_key(self):
        first_key = generate_key()

        new_user = User(
            name = 'temporary user',
            email = 'temporary@email.com',
            key = first_key,
            date = datetime.now()
        )

        db.session.add(new_user)
        db.session.commit()

        found_user = User.query.filter_by(
            email = 'temporary@email.com'
        ).first()

        second_key = unique_key()
        assert second_key != first_key

        db.session.delete(found_user)
        db.session.commit()

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