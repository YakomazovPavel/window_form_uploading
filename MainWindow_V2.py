# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_V2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)
import resource_file_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(543, 400)
        MainWindow.setMinimumSize(QSize(543, 400))
        MainWindow.setMaximumSize(QSize(543, 400))
        icon = QIcon()
        icon.addFile(u":/icons/upload_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setInputMethodHints(Qt.ImhNone)
        self.action_select_many_templates = QAction(MainWindow)
        self.action_select_many_templates.setObjectName(u"action_select_many_templates")
        self.action_select_temperature_template = QAction(MainWindow)
        self.action_select_temperature_template.setObjectName(u"action_select_temperature_template")
        self.action_select_pressure_template = QAction(MainWindow)
        self.action_select_pressure_template.setObjectName(u"action_select_pressure_template")
        self.action_select_flow_template = QAction(MainWindow)
        self.action_select_flow_template.setObjectName(u"action_select_flow_template")
        self.action_select_level_template = QAction(MainWindow)
        self.action_select_level_template.setObjectName(u"action_select_level_template")
        self.action_select_analyzer_template = QAction(MainWindow)
        self.action_select_analyzer_template.setObjectName(u"action_select_analyzer_template")
        self.action_select_control_valve_template = QAction(MainWindow)
        self.action_select_control_valve_template.setObjectName(u"action_select_control_valve_template")
        self.action_select_shut_off_valve_template = QAction(MainWindow)
        self.action_select_shut_off_valve_template.setObjectName(u"action_select_shut_off_valve_template")
        self.action_select_environments_descriptions = QAction(MainWindow)
        self.action_select_environments_descriptions.setObjectName(u"action_select_environments_descriptions")
        self.action_select_tsp_template = QAction(MainWindow)
        self.action_select_tsp_template.setObjectName(u"action_select_tsp_template")
        self.action_select_io_template = QAction(MainWindow)
        self.action_select_io_template.setObjectName(u"action_select_io_template")
        self.action_select_kj_template = QAction(MainWindow)
        self.action_select_kj_template.setObjectName(u"action_select_kj_template")
        self.action_select_specification_template = QAction(MainWindow)
        self.action_select_specification_template.setObjectName(u"action_select_specification_template")
        self.action_select_shared_save_directory = QAction(MainWindow)
        self.action_select_shared_save_directory.setObjectName(u"action_select_shared_save_directory")
        self.action_select_ol_save_directory = QAction(MainWindow)
        self.action_select_ol_save_directory.setObjectName(u"action_select_ol_save_directory")
        self.action_select_tsp_save_directory = QAction(MainWindow)
        self.action_select_tsp_save_directory.setObjectName(u"action_select_tsp_save_directory")
        self.action_select_io_save_directory = QAction(MainWindow)
        self.action_select_io_save_directory.setObjectName(u"action_select_io_save_directory")
        self.action_select_kj_save_directory = QAction(MainWindow)
        self.action_select_kj_save_directory.setObjectName(u"action_select_kj_save_directory")
        self.action_select_specifaication_save_directory = QAction(MainWindow)
        self.action_select_specifaication_save_directory.setObjectName(u"action_select_specifaication_save_directory")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.group_box_uploading_ol = QGroupBox(self.centralwidget)
        self.group_box_uploading_ol.setObjectName(u"group_box_uploading_ol")
        self.verticalLayoutWidget_6 = QWidget(self.group_box_uploading_ol)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 20, 151, 301))
        self.vertical_layout_uploading_ol = QVBoxLayout(self.verticalLayoutWidget_6)
        self.vertical_layout_uploading_ol.setSpacing(4)
        self.vertical_layout_uploading_ol.setObjectName(u"vertical_layout_uploading_ol")
        self.vertical_layout_uploading_ol.setSizeConstraint(QLayout.SetFixedSize)
        self.vertical_layout_uploading_ol.setContentsMargins(0, 0, 0, 0)
        self.push_btn_uploading_temperature = QPushButton(self.verticalLayoutWidget_6)
        self.push_btn_uploading_temperature.setObjectName(u"push_btn_uploading_temperature")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_btn_uploading_temperature.sizePolicy().hasHeightForWidth())
        self.push_btn_uploading_temperature.setSizePolicy(sizePolicy)
        self.push_btn_uploading_temperature.setMinimumSize(QSize(149, 37))
        self.push_btn_uploading_temperature.setMaximumSize(QSize(149, 37))
        self.push_btn_uploading_temperature.setBaseSize(QSize(149, 37))

        self.vertical_layout_uploading_ol.addWidget(self.push_btn_uploading_temperature)

        self.push_btn_uploading_pressure = QPushButton(self.verticalLayoutWidget_6)
        self.push_btn_uploading_pressure.setObjectName(u"push_btn_uploading_pressure")
        sizePolicy.setHeightForWidth(self.push_btn_uploading_pressure.sizePolicy().hasHeightForWidth())
        self.push_btn_uploading_pressure.setSizePolicy(sizePolicy)
        self.push_btn_uploading_pressure.setMinimumSize(QSize(149, 37))
        self.push_btn_uploading_pressure.setMaximumSize(QSize(149, 37))
        self.push_btn_uploading_pressure.setBaseSize(QSize(149, 37))

        self.vertical_layout_uploading_ol.addWidget(self.push_btn_uploading_pressure)

        self.push_btn_uploading_flow = QPushButton(self.verticalLayoutWidget_6)
        self.push_btn_uploading_flow.setObjectName(u"push_btn_uploading_flow")
        sizePolicy.setHeightForWidth(self.push_btn_uploading_flow.sizePolicy().hasHeightForWidth())
        self.push_btn_uploading_flow.setSizePolicy(sizePolicy)
        self.push_btn_uploading_flow.setMinimumSize(QSize(149, 37))
        self.push_btn_uploading_flow.setMaximumSize(QSize(149, 37))
        self.push_btn_uploading_flow.setBaseSize(QSize(149, 37))

        self.vertical_layout_uploading_ol.addWidget(self.push_btn_uploading_flow)

        self.push_btn_uploading_level = QPushButton(self.verticalLayoutWidget_6)
        self.push_btn_uploading_level.setObjectName(u"push_btn_uploading_level")
        sizePolicy.setHeightForWidth(self.push_btn_uploading_level.sizePolicy().hasHeightForWidth())
        self.push_btn_uploading_level.setSizePolicy(sizePolicy)
        self.push_btn_uploading_level.setMinimumSize(QSize(149, 37))
        self.push_btn_uploading_level.setMaximumSize(QSize(149, 37))
        self.push_btn_uploading_level.setBaseSize(QSize(149, 37))

        self.vertical_layout_uploading_ol.addWidget(self.push_btn_uploading_level)

        self.push_btn_uploading_analyzer = QPushButton(self.verticalLayoutWidget_6)
        self.push_btn_uploading_analyzer.setObjectName(u"push_btn_uploading_analyzer")
        sizePolicy.setHeightForWidth(self.push_btn_uploading_analyzer.sizePolicy().hasHeightForWidth())
        self.push_btn_uploading_analyzer.setSizePolicy(sizePolicy)
        self.push_btn_uploading_analyzer.setMinimumSize(QSize(149, 37))
        self.push_btn_uploading_analyzer.setMaximumSize(QSize(149, 37))
        self.push_btn_uploading_analyzer.setBaseSize(QSize(149, 37))

        self.vertical_layout_uploading_ol.addWidget(self.push_btn_uploading_analyzer)

        self.push_btn_uploading_control_valve = QPushButton(self.verticalLayoutWidget_6)
        self.push_btn_uploading_control_valve.setObjectName(u"push_btn_uploading_control_valve")
        sizePolicy.setHeightForWidth(self.push_btn_uploading_control_valve.sizePolicy().hasHeightForWidth())
        self.push_btn_uploading_control_valve.setSizePolicy(sizePolicy)
        self.push_btn_uploading_control_valve.setMinimumSize(QSize(149, 37))
        self.push_btn_uploading_control_valve.setMaximumSize(QSize(149, 37))
        self.push_btn_uploading_control_valve.setBaseSize(QSize(149, 37))

        self.vertical_layout_uploading_ol.addWidget(self.push_btn_uploading_control_valve)

        self.push_btn_uploading_shut_off_valve = QPushButton(self.verticalLayoutWidget_6)
        self.push_btn_uploading_shut_off_valve.setObjectName(u"push_btn_uploading_shut_off_valve")
        sizePolicy.setHeightForWidth(self.push_btn_uploading_shut_off_valve.sizePolicy().hasHeightForWidth())
        self.push_btn_uploading_shut_off_valve.setSizePolicy(sizePolicy)
        self.push_btn_uploading_shut_off_valve.setMinimumSize(QSize(149, 37))
        self.push_btn_uploading_shut_off_valve.setMaximumSize(QSize(149, 37))
        self.push_btn_uploading_shut_off_valve.setBaseSize(QSize(149, 37))

        self.vertical_layout_uploading_ol.addWidget(self.push_btn_uploading_shut_off_valve)


        self.horizontalLayout.addWidget(self.group_box_uploading_ol)

        self.group_box_uploading_documents = QGroupBox(self.centralwidget)
        self.group_box_uploading_documents.setObjectName(u"group_box_uploading_documents")
        self.verticalLayoutWidget_8 = QWidget(self.group_box_uploading_documents)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(10, 20, 151, 174))
        self.vertical_layout_uploading_documents = QVBoxLayout(self.verticalLayoutWidget_8)
        self.vertical_layout_uploading_documents.setSpacing(4)
        self.vertical_layout_uploading_documents.setObjectName(u"vertical_layout_uploading_documents")
        self.vertical_layout_uploading_documents.setSizeConstraint(QLayout.SetFixedSize)
        self.vertical_layout_uploading_documents.setContentsMargins(0, 0, 0, 0)
        self.push_btn_uploading_io = QPushButton(self.verticalLayoutWidget_8)
        self.push_btn_uploading_io.setObjectName(u"push_btn_uploading_io")
        sizePolicy.setHeightForWidth(self.push_btn_uploading_io.sizePolicy().hasHeightForWidth())
        self.push_btn_uploading_io.setSizePolicy(sizePolicy)
        self.push_btn_uploading_io.setMinimumSize(QSize(149, 37))
        self.push_btn_uploading_io.setMaximumSize(QSize(149, 37))
        self.push_btn_uploading_io.setBaseSize(QSize(149, 37))

        self.vertical_layout_uploading_documents.addWidget(self.push_btn_uploading_io)

        self.push_btn_uploading_tsp = QPushButton(self.verticalLayoutWidget_8)
        self.push_btn_uploading_tsp.setObjectName(u"push_btn_uploading_tsp")
        sizePolicy.setHeightForWidth(self.push_btn_uploading_tsp.sizePolicy().hasHeightForWidth())
        self.push_btn_uploading_tsp.setSizePolicy(sizePolicy)
        self.push_btn_uploading_tsp.setMinimumSize(QSize(149, 37))
        self.push_btn_uploading_tsp.setMaximumSize(QSize(149, 37))
        self.push_btn_uploading_tsp.setBaseSize(QSize(149, 37))

        self.vertical_layout_uploading_documents.addWidget(self.push_btn_uploading_tsp)

        self.push_btn_uploading_kj = QPushButton(self.verticalLayoutWidget_8)
        self.push_btn_uploading_kj.setObjectName(u"push_btn_uploading_kj")
        sizePolicy.setHeightForWidth(self.push_btn_uploading_kj.sizePolicy().hasHeightForWidth())
        self.push_btn_uploading_kj.setSizePolicy(sizePolicy)
        self.push_btn_uploading_kj.setMinimumSize(QSize(149, 37))
        self.push_btn_uploading_kj.setMaximumSize(QSize(149, 37))
        self.push_btn_uploading_kj.setBaseSize(QSize(149, 37))

        self.vertical_layout_uploading_documents.addWidget(self.push_btn_uploading_kj)

        self.push_btn_uploading_spec = QPushButton(self.verticalLayoutWidget_8)
        self.push_btn_uploading_spec.setObjectName(u"push_btn_uploading_spec")
        sizePolicy.setHeightForWidth(self.push_btn_uploading_spec.sizePolicy().hasHeightForWidth())
        self.push_btn_uploading_spec.setSizePolicy(sizePolicy)
        self.push_btn_uploading_spec.setMinimumSize(QSize(149, 37))
        self.push_btn_uploading_spec.setMaximumSize(QSize(149, 37))
        self.push_btn_uploading_spec.setBaseSize(QSize(149, 37))

        self.vertical_layout_uploading_documents.addWidget(self.push_btn_uploading_spec)


        self.horizontalLayout.addWidget(self.group_box_uploading_documents)

        self.group_box_reference_data = QGroupBox(self.centralwidget)
        self.group_box_reference_data.setObjectName(u"group_box_reference_data")
        self.verticalLayoutWidget_10 = QWidget(self.group_box_reference_data)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(10, 20, 151, 174))
        self.vertical_layout_reference_data = QVBoxLayout(self.verticalLayoutWidget_10)
        self.vertical_layout_reference_data.setSpacing(4)
        self.vertical_layout_reference_data.setObjectName(u"vertical_layout_reference_data")
        self.vertical_layout_reference_data.setSizeConstraint(QLayout.SetFixedSize)
        self.vertical_layout_reference_data.setContentsMargins(0, 0, 0, 0)
        self.push_btn_open_uploading_directory = QPushButton(self.verticalLayoutWidget_10)
        self.push_btn_open_uploading_directory.setObjectName(u"push_btn_open_uploading_directory")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.push_btn_open_uploading_directory.sizePolicy().hasHeightForWidth())
        self.push_btn_open_uploading_directory.setSizePolicy(sizePolicy1)
        self.push_btn_open_uploading_directory.setMinimumSize(QSize(149, 37))
        self.push_btn_open_uploading_directory.setMaximumSize(QSize(149, 37))
        self.push_btn_open_uploading_directory.setBaseSize(QSize(149, 37))
        self.push_btn_open_uploading_directory.setTabletTracking(False)
        self.push_btn_open_uploading_directory.setAcceptDrops(False)
        self.push_btn_open_uploading_directory.setToolTipDuration(0)
        self.push_btn_open_uploading_directory.setLayoutDirection(Qt.LeftToRight)
        self.push_btn_open_uploading_directory.setAutoFillBackground(False)

        self.vertical_layout_reference_data.addWidget(self.push_btn_open_uploading_directory)

        self.push_btn_open_templates_directory = QPushButton(self.verticalLayoutWidget_10)
        self.push_btn_open_templates_directory.setObjectName(u"push_btn_open_templates_directory")
        sizePolicy1.setHeightForWidth(self.push_btn_open_templates_directory.sizePolicy().hasHeightForWidth())
        self.push_btn_open_templates_directory.setSizePolicy(sizePolicy1)
        self.push_btn_open_templates_directory.setMinimumSize(QSize(149, 37))
        self.push_btn_open_templates_directory.setMaximumSize(QSize(149, 37))
        self.push_btn_open_templates_directory.setBaseSize(QSize(149, 37))
        self.push_btn_open_templates_directory.setTabletTracking(False)
        self.push_btn_open_templates_directory.setAcceptDrops(False)
        self.push_btn_open_templates_directory.setToolTipDuration(0)
        self.push_btn_open_templates_directory.setLayoutDirection(Qt.LeftToRight)
        self.push_btn_open_templates_directory.setAutoFillBackground(False)

        self.vertical_layout_reference_data.addWidget(self.push_btn_open_templates_directory)

        self.push_btn_open_reference_database = QPushButton(self.verticalLayoutWidget_10)
        self.push_btn_open_reference_database.setObjectName(u"push_btn_open_reference_database")
        sizePolicy1.setHeightForWidth(self.push_btn_open_reference_database.sizePolicy().hasHeightForWidth())
        self.push_btn_open_reference_database.setSizePolicy(sizePolicy1)
        self.push_btn_open_reference_database.setMinimumSize(QSize(149, 37))
        self.push_btn_open_reference_database.setMaximumSize(QSize(149, 37))
        self.push_btn_open_reference_database.setBaseSize(QSize(149, 37))
        self.push_btn_open_reference_database.setTabletTracking(False)
        self.push_btn_open_reference_database.setAcceptDrops(False)
        self.push_btn_open_reference_database.setToolTipDuration(0)
        self.push_btn_open_reference_database.setLayoutDirection(Qt.LeftToRight)
        self.push_btn_open_reference_database.setAutoFillBackground(False)

        self.vertical_layout_reference_data.addWidget(self.push_btn_open_reference_database)

        self.push_btn_open_database = QPushButton(self.verticalLayoutWidget_10)
        self.push_btn_open_database.setObjectName(u"push_btn_open_database")
        sizePolicy1.setHeightForWidth(self.push_btn_open_database.sizePolicy().hasHeightForWidth())
        self.push_btn_open_database.setSizePolicy(sizePolicy1)
        self.push_btn_open_database.setMinimumSize(QSize(149, 37))
        self.push_btn_open_database.setMaximumSize(QSize(149, 37))
        self.push_btn_open_database.setBaseSize(QSize(149, 37))
        self.push_btn_open_database.setTabletTracking(False)
        self.push_btn_open_database.setAcceptDrops(False)
        self.push_btn_open_database.setToolTipDuration(0)
        self.push_btn_open_database.setLayoutDirection(Qt.LeftToRight)
        self.push_btn_open_database.setAutoFillBackground(False)

        self.vertical_layout_reference_data.addWidget(self.push_btn_open_database)


        self.horizontalLayout.addWidget(self.group_box_reference_data)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 543, 21))
        self.menu_select_templates = QMenu(self.menubar)
        self.menu_select_templates.setObjectName(u"menu_select_templates")
        self.submenu_select_ol_templates = QMenu(self.menu_select_templates)
        self.submenu_select_ol_templates.setObjectName(u"submenu_select_ol_templates")
        self.menu_select_save_directories = QMenu(self.menubar)
        self.menu_select_save_directories.setObjectName(u"menu_select_save_directories")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_select_templates.menuAction())
        self.menubar.addAction(self.menu_select_save_directories.menuAction())
        self.menu_select_templates.addAction(self.action_select_many_templates)
        self.menu_select_templates.addSeparator()
        self.menu_select_templates.addAction(self.submenu_select_ol_templates.menuAction())
        self.menu_select_templates.addAction(self.action_select_tsp_template)
        self.menu_select_templates.addAction(self.action_select_io_template)
        self.menu_select_templates.addAction(self.action_select_kj_template)
        self.menu_select_templates.addAction(self.action_select_specification_template)
        self.submenu_select_ol_templates.addAction(self.action_select_temperature_template)
        self.submenu_select_ol_templates.addAction(self.action_select_pressure_template)
        self.submenu_select_ol_templates.addAction(self.action_select_flow_template)
        self.submenu_select_ol_templates.addAction(self.action_select_level_template)
        self.submenu_select_ol_templates.addAction(self.action_select_analyzer_template)
        self.submenu_select_ol_templates.addAction(self.action_select_control_valve_template)
        self.submenu_select_ol_templates.addAction(self.action_select_shut_off_valve_template)
        self.submenu_select_ol_templates.addSeparator()
        self.submenu_select_ol_templates.addAction(self.action_select_environments_descriptions)
        self.menu_select_save_directories.addAction(self.action_select_shared_save_directory)
        self.menu_select_save_directories.addSeparator()
        self.menu_select_save_directories.addAction(self.action_select_ol_save_directory)
        self.menu_select_save_directories.addAction(self.action_select_tsp_save_directory)
        self.menu_select_save_directories.addAction(self.action_select_io_save_directory)
        self.menu_select_save_directories.addAction(self.action_select_kj_save_directory)
        self.menu_select_save_directories.addAction(self.action_select_specifaication_save_directory)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SPIK SZMA Uploadind Documents", None))
        self.action_select_many_templates.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0448\u0430\u0431\u043b\u043e\u043d\u044b", None))
        self.action_select_temperature_template.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.action_select_pressure_template.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.action_select_flow_template.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434", None))
        self.action_select_level_template.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.action_select_analyzer_template.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437\u0430\u0442\u043e\u0440", None))
        self.action_select_control_valve_template.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u044e\u0449\u0438\u0439 \u043a\u043b\u0430\u043f\u0430\u043d", None))
        self.action_select_shut_off_valve_template.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u0447\u043d\u043e\u0439 \u043a\u043b\u0430\u043f\u0430\u043d", None))
        self.action_select_environments_descriptions.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u044b", None))
        self.action_select_tsp_template.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0421\u041f", None))
        self.action_select_io_template.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041e", None))
        self.action_select_kj_template.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0416", None))
        self.action_select_specification_template.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.action_select_shared_save_directory.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0438\u044f", None))
        self.action_select_ol_save_directory.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0440\u043e\u0441\u043d\u044b\u0435 \u043b\u0438\u0441\u0442\u044b", None))
        self.action_select_tsp_save_directory.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0421\u041f", None))
        self.action_select_io_save_directory.setText(QCoreApplication.translate("MainWindow", u"\u0418\u041e", None))
        self.action_select_kj_save_directory.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0416", None))
        self.action_select_specifaication_save_directory.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.group_box_uploading_ol.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0440\u043e\u0441\u043d\u044b\u0435 \u043b\u0438\u0441\u0442\u044b", None))
        self.push_btn_uploading_temperature.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430", None))
        self.push_btn_uploading_pressure.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.push_btn_uploading_flow.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434", None))
        self.push_btn_uploading_level.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.push_btn_uploading_analyzer.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437\u0430\u0442\u043e\u0440", None))
        self.push_btn_uploading_control_valve.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0443\u043b\u0438\u0440\u0443\u044e\u0449\u0438\u0439 \u043a\u043b\u0430\u043f\u0430\u043d", None))
        self.push_btn_uploading_shut_off_valve.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u0447\u043d\u043e\u0439 \u043a\u043b\u0430\u043f\u0430\u043d", None))
        self.group_box_uploading_documents.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u044f", None))
