from app.modules.core.message_enum import MessageEnum
from fastapi import HTTPException, status
import datetime
import pyotp
import re


def generate_code_otp():
    totp = pyotp.TOTP(pyotp.random_base32())
    code_otp = totp.now()
    datetime_now = datetime.datetime.now()
    datetime_expiration = datetime_now + datetime.timedelta(minutes=5)
    return code_otp, datetime_expiration


def valid_name(name: str):
    if not valid_string_any_less_characters(name, 5):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=MessageEnum.INVALID_NAME_LESS_CHAR.value,
        )
    if not valid_number_of_words_string(name, 2):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=MessageEnum.INVALID_NAME_LESS_NUMBER_WORDS.value,
        )


def valid_number_of_words_string(string, number_words):
    str_split = string.split()
    if len(str_split) < number_words:
        return False
    return True


def valid_string_format_email(email: str):
    regex = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(regex, email):
        return False
    return True


def valid_string_any_less_characters(string: str, max_characters: int):
    if len(string) < max_characters:
        return False
    return True


def valid_string_with_number(password: str):
    if not re.findall(r"\d", password):
        return False
    return True


def valid_string_with_upper_case(password: str):
    if not re.findall(r"[A-Z]", password):
        return False
    return True


def valid_string_with_lower_case(password: str):
    if not re.findall(r"[a-z]", password):
        return False
    return True


def valid_string_with_special_character(password: str):
    if not re.findall(r"[()[\]{}|\\`~!@#$%^&*_\-+=;:'\",<>./?]", password):
        return False
    return True


def valid_password(password):
    if not valid_string_any_less_characters(password, 8):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=MessageEnum.INVALID_PASSWORD_LESS_CHARACTER.value,
        )
    if not valid_string_with_number(password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=MessageEnum.INVALID_PASSWORD_WITH_NUMBER.value,
        )
    if not valid_string_with_upper_case(password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=MessageEnum.INVALID_PASSWORD_WITH_UPPER_CASE.value,
        )
    if not valid_string_with_lower_case(password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=MessageEnum.INVALID_PASSWORD_WITH_LOWER_CASE.value,
        )
    if not valid_string_with_special_character(password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=MessageEnum.INVALID_PASSWORD_WITH_SPECIAL_CHARACTER.value,
        )


def valid_email(email):
    if not valid_string_format_email(email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=MessageEnum.INVALID_FORMAT_EMAIL.value,
        )


