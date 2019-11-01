def parse_date_of_reception(text=''):
    """

    :param text: рядок,що ми отримуємо від користувача у форматі"число місяць рік", "1 вересня 2019"
    :return: int, "число", число від 1 до 12, "1"
    """
    month_number = 0
    month_list = ["січень","лютий", "березень", "квітень", "травень", "червень" ,"липень", "серпень", "вересень", "жовтень", "листопад", "грудень"]
    text = text.split(" ")
    for index in range(month_list):
        if month_list[index] in text:
            month_number = index + 1


    return month_number


if __name__=='__main__':

    parse_record_book('1 вересня 2019')