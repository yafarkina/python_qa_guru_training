from datetime import date
import pprint

test_email = {
    "subject": "My Report",
    "from": "person1@company.com ",
    "to": " person2@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}

test_emails = [
    "user@gmail.com",
    "admin@company.ru",
    "test_123@service.net",
    "Example.User@domain.com",
    "default@study.com",
    " hello@corp.ru  ",
    "user@site.NET",
    "user@domain.coM",
    "user.name@domain.ru",
    "usergmail.com",
    "user@domain",
    "user@domain.org",
    "@mail.ru",
    "name@.com",
    "name@domain.comm",
    "",
    "   ",
]

##Часть A. Функции

def normalize_addresses(value: str) -> str:
    """
    Возвращает значение, в котором адрес приведен к нижнему регистру и очищен от пробелов по краям.
    """
    return value.lower().strip()


def add_short_body(email: dict) -> dict:
    """
    Возвращает email с новым ключом email["short_body"] —
    первые 10 символов тела письма + "...".
    """
    email["short_body"] = email["body"][:10] + '...'
    return email


def clean_body_text(body: str) -> str:
    """
    Заменяет табы и переводы строк на пробелы.
    """
    return " ".join(body.split())


def build_sent_text(email: dict) -> str:
    """
    Формирует текст письма в формате:

    Кому: {to}, от {from}
    Тема: {subject}, дата {date}
    {clean_body}
    """
    return f'Кому: {email['recipient']}, от {email['sender']} Тема: {email['subject']}, дата {email["date"]} {email["clean_body"]}'

def check_empty_fields(subject: str, body:str) -> tuple[bool, bool]:
    """
    Возвращает кортеж (is_subject_empty, is_body_empty).
    True, если поле пустое.
    """
    if len(subject.strip()) <=0:
        is_subject_empty = False
    else:
        is_subject_empty = True
    if len(body.strip()) <= 0:
        is_body_empty = False
    else:
        is_body_empty = True
    return is_subject_empty, is_body_empty


def extract_login_domain(address: str) -> tuple[str, str]:
    """
    Возвращает логин и домен отправителя.
    Пример: "user@mail.ru" -> ("user", "mail.ru")
    """
    address = normalize_addresses(address)
    pos_sim = address.index('@')
    login = address[:pos_sim]
    domain = address[pos_sim+1:]
    return login, domain


def mask_sender_email(login: str, domain: str) -> str:
    """
    Возвращает маску email: первые 2 символа логина + "***@" + домен.
    """
    return f'{login[:2]}***@{domain}'


def get_correct_email(email_list: list[str]) -> list[str]:
    """
    Возвращает список корректных email.
    """
    valid_list = []
    for item in email_list:
        if  '@' in item:
            if (item.endswith('.com') or item.endswith('.ru') or item.endswith('.net')):
                if len(item[:item.index('@')])>0:
                    valid_list.append(item)
    return valid_list


def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    """
    Создает словарь email с базовыми полями:
    'sender', 'recipient', 'subject', 'body'
    """
    email = {
        'sender' : sender,
        'recipient' : recipient,
        'subject' : subject,
        'body' : body
    }
    return email



def add_send_date(email: dict) -> dict:
    """
    Возвращает email с добавленным ключом email["date"] — текущая дата в формате YYYY-MM-DD.
    """
    send_date = date.today()
    email["date"] = send_date.isoformat()
    return email["date"]


#1. Нормализация email адресов - приводит адреса к нижнему регистру и убирает пробелы
test_email['from'] = normalize_addresses(test_email['from'])
test_email['to'] = normalize_addresses(test_email['to'])


#8. Создание словаря письма - создает базовую структуру письма
test_email = create_email(test_email['from'], test_email['to'], test_email['subject'], test_email['body'])

#2. Сокращенная версия тела письма - создает короткую версию тела (первые 10 символов + "...")
test_email["short_body"] = add_short_body(test_email)


#3. Очистка текста письма - заменяет табы и переводы строк на пробелы
test_email["clean_body"] = clean_body_text(test_email["body"])


#9. Добавление даты отправки - добавляет текущую дату
test_email["date"] = add_send_date(test_email)


#4. Формирование итогового текста письма - создает форматированный текст письма
test_email["sent_text"] = build_sent_text(test_email)


#5. Проверка пустоты темы и тела - проверяет, заполнены ли обязательные поля
is_subject_empty, is_body_empty = check_empty_fields(test_email['subject'], test_email["body"])


#6. Маска email отправителя - создает маскированную версию email (первые 2 символа + "***@" + домен)
test_email["masked_from"] = mask_sender_email(extract_login_domain(test_email['sender'])[0], extract_login_domain(test_email['sender'])[1])


#7. Проверка корректности email - проверяет наличие @ и допустимые домены (.com, .ru, .net)
(get_correct_email(test_emails))


#10. Получение логина и домена - разделяет email на логин и домен
login, domain = extract_login_domain(test_email['sender'])



## Часть B. Отправка письма

def sender_email(recipient_list: list[str],
                 subject: str,
                 message: str,
                 *,
                 sender="default@study.com") -> list[dict]:

    empty_list = []
#1. Проверить, что список получателей recipient_list не пустой
    if not recipient_list:
        return empty_list

#3. Проверить пустоту темы и тела письма через check_empty_fields(). Если одно из них пустое — вернуть пустой список.
    is_subject_empty, is_message_empty =  check_empty_fields(subject, message)
    if is_subject_empty == False or is_message_empty == False:
        return empty_list

#2. Проверить корректность email адресов отправителя и получателей через get_correct_email()
    correct_email_recipient = get_correct_email(recipient_list)
    correct_email_sender = get_correct_email([sender])

#4. Исключить отправку самому себе: пройти по каждому элементу recipient_list в цикле for, если адрес совпадает с sender, удалить его из списка.
    with_out_sender_recipient_list = list(filter(lambda x: x!=sender, correct_email_recipient))

#5. Нормализовать все текстовые данные subject и body → с помощью clean_body_text() recipient_list и sender → с помощью normalize_addresses()
    clean_subject = clean_body_text(subject)
    clean_message = clean_body_text(message)
    clean_recipient_list = list(map(normalize_addresses, with_out_sender_recipient_list))
    clean_sender = normalize_addresses(correct_email_sender[0])

#6. Создать письмо для каждого получателя функцией create_email().
    emails = []
    for item in clean_recipient_list:
        email = create_email(clean_sender, item, clean_subject, clean_message)
        email["clean_body"] = clean_message
        emails.append(email)

#7. Добавить дату отправки с помощью add_send_date().
    for email in emails:
        email["date"] = add_send_date(email)

#8. Замаскировать email отправителя с помощью extract_login_domain() и mask_sender_email().
    for email in emails:
        email["masked_from"] = mask_sender_email(extract_login_domain(email['sender'])[0], extract_login_domain(email['sender'])[1])

#9. Создать короткую версию тела письма. Сохранить короткую версию в email["short_body"].
    for email in emails:
        email["short_body"] = add_short_body(email)


#10. Сформировать итоговый текст письма функцией build_sent_text().
    result_responses =[]
    for email in emails:
        result_response = build_sent_text(email)
        result_responses.append(result_response)
    return result_responses


print(sender_email(
    recipient_list=[
        " user@gmail.com",
        "admin@company.ru",
        "test_123@service.net ",
        "Example.User@domain.com",
        "default@study.com",
        " hello@corp.ru  ",
        "user@site.NET",
        "user@domain.coM",
        "user.name@domain.ru",
        "usergmail.com",
        "user@domain",
        "user@domain.org",
        "@mail.ru",
        "name@.com",
        "name@domain.comm",
        "",
        "   ",
    ],
    subject="Hello!",
    message="Привет, коллега!",
    sender="default@study.com",
))










### Результат:
#Список с готовыми письмами, содержащими все обработанные данные. Вернуть итоговый список писем.
