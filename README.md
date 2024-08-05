# Python API Automation Framework

### Tech Stack
- Python 3.12
- Requests - HTTP Requests
- Pytest - Testing Framework
- Reporting - Allure Report , PyTest HTML
- Test Data - CSV,Excel,JSON,Faker
- Advance API Testing - Jsonschema
- Parallel Execution - x distribute (xidst)

### How To Install Packages

```pip install requests pytest pytest-html faker allure-pytest jsonschema```

### How To Run Your Testcase Parallel

```pip install pytest-xdist```

### How To Add the .gitignore File?

Copy the content from this to .gitignore file
https://www.toptal.com/developers/gitignore/api/pycharm

### How to Run the Basic Testcases

```pytest src/helpers/payload_manager.py --alluredir=allure_result```
