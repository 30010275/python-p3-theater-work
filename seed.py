from models.database import SessionLocal
from models.audition import Audition
from models.role import Role

session = SessionLocal()

# Create Roles
role1 = Role(character_name="Hamlet")
role2 = Role(character_name="Othello")

# Create Auditions with Kenyan names
audition1 = Audition(actor="Amani Mwangi", location="New York", phone=123456789, role=role1)
audition2 = Audition(actor="Kasongo Wiliam", location="Los Angeles", phone=987654321, hired=True, role=role1)
audition3 = Audition(actor="Wanjiru Njeri", location="Chicago", phone=456123789, hired=True, role=role2)

# Add to session and commit
session.add_all([role1, role2, audition1, audition2, audition3])
session.commit()

print("✅ Database seeded successfully!")
