from flask import Blueprint

auth_views = Blueprint("auth_views", __name__)
from views.auth import *