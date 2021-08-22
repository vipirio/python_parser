import json

from main import main


expected_result = json.loads(open('tests/result.json').read())
file_path = 'tests/test_log.log'
date = '2021-05-01'

def test_fail_password_delimeter_parser():
    output = main(file_path)
    assert output['Failed password'] == expected_result['fail_password']

def test_fail_password_delimeter_parser_with_date():
    output = main(file_path, date)
    assert output['Failed password'] == expected_result['fail_password_with_date']

def test_reverse_mapping_delimeter_parser():
    output = main(file_path)
    assert  output['reverse mapping'] == expected_result['reverse_mapping']

def test_reverse_mapping_delimeter_parser_with_date():
    output = main(file_path,date)
    assert output['reverse mapping'] == expected_result['reverse_mapping_with_date']


