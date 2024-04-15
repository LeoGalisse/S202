from database.database import Database
from controller.motoristacli import MotoristaCLI

db = Database(database="entrai", collection="motoristas")
db.reset_database()

cli = MotoristaCLI(db)
cli.menu()