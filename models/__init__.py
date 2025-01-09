#!/usr/bin/python3
"""This module instantiates the storage engine to either FileStorage or
   Database storage, based on the environment variable set.
"""
import os
from models.engine.file_storage import FileStorage

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
