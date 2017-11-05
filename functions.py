import sys
sys.dont_write_bytecode = True

import sqlite3
import json


def dict_factory(cursor, row):
	d = {}
	for i, col in enumerate(cursor.description):
		d[col[0]] = row[i]
	return d


class DB:
	def __init__(self):
		self.connection = sqlite3.connect("database.db")
		self.connection.row_factory = dict_factory

		self.cursor = self.connection.cursor()

	def __del__(self):
		self.connection.close()
