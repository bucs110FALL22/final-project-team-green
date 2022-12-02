from replit import db

class Database():
  def __init__(self):
    self.db = db

  def addData(self, key, value):
    self.db[key] = value