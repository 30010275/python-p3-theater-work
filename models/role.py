from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.database import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)

    auditions = relationship("Audition", back_populates="role")

    def actors(self):
        """Returns a list of actor names for this role."""
        return [audition.actor for audition in self.auditions]

    def locations(self):
        """Returns a list of locations for this role."""
        return [audition.location for audition in self.auditions]

    def lead(self):
        """Returns the first hired actor for this role, or a default message."""
        hired_actors = [audition for audition in self.auditions if audition.hired]
        return hired_actors[0] if hired_actors else "No actor has been hired for this role."

    def understudy(self):
        """Returns the second hired actor, or a default message."""
        hired_actors = [audition for audition in self.auditions if audition.hired]
        return hired_actors[1] if len(hired_actors) > 1 else "No actor has been hired for understudy for this role."
