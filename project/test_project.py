import pytest
import time
from project import get_todos, write_todos, get_current_time


def test_get_todos(tmp_path):
    test_file = tmp_path / "test_todos.txt"
    test_file.write_text("todo 1\n" + "todo 2\n")
    todos = get_todos(test_file)
    assert todos == ["todo 1\n", "todo 2\n"]

def test_write_todos(tmp_path):
    test_file = tmp_path / "test_todos.txt"
    write_todos(["todo 1\n", "todo 2\n"], test_file)
    with open(test_file, 'r') as file:
        contents = file.readlines()
    assert contents == ["todo 1\n", "todo 2\n"]

def test_get_current_time():
    current_time = get_current_time()
    expected_time = time.strftime("%b %d, %Y %H:%M:%S")
    assert current_time == expected_time
    
