import sys

from db_functions import create_db, load_db, write_issue, read_issues

create_db('test_db')

session = load_db('test_db')

