import geopy.distance
from const import MapCoordinateTable, getRad
import pygsheets
import sqlite3 as sq
import datetime

current_time = datetime.datetime.now()
timestamp = current_time.timestamp()

# --------------UPDATE-------------- #
# ПОЛУЧАЕМ НОВЫЕ ДАННЫЕ GOOGLE (lat lng vel)
#
gc = pygsheets.authorize(service_file='secret.json')
sh = gc.open_by_key('1xnkJuqTwRnKZRYtNPxeJ4BkbPEN_a3zFqv9RkXZtodM')
wks = sh.worksheet_by_title('Table')

length = 82
load = wks.get_values('A2', 'I83'.format(length))
tsm_load = wks.get_values('AJ2', 'AJ83'.format(length))

lat = []
lng = []
vel = []
chat_id = []
phone = []
uid = []
car_driver = []
car_driver_short = []
car_num = []
in_zoneList = []
tsm = []
y_url = []
y_parsed = []
y_sent = []

for i in range(0, length):
    lat.append(load[i][6])
    lng.append(load[i][7])
    vel.append(load[i][8])
    chat_id.append(load[i][0])
    phone.append(load[i][1])
    uid.append(load[i][2])
    car_driver.append(load[i][4])
    car_driver_short.append(load[i][5])
    car_num.append(load[i][3])
    tsm.append(tsm_load[i][0])

# ПОЛУЧАЕМ СТАРЫЕ ДАННЫЕ ИЗ DB (lat_old, lng_old, was_in_zone)
#
base = sq.connect('db.sqlite3')
# base = sq.connect('log.db')
cur = base.cursor()
if base:
    print('Data base connected OK!')
cur.execute("SELECT lat,lng FROM first_driver")
lat_lng_old = cur.fetchall()
cur.execute("SELECT in_zoneList FROM first_driver")
was_in_zonelist_load = cur.fetchall()
cur.execute("SELECT airport_msg FROM first_driver")
airport_msg_load = cur.fetchall()
cur.execute("SELECT airport_msg_time FROM first_driver")
airport_msg_time_load = cur.fetchall()
cur.execute("SELECT y_url FROM first_driver")
y_url_load = cur.fetchall()
cur.execute("SELECT y_parsed FROM first_driver")
y_parsed_load = cur.fetchall()
cur.execute("SELECT y_sent FROM first_driver")
y_sent_load = cur.fetchall()

airport_msg = [''] * length
airport_msg_time = [''] * length
was_in_zonelist = [''] * length
y_url = [''] * length
y_parsed = [''] * length
y_sent = [''] * length

for i in range(0, length):
    airport_msg[i] = airport_msg_load[i][0]
    airport_msg_time[i] = airport_msg_time_load[i][0]
    was_in_zonelist[i] = was_in_zonelist_load[i][0]
    y_url[i] = y_url_load[i][0]
    y_parsed[i] = y_parsed_load[i][0]
    y_sent[i] = y_sent_load[i][0]

car_num_short = []
for num in car_num:
    car_num_short.append(num[1:4])


# IF NO TASK ------------------------------------
# СМОТРИМ, ТЕПЕРЬ В ЗОНЕ ИЛИ НЕТ
#
zoneList = ['в пути'] * length
in_zoneList = [0] * length

for i in range(0, length):
    for x in MapCoordinateTable:
        if geopy.distance.geodesic((float(lat[i].replace(",", ".")), float(lng[i].replace(",", "."))),
                                   (MapCoordinateTable[x])).km < getRad(x):
            zoneList[i] = x
            in_zoneList[i] = 1
            break

for i in range(0, length):
    if (in_zoneList[i]) == 1 and (was_in_zonelist[i]) == 0:
        print('-')
        airport_msg[i] = f'Прибыл на {zoneList[i]}'
        airport_msg_time[i] = current_time
    elif (in_zoneList[i]) == 0 and (was_in_zonelist[i]) == 1:
        print('--')
        airport_msg[i] = f'Уехал из {zoneList[i]}'
        airport_msg_time[i] = current_time
# IF NO TASK ------------------------------------


# airport_msg = ['']*82
# airport_msg_time = ['']*82
# was_in_zonelist = ['']*82
# y_url = ['']*82
# y_parsed = ['']*82
# y_sent = ['']*82


# -------ЗАГРУЖАЕМ В BD--------#
#
if len(lat_lng_old) == 0:
    lat_lng_old = [[None for y in range(2)] for x in range(82)]
all = []
for i in range(0, length):
    all.append([chat_id[i], phone[i], uid[i], car_num[i], car_num_short[i], tsm[i], car_driver[i], car_driver_short[i],
                float(lat[i].replace(",", ".")), float(lng[i].replace(",", ".")), vel[i],
                lat_lng_old[i][0], lat_lng_old[i][1], zoneList[i], in_zoneList[i],
                airport_msg[i], airport_msg_time[i],
                y_url[i], y_parsed[i], y_sent[i]])

base.execute('DROP TABLE IF EXISTS first_driver')
base.commit()
base.execute('CREATE TABLE IF NOT EXISTS first_driver(chat,phone,uid PRIMARY KEY,car_num,car_num_short,tsm,'
             'car_driver,car_driver_short,lat,lng,vel,lat_old,lng_old,zone,in_zoneList,airport_msg,airport_msg_time,'
             'y_url,y_parsed,y_sent)')
base.commit()
cur.executemany('INSERT INTO first_driver VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (all))
base.commit()


print('done')