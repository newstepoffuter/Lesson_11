import allure
import os
from selene import have, by, be
from selene import browser


@allure.title("Успешно заполнение формы")
def test_registration_form(setup_browser):

    with allure.step("Открываем форму регистрации"):
        browser.open('/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    with allure.step("Заполняем форму"):
        browser.element('#firstName').should(be.blank).type('Alexandro')
        browser.element('#lastName').should(be.blank).type('Gonzales')
        browser.element('#userEmail').should(be.blank).type('Agonzales@gmal.com')
        browser.element('[for=gender-radio-1]').click()
        browser.element('[id=userNumber]').should(be.blank).type('1234567890')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text('April')).click()
        browser.element('.react-datepicker__year-select').click().element(by.text('2001')).click()
        browser.element('.react-datepicker__day--007').click()
        browser.element('#subjectsInput').type('Computer Science').press_enter()
        browser.element('#subjectsInput').type('Maths').press_enter()
        browser.element('[for=hobbies-checkbox-3]').click()
        browser.element('#uploadPicture').send_keys(os.path.abspath('../picture/123.png'))
        browser.element('#currentAddress').set('India')
        browser.element('#state').click().element(by.text('Uttar Pradesh')).click()
        browser.element('#city').click().element(by.text('Agra')).click()
        browser.element('#submit').click()

    with allure.step("Проверяем форму"):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.element("[class='table-responsive']").should(have.text('Alexandro Gonzales'))
        browser.element("[class='table-responsive']").should(have.text('Agonzales@gmal.com'))
        browser.element("[class='table-responsive']").should(have.text('1234567890'))
        browser.element("[class='table-responsive']").should(have.text('7 April,2001'))
        browser.element("[class='table-responsive']").should(have.text('Computer Science, Maths'))
        browser.element("[class='table-responsive']").should(have.text('Music'))
        browser.element("[class='table-responsive']").should(have.text('123.png'))
        browser.element("[class='table-responsive']").should(have.text('123'))
        browser.element("[class='table-responsive']").should(have.text('Uttar Pradesh Agra'))
