#!/usr/bin/python3
"""Module that performs unittest for the console(commandline interface)
"""
import os
import MySQLdb
import unittest
from console import HBNBCommand
from models.state import State
from models import storage
from io import StringIO
from unittest.mock import patch

class TestConsole(unittest.TestCase):
    """Test class for the HBNBCommand class
    """
    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db',
        "Test only for database storage")
    def test_create_state(self):
        """Test for record change once new state is created
        """
        cli = HBNBCommand()
        dbcn = MySQLdb.connect(
            host = os.getenv('HBNB_MYSQL_HOST'),
            user = os.getenv('HBNB_MYSQL_USER'),
            passwd = os.getenv('HBNB_MYSQL_PWD'), 
            db = os.getenv('HBNB_MYSQL_DB')
        )

        cursor = dbcn.cursor()
        cursor.execute("SELECT COUNT(*) FROM states;")
        initial_count = cursor.fetchone()[0]

        with patch('sys.stdout', new=StringIO()) as res:
            cli.onecmd('Create State.name="Carlifornia"')
        
        cursor.execute("SELECT COUNT(*) FROM states")
        new_count = cursor.fetchone()[0]

        self.assertEqual(new_count, initial_count+1)

        cursor.close()
        dbcn.close()