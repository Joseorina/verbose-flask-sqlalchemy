from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    """
    Generate JWT token

    Arguments:
        username {[type]} -- [description]
        password {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    """
    Authenticate an endpoint
    Arguments:
        payload {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
