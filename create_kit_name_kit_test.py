import sender_stand_request
import data

def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_new_user(user_body)
    return response.json()["authToken"]
def get_kit_body(name):
    resp_kit = data.kit_body.copy()
    # изменение значения в поле name
    resp_kit["name"] = name
    #assert resp_kit.json()["name"] == data.kit_body["name"]
    return resp_kit
def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]
def negative_assert_code_400(kit_name):
    kit_body = get_kit_body(kit_name)
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"

def negative_assert_without_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

#Тест проверяет минимально допустимое количество символов для поля name набора продуктов
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("а")

#Тест проверяет максимально допустимое количество символов для поля name набора продуктов
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda/"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
                    "cdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda/"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Негативный тест проверяет ответ при отсутствии символов для поля name набора продуктов
def test_create_kit_without_letter_in_name_get_success_response():
    #В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body("")
    #Проверка полученного ответа
    negative_assert_code_400(kit_body)

#Негативный тест проверяет ответ при превышении максимально допустимого кол-ва символов для поля name набора продуктов
def test_create_kit_512_letter_in_name_get_success_response():
    kit_body = get_kit_body("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda/"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
                    "cdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab/"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd/"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda/"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabCa")
    negative_assert_code_400(kit_body)

#Тест проверяет принятие английских букв для поля name набора продуктов
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

#Тест проверяет принятие русских букв для поля name набора продуктов
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

#Тест проверяет принятие спецсимволов для поля name набора продуктов
def test_create_kit_symbols_letter_in_name_get_success_response():
    positive_assert("\"№%@\",")

#Тест проверяет принятие пробелов для поля name набора продуктов
def test_create_kit_space_in_name_get_success_response():
    positive_assert("Человек и КО")

#Тест проверяет принятие цифр для поля name набора продуктов
def test_create_kit_number_in_name_get_success_response():
    positive_assert("123")

#Негативный тест проверяет отсутствие значения для поля name набора продуктов
def test_create_kit_empty_in_name_get_success_response():
    #Копируется словарь с телом запроса из файла data в переменную kit_body
    kit_body = data.kit_body.copy()
    #Удаление параметра name из запроса
    kit_body.pop("name")
    #Проверка полученного ответа
    negative_assert_without_name(kit_body)

#Негативный тест проверяет непринятие другого типа параметра для поля name набора продуктов
def test_create_kit_other_type_in_name_get_success_response():
    #В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(123)
    #Проверка полученного ответа
    negative_assert_code_400(kit_body)
    #negative_assert_code_400(123)