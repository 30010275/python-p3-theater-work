import unittest
from unittest.mock import MagicMock
from .models import Role, Audition

class TestTheaterModels(unittest.TestCase):

    def test_create_role(self):
        role = Role(character_name='Hamlet')
        self.assertEqual(role.character_name, 'Hamlet')

    def test_create_audition(self):
        role = Role(character_name='Macbeth')
        audition = Audition(actor='John Doe', location='Theater A', phone=1234567890, hired=False, role_id=1)
        self.assertEqual(audition.actor, 'John Doe')
        self.assertEqual(audition.role_id, 1)

    def test_audition_callback(self):
        audition = Audition(actor='Jane Doe', location='Theater B', phone=9876543210, hired=False, role_id=1)
        audition.call_back()
        self.assertTrue(audition.hired)

    def test_role_auditions(self):
        role = Role(character_name='King Lear')
        audition1 = Audition(actor='Actor 1', location='Theater C', phone=1112223333, hired=True, role_id=1)
        audition2 = Audition(actor='Actor 2', location='Theater D', phone=4445556666, hired=False, role_id=1)
        role.auditions = [audition1, audition2]
        self.assertEqual(role.auditions[0].actor, 'Actor 1')
        self.assertEqual(role.auditions[1].actor, 'Actor 2')

    def test_role_lead(self):
        role = Role(character_name='Julius Caesar')
        audition1 = Audition(actor='Actor 3', location='Theater E', phone=7778889999, hired=True, role_id=1)
        role.auditions = [audition1]
        self.assertEqual(role.lead().actor, 'Actor 3')

    def test_role_understudy(self):
        role = Role(character_name='Brutus')
        audition1 = Audition(actor='Actor 4', location='Theater F', phone=1011121314, hired=True, role_id=1)
        audition2 = Audition(actor='Actor 5', location='Theater G', phone=1516171819, hired=True, role_id=1)
        role.auditions = [audition1, audition2]
        self.assertEqual(role.understudy().actor, 'Actor 5')

if __name__ == '__main__':
    unittest.main()
