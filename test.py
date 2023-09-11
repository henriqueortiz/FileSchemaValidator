from fileschemavalidator import CsvSchemaValidator
import csv

SCHEMA = {
    "column1":{"type": "int", "is_required": 1},
    "column2":{"type": "string", "is_required": 0},
    "column3":{"type": "float", "is_required": 0},
    "column4":{"type": "date", "format": "%Y-%m-%d", "is_required": 0},
    "column5":{"type": "bool", "is_required": 0},
    "column6":{"type": "timestamp", "format": "%Y-%m-%d %H:%M:%S.%f", "is_required": 0}
}

FILES = ['sucess.csv', 'column-warning.csv', 'column-error.csv', 'type-error.csv', 'required-error.csv']

class TestCsvSchemaValidator():
    def __init__(self):
          pass
    
    def setUp(self):
        print("\nRunning setUp method...")
        for file in FILES:
            csv_buffer = open(f'./fileschemavalidator/test-files/{file}', encoding='utf8')
            csv_reader = csv.DictReader(csv_buffer, delimiter=';')
            validator = CsvSchemaValidator(SCHEMA, csv_reader)

    def test_sucess(self):
        print("\nRunning sucess test...")
        csv_buffer = open('./fileschemavalidator/test-files/sucess.csv', encoding='utf8')
        csv_reader = csv.DictReader(csv_buffer, delimiter=';')
        validator = CsvSchemaValidator(SCHEMA, csv_reader)
        try:
            validator.validate_columns()
            validator.validate_rows()
        except Exception as e:
            print(validator.validate_columns_errors)
            print(validator.validate_rows_errors)

    def test_warning(self):
        print("\nRunning warning test...")
        csv_buffer = open('./fileschemavalidator/test-files/column-warning.csv', encoding='utf8')
        csv_reader = csv.DictReader(csv_buffer, delimiter=';')
        validator = CsvSchemaValidator(SCHEMA, csv_reader)
        try:
            validator.validate_columns()
            validator.validate_rows()
        except Exception as e:
            print(validator.validate_columns_errors)
            print(validator.validate_rows_errors)

    def test_column_error(self):
        print("\nRunning column-error test...")
        csv_buffer = open('./fileschemavalidator/test-files/column-error.csv', encoding='utf8')
        csv_reader = csv.DictReader(csv_buffer, delimiter=';')
        validator = CsvSchemaValidator(SCHEMA, csv_reader)
        try:
            validator.validate_columns()
            validator.validate_rows()
        except Exception as e:
            print(validator.validate_columns_errors)
            print(validator.validate_rows_errors)

    def test_type_error(self):
        print("\nRunning type-error test...")
        csv_buffer = open('./fileschemavalidator/test-files/type-error.csv', encoding='utf8')
        csv_reader = csv.DictReader(csv_buffer, delimiter=';')
        validator = CsvSchemaValidator(SCHEMA, csv_reader)
        try:
            validator.validate_columns()
            validator.validate_rows()
        except Exception as e:
            print(validator.validate_columns_errors)
            print(validator.validate_rows_errors)
    
    def test_required_error(self):
        print("\nRunning required-error test...")
        csv_buffer = open('./fileschemavalidator/test-files/required-error.csv', encoding='utf8')
        csv_reader = csv.DictReader(csv_buffer, delimiter=';')
        validator = CsvSchemaValidator(SCHEMA, csv_reader)
        try:
            validator.validate_columns()
            validator.validate_rows()
        except Exception as e:
            print(validator.validate_columns_errors)
            print(validator.validate_rows_errors)

    def test_bool_error(self):
        print("\nRunning bool-error test...")
        csv_buffer = open('./fileschemavalidator/test-files/bool-error.csv', encoding='utf8')
        csv_reader = csv.DictReader(csv_buffer, delimiter=';')
        validator = CsvSchemaValidator(SCHEMA, csv_reader)
        try:
            validator.validate_columns()
            validator.validate_rows()
        except Exception as e:
            print(validator.validate_columns_errors)
            print(validator.validate_rows_errors)

if __name__=='__main__':
    test = TestCsvSchemaValidator()
    try:
        test.test_sucess()
    except Exception as e:
        print(e)
    try:
        test.test_warning()
    except Exception as e:
        print(e)
    try:
        test.test_column_error()
    except Exception as e:
        print(e)
    try:
        test.test_type_error()
    except Exception as e:
        print(e)
    try:
        test.test_required_error()
    except Exception as e:
        print(e)
    try:
        test.test_bool_error()
    except Exception as e:
        print(e)