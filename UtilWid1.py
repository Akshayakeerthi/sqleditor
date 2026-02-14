from PySide6.QtWidgets import QApplication, QMainWindow, QSizePolicy, QTableWidget, QListWidget, QTabWidget, QSplitter, QWidget, QMenu
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QFormLayout, QFileDialog, QRadioButton, QPushButton, QComboBox, QLineEdit, QLabel
from PySide6.QtWidgets import QTableWidgetItem, QListWidgetItem, QCheckBox, QDialog
from PySide6.QtGui import QIcon, QBrush, QColor, QAction, QPainter, QRegularExpressionValidator
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtPdf import QPdfDocument
from PySide6.QtCore import QPoint, Qt

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

import mysql.connector
import math
import csv
import sys
import re

class InsertListItem(QWidget):
    def __init__(self, form_layout, parent=None):
        super().__init__(parent)
        
        layout = QHBoxLayout()
        self.del_button = RoundButton("bin.png", "+", self)
        #self.del_button.move(self.width() - self.del_button.width(), 0)
        self.form_edit = form_layout
        layout.addLayout(self.form_edit)
        layout.addWidget(self.del_button)
        
        self.setLayout(layout)
        
class ConditionListItem(QWidget):
    def __init__(self, cmb_box1, cmb_box2, parent=None):
        super().__init__(parent)
        
        llayout = QHBoxLayout()
        self.layout = QHBoxLayout()
        self.del_button = RoundButton("bin.png", "X", self)
        #self.del_button.move(self.width() - self.del_button.width(), 0)
        self.cmb1 = cmb_box1
        self.rad = QRadioButton("NOT")
        self.cmb2 = cmb_box2
        self.wid = None
        self.layout.addWidget(self.cmb1)
        self.layout.addWidget(self.rad)
        self.layout.addWidget(self.cmb2)
        llayout.addLayout(self.layout)
        llayout.addWidget(self.del_button)
        self.setLayout(llayout)
        
    def addWidget(self, wid):
        self.wid = wid
        self.layout.addWidget(self.wid)
        
    def removeWidget(self):
        if self.wid:
            self.layout.removeWidget(self.wid)
            self.wid.setParent(None)
            self.wid = None
        
class UpdateListItem(QWidget):
    def __init__(self, form_layout, parent=None):
        super().__init__(parent)
        
        layout = QHBoxLayout()
        self.del_button = RoundButton("bin.png", "+", self)
        #self.del_button.move(self.width() - self.del_button.width(), 0)
        self.form_edit = form_layout
        layout.addLayout(self.form_edit)
        layout.addWidget(self.del_button)
        
        self.setLayout(layout)
        
class SelectListItem(QWidget):
    def __init__(self, form_layout, parent=None):
        super().__init__(parent)
        
        layout = QHBoxLayout()
        self.del_button = RoundButton("bin.png", "+", self)
        #self.del_button.move(self.width() - self.del_button.width(), 0)
        self.form_edit = form_layout
        layout.addLayout(self.form_edit)
        layout.addWidget(self.del_button)
        
        self.setLayout(layout)
        
class RoundButton(QPushButton):
    def __init__(self, path, text="", parent=None):
        super().__init__(text, parent)
        self.setFixedSize(20, 20)  # Set the fixed size to make it round
        self.icon = QIcon(path)
        self.normal_color = QColor(80, 80, 100)  # Normal color
        self.normal_color.setAlpha(0)
        self.hover_color = QColor(130, 130, 150)  # Color when hovered
        self.hover_color.setAlpha(80)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(self.normal_color))  # Use normal color by default
        painter.setPen(Qt.NoPen)
        
        if self.underMouse():
            painter.setBrush(QBrush(self.hover_color))
        else:
            painter.setBrush(QBrush(self.normal_color))
            
        if self.icon:
            icon_size = min(self.width(), self.height())  # Make sure the icon fits inside the button
            icon_pixmap = self.icon.pixmap(icon_size, icon_size)
            painter.drawEllipse(0, 0, self.width(), self.height())
            painter.drawPixmap((self.width() - icon_size) / 2, (self.height() - icon_size) / 2, icon_pixmap)
        
        painter.drawText(event.rect(), Qt.AlignCenter, self.text())

    def enterEvent(self, event):
        self.normal_color = self.hover_color  # Change color when hovered
        self.update()

    def leaveEvent(self, event):
        self.normal_color = QColor(80, 80, 100)    # Reset color when mouse leaves
        self.normal_color.setAlpha(0)
        self.update()
        
