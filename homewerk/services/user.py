from homewerk.services import Singleton
from homewerk import models as m
from homewerk import utils

class UserService(Singleton):
    def get_user(self):
        return 'test2'

    def create_user(self, data):
        user = m.User()
        user.name = data.get('name')
        m.db.session.add(user)
        m.db.session.commit()

        return user.name