#if QT_CONFIG(tooltip)
        self.push_btn_uploading_io.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.push_btn_uploading_io.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0435\n"
"\u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u0435", None))
#if QT_CONFIG(tooltip)
        self.push_btn_uploading_tsp.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.push_btn_uploading_tsp.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u0439\n"
"\u0438 \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0439", None))
#if QT_CONFIG(tooltip)
        self.push_btn_uploading_kj.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.push_btn_uploading_kj.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0431\u0435\u043b\u044c\u043d\u044b\u0439\u0442\n"
"\u0436\u0443\u0440\u043d\u0430\u043b", None))
#if QT_CONFIG(tooltip)
        self.push_btn_uploading_spec.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.push_btn_uploading_spec.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.group_box_reference_data.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0430\u0432\u043e\u0447\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
#if QT_CONFIG(tooltip)
        self.push_btn_open_uploading_directory.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.push_btn_open_uploading_directory.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.push_btn_open_uploading_directory.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0432\u044b\u0433\u0440\u0443\u0437\u043a\u0438", None))
#if QT_CONFIG(tooltip)
        self.push_btn_open_templates_directory.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.push_btn_open_templates_directory.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.push_btn_open_templates_directory.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u0448\u0430\u0431\u043b\u043e\u043d\u043e\u0432", None))
#if QT_CONFIG(tooltip)
        self.push_btn_open_reference_database.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.push_btn_open_reference_database.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.push_btn_open_reference_database.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0443\u044e\n"
"\u0431\u0430\u0437\u0443", None))
#if QT_CONFIG(tooltip)
        self.push_btn_open_database.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.push_btn_open_database.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.push_btn_open_database.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0431\u0430\u0437\u0443 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.menu_select_templates.setTitle(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0431\u043b\u043e\u043d\u044b", None))
        self.submenu_select_ol_templates.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0440\u043e\u0441\u043d\u044b\u0435 \u043b\u0438\u0441\u0442\u044b", None))
        self.menu_select_save_directories.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

