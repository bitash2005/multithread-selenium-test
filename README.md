# Multithreaded Selenium Concurrency Test

A Python-based test automation framework using Selenium WebDriver and Python's threading module to validate race condition scenarios and system response to concurrent user actions.

## Test Scenario
1. Thread 1 (Delete Thread): Logs into the target account on http://automationexercise.com and deletes the user account.
2. Thread 2 (Login Thread): Waits for the deletion completion signal using threading.Event() and attempts to log in using the same (now deleted) credentials.
3. Assertion: Verifies that the login attempt fails as expected and asserts the presence of the system error message: "Your email or password is incorrect!".

---

## Tech Stack
- Language: Python 3.x
- Automation Tool: Selenium WebDriver
- Design Pattern: Page Object Model (POM) structure (action.py for locators/methods, main.py for test runner)
- Concurrency & Synchronization: threading.Thread, threading.Event

---

## Important Note Before Running

Since Thread 1 permanently deletes the account during execution, you must either:
1. Create a fresh test user on http://automationexercise.com before each run, OR
2. Update the credentials inside action.py to match an existing test account:

```python
# In action.py
enter_mail.send_keys("YOUR_REGISTERED_EMAIL")
enter_pass.send_keys("YOUR_PASSWORD")

how to run 
pip install -r requirements.txt

run
 python main.py

