import re


def return_final_date(final_date):
    """

    :param final_date: дата до якої діисний студентський квиток в форматі : дата(число) місяць(слово) рік(число і
    'р.') :return: дата до якої діисний студентський квиток в форматі : дата(число)/місяць(слово)/дві останні цифри
    року(число)
    """

    print(final_date[:2]+"/червня/"+final_date[-4:-2])
    return None


if __name__ == "__main__":
    return_final_date("30 червня 2023р.")
