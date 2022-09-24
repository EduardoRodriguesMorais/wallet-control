from enum import Enum


class MessageEnum(Enum):
    """
    Enum for message types.
    """

    """
    VALIDATION_NOT_IMPLEMENTED_FIELD = "Validation not implemented for this country"
    VALIDATION_NOT_IMPLEMENTED_COUNTY = "Validation not implemented for this country"
    CNPJ_INVALID = "Invalid CNPJ. Please enter an existing value."
    CPF_INVALID = "Invalid CPF. Please enter an existing value."
    COUNTRY_NOT_FOUND = "Country not found"
    NAME_COUNTRY_EXISTS = "Name country already exists"
    CODE_COUNTRY_EXISTS = "Code country already exists"
    EMAIL_SUBJECT_RESET_PASS = "Redefinir senha. [GravScale]"
    EMAIL_SUBJECT_VERIFY_CODE = "Código de verificação. [GravScale]"
    EMAIL_SUBJECT_WELCOME = "Boas-vindas! [GravScale]"
    ERROR_SEND_EMAIL = "Error sending email."
    EXPIRED_CODE_OTP = "Your Code has expired. Request to send a new code."
    INVALID_CODE_OTP = "Code invalid."
    PHONE_NUMBERS_EQUALS = "Mobile and landline numbers cannot be the same."
    USER_EMAIL_NOT_VERIFIED = "User email not verified."
    USER_NOT_UPDATED = "User not updated"
    USER_INVALID_PASSWORD = "Invalid password"
    USER_NOT_FOUND = "User not found"
    COMPANY_ALREADY_EXISTS = "Company already registered"
    EMAIL_NOT_FOUND = "Email not registered"
    
    """
    INVALID_NAME_LESS_NUMBER_WORDS = "Text field needs at least 2 words."
    INVALID_NAME_LESS_CHAR = "Text field needs at least 5 characters."
    EMAIL_ALREADY_EXISTS = "Email already registered"
    INVALID_FORMAT_EMAIL = "Format email invalid."
    INVALID_PASSWORD_LESS_CHARACTER = "The password must contain at least 8 positions."
    INVALID_PASSWORD_WITH_NUMBER = (
        "The password must contain at least 1 digit, example: 0-9."
    )
    INVALID_PASSWORD_WITH_UPPER_CASE = (
        "Password must contain at least 1 uppercase letter, example: A-Z."
    )
    INVALID_PASSWORD_WITH_LOWER_CASE = (
        "Password must contain at least 1 lowercase letter, example: a-z."
    )
    INVALID_PASSWORD_WITH_SPECIAL_CHARACTER = (
        "Password must contain at least 1 symbol, example: ()[]{"
        r"}|\`~!@#$%^&*_-+=;:'\",<>./? . "
    )
    USER_INVALID_PASSWORD = "Invalid password"
    USER_NOT_FOUND = "User not found"





