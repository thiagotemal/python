
from dataclasses import dataclass
import azure.functions as func
import logging
import json


app = func.FunctionApp()

@dataclass
class ValidationInnerResponse:
    valid: bool
    def to_dict(self):
        return {'valid': self.valid}
@dataclass
class DataResponse:
    data: ValidationInnerResponse

    def to_dict(self):
        return {'data': self.data.__dict__}



@app.route(route="v1/documents/validations", auth_level=func.AuthLevel.ANONYMOUS, methods=["POST"] )
def http_post(req: func.HttpRequest) -> func.HttpResponse:
    """
    Validates a CPF received in the body of a POST request.

    Expects that the request body is a JSON object with a "data" field, which
    is itself a JSON object with a "cpf" field. That field should contain a
    string with the CPF number to be validated.

    Returns a 200 response with the body "CPF válido" if the CPF is valid,
    a 400 response with the body "CPF inválido" if the CPF is invalid, a 400
    response with the body "Requisi o sem corpo ou sem campo 'data'" if the
    request body does not have a "data" field, and a 500 response with the
    body "Ocorreu um erro ao processar a requisi o" if any unexpected error
    occurs.
    """
    logging.info('Python HTTP trigger function processed a request.')

    try:
        cpf = validated_request_body(req)  
        data = ValidationInnerResponse(valid = validate_cpf(cpf))
        response = DataResponse(data = data)
        return func.HttpResponse(
            status_code=200,
            body= json.dumps(response.to_dict()).encode('utf-8'),
            mimetype="application/json"
        )
    except ValueError:
        return func.HttpResponse(
            status_code=400,
            body="Requisi o sem corpo ou sem campo 'cpf'",
        )
    except Exception as err:
        logging.error(f"Unexpected {err=}, {type(err)=}")
        return func.HttpResponse(
            status_code=500,
            body="Ocorreu um erro ao processar a requisição",
        )


def validated_request_body(req: func.HttpRequest) -> dict:
    """
    Valida se a requisi o  possui um corpo com o campo 'cpf' e retorna o valor
    desse campo. Caso contr rio, lan a um ValueError.
    """
    data = req.get_json()

    if not data or not isinstance(data, dict):
        raise ValueError
    return data

def validate_cpf(cpf) -> bool :
    # Remove non-numeric characters

    """
    Verifica se um CPF  valido.

    O CPF  considerado v  lido se possuir 11 d  gitos num  ricos,
    n o possuir todos os d  gitos iguais, n o possuir todos os d  gitos
    zeros, e se passar nas verifica es de dig  to verificador.

    :param cpf: CPF a ser validado
    :type cpf: str
    :return: True se o CPF for v  lido, False caso contr rio
    :rtype: bool
    """
    cpf = ''.join(filter(str.isdigit, cpf))

    # Check if CPF has 11 digits
    if len(cpf) != 11:
        return False

    # Check if all digits are the same or if the CPF is only zeros
    if cpf == cpf[0] * 11 or cpf == '0' * 11:
        return False

    # Validate CPF using its validation rules
    def calculate_digit(digits):
        weight = len(digits) + 1
        total_sum = sum(int(d) * (weight - i) for i, d in enumerate(digits))
        remainder = total_sum % 11
        return '0' if remainder < 2 else str(11 - remainder)

    # Verify first digit
    if calculate_digit(cpf[:9]) != cpf[9]:
        return False

    # Verify second digit
    if calculate_digit(cpf[:10]) != cpf[10]:
        return False

    return True

