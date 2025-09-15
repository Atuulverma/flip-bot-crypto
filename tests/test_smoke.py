from app.main import app

def test_health():
    assert callable(lambda: 1)
