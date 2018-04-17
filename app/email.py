# Cody Mitton
# ccm326
# CSE 4283 Software Testing and Quality Assurance
# Professional Practice Assignment 1
# Behavior-Driven Development and Unit Testing
import re


def verify_email(email):
    regex = r"^[a-zA-Z!$%*+\-=?^_{|}~]+(((\.[\w!$%*+\-=?^_{|}~]+)+|[\w!$%*+\-=?^_{|}~])+)@((?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}$"
    is_email = re.fullmatch(regex, email, re.IGNORECASE)
    if is_email:
        return True
    else:
        return False
