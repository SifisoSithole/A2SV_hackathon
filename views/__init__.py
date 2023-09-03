from flask import Blueprint

auth_views = Blueprint("auth_views", __name__)
chatgpt_views = Blueprint("chatgpt_views", __name__)
pest_detection_views = Blueprint("pest_detection_views", __name__)

from views.auth import *
from views.chatgpt import *
from views.pestdetection import *