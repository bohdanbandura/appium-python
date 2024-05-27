import pytest

@pytest.fixture
def device_selector(request):
    device = request.config.getoption('--device')
    env = request.config.getoption('--env')
    return device
    