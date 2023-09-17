"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
var test_1 = require("@playwright/test");
var chromium = require('playwright').chromium;
(0, test_1.test)("Тест авторизации на www.sima-land.ru", function (_a) {
    var page = _a.page, browser = _a.browser;
    return __awaiter(void 0, void 0, void 0, function () {
        var errorMessageBox, errorMessage;
        return __generator(this, function (_b) {
            switch (_b.label) {
                case 0: return [4 /*yield*/, chromium.launch()];
                case 1:
                    browser = _b.sent();
                    // Шаг 1: Перейти на главную www.sima-land.ru
                    return [4 /*yield*/, page.goto('https://www.sima-land.ru')];
                case 2:
                    // Шаг 1: Перейти на главную www.sima-land.ru
                    _b.sent();
                    // Шаг 2: В хедере нажать на кнопку "Войти"
                    return [4 /*yield*/, page.click('//*[@id="page-header"]/div/div[2]/div/div[2]/nav/div[2]')];
                case 3:
                    // Шаг 2: В хедере нажать на кнопку "Войти"
                    _b.sent();
                    // Шаг 3: Ввести логин: qa_test@test.ru
                    return [4 /*yield*/, page.fill('//*[@id="entry-forms"]/div/div/div[2]/div[4]/div/div/div/form/div[1]/div/div/div/div/div/input', 'qa_test@test.ru')];
                case 4:
                    // Шаг 3: Ввести логин: qa_test@test.ru
                    _b.sent();
                    // Шаг 4: Ввести пароль: qa_test
                    return [4 /*yield*/, page.fill('//*[@id="entry-forms"]/div/div/div[2]/div[4]/div/div/div/form/div[2]/div[1]/div/div[1]/div/div/input', 'qa_test')];
                case 5:
                    // Шаг 4: Ввести пароль: qa_test
                    _b.sent();
                    // Шаг 5: Нажать кнопку "Войти в форме"
                    return [4 /*yield*/, page.click('//*[@id="entry-forms"]/div/div/div[2]/div[4]/div/div/div/form/div[4]/button')];
                case 6:
                    // Шаг 5: Нажать кнопку "Войти в форме"
                    _b.sent();
                    // Шаг 6: Кликнуть по чекбоксу капчи
                    return [4 /*yield*/, page.click('//*[@id="recaptcha-anchor"]/div[1]')];
                case 7:
                    // Шаг 6: Кликнуть по чекбоксу капчи
                    _b.sent();
                    // Шаг 7: Нажать кнопку "Войти снова в форме"
                    return [4 /*yield*/, page.click('//*[@id="entry-forms"]/div/div/div[2]/div[4]/div/div/div/form/div[4]/button')];
                case 8:
                    // Шаг 7: Нажать кнопку "Войти снова в форме"
                    _b.sent();
                    return [4 /*yield*/, page.$('.errortext')];
                case 9:
                    errorMessageBox = _b.sent();
                    if (!errorMessageBox) return [3 /*break*/, 11];
                    return [4 /*yield*/, errorMessageBox.innerText()];
                case 10:
                    errorMessage = _b.sent();
                    if (errorMessage.includes('Неправильный email, телефон или пароль')) {
                        console.error('Авторизация не удалась. Сообщение об ошибке: ', errorMessage);
                    }
                    else {
                        console.error('Авторизация не удалась. Неизвестная ошибка: ', errorMessage);
                    }
                    return [3 /*break*/, 12];
                case 11:
                    console.log('Авторизация прошла успешно!');
                    _b.label = 12;
                case 12: return [4 /*yield*/, browser.close()];
                case 13:
                    _b.sent();
                    return [2 /*return*/];
            }
        });
    });
});
