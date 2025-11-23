# conftest.py
import os
import pytest


@pytest.fixture
def driver_path():
    """Ensure pytest-selenium receives a valid SafariDriver path."""
    path = os.getenv("SAFARI_DRIVER_PATH", "/usr/bin/safaridriver")
    if not os.path.exists(path):
        raise RuntimeError(f"SafariDriver not found at: {path}")
    return path


@pytest.fixture
def driver_args():
    """pytest-selenium passes this to Safari Service."""
    return []


@pytest.fixture
def driver_log(tmp_path):
    """pytest-selenium writes Safari logs here."""
    return str(tmp_path / "safaridriver.log")
