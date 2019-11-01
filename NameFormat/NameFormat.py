def name_format(name, surname, patronim) :
    """

       :param name: str, input from user, name, Олександр
            surname: str, input from user, surname, Малахатка
            patronim: str, input from user, patronim, Володимирович



       :return: str input from user, full_name, Малахатка О.В.



       """
    return (surname + ' ' + name[0]+ '.' + patronim[0]+'.')