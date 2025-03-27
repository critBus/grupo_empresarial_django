from typing import Dict, List

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone




User = get_user_model()
ROL_NAME_ADMIN="admin"