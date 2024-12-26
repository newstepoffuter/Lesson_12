from data import resources
from selene import browser, by, have, be


class PracticeFormPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.element('#genterWrapper')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.month_of_birth = browser.element('.react-datepicker__month-select')
        self.year_of_birth = browser.element('.react-datepicker__year-select')
        self.day_of_birth = browser.element('.react-datepicker__day--020')
        self.user_number = browser.element('#userNumber')
        self.address = browser.element('#currentAddress')
        self.subject = browser.element("#subjectsInput")
        self.picture = browser.element('#uploadPicture')

    def open(self):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def submit_first_name(self, value):
        self.first_name.should(be.visible).type(value)

    def submit_last_name(self, value):
        self.last_name.should(be.visible).type(value)

    def submit_email(self, value):
        self.email.type(value)

    def submit_gender(self, value):
        self.gender.element(by.text(value)).click()

    def submit_user_number(self, value):
        self.user_number.type(value)

    def submit_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element("[class='react-datepicker__year-select']").click().element(by.text(f"{year}")).click()
        browser.element("[class='react-datepicker__month-select']").click().element(by.text(f"{month}")).click()
        browser.element(by.text(f"{day}")).click()

    def submit_subject(self, value):
        self.subject.type(value).press_enter()

    def submit_interest_music(self):
        browser.element(by.text("Music")).click()

    def upload_image(self, value):
        self.picture.set_value(resources.path(value))

    def submit_state(self, value):
        browser.element('#state').click()
        browser.element(by.text(value)).click()

    def submit_city(self, value):
        browser.element('#city').click()
        browser.element(by.text(value)).click()

    def submit_address(self, value):
        self.address.type(value)

    def submit_button(self):
        browser.element('#submit').should(be.visible).click()

    def check_new_user(self, full_name, email, gender, user_number, birthdate, subjects, hobby, file,
                       address, location):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                user_number,
                birthdate,
                subjects,
                hobby,
                file,
                address,
                location,
            )
        )
