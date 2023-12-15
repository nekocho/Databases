from lib.database_connection import DatabaseConnection
from lib.post_repository import *
from lib.comment import *


class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/blog.sql")

  def run(self):
    post_repository = PostRepository(self._connection)
    post = post_repository.find_with_comments(1)
    print(post)

if __name__ == '__main__':
    app = Application()
    app.run()