import pytest
from jsonmerge import merge

@pytest.fixture(scope='session')
def session_capabilities():
  capabilities = {}
  return capabilities


def pytest_sessionfinish(session, exitstatus):
  print("Session completed")
