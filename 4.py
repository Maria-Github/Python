from tkinter import Tk, Canvas
from datetime import datetime, date
def get_events(filename):
    date_list = []
    name_list = []
    with open(filename, encoding='utf-8') as file:
        for line in file:

            line = line.rstrip('\n')

            text = line.split(',')
            print(text[1])
            print(text[0])

            date = datetime.strptime(text[1], "%d/%m/%Y").date()
            name = text[0]
            date_list.append(date)
            name_list.append(name)


        return name_list, date_list

def which_weekday(z):
    name_of_day = ''
    day_type = ''
    if z < 5:
        day_type = 'будний день'
    else:
        day_type = 'выходной'
    if z == 0:
        name_of_day = 'понедельник'
    elif z == 1:
        name_of_day = 'вторник'
    elif name_of_day == 2:
        name_of_day = 'среда'
    elif z == 3:
        name_of_day = 'четверг'
    elif z == 4:
        name_of_day = 'пятница'
    elif z == 5:
        name_of_day = 'суббота'
    else:
        name_of_day = 'воскресенье'
    return day_type + ' ' + name_of_day
def days_till_deadline(now, deadline, name):
    if now > deadline:
        period = now - deadline

        message = 'Праздник {} уже прошел {} дней назад.\nЭто был {}.' \
            .format(name, period.days, which_weekday(date.weekday(deadline)))

    elif now.day == deadline.day and now.month == deadline.month and now.year == deadline.year:
        message = ("{} сегодня".format(name))
    else:
        period = deadline - now
        message = ('До праздника {} осталось {} дней.\nЭто будет {}.' \
                   .format(name, period.days, which_weekday(date.weekday(deadline))))
    return message

event_name_list, event_date_list = get_events('events.txt')
today = date.today()
event_date = event_date_list[1]
event_name = event_name_list[1]
print(days_till_deadline(today, event_date, event_name))
for i in range(len(event_name_list)):
    print(days_till_deadline(today, event_date_list[i], event_name_list[i]))
root = Tk()
canvas = Canvas(root, width=1200, height=800, bg='#F0F8FF')
canvas.pack()
canvas.create_text(550, 25, anchor='n', fill='#191970', font='Timesnewroman 20 bold',
                   text="Первое приложение. \nКалендарь ожидания.")
vertical_space = 100
for i in range(len(event_date_list)):
    display = days_till_deadline(today, event_date_list[i], event_name_list[i])
    canvas.create_text(550, vertical_space, anchor='n', fill='#696969', font='Arial 15 bold', text=display)
    vertical_space += 50
root.mainloop()
