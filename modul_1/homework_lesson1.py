from datetime import date
import math as m

#Задание
#1. Создайте словарь email, содержащий следующие поля:
# "subject" (тема письма),
# "from" (адрес отправителя),
# "to" (адрес получателя), "body" (текст письма).
email = {
    "subject": "My Report",
    "from": "person1@company.com ",
    "to": " person2@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}


#2. Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD
# и запишите её в email["date"].
send_date = date.today()
email["date"] = send_date.isoformat()


#3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру
# и уберите пробелы по краям. Запишите обратно в email["from"] и email["to"].
email['from'] = email['from'].lower().strip()
email['to'] = email['to'].lower().strip()


#4. Извлеките логин и домен отправителя в две переменные login и domain.
pos_sim = email['from'].index('@')
login = email['from'][:pos_sim]
domain = email['from'][pos_sim+1:]


#5. Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
#Сохраните в новый ключ словаря: email["short_body"].
email["short_body"] = email["body"][:10] + '...'


#6. Списки доменов: создайте список личных доменов и список корпоративных доменов
person_domain = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
company_domain = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']


#7. Проверьте что в списке личных и корпоративных доменов нет пересечений:
# ни один домен не должен входить в оба списка одновременно.
is_peres = 0
for person in person_domain:
    for company in company_domain:
        if person == company:
            is_peres = 1
            print(f"Есть пересечение: {person}")
            break
if is_peres == 0:
    print("Пересечений нет")

#8. Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate, равную результату проверки вхождения домена отправителя в список корпоративных доменов.
is_corporate = email['from'] in company_domain


#9. Соберите «чистый» текст сообщения без табов и переводов строк: замените "\t" и "\n" на пробел.
#Сохраните в email["clean_body"].
email["clean_body"] =  " ".join(email["body"].split())


#10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
#Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}
email["sent_text"] = f'''Кому: {email['to']}, от {email['from']} Тема: {email['subject']}, дата {email["date"]} {email["clean_body"]}'''


#11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
#Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.
pages = m.ceil(len(email["sent_text"])/500)


#12. Проверьте пустоту темы и тела письма: создайте переменные is_subject_empty, is_body_empty в котором будет хранится что тема письма содержит данные.
if len(email['subject']) !=0:
    is_subject_empty = 1
if len(email["body"]) !=0:
    is_body_empty = 1


#13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
#Запишите в email["masked_from"].
email["masked_from"] = f'{login[:2]}***@{domain}'


#14. Удалите из списка личных доменов значения "list.ru" и "bk.ru".
person_domain.remove('list.ru')
person_domain.remove('bk.ru')
