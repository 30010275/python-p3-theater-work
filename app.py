from models.database import engine, Base
from models.audition import Audition
from models.role import Role

Base.metadata.create_all(bind=engine)
print("✅ Database and tables created successfully!")
