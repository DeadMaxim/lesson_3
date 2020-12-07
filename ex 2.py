def user_data(name, surname, year, city, mail_address, phone_number):
    print(f'"Имя: " {name}, '
          f'"Фамилия: " {surname}, '
          f'"Год рождения: " {year}, '
          f'"Город проживания: " {city}, '
          f'"Адрес электронной почты: " '
          f'{mail_address}, "Номер телефона: '
          f'" {phone_number}')


user_data(name=input('Укажите имя: '),
          surname=input('Укажите фамилию: '),
          year=input('Укажите год рождения: '),
          city=input('Укажите город проживания: '),
          mail_address=input('Укажите адрес электронной почты: '),
          phone_number=input('Укажите номер телефона: '))
