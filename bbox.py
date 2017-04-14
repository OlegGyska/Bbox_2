
# coding: utf
import sys
import datetime
import bbox_db
import bbox_ui
import bbox_wreg
import calendar
from Queue import Queue
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QAbstractListModel, Qt, QThread
from PyQt4.QtGui import QMainWindow

DB_FILE_NAME = 'bbox_db.ini'
WINDOW_ICON = '\\resources\\icons\\window.png'
TRAY_ICON = '\\resources\\icons\\tray.png'

try:  # Code by QtDesigner
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s

try:  # Code by QtDesigner
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class MainWindow(QMainWindow):  # Part of the code by QtDesigner
    def __init__(self, database, window_icon, tray_icon, parent=None):
        super(MainWindow, self).__init__(parent)
        self.database = database
        self.birthday_manager = bbox_db.BirthdayManager(self.database)
        self.settings_manager = bbox_db.SettingsManager(self.database)
        self.tray_icon_file = self.database.file_path + tray_icon
        self.window_icon_file = self.database.file_path + window_icon
        self.setObjectName(_fromUtf8("MainWindow"))
        self.window_icon = QtGui.QIcon(self.window_icon_file)
        self.setWindowIcon(self.window_icon)
        self.setFixedHeight(470)
        self.setFixedWidth(505)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setWindowTitle(_fromUtf8("Birthday box"))
        self.setTabShape(QtGui.QTabWidget.Triangular)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 505, 406))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(200, 340, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listView = QtGui.QListView(self.tab)
        self.listView.setGeometry(QtCore.QRect(0, 35, 501, 150))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 200, 500, 120))
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setMargin(3)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 117, 17))
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.listView_2 = QtGui.QListView(self.tab_2)
        self.listView_2.setGeometry(QtCore.QRect(0, 35, 500, 292))
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 340, 98, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 340, 98, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(393, 340, 98, 27))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 12, 84, 17))
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.radioButton = QtGui.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(325, 12, 62, 22))
        self.radioButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.tab_2)
        self.radioButton_2.setGeometry(QtCore.QRect(392, 12, 72, 22))
        self.radioButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(261, 13, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(383, 340, 107, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_3)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 340, 98, 27))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.spinBox = QtGui.QSpinBox(self.tab_3)
        self.spinBox.setGeometry(QtCore.QRect(30, 90, 60, 27))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(99)
        self.spinBox_2 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_2.setGeometry(QtCore.QRect(30, 140, 60, 27))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(99)
        self.checkBox = QtGui.QCheckBox(self.tab_3)
        self.checkBox.setGeometry(QtCore.QRect(30, 200, 103, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 250, 134, 22))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 343, 151, 22))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(100, 145, 134, 17))
        self.label_5.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(100, 95, 172, 17))
        self.label_6.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.spinBox_3 = QtGui.QSpinBox(self.tab_3)
        self.spinBox_3.setGeometry(QtCore.QRect(30, 40, 60, 27))
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(60)
        self.label_7 = QtGui.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(100, 45, 208, 17))
        self.label_7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(419, 10, 71, 27))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(393, 10, 100, 27))
        self.radioButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        self.pushButton.setText(_translate("MainWindow", "Edit gift", None))
        self.label.setText(_translate("MainWindow", "Select event to see details", None))
        self.label_2.setText(_translate("MainWindow", "Upcoming events", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Home", None))
        self.pushButton_4.setText(_translate("MainWindow", "Add person", None))
        self.pushButton_5.setText(_translate("MainWindow", "Edit", None))
        self.pushButton_6.setText(_translate("MainWindow", "Remove", None))
        self.label_3.setText(_translate("MainWindow", "Birthday list", None))
        self.radioButton.setText(_translate("MainWindow", "date", None))
        self.radioButton_2.setText(_translate("MainWindow", "name", None))
        self.label_4.setText(_translate("MainWindow", "Sort by:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Birhtday list", None))
        self.pushButton_3.setText(_translate("MainWindow", "Apply settings", None))
        self.pushButton_7.setText(_translate("MainWindow", "Reset", None))
        self.checkBox.setText(_translate("MainWindow", "Auto start", None))
        self.checkBox_2.setText(_translate("MainWindow", "Start minimized", None))
        self.checkBox_3.setText(_translate("MainWindow", "Hide notifications", None))
        self.label_5.setText(_translate("MainWindow", "Remind every, min.", None))
        self.label_6.setText(_translate("MainWindow", "Remind times a day limit", None))
        self.label_7.setText(_translate("MainWindow", "Start reminding when days left", None))
        self.pushButton_8.setText(_translate("MainWindow", "About", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Settings", None))
        self.pushButton_2.setText(_translate("MainWindow", "Minimize", None))
        self.tray_icon = QtGui.QSystemTrayIcon(self)
        self.tray_ico = QtGui.QIcon(self.tray_icon_file)
        self.tray_icon.setIcon(self.tray_ico)
        self.tray_menu = QtGui.QMenu(self)
        self.tray_action_restore = QtGui.QAction('Restore', self)
        self.tray_action_show = QtGui.QAction('Show upcoming events', self)
        self.tray_menu.addAction(self.tray_action_restore)
        self.tray_menu.addAction(self.tray_action_show)
        self.tray_icon.setContextMenu(self.tray_menu)

#        locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
        self.nt_busy_mutex = QtCore.QMutex()
        self.db_write_mutex = QtCore.QMutex()
        self.main_thread_queue = Queue()
        self.reset_settings_button()
        self.update_person_list()
        self.update_events_list()
        self.tray_icon.show()
        self.birthday_manager.check_hidden(days_limit=self.settings_manager.get_option('days_left'))
        self.tray_icon.setToolTip('Birthday box')
        self.notify_thread = NotifyThread(self.birthday_manager, self.settings_manager, self.tray_icon)
        self.show_events_thread = ShowEventsTread(self.nt_busy_mutex, self.notify_thread)
        self.main_thread = MainThread(self.birthday_manager, self.settings_manager, self.nt_busy_mutex,
                                      self.db_write_mutex, self.notify_thread, self.main_thread_queue)
        self.main_thread.start()
        if not self.settings_manager.get_option('minimized'):
            self.show()
        if self.settings_manager.get_option('auto_start'):
            if not bbox_wreg.check('Bbox'):
                bbox_wreg.add('Bbox', '%s\\Bbox.exe' % self.database.file_path)

        """ Qt signals mapping """
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.minimize_button)
        QtCore.QObject.connect(self.tray_action_restore, QtCore.SIGNAL('triggered()'), self.tray_restore)
        QtCore.QObject.connect(self.tray_icon, QtCore.SIGNAL('activated(QSystemTrayIcon::ActivationReason)'),
                               self.dclick_restore)
        QtCore.QObject.connect(self.tray_action_show, QtCore.SIGNAL('triggered()'), self.tray_show)
        QtCore.QObject.connect(self.tray_icon, QtCore.SIGNAL('messageClicked()'), self.tray_restore)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL('clicked()'), self.about_button)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL('clicked()'), self.add_person_button)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL('clicked()'), self.edit_person_button)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL('clicked()'), self.delete_person_button)
        QtCore.QObject.connect(self.listView, QtCore.SIGNAL("clicked(QModelIndex)"), self.selected_in_event_list)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.edit_gift_button)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL('released()'), self.update_person_list)
        QtCore.QObject.connect(self.radioButton_2, QtCore.SIGNAL('released()'), self.update_person_list)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL('clicked()'), self.reset_settings_button)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL('clicked()'), self.apply_settings_button)
        QtCore.QObject.connect(self.main_thread, QtCore.SIGNAL('refresh_eventlist'), self.update_events_list)
        QtCore.QObject.connect(self.listView_2, QtCore.SIGNAL('doubleClicked(QModelIndex)'), self.edit_person_button)
        QtCore.QObject.connect(self.checkBox_3, QtCore.SIGNAL('released()'), self.hide_checkbox_changed)

    def minimize_button(self):
        self.hide()

    def tray_restore(self):
        self.show()

    def dclick_restore(self, reason):
        if reason == 2:
            self.show()

    def closeEvent(self, event):  # Program close event catch and override
        exit_dialog = bbox_ui.ExitDialog(self.window_icon_file)
        if not exit_dialog.exec_():
            event.ignore()

    def about_button(self):
        message = 'CREDITS: \n Idea - EvaLeo \n Code - Lax-T \n\n Version - 0.93B'
        inform_dialog = bbox_ui.InformDialog(message, self.window_icon_file)
        inform_dialog.exec_()

    def add_person_button(self):
        add_person_dialog = bbox_ui.EditPersonDialog(self.window_icon_file, name='', date=datetime.datetime.now())
        if add_person_dialog.exec_():
            self.db_write_mutex.lock()
            self.birthday_manager.add_person(add_person_dialog.name, add_person_dialog.date)
            self.db_write_mutex.unlock()
        self.update_person_list()
        self.update_events_list()

    def edit_person_button(self):
        row_selected = self.listView_2.currentIndex().row()
        person_list = self.birthday_manager.get_person_list()
        add_person_dialog = bbox_ui.EditPersonDialog(self.window_icon_file, name=person_list[row_selected][0],
                                                     date=person_list[row_selected][1])
        if add_person_dialog.exec_():
            confirm_dialog = bbox_ui.ConfirmDialog('Save changes?', self.window_icon_file)
            if confirm_dialog.exec_():
                self.db_write_mutex.lock()
                self.birthday_manager.edit_person(oldname=person_list[row_selected][0],
                                                  newname=add_person_dialog.name,
                                                  date=add_person_dialog.date)
                self.db_write_mutex.unlock()
        self.update_person_list()
        self.update_events_list()

    def delete_person_button(self):
        row_selected = self.listView_2.currentIndex().row()
        person_list = self.birthday_manager.get_person_list()
        confirm_dialog = bbox_ui.ConfirmDialog('Remove %s \n from list?' % person_list[row_selected][0],
                                               self.window_icon_file)
        if confirm_dialog.exec_():
            self.db_write_mutex.lock()
            self.birthday_manager.remove_person(person_list[row_selected][0])
            self.db_write_mutex.unlock()
        self.update_person_list()
        self.update_events_list()

    def edit_gift_button(self):
        selected_row = self.listView.currentIndex().row()
        names = self.birthday_manager.get_next_birthdays(days_limit=self.settings_manager
                                                         .get_option('days_left'))
        if 0 <= selected_row < len(names):
            name = names[selected_row]
            date, gift = self.birthday_manager.get_person_details(name)
            edit_gift_dialog = bbox_ui.EditGiftDialog(gift, self.window_icon_file)
            if edit_gift_dialog.exec_():
                confirm_dialog = bbox_ui.ConfirmDialog('Save gift?', self.window_icon_file)
                if confirm_dialog.exec_():
                    self.db_write_mutex.lock()
                    self.birthday_manager.edit_person(oldname=name, gift=edit_gift_dialog.gift)
                    self.db_write_mutex.unlock()
                    self.update_event_label(name)
        else:
            inform_dialog = bbox_ui.InformDialog('Event is not selected!', self.window_icon_file)
            inform_dialog.exec_()

    def reset_settings_button(self):
        settings = self.settings_manager.get_settings()
        self.spinBox.setValue(settings['remind_times'])
        self.spinBox_2.setValue(settings['remind_every_min'])
        self.spinBox_3.setValue(settings['days_left'])
        self.checkBox.setChecked(settings['auto_start'])
        self.checkBox_2.setChecked(settings['minimized'])

    def apply_settings_button(self):
        confirm_dialog = bbox_ui.ConfirmDialog('Save settings?', self.window_icon_file)
        if confirm_dialog.exec_():
            settings = {'remind_times': self.spinBox.value(), 'remind_every_min': self.spinBox_2.value(),
                        'days_left': self.spinBox_3.value(), 'auto_start': self.checkBox.isChecked(),
                        'minimized': self.checkBox_2.isChecked()}
            self.db_write_mutex.lock()
            self.settings_manager.store_settings(settings)
            self.db_write_mutex.unlock()
            self.update_events_list()
            self.main_thread_queue.put('settings_updated')
            if settings['auto_start']:
                if not bbox_wreg.check('Bbox'):
                    bbox_wreg.add('Bbox', '%s\\Bbox.exe' % self.database.file_path)
            else:
                if bbox_wreg.check('Bbox'):
                    bbox_wreg.delete('Bbox')

    def selected_in_event_list(self):
        selected_row = self.listView.currentIndex().row()
        name = self.birthday_manager.get_next_birthdays(days_limit=self.settings_manager
                                                        .get_option('days_left'))[selected_row]
        self.update_event_label(name)
        self.checkBox_3.setDisabled(False)
        self.checkBox_3.setChecked(self.birthday_manager.is_hidden(name))

    def hide_checkbox_changed(self):
        selected_row = self.listView.currentIndex().row()
        name = self.birthday_manager.get_next_birthdays(days_limit=self.settings_manager
                                                        .get_option('days_left'))[selected_row]
        self.db_write_mutex.lock()
        self.birthday_manager.set_hidden(name, self.checkBox_3.isChecked())
        self.db_write_mutex.unlock()

    def update_event_label(self, name):
        date, gift = self.birthday_manager.get_person_details(name)
        date_now = datetime.datetime.now()
        if date.month == 2 and date.day == 29 and not calendar.isleap(date_now.year):
            leap_correction = True
        else:
            leap_correction = False
        days_left = (datetime.datetime.strptime('%s.%s.%s' % (date.day-1 if leap_correction else date.day, date.month,
                                                              date_now.year+1 if date_now.month > date.month
                                                              else date_now.year), '%d.%m.%Y') - date_now).days
        if date_now.month > date.month:
            years_old = date_now.year + 1 - date.year
        else:
            years_old = date_now.year - date.year

        if days_left == 0:
            days_left_string = 'Tomorrow'
        elif days_left > 0:
            days_left_string = 'In %s days' % (days_left + 1)
        else:
            days_left_string = 'Today'
        if years_old == 1:
            years_string = 'year'
        else:
            years_string = 'years'

        self.label.setText("%s (%s) it's %s birthday!\nHe(she) is gonna be %s %s old.\n"
                           "You are planning to give: %s" % (days_left_string, date.strftime('%d %b'),
                                                             name, years_old, years_string, gift))

    def update_person_list(self):  # Person list refresh
        list_data = []
        if self.radioButton.isChecked():
            person_list = self.birthday_manager.get_person_list(sort_by='date')

        else:
            person_list = self.birthday_manager.get_person_list(sort_by='name')

        for person_data in person_list:
            list_data.append('%s  -  %s' % (person_data[1].strftime('%d %b %Y'), person_data[0]))
        person_list_model = ListModel(list_data, '')
        self.listView_2.setModel(person_list_model)
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setDisabled(True)
        self.label.setText("Select event to see details")

    def update_events_list(self):  # Event list refresh
        event_list = self.birthday_manager.get_next_birthdays(days_limit=self.settings_manager.get_option('days_left'))
        list_data = []
        for name in event_list:
            date, gift = self.birthday_manager.get_person_details(name)
            list_data.append('%s  -  %s' % (date.strftime('%d %b %Y'), name))
        event_list_model = ListModel(list_data, '')
        self.listView.setModel(event_list_model)
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setDisabled(True)
        self.label.setText("Select event to see details")

    def tray_show(self):  # Manual notification trigger
        self.show_events_thread.start()


