"""
Helper functions to access and update the id and type
used in event tracking.
"""
from uuid import uuid4, UUID
from request_cache import get_cache


def get_user_action_id():
    """
    Retrieves the current user action id from the request
    cache.
    """
    return get_cache('grade_tracking').get('user_action_id', None)


def get_user_action_type():
    """
    Retrieves the current user action type from the request
    cache.
    """
    return get_cache('grade_tracking').get('user_action_type', None)


def create_new_user_action_id(explicit_id=None):
    """
    Generates a new UUID and stores it in the request cache
    as the user action id.
    If explicit_id is provided, sets the 
    """
    new_id = UUID(explicit_id) if explicit_id else uuid4()
    get_cache('grade_tracking')['user_action_id'] = new_id
    return new_id


def set_user_action_type(action_type):
    """
    Takes a string and stores it in the request cache
    as the user action type.
    """
    get_cache('grade_tracking')['user_action_type'] = action_type
