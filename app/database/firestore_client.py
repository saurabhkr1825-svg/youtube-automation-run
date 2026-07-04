import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from app.config import SERVICE_ACCOUNT_FILE


class FirestoreClient:

    def __init__(self):

        if not firebase_admin._apps:
            cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
            firebase_admin.initialize_app(cred)

        self.db = firestore.client()