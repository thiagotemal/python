import unittest
from unittest.mock import patch
from function_app import validated_request_body, validate_cpf, ValidationInnerResponse, DataResponse, http_post
import azure.functions as func

class TestValidatedRequestBody(unittest.TestCase):
    @patch('function_app.func.HttpRequest')
    def test_validated_request_body(self, mock_request):
        mock_request.get_json.return_value = {'cpf': '12345678901'}
        self.assertEqual(validated_request_body(mock_request), {'cpf': '12345678901'})

    @patch('function_app.func.HttpRequest')
    def test_validated_request_body_without_body(self, mock_request):
        mock_request.get_json.return_value = None
        with self.assertRaises(ValueError):
            validated_request_body(mock_request)



class TestValidateCpf(unittest.TestCase):
    def test_validate_cpf(self):
        self.assertTrue(validate_cpf('93117388915'))

    def test_validate_cpf_invalid(self):
        self.assertFalse(validate_cpf('1234567890'))

    def test_validate_cpf_invalid_length(self):
        self.assertFalse(validate_cpf('1234567890123'))

    def test_validate_cpf_invalid_all_zero(self):
        self.assertFalse(validate_cpf('00000000000'))

    def test_validate_cpf_invalid_all_same(self):
        self.assertFalse(validate_cpf('11111111111'))


class TestDataResponse(unittest.TestCase):
    def test_to_dict(self):
        inner_response = ValidationInnerResponse(valid=True)
        data_response = DataResponse(data=inner_response)
        self.assertEqual(data_response.to_dict(), {'data': {'valid': True}})


if __name__ == '__main__':
    unittest.main()
