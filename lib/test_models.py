import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Role, Audition

class TestTheaterModels(unittest.TestCase):

    def setUp(self):
        # Setup code for creating a session
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def test_create_role(self):
        role = Role(character_name='Hamlet')
        self.session.add(role)
        self.session.commit()
        self.assertEqual(role.character_name, 'Hamlet')

    def test_create_audition(self):
        role = Role(character_name='Macbeth')
        self.session.add(role)
        self.session.commit()

        audition = Audition(actor='Diego Iso', location='Theater A', phone=1234567890, hired=False, role_id=role.id)
        self.session.add(audition)
        self.session.commit()

        self.assertEqual(audition.actor, 'Diego Iso')
        self.assertEqual(audition.role_id, role.id)

    def test_audition_callback(self):
        role = Role(character_name='Othello')
        self.session.add(role)
        self.session.commit()

        audition = Audition(actor='Leah Kong', location='Theater B', phone=9876543210, hired=False, role_id=role.id)
        self.session.add(audition)
        self.session.commit()

        audition.call_back()
        self.assertTrue(audition.hired)

    def test_role_auditions(self):
        role = Role(character_name='King Lear')
        self.session.add(role)
        self.session.commit()

        audition1 = Audition(actor='Actor 1', location='Theater C', phone=1112223333, hired=True, role_id=role.id)
        audition2 = Audition(actor='Actor 2', location='Theater D', phone=4445556666, hired=False, role_id=role.id)
        self.session.add(audition1)
        self.session.add(audition2)
        self.session.commit()

        self.assertEqual(role.auditions[0].actor, 'Actor 1')
        self.assertEqual(role.auditions[1].actor, 'Actor 2')

    def test_role_lead(self):
        role = Role(character_name='Julius Caesar')
        self.session.add(role)
        self.session.commit()

        audition1 = Audition(actor='Actor 3', location='Theater E', phone=7778889999, hired=True, role_id=role.id)
        self.session.add(audition1)
        self.session.commit()

        self.assertEqual(role.lead().actor, 'Actor 3')

    def test_role_understudy(self):
        role = Role(character_name='Brutus')
        self.session.add(role)
        self.session.commit()

        audition1 = Audition(actor='Actor 4', location='Theater F', phone=1011121314, hired=True, role_id=role.id)
        audition2 = Audition(actor='Actor 5', location='Theater G', phone=1516171819, hired=True, role_id=role.id)
        self.session.add(audition1)
        self.session.add(audition2)
        self.session.commit()

        self.assertEqual(role.understudy().actor, 'Actor 5')

if __name__ == '__main__':
    unittest.main()
