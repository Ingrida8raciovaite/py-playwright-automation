from pytest import mark

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
    assert not desktop_app_auth.test_cases.check_test_exists('sdfsdsfgfsfdv')


def test_delete_test_case(desktop_app_auth, get_web_service):
    test_name = 'test for delete'
    get_web_service.create_test(test_name, 'delete me pls')
    desktop_app_auth.navigate_to('Test Cases')
    assert desktop_app_auth.test_cases.check_test_exists(test_name)
    desktop_app_auth.test_cases.delete_test_by_name(test_name)
    assert not desktop_app_auth.test_cases.check_test_exists(test_name)


@mark.parametrize(**ddt)
def test_delete_test_case_via_db(desktop_app_auth, name, description, get_db):
    test = get_db.list_test_cases()
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(name, description)
    desktop_app_auth.navigate_to('Test Cases')
    assert desktop_app_auth.test_cases.check_test_exists(name)
    assert len(test) + 1 == len(get_db.list_test_cases())
    get_db.delete_test_case(name)