class NewItemWidget(QListWidget):
    def __init__(self, val_edit=None, parent=None):
        super().__init__(parent)
        
        self.setDragDropMode(QListWidget.NoDragDrop)
        self.resize(350, 350)
        
        self.val_edit = val_edit
        
        self.add_button = RoundButton("plus.png", "Round Button", self)
        self.add_button.clicked.connect(self.add_new_widget)
        self.add_button.move(self.size().width()-self.add_button.width(), self.size().height()-self.add_button.height())
        
    def add_new_widget(self):
        
        form_layout = QFormLayout()
        
        for i in self.val_edit:
            if 'date' in i[1]:
                validator = QRegularExpressionValidator(r"^\d{4}-\d{2}-\d{2}$", self)
            elif 'int' in i[1]:
                l = i[1].split("(")
                lim = str(l[1][:-1])
                validator = QRegularExpressionValidator(r"^(\d{1," + lim + r"},)+$")
            elif 'varchar' in i[1]:
                if i[0] == "CLASS_ID":
                    validator = QRegularExpressionValidator(r"^(I|II|III|IV|V)$", self)
                else:
                    l = i[1].split("(")
                    lim = str(l[1][:-1])
                    validator = QRegularExpressionValidator(r"^[^,]{1," + lim + r"}$", self)
            form_item = QLineEdit()
            form_item.setValidator(validator)
            form_layout.addRow(f"{i[0]}:", form_item)
        item = QListWidgetItem()
        self.addItem(item)
        custom_widget = InsertListItem(form_layout)
        custom_widget.del_button.clicked.connect(self.delete_widget)
        item.setSizeHint(custom_widget.sizeHint())
        self.setItemWidget(item, custom_widget)
            
    def delete_widget(self):
        
        global_pos = self.sender().mapTo(self.sender().parent().parent().parent(), self.sender().rect().topLeft())
        self.takeItem(self.row(self.itemAt(global_pos)))
        
    def get_string(self):
        key, val = "", ""
        for j in range(self.count()):
            item = self.itemWidget(self.item(j)).form_edit
            val += "("
            cls = ""
            for i in range(item.rowCount()):
                if j == 0:
                    key += self.val_edit[i][0]
                    key += ","
                if 'date' in self.val_edit[i][1]:
                    if item.itemAt(i, QFormLayout.FieldRole).widget().text(): val = val + "date('" + item.itemAt(i, QFormLayout.FieldRole).widget().text() + "'),"
                    elif self.val_edit[i][2]: val = val + "date('" + self.val_edit[i][2] + "'),"
                    else: return None
                elif 'int' in self.val_edit[i][1]:
                    if item.itemAt(i, QFormLayout.FieldRole).widget().text(): val = val + item.itemAt(i, QFormLayout.FieldRole).widget().text() + ","
                    elif self.val_edit[i][2]: val = val + self.val_edit[i][2] + ","
                    else: return None
                else:
                    if item.itemAt(i, QFormLayout.FieldRole).widget().text():
                        if item.itemAt(i, QFormLayout.FieldRole).widget().text() in ["I", "II", "III", "IV", "V"]:
                            cls = f"class_{item.itemAt(i, QFormLayout.FieldRole).widget().text().lower()}"
                        val = val + "'" + item.itemAt(i, QFormLayout.FieldRole).widget().text() + "',"
                    elif self.val_edit[i][2]: val = val + "'" + self.val_edit[i][2] + "',"
                    else: return None
            val = val[:-1] + "),"
        keys = key.split(",")
        key0 = f"{keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}, {keys[4]}"
        key1 = f"{keys[0]}, {keys[5]}, {keys[6]}, {keys[7]}"
        vals = val.split(",")
        val0 = f"{vals[0]}, {vals[1]}, {vals[2]}, {vals[3]}, {vals[4]}"
        val1 = f"{vals[0]}, {vals[5]}, {vals[6]}, {vals[7]}"
        return f"INSERT INTO student_info({key0}) VALUES{val0});", f"INSERT INTO students({key1}) VALUES{val1};", f"INSERT INTO {cls}({keys[0]}, GRADE) VALUES{vals[0]}, 'D');"
    
    def get_csv_string(self, file):
        key, val, cls = "", "", ""
        for j in range(len(file)):
            item = self.itemWidget(self.item(j)).form_edit
            val += "("
            if len(file[j]) != len(self.val_edit): continue
            for i in range(len(file[j])):
                if j == 0:
                    key += self.val_edit[i][0]
                    key += ","
                if 'date' in self.val_edit[i][1] and re.match(r"^\d{4}-\d{2}-\d{2}$", file[j][i]):
                    val = val + "date('" + file[j][i] + "'),"
                elif 'int' in self.val_edit[i][1]:
                    val = val + file[j][i] + ","
                elif item.itemAt(i, QFormLayout.FieldRole).widget().text():
                    if item.itemAt(i, QFormLayout.FieldRole).widget().text() in ["I", "II", "III", "IV", "V"]:
                        cls = f"class_{item.itemAt(i, QFormLayout.FieldRole).widget().text().lower()}"
                    val = val + "'" + file[j][i] + "',"
                else: return
                    
            val = val[:-1] + "),"
        keys = key.split(",")
        key0 = f"{keys[0]}, {keys[1]}, {keys[2]}, {keys[3]}, {keys[4]}"
        key1 = f"{keys[0]}, {keys[5]}, {keys[6]}, {keys[7]}"
        vals = val.split(",")
        val0 = f"{vals[0]}, {vals[1]}, {vals[2]}, {vals[3]}, {vals[4]}"
        val1 = f"{vals[0]}, {vals[5]}, {vals[6]}, {vals[7]}"
        return f"INSERT INTO student_info({key0}) VALUES{val0});", f"INSERT INTO students({key1}) VALUES{val1};", f"INSERT INTO {cls}({keys[0]}) VALUES{vals[0]};"
    def resizeEvent(self, event):
        # Call the base class resizeEvent
        super().resizeEvent(event)
        
        # Perform any additional actions upon resizing
        self.add_button.move(event.size().width()-self.add_button.width(), event.size().height()-self.add_button.height())
        
