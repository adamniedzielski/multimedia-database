
class DirectoriesController:

  def create(path):
    if Directory.select().where(Directory.path == path).count() == 0:
      Directory.create(path = path)
