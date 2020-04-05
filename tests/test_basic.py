from .context import boilerplate
# https://docs.python-guide.org/writing/structure/#test-suite
import boilerplate.tools.example


def test_sleeper():
    parameter_in = 0.5
    expected = 0.5
    assert boilerplate.tools.example.sleeper(parameter_in) == expected
