from unittest import TestCase

import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
