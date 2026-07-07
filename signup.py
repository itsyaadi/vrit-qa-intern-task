from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_home(driver):
    driver.get("https://authorized-partner.vercel.app/")


def click_get_started(driver):
    get_started = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Get Started')]")
        )
    )
    get_started.click()


def accept_terms_and_continue(driver):
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "remember")
        )
    )
    checkbox.click()

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Continue')]")
        )
    )
    continue_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.NAME, "firstName")
        )
    )


def fill_signup_form(driver, first_name, last_name, email, phone, password):
    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.NAME, "firstName"))
    ).send_keys(first_name)

    driver.find_element(By.NAME, "lastName").send_keys(last_name)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "phoneNumber").send_keys(phone)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "confirmPassword").send_keys(password)


def submit_form(driver):
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Next')]")
        )
    )

    next_button.click()

    import time
    time.sleep(5)


def wait_for_otp_verification(driver):
    print("=" * 60)
    print("Waiting for manual OTP verification...")
    print("Please enter the OTP and click Verify Code.")
    print("=" * 60)

    WebDriverWait(driver, 300).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Agency Details')]")
        )
    )

    print("OTP verified successfully. Continuing automation...")