class ConditionWidget(QListWidget):
    def __init__(self, val_edit=None, parent=None):
        super().__init__(parent)
        
        self.setDragDropMode(QListWidget.NoDragDrop)
        self.resize(350, 350)
        
        self.val_edit = val_edit
        self.idx = 0
        
        self.add_button = RoundButton("plus.png", "Round Button", self)
        self.add_button.clicked.connect(self.add_new_widget)
        self.add_button.move(self.size().width()-self.add_button.width(), self.size().height()-self.add_button.height())
        
    def add_new_widget(self):
        
        cmbobx1 = QComboBox()
        cmbobx1.addItem(self.val_edit[0][0])
        for j in self.val_edit[self.idx+1][1]:
            cmbobx1.addItem(j)
        cmbobx2 = QComboBox()
        
        item = QListWidgetItem()
        
        itm = ConditionListItem(cmbobx1, cmbobx2, self)
        itm.del_button.clicked.connect(self.delete_widget)
        
        self.addItem(item)
        item.setSizeHint(itm.sizeHint())
        
        self.setItemWidget(item, itm)
        self.add_cmbo_itm(self.val_edit[0][0])
        cmbobx1.currentIndexChanged.connect(self.on_comb1_changed)
        cmbobx2.currentIndexChanged.connect(self.on_comb2_changed)
        
    def setCmbo(self, i):
        
        self.idx = i
        self.clear()
        
    def delete_widget(self):
        
        #itm = self.sender().pos()
        global_pos = self.sender().mapTo(self.sender().parent().parent().parent(), self.sender().rect().topLeft())
        self.takeItem(self.row(self.itemAt(global_pos)))
        
    def on_comb1_changed(self, index):
        self.sender().parent().cmb2.clear()
        self.add_cmbo_itm(self.sender().parent().cmb1.currentText(), self.sender().parent())
        
    def on_comb2_changed(self, index):
        txt = self.sender().parent().cmb2.itemText(index)
        self.sender().parent().removeWidget()
        if self.sender().parent().cmb1.currentText() == self.val_edit[0][0]:
            l = self.val_edit[self.sender().parent().cmb1.currentIndex()][1].split("(")
            lim = str(l[1][:-1])
            if 'In List' == txt:
                self.sender().parent().addWidget(QLineEdit())
                validator = QRegularExpressionValidator(r"^(\d{1," + lim + r"},)+$")
                self.sender().parent().wid.setValidator(validator)
            elif txt == '=':
                self.sender().parent().addWidget(QLineEdit())
                validator = QRegularExpressionValidator(r"^\d{1," + lim + r"}$")
                self.sender().parent().wid.setValidator(validator)
        elif self.sender().parent().cmb1.currentText() == "GRADE":
            if 'In List' == txt:
                self.sender().parent().addWidget(QLineEdit())
                validator = QRegularExpressionValidator(r"^((S|A|B|C|D),)+$")
                self.sender().parent().wid.setValidator(validator)
            elif txt == '=':
                self.sender().parent().addWidget(QLineEdit())
                validator = QRegularExpressionValidator(r"^(S|A|B|C|D)$")
                self.sender().parent().wid.setValidator(validator)
        else:
            if 'In List' == txt:
                self.sender().parent().addWidget(QLineEdit())
                validator = QRegularExpressionValidator(r"^((100\.00|[0-9]{1,2}(\.\d{1,2})?),)+$")
                self.sender().parent().wid.setValidator(validator)
            elif txt in ['=', '<=', '>=']:
                self.sender().parent().addWidget(QLineEdit())
                validator = QRegularExpressionValidator(r"^(100\.00|[0-9]{1,2}(\.\d{1,2})?)$")
                self.sender().parent().wid.setValidator(validator)
        
    def add_cmbo_itm(self, val, addwid = None):
        
        if not addwid:
            addwid = self.itemWidget(self.item(self.count()-1))
            
        addwid.removeWidget()
        
        if val == self.val_edit[0][0]:
            l = self.val_edit[0][1].split("(")
            lim = str(l[1][:-1])
            for i in ["In List", "="]:
                addwid.cmb2.addItem(i)
            validator = QRegularExpressionValidator(r"^(\d{1," + lim + r"},)+$")
            addwid.addWidget(QLineEdit())
            addwid.wid.setValidator(validator)
        elif val == "GRADE":
            for i in ["NULL", "In List", "="]:
                addwid.cmb2.addItem(i) #%b% or b% or %b or "____"
        else:
            for i in ["NULL", "In List", "=", "<=", ">="]:
                addwid.cmb2.addItem(i) #%b% or b% or %b or "____"
    def get_string(self):
        val = ""
        for j in range(self.count()):
            item = self.itemWidget(self.item(j))
            if self.val_edit[0][0] in item.cmb1.currentText():
                l = self.val_edit[item.cmb1.currentIndex()][1].split("(")
                lim = str(l[1][:-1])
                if 'In List' == item.cmb2.currentText():
                    txt = item.wid.text().split(",")
                    
                    if not re.match(r"^\d{1," + str(lim) + r"}$", txt[-1]): return None
                    if item.rad.isChecked(): val += f"{item.cmb1.currentText()} NOT IN ("
                    else: val += f"{item.cmb1.currentText()} IN ("
                    
                    for i in txt:
                        val += f"{i}, "
                    val = val[:-2] + ") "
                elif '=' == item.cmb2.currentText():
                    txt = item.wid.text()
                    if not txt: return None
                    if item.rad.isChecked(): val += f"{item.cmb1.currentText()} <> {txt} "
                    else: val += f"{item.cmb1.currentText()} = {txt} "
                elif 'NULL' == item.cmb2.currentText():
                    if item.rad.isChecked(): val += f"{item.cmb1.currentText()} IS NOT NULL "
                    else: val += f"{item.cmb1.currentText()} IS NULL "
            elif "GRADE" == item.cmb1.currentText():
                l = self.val_edit[item.cmb1.currentIndex()][1].split("(")
                lim = str(l[1][:-1])
                if 'In List' == item.cmb2.currentText():
                    txt = item.wid.text().split(",")
                    
                    if not re.match(r"^(S|A|B|C|D)$", txt[-1]): return None
                    if item.rad.isChecked(): val += f"{item.cmb1.currentText()} NOT IN ("
                    else: val += f"{item.cmb1.currentText()} IN ("
                    
                    for i in txt:
                        val += f"'{i}', "
                    val = val[:-2] + ") "
                elif '=' == item.cmb2.currentText():
                    txt = item.wid.text()
                    if not txt: return None
                    if item.rad.isChecked(): val += f"{item.cmb1.currentText()} <> {txt} "
                    else: val += f"{item.cmb1.currentText()} = {txt} "
                elif 'NULL' == item.cmb2.currentText():
                    if item.rad.isChecked(): val += f"{item.cmb1.currentText()} IS NOT NULL "
                    else: val += f"{item.cmb1.currentText()} IS NULL "
            else:
                if 'In List' == item.cmb2.currentText():
                    txt = item.wid.text().split(",")
                    
                    if not re.match(r"^(100\.00|[0-9]{1,2}(\.\d{1,2})?)$", txt[-1]): return None
                    if item.rad.isChecked(): val += f"{item.cmb1.currentText()} NOT IN ("
                    else: val += f"{item.cmb1.currentText()} IN ("
                    
                    for i in txt:
                        val += f"'{i}', "
                    val = val[:-2] + ") "
                elif '=' == item.cmb2.currentText():
                    txt = item.wid.text()
                    if not txt: return None
                    if item.rad.isChecked(): val += f"{item.cmb1.currentText()} <> {txt} "
                    else: val += f"{item.cmb1.currentText()} = {txt} "
                elif '<=' == item.cmb2.currentText():
                    txt = item.wid.text()
                    if not txt: return None
                    if item.rad.isChecked(): val += f"{item.cmb1.currentText()} > {txt} "
                    else: val += f"{item.cmb1.currentText()} <= {txt} "
                elif '>=' == item.cmb2.currentText():
                    txt = item.wid.text()
                    if not txt: return None
                    if item.rad.isChecked(): val += f"{item.cmb1.currentText()} < {txt} "
                    else: val += f"{item.cmb1.currentText()} >= {txt} "
                elif 'NULL' == item.cmb2.currentText():
                    if item.rad.isChecked(): val += f"{item.cmb1.currentText()} IS NOT NULL "
                    else: val += f"{item.cmb1.currentText()} IS NULL "
                
            val += "AND "
            #val = val[:-1] + "),"
        return val[:-5]
        
    def resizeEvent(self, event):
        # Call the base class resizeEvent
        super().resizeEvent(event)
        
        # Perform any additional actions upon resizing
        self.add_button.move(event.size().width()-self.add_button.width(), event.size().height()-self.add_button.height())

