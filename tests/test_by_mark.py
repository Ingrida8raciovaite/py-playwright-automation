from pytest import mark

# ПЕРШИЙ СПОСІБ
# ми оптимізовуємо тести, які є файл test_tc.py, щоб їх було менше
# data - прописуємо усі значення, які ми хочемо протестувати
data = [('hello', 'world'),
        ('hello', ''),
        ('123', 'world')]


# 'name,description' - назви змінних, які ми будемо передавати
# data - змінна в, якій ми беремо ці дані
# ids - для кожної пари даних (тест кейсу) прописуємо назву тест кейсу
@mark.parametrize('name,description', data,
                  ids=['general test', 'test with no description', 'test with digits in name'])
def test_testcase(desktop_app_auth, name, description):
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(name, description)
    desktop_app_auth.navigate_to('Test Cases')
    assert desktop_app_auth.test_cases.check_test_exists(name)
    desktop_app_auth.test_cases.delete_test_by_name(name)


# ДРУГИЙ СПОСІБ
ddt = {
    'argnames': 'name,description',
    'argvalues': [('hello', 'world'),
                  ('hello', ''),
                  ('123', 'world')],
    'ids': ['general test', 'test with no description', 'test with digits in name']
}


@mark.parametrize(**ddt)
def test_testcase(desktop_app_auth, name, description):
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(name, description)
    desktop_app_auth.navigate_to('Test Cases')
    assert desktop_app_auth.test_cases.check_test_exists(name)
    desktop_app_auth.test_cases.delete_test_by_name(name)


def test_tc_does_not_exist(desktop_app_auth):
    desktop_app_auth.navigate_to('Test Cases')
    # query_selector не має власного timeout, якщо елемент знайдено за селектором, то він його поверне.
    # Якщо немає , то поверне null
    assert not desktop_app_auth.test_cases.check_test_exists('sdfsdsfgfsfdv')
