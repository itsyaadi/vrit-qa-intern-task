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

from verification import (
    fill_verification,
    submit_verification,
)

from test_data import *


def test_registration(driver):
    # STEP 1 - Open Website
    open_home(driver)

    # STEP 2 - Click Get Started
    click_get_started(driver)

    # STEP 3 - Accept Terms
    accept_terms_and_continue(driver)

    # STEP 4 - Fill Account Details
    fill_signup_form(
        driver=driver,
        first_name=FIRST_NAME,
        last_name=LAST_NAME,
        email=EMAIL,
        phone=PHONE,
        password=PASSWORD,
    )

    # STEP 5 - Submit Account Details
    submit_form(driver)

    # STEP 6 - Manual OTP
    wait_for_otp_verification(driver)
    print(" Step 1 completed successfully.")

    # STEP 7 - Agency Details
    fill_agency_details(
        driver=driver,
        agency_name=AGENCY_NAME,
        role=ROLE,
        agency_email=AGENCY_EMAIL,
        website=WEBSITE,
        address=ADDRESS,
        region=REGION,
    )

    submit_agency(driver)
    print(" Step 2 completed successfully.")

    # STEP 8 - Professional Experience
    fill_experience_details(
        driver=driver,
        years=YEARS,
        students=STUDENTS,
        focus_area=FOCUS_AREA,
        success_rate=SUCCESS_RATE,
    )

    submit_experience(driver)
    print(" Step 3 completed successfully.")

    # STEP 9 - Verification
    fill_verification(
        driver=driver,
        registration_number=REGISTRATION_NUMBER,
        preferred_countries=PREFERRED_COUNTRIES,
        institution_types=INSTITUTION_TYPES,
        certification=CERTIFICATION,
        document_path=DOCUMENT,
    )

    submit_verification(driver)

    print(" Registration automation completed successfully.")