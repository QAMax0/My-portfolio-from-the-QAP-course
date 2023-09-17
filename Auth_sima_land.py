from playwright.sync_api import sync_playwright, Playwright

# Запуск браузера
p: Playwright
with sync_playwright() as p:
    browser = p.chromium.launch()

    # Создание новой страницы
    page = browser.new_page()

    # Перейти на главную страницу www.sima-land.ru
    page.goto('https://www.sima-land.ru')

    # Нажать на кнопку "Войти" в хедере
    page.click('//*[@id="page-header"]/div/div[2]/div/div[2]/nav/div[2]')

    # Ввести логин
    page.type('//*[@id="entry-forms"]/div/div/div[2]/div[4]/div/div/div/form/div[1]/div/div/div/div/div/input',
              'qa_test@test.ru')

    # Ввести пароль
    page.type('//*[@id="entry-forms"]/div/div/div[2]/div[4]/div/div/div/form/div[2]/div[1]/div/div[1]/div/div/input',
              'qa_test')

    # Нажать кнопку "Войти"
    page.click('//*[@id="entry-forms"]/div/div/div[2]/div[4]/div/div/div/form/div[4]/button')

    # Нажать на чек-бокс капчи
    # page.click('//*[@id="recaptcha-anchor-label"]')

    # Нажать кнопку "Войти"
    # page.click('//*[@id="entry-forms"]/div/div/div[2]/div[4]/div/div/div/form/div[4]/button')

    try:
        page.wait_for_selector('// *[ @ id = "entry-forms"] / div / div / div[2] / div[4] /'
                               ' div / div / div / form / div[2] / div[1] / div[2]', timeout=5000)
        print("Авторизация прошла успешно")
    except:
        print("Авторизация не удалась: неправильный email, телефон или пароль")

    # Закрыть браузер
    browser.close()
