# Playwright automation with python 
Test project to show:

- features of MS Playwright on Python
- automation project structure using pytest

Tools:
- Playwright
- Python
- PyCharm

## Install guide
1. Install python
2. Install PyCharm
3. Install python dependencies pip install -r requirements.txt
4. Make sure playwright version 1.8+ installed

## Project structure 
- conftest.py file contains main fixtures to work
- Page objects stored in page_object folder
- Tests stored in tests folder
- Settings are spread between:
  * pytest.ini
  * settings.py

## Run guide
[^1] Create file secure.json for logins and passwords. Structure:
```
  git status
  git add
  git commit
```
[^2] Install software to test [Test-Me](https://github.com/Ypurek/TestMe-TCM)
[^3] Set correct path to DB in pytest.ini file
[^4] Run Test-Me (check guide in it's repo)
[^5] Run tests using command `pytest`

## Useful links
https://playwright.dev/python/
https://github.com/microsoft/playwright-python


