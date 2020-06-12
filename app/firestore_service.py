import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


project_id='platzi-flask-279622'
cred = credentials.ApplicationDefault()
#cred = credentials.Certificate('platzi-flask-279622-715ec813a19f.json')
firebase_admin.initialize_app(cred)
#token = cred.get_access_token()
#default_app = firebase_admin.initialize_app(cred)
#default_app = firebase_admin.initialize_app(credential, {'projectID': project_id})

db = firestore.client()

def get_users():
    return db.collection('users').get()

def get_user(user_id):
    return db.collection('users').document(user_id).get()

def get_todos(user_id):
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()



def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password })
    
