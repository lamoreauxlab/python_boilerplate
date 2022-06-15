"""Test main functions."""
from boilerplate import __version__ as vers


def test_version():
    """Test Version."""
    assert vers == "0.0.1"
