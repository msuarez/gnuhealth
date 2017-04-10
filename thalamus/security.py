from flask_httpauth import HTTPBasicAuth
import thalamus
import bcrypt

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    """
    Takes the username and password from the client
    and checks them against the entry on the people db collection
    The password is bcrypt hashed
    """ 
    user = thalamus.mongo.db.people.find_one({'_id' : username})
    if (user):
        account = thalamus.mongo.db.people.find_one({'_id' : username})
        person = account['_id']
        hashed_password = account['password']
        if bcrypt.checkpw(password.encode('utf-8'), 
            hashed_password.encode('utf-8')):
            return True
        else:
            return False
        
    else:
       return False

