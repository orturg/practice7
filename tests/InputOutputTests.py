import unittest
from unittest.mock import mock_open, patch
from app.io.input import read_from_file, read_from_file_pandas
import pandas as panda
import io


class TestReadInputMethods(unittest.TestCase):
    def test_read_from_file_existing_file(self):
        mock_data = "Hello"
        with patch("builtins.open", mock_open(read_data = mock_data)):
            result = read_from_file("file1.txt")
            self.assertEqual(result, mock_data)

    def test_read_from_file_file_not_found(self):
        result = read_from_file("fileqqq.txt")
        self.assertEqual(result, "такого файлу не існую")

    def test_read_from_file_empty_file(self):
        with patch("builtins.open", mock_open(read_data = "")):
            result = read_from_file("empty.txt")
            self.assertEqual(result, "")

    def test_read_from_file_pandas_existing_file(self):
        mock_csv_data = "Hello"
        with patch("builtins.open", mock_open(read_data = mock_csv_data)):
            with patch("pandas.read_csv", return_value = panda.read_csv(io.StringIO(mock_csv_data))):
                result = read_from_file_pandas("file1.csv")
                self.assertIn("Hello", result)

    def test_read_from_file_pandas_file_not_found(self):
        result = read_from_file_pandas("nonExisted.csv")
        self.assertEqual(result, "такого файлу не існую")

    def test_read_from_file_pandas_empty_file(self):
        with patch("builtins.open", mock_open(read_data = "")):
            with patch("pandas.read_csv", side_effect = panda.errors.EmptyDataError):
                result = read_from_file_pandas("empty.csv")
                self.assertEqual(result, "такого файлу не існую")


if __name__ == "__main__":
    unittest.main()