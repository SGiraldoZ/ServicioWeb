from ..DAO.OwnerDAO import *

def getOwnerId(owner):
    return get_owner_id(owner)

def getAllOwners():
    return {"Owners": get_all_owners()}