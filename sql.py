import sqlite3
import os

class Database:
	def __init__(self, file="db.sqlite"):
		if not os.path.exists(file):
			with open(file, "w") as f:
				f.write("")
		self.db = sqlite3.connect(file, check_same_thread=False)
		self.sql = self.db.cursor()

	def query(self, query: str):
		execute = self.sql.execute(query)
		if not "select" in query.lower():
			self.db.commit()
			return "The database updates"
		else:
			return execute.fetchall()

if __name__ == "__main__":
    while True:
        sql = Database()
        query = input("Please enter a query: ")
        if query == "":
            break
        try:
            q = sql.query(query)
            print(q)
        except Exception as e:
            print(e)
