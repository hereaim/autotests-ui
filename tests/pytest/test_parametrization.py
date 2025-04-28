import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number", [1, 2, 3, -1])
# Название "number" в декораторе "parametrize" и в аргументах автотеста должны совпадать
def  test_numbers(number: int):
    assert number > 0
    

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected
    
@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("browser", ["chromium", "webkit", "firefox"])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0

@pytest.fixture(params=["chromium", "webkit", "firefox"])
# Фикстура будет возвращать три разных браузера
def browser(request: SubRequest) -> str:
    return request.param

# В самом автотесте уже не нужно добавлять параметризацию, он будет автоматически параметризован из фикстуры
def test_open_browser(browser: str):
    print(f"Running test on browser: {browser}")

# Для тестовых классов параметризация указывается для самого класса    
@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    # Параметр "user" передается в качестве аргумента в каждый тестовый метод класса
    @pytest.mark.parametrize("account", ["Creadit card", "Debit card"])
    def test_user_with_operations(self, user: str, account: str):
        print(f"User with operations: {user}")
    
    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")

users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}

@pytest.mark.parametrize("phone_number", users.keys(),
                         ids=lambda phone_number: f"{phone_number} - {users[phone_number]}")
# Параметризация с использованием словаря и функции "ids" для создания идентификаторов
def test_identifiers(phone_number: str):
    pass