from lib.database_connection import DatabaseConnection
from lib.cohort_repository import *


class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/student_directory_2.sql")

  def run(self):
    cohort_repository = CohortRepository(self._connection)

    print(
       cohort_repository.find_with_students(1)
    )



#     print("Welcome to the music library manager!")

#     print("What would you like to do?")
#     print('1 - List all albums')
#     print('2 - List all artists')
#     inp = int(input("Enter your choice:"))
#     if inp == 1:
#         print('Here is a list of artists:')
#         for artist in artists:
#             print(f"{artist.id}: {artist.name} ({artist.genre})")
#     if inp == 2:
#         print('Here is a list of albums:')
#         for album in albums:
#             print(f"{album.id}: {album.title} ({album.release_year} {album.artist_id})")

if __name__ == '__main__':
    app = Application()
    app.run()