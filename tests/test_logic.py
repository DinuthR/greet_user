from app import logic

def test_greet_user_under_18(monkeypatch) -> str:
    inputs = iter(["Dinuth", "16"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = logic.greet_user()
    assert "not allowed"in result

def test_greet_user_adult(monkeypatch) -> str:
    inputs = iter(["Dinuth", "20"])
    monkeypatch.setattr("builtins.input",lambda _: next(inputs))
    result = logic.greet_user()
    assert "Welcome" in result



