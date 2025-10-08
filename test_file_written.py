import os
from file_writter import write_to_file

def test_write_file():
    test_filename = "text_output.txt"
    test_content = "Test content for CI"
    write_to_file(test_filename, test_content)

    assert os.path.exists(test_filename), "File not created "

    with open(test_filename, 'r') as f:
        content = f.read()
        assert content == test_content, "File content do not match ..."
        

