from base_page.form_page import PracticeFormPage
import allure


@allure.title("Заполнение тренировочной формы DemoQA")
def test_practice_form(browser_settings):
    with allure.step("Открытие формы регистрации"):
        practice_form_page = PracticeFormPage()
        practice_form_page.open()

    with allure.step("Заполнение поля имя"):
        practice_form_page.submit_first_name("Alexandro")
        practice_form_page.submit_last_name("Gonzales")

    with allure.step("Заполнение поля email"):
        practice_form_page.submit_email("jopavmule@zhizni.net")

    with allure.step("Выбор пола"):
        practice_form_page.submit_gender("Male")

    with allure.step("Заполнение поля телефонный номер"):
        practice_form_page.submit_user_number("0987654321")

    with allure.step("Выбор даты рождения"):
        practice_form_page.submit_date_of_birth("2003", "April", "20")

    with allure.step("Выбор предметов"):
        practice_form_page.submit_subject("Computer Science")

    with allure.step("Выбор хобби"):
        practice_form_page.submit_interest_music()

    with allure.step("Загрузка изображения"):
        practice_form_page.upload_image("123.png")

    with allure.step("Заполнение полного адреса"):
        practice_form_page.submit_address("City Name, Street Name")
        practice_form_page.submit_state("Uttar Pradesh")
        practice_form_page.submit_city("Merrut")

    with allure.step("Отправка формы регистрации"):
        practice_form_page.submit_button()

    with allure.step("Сравнение отправленных и переданных значений"):
        practice_form_page.check_new_user(
            "Alexandro Gonzales",
            "jopavmule@zhizni.net",
            "Male",
            "0987654321",
            "20 April,2003",
            "Computer Science",
            "Music",
            "123.png",
            "City Name, Street Name",
            "Uttar Pradesh Merrut"
        )
