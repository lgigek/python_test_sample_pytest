# python_test_sample_pytest
This project contains a code with basic math operations. It was created to make unit tests and comprehend how [pytest](https://pytest.org/) works.

## Executing tests
Before execute the tests, is necessary to install the dependencies using the following command:

`pip install -r requirements-dev.txt`


After that, the tests can be executed using the following command:

`pytest`

The output should be something like this:

```
======================================================================================= test session starts ========================================================================================
platform linux -- Python 3.6.7, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: /home/eg/Development/git-personal/python_test_sample_pytest, inifile:
plugins: mock-1.10.1
collected 5 items                                                                                                                                                                                  

test/test_math_helper.py .....                                                                                                                                                               [100%]

===================================================================================== 5 passed in 0.02 seconds =====================================================================================
```

Also, the tests can be executed checking the coverage. It is necessary to use the following command:

`pytest --cov=python_test_sample.math_helper`

And the output should be something like this:


```
======================================================================================= test session starts ========================================================================================
platform linux -- Python 3.6.7, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: /home/eg/Development/git-personal/python_test_sample_pytest, inifile:
plugins: mock-1.10.1, cov-2.6.1
collected 5 items                                                                                                                                                                                  

test/test_math_helper.py .....                                                                                                                                                               [100%]

----------- coverage: platform linux, python 3.6.7-final-0 -----------
Name                                Stmts   Miss  Cover
-------------------------------------------------------
python_test_sample/math_helper.py      12      0   100%


===================================================================================== 5 passed in 0.05 seconds =====================================================================================
```