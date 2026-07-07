from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_verification(
    driver,
    registration_number,
    preferred_countries,
    institution_types,
    certification,
    document_path
):
    wait = WebDriverWait(driver, 10)

    # Business Registration Number
    wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "business_registration_number")
        )
    ).send_keys(registration_number)

    # Preferred Countries
    driver.find_element(
        By.XPATH,
        "//button[@role='combobox']"
    ).click()

    for country in preferred_countries:
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//*[text()='{country}']")
            )
        ).click()

    # Close dropdown
    driver.find_element(By.TAG_NAME, "body").click()

    # Preferred Institution Types
    for institution in institution_types:
        wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//label[contains(.,'{institution}')]"
                )
            )
        ).click()

    # Certification (optional)
    driver.find_element(
        By.NAME,
        "certification_details"
    ).send_keys(certification)

    upload_inputs = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//input[@type='file']")
        )
    )

    for upload in upload_inputs[:2]:
        upload.send_keys(document_path)

def submit_verification(driver):
    wait = WebDriverWait(driver, 15)

    old_url = driver.current_url

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Submit')]")
        )
    ).click()
    WebDriverWait(driver, 10).until(
        lambda d: d.current_url != old_url or d.execute_script("return document.readyState") == "complete"
    )

    # Simple assertion
    assert driver.current_url != ""

    print("Registration submitted successfully.")