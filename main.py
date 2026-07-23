import os
import threading
import time
import traceback
from action import action
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

c_directory = os.path.dirname(os.path.abspath(__file__))
local_driver_path = os.path.join(c_directory, "chromedriver.exe")


account_deleted_event = threading.Event()


def thread_1_delete():
    service = Service(executable_path=local_driver_path)
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("http://automationexercise.com")
        driver.maximize_window()
        do = action(driver)

        print("[Thread 1]  login ..")
        do.delete()
        print("[Thread 1] account deleted ")

    except Exception:
        print("[Thread 1] error .")
        traceback.print_exc()
    finally:
        
        account_deleted_event.set()
        time.sleep(2)
        driver.quit()


def thread_2_login_attempt():
    service = Service(executable_path=local_driver_path)
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("http://automationexercise.com")
        driver.maximize_window()
        do = action(driver)

        print("[Thread 2] wating fo thread 1..")
        
        account_deleted_event.wait()

        print("[Thread 2] try to login with deleted account..")
        do.login()

        
        do.verify_login_failed()
        print(" test pass")

    except AssertionError as ae:
        print(f"[Thread 2] ❌ Test FAILED (Assertion Error): {ae}")
    except Exception:
        print("[Thread 2] ❌ Error occurred during login process:")
        traceback.print_exc()
    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    t1 = threading.Thread(target=thread_1_delete, name="DeleteThread")
    t2 = threading.Thread(target=thread_2_login_attempt, name="LoginThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("done")