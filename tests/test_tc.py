class TestMyClass:

    # повідомлення буде вивовдитися перед кожним тестом
    # def setup(self):
    #     print("start")

    def test_testcase(self, desktop_app_auth):
        test_name = 'hello'
        desktop_app_auth.navigate_to('Create new test')
        desktop_app_auth.create_test(test_name, 'world')
        desktop_app_auth.navigate_to('Test Cases')
        assert desktop_app_auth.test_cases.check_test_exists(test_name)
        desktop_app_auth.test_cases.delete_test_by_name(test_name)

    def test_testcase_no_description(self, desktop_app_auth):
        test_name = 'hello'
        desktop_app_auth.navigate_to('Create new test')
        desktop_app_auth.create_test(test_name, '')
        desktop_app_auth.navigate_to('Test Cases')
        assert desktop_app_auth.test_cases.check_test_exists(test_name)
        desktop_app_auth.test_cases.delete_test_by_name(test_name)

    def test_testcase_digits_name(self, desktop_app_auth):
        test_name = '123'
        desktop_app_auth.navigate_to('Create new test')
        desktop_app_auth.create_test(test_name, 'world')
        desktop_app_auth.navigate_to('Test Cases')
        assert desktop_app_auth.test_cases.check_test_exists(test_name)
        desktop_app_auth.test_cases.delete_test_by_name(test_name)

    # повідомлення буде виводитися вкінці кожного тесту
    # def teardown(self):
    #     print('Finish')
