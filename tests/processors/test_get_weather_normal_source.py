import pytest
from eemeter.structures import ZIPCodeSite

from eemeter.processors.location import get_weather_normal_source


@pytest.fixture
def site():
    return ZIPCodeSite("91104")


@pytest.fixture
def site_bad_zip():
    return ZIPCodeSite("00000")


def test_basic_usage(site):

    ws = get_weather_normal_source(site)

    assert ws.usaf_id == '722904'


def test_bad_zip(site_bad_zip):
    assert get_weather_normal_source(site_bad_zip) is None

