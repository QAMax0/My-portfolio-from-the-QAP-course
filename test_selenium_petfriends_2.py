import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Авторизация на сайте https://petfriends.skillfactory.ru/
@pytest.fixture(autouse=True)
def testing():
    driver = Service("Selenium_edukation/chromedriver/")
    pytest.driver = webdriver.Chrome(service=driver)
    # Переходим на страницу авторизации
    pytest.driver.get('https://petfriends.skillfactory.ru/login')

    # Вводим email
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))).send_keys(valid_email)

    # Вводим пароль
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'pass'))).send_keys(valid_password)

    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))).click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"


    yield

    pytest.driver.quit()

# Тест карточек всех питомцев сайта!
def test_show_all_pets_cards():
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
    pytest.driver.implicitly_wait(10)
    for i in range(len(names)):                      # У питомца есть:
        assert images[i].get_attribute('src') != ''  # фото, а не ''
        assert names[i].text != ''                   # имя, а не ''
        assert descriptions[i].text != ''            # описание, а не ''
        assert ', ' in descriptions[i].text          # запятая между видом и возрастом.
        parts = descriptions[i].text.split(", ")     # Разделяем вид и возраст по запятой
        assert len(parts[0]) > 0                     # Первая часть разделённой строки > 0
        assert len(parts[1]) > 0                     # Вторая часть разделённой строки > 0

# Написать тест, который проверяет, что на странице со списком питомцев пользователя:
# 1) Присутствуют все питомцы.
# 2) Хотя бы у половины питомцев есть фото.
# 3) У всех питомцев есть имя, возраст и порода.
# 4) У всех питомцев разные имена.
# 5) В списке нет повторяющихся питомцев. (Сложное задание).
def test_show_my_pets():

    # Нажимаем на кнопку "Мои питомцы"
    WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link'))).click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "Maksimus80"

    statistics_pets_total = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div/div[1]")))
    # Текст вытащили весь из статистики пользователя и теперь достаём нужный элемент - количество питомцев.
    statistics_pets_total = statistics_pets_total.text.split('\n')
    statistics_pets_total = statistics_pets_total[1].split(':')
    statistics_count_my_pets = int(statistics_pets_total[1])

    quantity_real_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, "#all_my_pets > table > tbody > tr")
    # Кладём в переменную количество реальных питомцев пользователя (количество строк).
    count_real_my_pets = len(quantity_real_my_pets)

    """ 1) Присутствуют ли все питомцы? Сравниваем количество питомцев из статистики 
    с реальным количеством строк питомцев."""
    assert statistics_count_my_pets == count_real_my_pets

    # Кладём в переменную всех питомцев с тегом img
    my_pets_images = pytest.driver.find_elements(By.CSS_SELECTOR,
                                                 "#all_my_pets > table > tbody > tr > th > img")
    # Кладём в переменную счётчик количество питомцев с фото
    count_photo_my_pets = 0
    for i in range(len(my_pets_images)):
        if my_pets_images[i].get_attribute('src') != "":
            count_photo_my_pets += 1

    """ 2) Присутствует ли хотя бы у половины питомцев фотографии? 
    Количество питомцев с фото >= общее количество питомцев / 2"""

    assert count_photo_my_pets >= count_real_my_pets / 2

    names_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR,
                                                "#all_my_pets > table > tbody > tr > td:nth-child(2)")
    breed_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR,
                                                '#all_my_pets > table > tbody > tr > td:nth-child(3)')
    age_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR,
                                              "#all_my_pets > table > tbody > tr > td:nth-child(4)")

    names_my_pets_real = []
    breed_my_pets_real = []
    age_my_pets_real = []
    for i in range(count_real_my_pets):
        """ 3) У всех питомцев есть имя, порода и возраст?"""
        assert names_my_pets[i].text != ''  # нет пустых имён в столбце "Имя"
        assert breed_my_pets[i].text != ''  # нет пустых строк в столбце "Порода"
        assert age_my_pets[i].text != ''  # нет пустой строки в столбце "Возраст"
        names_my_pets_real.append(names_my_pets[i].text)  # добавляем в список все имена питомцев
        breed_my_pets_real.append(breed_my_pets[i].text)  # добавляем в список все породы питомцев
        age_my_pets_real.append(age_my_pets[i].text)  # добавляем в список все возраста питомцев


    """4) У всех питомцев разные имена?"""

    # сравниваем количества уникальных имён (set!) c общим их количеством.
    # Если != значения, значит есть однаковые имена у каких то питомцев
    assert len(set(names_my_pets_real)) == len(names_my_pets_real)

    """ 5) В списке нет повторяющихся питомцев. 
    Повторяющиеся питомцы — это питомцы, у которых одинаковое имя, порода и возраст"""

    # Формируем общий список питомцев с их значениями. Индекс в списке это значения каждого питомца
    # (имя, порода, возраст) в виде кортежа для сравнения ниже!

    new_list_my_pets = list(map(tuple, zip(names_my_pets_real, breed_my_pets_real, age_my_pets_real)))

    # Сравниваем количество питомцев с уникальными значениями
    # (индекс списка - (имя, порода, возраст) питомца)
    # и количество питомцев со своими значениями (могут быть питомцы с одинаковыми значениями)
    # Если тест не проходит, значит есть повторяющиеся питомцы!
    assert len(set(new_list_my_pets)) == len(new_list_my_pets)
