
# coding: utf8

import os
import json
import datetime
from PyQt4 import QtCore

DB_FILE_NAME = 'bbox_db.ini'


class MainBD(object):
    def __init__(self, db_file_name):
        self.db_file_name = db_file_name
        application_core = QtCore.QCoreApplication([])  # Detect current working directory
        self.file_path = application_core.applicationDirPath().replace('/', '\\')
        if os.path.isfile('%s\\%s' % (self.file_path, self.db_file_name)):
            with open('%s\\%s' % (self.file_path, self.db_file_name), 'r') as db_file:
                self.database = db_file.read().strip()
                self.database = json.loads(self.database)
        else:
            self.database = {'birthday_list': {'Example Name': {'date': '01.12.2016',
                                                                'gift': 'Example gift: house, car and brand new tree)',
                                                                'hide': False
                                                                }
                                               },
                             'settings': {'days_left': 7,
                                          'remind_times': 24,
                                          'remind_every_min': 60,
                                          'minimized': False,
                                          'auto_start': False
                                          }
                             }
            with open('%s\\%s' % (self.file_path, self.db_file_name), 'w') as db_file:
                db_file.write(json.dumps(self.database))

    def get_section(self, section_name):
        try:
            return self.database[section_name]
        except KeyError:
            raise Exception('Incorrect section name!')  # To prevent DB corruption and catch bugs

    def store_section(self, section_name, data):
        if section_name not in self.database.keys():
            raise Exception('Incorrect section name!')  # To prevent DB corruption and catch bugs
        self.database[section_name] = data
        with open('%s\\%s' % (self.file_path, self.db_file_name), 'w') as db_file:
            db_file.write(json.dumps(self.database))


class BirthdayManager(object):  # For person DB interaction
    def __init__(self, database):
        self.database = database

    def get_person_list(self, sort_by='date'):
        birthday_list = self.database.get_section('birthday_list')

        if sort_by == 'date':
            sorted_names = sorted(birthday_list, key=lambda in_key: birthday_list[in_key]['date'])

        elif sort_by == 'name':
            sorted_names = sorted(birthday_list.keys())

        else:
            return None

        person_list = []
        for name in sorted_names:
            name_date_pair = []
            name_date_pair.append(name)
            name_date_pair.append(datetime.datetime.strptime(birthday_list[name]['date'], '%m.%d.%Y'))
            person_list.append(name_date_pair)
        return person_list

    def add_person(self, name, date, gift='No gift yet)'):
        birthday_list = self.database.get_section('birthday_list')
        birthday_list[name] = {'date': date.strftime('%m.%d.%Y'),
                               'gift': gift, 'hide': False
                               }
        self.database.store_section('birthday_list', birthday_list)

    def edit_person(self, oldname, newname=None, date=None, gift=None):
        birthday_list = self.database.get_section('birthday_list')
        if date is None:
            date = birthday_list[oldname]['date']
        else:
            date = date.strftime('%m.%d.%Y')

        if gift is None:
            gift = birthday_list[oldname]['gift']

        hide = birthday_list[oldname]['hide']

        if oldname == newname or newname is None:
            birthday_list[oldname] = {'date': date,
                                      'gift': gift,
                                      'hide': hide
                                      }
        else:
            del birthday_list[oldname]
            birthday_list[newname] = {'date': date,
                                      'gift': gift,
                                      'hide': hide
                                      }
        self.database.store_section('birthday_list', birthday_list)

    def get_person_details(self, name):
        birthday_list = self.database.get_section('birthday_list')
        return datetime.datetime.strptime(birthday_list[name]['date'], '%m.%d.%Y'), birthday_list[name]['gift']

    def is_hidden(self, name):
        birthday_list = self.database.get_section('birthday_list')
        return birthday_list[name]['hide']

    def set_hidden(self, name, hidden):
        if hidden is True or hidden is False:
            birthday_list = self.database.get_section('birthday_list')
            person = birthday_list[name]
            person['hide'] = hidden
            birthday_list[name] = person
            self.database.store_section('birthday_list', birthday_list)

    def check_hidden(self, days_limit=30):
        birthday_list = self.database.get_section('birthday_list')
        today_date = (datetime.datetime.now()+datetime.timedelta(1)).strftime('%m.%d')
        future_date = (datetime.datetime.now() + datetime.timedelta(days_limit)).strftime('%m.%d')
        for name in birthday_list:
            if today_date > future_date:
                if future_date < birthday_list[name]['date'][0:5] <= today_date:
                    birthday_list[name]['hide'] = False
            else:
                if birthday_list[name]['date'][0:5] > future_date or birthday_list[name]['date'][0:5] <= today_date:
                    birthday_list[name]['hide'] = False
        self.database.store_section('birthday_list', birthday_list)

    def remove_person(self, name):
        birthday_list = self.database.get_section('birthday_list')
        del birthday_list[name]
        self.database.store_section('birthday_list', birthday_list)

    def get_next_birthdays(self, days_limit=30, include_hidden=True):
        birthday_list = self.database.get_section('birthday_list')
        sorted_names = sorted(birthday_list, key=lambda in_key: birthday_list[in_key]['date'])
        if len(sorted_names) == 0:
            return []
        next_birthdays_names = []
        today_date = datetime.datetime.now().strftime('%m.%d')
        future_date = (datetime.datetime.now() + datetime.timedelta(days_limit)).strftime('%m.%d')
        counter = 0
        for name in sorted_names:
            if include_hidden or not birthday_list[name]['hide']:
                if today_date > future_date:
                    if today_date <= birthday_list[name]['date'][0:5] <= '12.31' or \
                                            '01.01' <= birthday_list[name]['date'][0:5] <= future_date:
                        next_birthdays_names.append(name)
                        counter += 1
                        if counter >= 25:
                            break
                else:
                    if today_date <= birthday_list[name]['date'][0:5] <= future_date:
                        next_birthdays_names.append(name)
                        counter += 1
                        if counter >= 25:
                            break
        return next_birthdays_names


class SettingsManager(object):  # Settings DB interaction
    def __init__(self, database):
        self.database = database

    def get_settings(self):
        return self.database.get_section('settings')

    def get_option(self, option):
        settings = self.database.get_section('settings')
        if option in settings.keys():
            return settings[option]
        else:
            return None

    def store_settings(self, settings):
        self.database.store_section('settings', settings)


if __name__ == '__main__':
    main_db = MainBD(DB_FILE_NAME)
    birthday_mgr = BirthdayManager(main_db)
    settings_mgr = SettingsManager(main_db)
