import re

import pytest

from sampy.exceptions import ParameterConflictException
from sampy.generators import EmailGenerator


def test_generate_email(mocker):
    generator = EmailGenerator()
    test_user_name = "foo"
    test_domain_name = "bar.com"

    mocker.patch.object(generator.faker, 'user_name', return_value=test_user_name)
    mocker.patch.object(generator.faker, 'domain_name', return_value=test_domain_name)
    email = generator.generate()

    assert email == f"{test_user_name}@{test_domain_name}"
    generator.faker.user_name.assert_called_once()
    generator.faker.domain_name.assert_called_once()


def test_generate_email_anon_user(mocker):
    generator = EmailGenerator(anon_username=True)
    test_domain_name = "bar.com"

    mocker.patch.object(generator.faker, 'domain_name', return_value=test_domain_name)
    email = generator.generate().split("@")


    assert re.match(r'^[a-z]{12}$', email[0])
    assert email[1] == test_domain_name
    generator.faker.domain_name.assert_called_once()


def test_generate_email_public_domain(mocker):
    generator = EmailGenerator(public_domain=True)
    test_user_name = "foo"
    test_domain_name = "bar.com"

    mocker.patch.object(generator.faker, 'user_name', return_value=test_user_name)
    mocker.patch.object(generator.faker, 'free_email_domain', return_value=test_domain_name)
    email = generator.generate()

    assert email == f"{test_user_name}@{test_domain_name}"
    generator.faker.user_name.assert_called_once()
    generator.faker.free_email_domain.assert_called_once()


def test_generate_email_safe_domain(mocker):
    generator = EmailGenerator(safe_domain=True)
    test_user_name = "foo"
    test_domain_name = "bar.com"

    mocker.patch.object(generator.faker, 'user_name', return_value=test_user_name)
    mocker.patch.object(generator.faker, 'safe_domain_name', return_value=test_domain_name)
    email = generator.generate()

    assert email == f"{test_user_name}@{test_domain_name}"
    generator.faker.user_name.assert_called_once()
    generator.faker.safe_domain_name.assert_called_once()


def test_validate_fail_multi_domains_set():
    with pytest.raises(ParameterConflictException):
        EmailGenerator(safe_domain=True, public_domain=True)
