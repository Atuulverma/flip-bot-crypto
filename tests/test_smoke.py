from app.main import app

def test_health():
    assert app is not None
