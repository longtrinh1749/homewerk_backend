from homewerk.models import db
from homewerk import models as m
from homewerk.services.base import Singleton
from homewerk.constants import SAVED_TYPE

class SavedService(Singleton):
    def create_saved(self, data):
        saved = m.Saved()
        user_id = data.get('user_id')
        if user_id:
            saved.user_id = user_id

        type = data.get('type')
        if type and type in SAVED_TYPE:
            saved.type = type

        type_id = data.get('type_id')
        if type_id:
            saved.type_id = type_id

        if not (user_id and type and type_id):
            return
        else:
            old_saved = m.Saved.query.filter(m.Saved.type == type,
                                             m.Saved.type_id == type_id,
                                             m.Saved.user_id == user_id).first()
            if old_saved:
                return old_saved

        m.db.session.add(saved)
        m.db.session.commit()

        return saved

    def get_saved(self, data):
        query = m.Saved.query
        user_id = data.get('user_id')
        if user_id:
            query = query.filter(m.Saved.user_id == user_id)

        saved = query.all()
        return saved

    def delete_saved(self, data):
        user_id = data.get('user_id')
        type = data.get('type')
        type_id = data.get('type_id')
        m.Saved.query.filter(m.Saved.user_id == user_id,
                             m.Saved.type == type,
                             m.Saved.type_id == type_id).delete()

        return True

