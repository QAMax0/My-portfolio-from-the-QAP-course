import { test, expect } from "@playwright/test";
const { chromium } = require('playwright');


test("Тест авторизации на www.sima-land.ru", async ({ page, browser }) => {
  browser = await chromium.launch();
  // Шаг 1: Перейти на главную www.sima-land.ru
  await page.goto('https://www.sima-land.ru');

  // Шаг 2: В хедере нажать на кнопку "Войти"
  await page.click('//*[@id="page-header"]/div/div[2]/div/div[2]/nav/div[2]');

  // Шаг 3: Ввести логин: qa_test@test.ru
  await page.fill('//*[@id="entry-forms"]/div/div/div[2]/div[4]/div/div/div/form/div[1]/div/div/div/div/div/input', 'qa_test@test.ru');

  // Шаг 4: Ввести пароль: qa_test
  await page.fill('//*[@id="entry-forms"]/div/div/div[2]/div[4]/div/div/div/form/div[2]/div[1]/div/div[1]/div/div/input', 'qa_test');

  // Шаг 5: Нажать кнопку "Войти в форме"
  await page.click('//*[@id="entry-forms"]/div/div/div[2]/div[4]/div/div/div/form/div[4]/button');

  // Шаг 6: Кликнуть по чекбоксу капчи
  await page.click('//*[@id="recaptcha-anchor"]/div[1]');

  // Шаг 7: Нажать кнопку "Войти снова в форме"
  await page.click('//*[@id="entry-forms"]/div/div/div[2]/div[4]/div/div/div/form/div[4]/button');

  // Шаг 8: Проверить, что авторизация прошла успешно
  // Проверить наличие сообщения об ошибке
  const errorMessageBox = await page.$('.errortext');

  if (errorMessageBox) {
    const errorMessage = await errorMessageBox.innerText();
    if (errorMessage.includes('Неправильный email, телефон или пароль')) {
      console.error('Авторизация не удалась. Сообщение об ошибке: ', errorMessage);
    } else {
      console.error('Авторизация не удалась. Неизвестная ошибка: ', errorMessage);
    }
  } else {
    console.log('Авторизация прошла успешно!');
  }

  await browser.close();
});