class UpdateItemWidget(QListWidget):
    def __init__(self, val_edit=None, parent=None):
        super().__init__(parent)
        
        self.setDragDropMode(QListWidget.NoDragDrop)
        self.resize(350, 350)
        
        self.val_edit = val_edit
        
    def add_new_widget(self, title):
        
        form_layout = QFormLayout()
        if title == "GRADE":
            validator = QRegularExpressionValidator(r"^(S|A|B|C|D)$", self)
        else:
            validator = QRegularExpressionValidator(r"^(100\.00|[0-9]{1,2}(\.\d{1,2})?)$")
        form_item = QLineEdit()
        form_item.setValidator(validator)
        form_layout.addRow(f"{title}:", form_item)
        
        item = QListWidgetItem()
        self.addItem(item)
        custom_widget = UpdateListItem(form_layout)
        custom_widget.del_button.clicked.connect(self.delete_widget)
        item.setSizeHint(custom_widget.sizeHint())
        self.setItemWidget(item, custom_widget)
        
    def delete_widget(self):
        
        global_pos = self.sender().mapTo(self.sender().parent().parent().parent(), self.sender().rect().topLeft())
        self.takeItem(self.row(self.itemAt(global_pos)))
        
    def get_string(self):
        val = ""
        for j in range(self.count()):
            item = self.itemWidget(self.item(j)).form_edit
            val += f"{item.itemAt(0, QFormLayout.LabelRole).widget().text()[:-1]} = "
            
            #print(item.itemAt(0, QFormLayout.LabelRole).widget().text()[:-1], item.itemAt(0, QFormLayout.FieldRole).widget().text())
            
            if "GRADE" == item.itemAt(0, QFormLayout.LabelRole).widget().text()[:-1]:
                if item.itemAt(0, QFormLayout.FieldRole).widget().text():
                    val = val + "'" + item.itemAt(0, QFormLayout.FieldRole).widget().text() + "',"
                else: return None
            else:
                if item.itemAt(0, QFormLayout.FieldRole).widget().text():
                    val = val + item.itemAt(0, QFormLayout.FieldRole).widget().text() + ","
                else: return None
        return val[:-1]
    
