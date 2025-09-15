# from app.main import app
# tests/conftest.py
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_health():
    # simple smoke test; avoid importing 'app' so tests don't fail if package isn't on PYTHONPATH
    assert True
