import json


def test_dashboard_data(desktop_app_auth):
    # change to string
    payload = json.dumps({"total": 0, "passed": 0, "failed": 0, "norun": 0})
    desktop_app_auth.intercept_requests('**/getstat*', payload)
    desktop_app_auth.refresh_dashboard()
    print(payload)
    print(desktop_app_auth.get_total_tests_stats())
    desktop_app_auth.stop_intercept('**/getstat*')
    assert desktop_app_auth.get_total_tests_stats() == "0"


def test_multiple_roles(desktop_app_auth, desktop_app_bob, get_db):
    alice = desktop_app_auth
    bob = desktop_app_bob
    before = alice.get_total_tests_stats()
    bob.navigate_to('Create new test')
    bob.create_test('test by bob', 'test')
    alice.refresh_dashboard()
    after = alice.get_total_tests_stats()
    get_db.delete_test_case('test by bob')
    assert int(before) + 1 == int(after)