class ListModel(QAbstractListModel):  # List builder, modified but 80% class code from internet
    def __init__(self, datain, headerdata, parent=None):

        QAbstractListModel.__init__(self, parent)
        self.array_data = datain
        self.header_data = headerdata

    def rowCount(self, parent=None, *args):
        return len(self.array_data)

    def data(self, index, role=None):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return "%s" % self.array_data[index.row()]

    def headerData(self, col, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header_data[col]
        return None


class ShowEventsTread(QThread):
    """If triggered notification manually this sub thread checks if main Notification thread is busy. It's needed
     to avoid double run calls that can cause error"""
    def __init__(self, mutex, notification_thread):
        QThread.__init__(self)
        self.nt_busy_mutex = mutex
        self.notification_thread = notification_thread

    def run(self):
        mutex_status = self.nt_busy_mutex.tryLock()
        while not mutex_status:
            self.sleep(10)
            mutex_status = self.nt_busy_mutex.tryLock()
        self.notification_thread.start()
        while self.notification_thread.isRunning():
            self.sleep(5)
        self.nt_busy_mutex.unlock()


class MainThread(QThread):
    """Main background thread, sleeps most of the time:)"""
    def __init__(self, birthday_manager, settings_manager, nt_busy_mutex, db_write_mutex,
                 notification_thread, mt_queue):
        QThread.__init__(self)
        self.birthday_manager = birthday_manager
        self.settings_manager = settings_manager
        self.nt_busy_mutex = nt_busy_mutex
        self.db_write_mutex = db_write_mutex
        self.notification_thread = notification_thread
        self.mt_queue = mt_queue
        self.notify_period = settings_manager.get_option('remind_every_min')*3
        self.notify_period_count = self.notify_period
        self.notify_times_limit = settings_manager.get_option('remind_times')
        self.days_left_limit = settings_manager.get_option('days_left')
        self.notify_times_count = 0
        self.current_notify_period = datetime.datetime.now().day
        self.signal = QtCore.SIGNAL('refresh_eventlist')

    def update_settings(self):
        self.notify_period = self.settings_manager.get_option('remind_every_min')*3
        self.notify_times_limit = self.settings_manager.get_option('remind_times')
        self.days_left_limit = self.settings_manager.get_option('days_left')

    def run(self):
        while True:

            if not self.mt_queue.empty():
                command = self.mt_queue.get()
                if command == 'settings_updated':
                    self.update_settings()

            if self.current_notify_period != datetime.datetime.now().day:
                self.emit(self.signal, 'refresh_eventlist')
                self.db_write_mutex.lock()
                self.birthday_manager.check_hidden(days_limit=self.days_left_limit)
                self.db_write_mutex.unlock()
                self.current_notify_period = datetime.datetime.now().day
                self.notify_times_count = 0
                self.notify_period_count = self.notify_period-1

            if self.notify_times_count <= self.notify_times_limit:
                if self.notify_period_count >= self.notify_period:
                    if self.nt_busy_mutex.tryLock():
                        self.notification_thread.start()
                        infinite_loop_prot = 0
                        while self.notification_thread.isRunning() or infinite_loop_prot > 100:
                            infinite_loop_prot += 1
                            self.sleep(5)
                        self.nt_busy_mutex.unlock()
                        self.notify_period_count = 0
                        self.notify_times_limit += 1
                else:
                    self.notify_period_count += 1

            self.sleep(20)


class NotifyThread(QThread):
    """Notification thread, when executed checks if any notifications match criteria and shows them."""
    def __init__(self, birthday_manager, settings_manager, tray_icon):
        QThread.__init__(self)
        self.birthday_manager = birthday_manager
        self.settings_manager = settings_manager
        self.tray_icon = tray_icon
        self.days_left_limit = self.settings_manager.get_option('days_left')
        self.notify_list = self.birthday_manager.get_next_birthdays(days_limit=self.days_left_limit)

    def run(self):
        self.days_left_limit = self.settings_manager.get_option('days_left')
        self.notify_list = self.birthday_manager.get_next_birthdays(days_limit=self.days_left_limit,
                                                                    include_hidden=False)
        date_now = datetime.datetime.now()
        for name in self.notify_list:
            date, gift = self.birthday_manager.get_person_details(name)
            if date.month == 2 and date.day == 29 and not calendar.isleap(date_now.year):
                leap_correction = True
            else:
                leap_correction = False
            days_left = (datetime.datetime.strptime('%s.%s.%s' % (date.day-1 if leap_correction else date.day,
                                                                  date.month, date_now.year+1 if
                                                                  date_now.month > date.month else date_now.year),
                                                    '%d.%m.%Y') - date_now).days

            if days_left == 0:
                days_left_string = 'tomorrow'
            elif days_left > 0:
                days_left_string = 'in %s days' % (days_left + 1)
            else:
                days_left_string = 'today'

            self.tray_icon.showMessage("%s birthday %s!" % (name, days_left_string),
                                       "%s (%s) it's %s birthday!\nCheck Bbox for details."
                                       % (days_left_string.capitalize(),
                                          date.strftime('%d %b'), name))
            self.sleep(20)
        self.quit()


if __name__ == '__main__':
    main_database = bbox_db.MainBD(DB_FILE_NAME)
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow(main_database, WINDOW_ICON, TRAY_ICON)
    sys.exit(app.exec_())