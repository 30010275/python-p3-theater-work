from database import session
from models import Role, Audition

# Create Roles
role1 = Role(character_name="Hamlet")
role2 = Role(character_name="Macbeth")

# Create Auditions
audition1 = Audition(actor="diego iso", location="New York", phone=1234567890, hired=True, role=role1)
audition2 = Audition(actor="Jane Smith", location="Los Angeles", phone=9876543210, hired=False, role=role1)
audition3 = Audition(actor="Emily Johnson", location="Chicago", phone=5678901234, hired=True, role=role2)

# Add to DB
session.add_all([role1, role2, audition1, audition2, audition3])
session.commit()

print("Database seeded successfully!")
