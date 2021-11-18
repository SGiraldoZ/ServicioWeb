from flask import Blueprint, request
from ..service.ownerService import *

owner_controller = Blueprint("owner", __name__)

@owner_controller.route("/owners.json", methods = ['POST','GET'])
def getOwners():
    return get_all_owners()