from signup import (
    open_home,
    click_get_started,
    accept_terms_and_continue,
    fill_signup_form,
    submit_form,
    wait_for_otp_verification,
)

from agency import (
    fill_agency_details,
    submit_agency,
)

from experience import (
    fill_experience_details,
    submit_experience,
)

from test_data import *


def test_registration(driver):
    # STEP 1 - Open Website
    open_home(driver)

    # STEP 2 - Click Get Started
    click_get_started(driver)

    # STEP 3 - Accept Terms & Continue
    accept_terms_and_continue(driver)

    # STEP 4 - Fill Sign Up Form
    fill_signup_form(
        driver=driver,
        first_name=FIRST_NAME,
        last_name=LAST_NAME,
        email=EMAIL,
        phone=PHONE,
        password=PASSWORD,
    )

    # STEP 5 - Submit Sign Up
    submit_form(driver)

    # STEP 6 - Wait for Manual OTP Verification
    wait_for_otp_verification(driver)

    print("✅ Step 1 completed successfully.")

    # STEP 7 - Fill Agency Details
    fill_agency_details(
        driver=driver,
        agency_name=AGENCY_NAME,
        role=ROLE,
        agency_email=AGENCY_EMAIL,
        website=WEBSITE,
        address=ADDRESS,
        region=REGION,
    )

    # STEP 8 - Submit Agency Details
    submit_agency(driver)

    print("✅ Step 2 completed successfully.")
    print("➡️ Ready for Professional Experience automation.")

fill_experience_details(
    driver,
    YEARS,
    STUDENTS,
    FOCUS_AREA,
    SUCCESS_RATE,
)

submit_experience(driver)

print("Page 3 completed successfully.")