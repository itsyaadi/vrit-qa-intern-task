from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_agency_details(
    driver,
    agency_name,
    role,
    agency_email,
    website,
    address,
    region
):
    wait = WebDriverWait(driver, 10)

    # Agency Name
    wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "agency_name")
        )
    ).send_keys(agency_name)

    # Role in Agency
    driver.find_element(
        By.NAME,
        "role_in_agency"
    ).send_keys(role)

    # Agency Email
    driver.find_element(
        By.NAME,
        "agency_email"
    ).send_keys(agency_email)

    # Website
    driver.find_element(
        By.NAME,
        "agency_website"
    ).send_keys(website)

    # Address
    driver.find_element(
        By.NAME,
        "agency_address"
    ).send_keys(address)

    # Region of Operation (Radix UI Combobox)
    region_dropdown = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@role='combobox']")
        )
    )
    region_dropdown.click()

    region_option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, f"//*[contains(text(), '{region}')]")
        )
    )
    region_option.click()


def submit_agency(driver):
    wait = WebDriverWait(driver, 10)

    next_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Next')]")
        )
    )

    next_button.click()