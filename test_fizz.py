import importlib
import sys
import io

def test_fizz(monkeypatch):
    mocked_stdout = io.StringIO()
    expected_output = "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FizzBuzz1617Fizz19\
        BuzzFizz2223FizzBuzz26Fizz2829FizzBuzz3132Fizz34BuzzFizz3738FizzBuzz\
        41Fizz4344FizzBuzz4647Fizz49BuzzFizz5253FizzBuzz56Fizz5859FizzBuzz\
        6162Fizz64BuzzFizz6768FizzBuzz71Fizz7374FizzBuzz7677Fizz79\
        BuzzFizz8283FizzBuzz86Fizz8889FizzBuzz9192Fizz94BuzzFizz\
        9798FizzBuzz"

    with monkeypatch.context() as m:
        m.setattr(sys, "stdout", mocked_stdout)
        sys.modules.pop("fizzbuzz", None)
        importlib.import_module(name="fizzbuzz", package="files")
    
    result = mocked_stdout.getvalue()
    assert "".join(result.split()) == "".join(expected_output.split())