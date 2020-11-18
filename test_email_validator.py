import unittest
from email_validator import EmailValidator


class EmailValidatorTestCase(unittest.TestCase):

    def test_no_blank_email(self):
        value = ""
        result = EmailValidator(value).is_valid()
        self.assertFalse(result)

    def test_email_has_at_sign(self):
        value = "123@"
        result = EmailValidator(value).is_valid()
        self.assertTrue(result)

    def test_email_has_text_before_and_after_sign(self):
        value = "123@123"
        result = EmailValidator(value).is_valid()
        self.assertTrue(result)

    def test_email_has_domain_after_sign(self):
        value = "123@123.com"
        result = EmailValidator(value).is_valid()
        self.assertTrue(result)

    def test_email_username_should_be_without_spaces(self):
        value = "1 23@123.com"
        result = EmailValidator(value).is_valid()
        self.assertFalse(result)

    def test_email_username_can_use_dots(self):
        value = "1.2..3@123.com"
        result = EmailValidator(value).is_valid()
        self.assertTrue(result)

    def test_email_domains_can_have_dots(self):
        value = "123@12.co.ll"
        result = EmailValidator(value).is_valid()
        self.assertTrue(result)
