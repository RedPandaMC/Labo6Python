import validators
from validators import ValidationFailure

def is_string_an_url(url_string: str) -> bool:
    url_string = url_string.strip()
    result = validators.url(url_string)
    if isinstance(result, ValidationFailure):
        return False
    return result
