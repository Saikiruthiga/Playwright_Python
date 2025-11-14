import report
import json
import pytest

@pytest.fixture(scope="module")
def report_json():
    report.generate_report()

    with open("report.json") as file:
        return json.load(file) # read the json content and convert it into python
    

def test_report_json(report_json):
    assert type(report_json) == dict

def test_report_fields(report_json):
    assert "name" in report_json
    assert "Age" in report_json
