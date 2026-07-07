from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_experience_details(
    driver,
    years,
    students,
    focus_area,
    success_rate
):
    wait = WebDriverWait(driver, 10)

    # Years of experience dropdown
    driver.find_element(
        By.XPATH,
        "//button[@role='combobox']"
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//*[contains(text(),'{years}')]")
        )
    ).click()

    # Number of students
    driver.find_element(
        By.NAME,
        "number_of_students_recruited_annually"
    ).send_keys(students)

    # Focus area
    driver.find_element(
        By.NAME,
        "focus_area"
    ).send_keys(focus_area)

    # Success rate
    driver.find_element(
        By.NAME,
        "success_metrics"
    ).send_keys(success_rate)

    # Services Provided
    driver.find_element(
        By.XPATH,
        "//label[contains(.,'Career Counseling')]"
    ).click()

    driver.find_element(
        By.XPATH,
        "//label[contains(.,'Admission Applications')]"
    ).click()

    driver.find_element(
        By.XPATH,
        "//label[contains(.,'Visa Processing')]"
    ).click()

    driver.find_element(
        By.XPATH,
        "//label[contains(.,'Test Preparation')]"
    ).click()


def submit_experience(driver):
    driver.find_element(
        By.XPATH,
        "//button[contains(text(),'Next')]"
    ).click()