class SelectViewWidget(QListWidget):
    def __init__(self, val_edit=None, parent=None):
        super().__init__(parent)
        
        self.setDragDropMode(QListWidget.NoDragDrop)
        self.resize(350, 350)
        
        self.val_edit = val_edit
        
    def add_new_widget(self, title):
        
        form_layout = QFormLayout()
        for i in self.val_edit:
            if title == i:
                validator = QRegularExpressionValidator(r"^[a-zA-Z]{0,50}$", self)
                form_item = QLineEdit()
                form_item.setValidator(validator)
                form_layout.addRow(f"{i}:", form_item)
                break
        item = QListWidgetItem()
        self.addItem(item)
        custom_widget = SelectListItem(form_layout)
        custom_widget.del_button.clicked.connect(self.delete_widget)
        item.setSizeHint(custom_widget.sizeHint())
        self.setItemWidget(item, custom_widget)
        
    def delete_widget(self):
        
        global_pos = self.sender().mapTo(self.sender().parent().parent().parent(), self.sender().rect().topLeft())
        self.takeItem(self.row(self.itemAt(global_pos)))
        
    def get_string(self):
        val = ""
        for j in range(self.count()):
            item = self.itemWidget(self.item(j)).form_edit
            val += f"{item.itemAt(0, QFormLayout.LabelRole).widget().text()[:-1]}"
            if item.itemAt(0, QFormLayout.FieldRole).widget().text():
                val += f" AS {item.itemAt(0, QFormLayout.FieldRole).widget().text()}, "
            else:
                val += ", "
        return val[:-2]