from UtilWid1 import *
        
class add_dialog(QDialog):
    def __init__(self, val_edit=None, parent=None):
        super().__init__(parent)
        self.setMinimumSize(350, 350)
        self.setWindowTitle("Insert Entry")
        
        self.add_wid = NewItemWidget(val_edit, self)
        
        dvlayout = QVBoxLayout()
        dhlayout = QHBoxLayout()
        self.setLayout(dvlayout)
        
        #self.add_wid.add_new_widget()
        self.import_button = QPushButton("Import")
        #self.import_button.clicked.connect(self.import_item)
        
        self.submit_button = QPushButton("Submit")
        #self.submit_button.clicked.connect(self.place_item)
        
        h_wid = QWidget()
        h_wid.setLayout(dhlayout)
        
        dhlayout.addWidget(self.import_button)
        dhlayout.addWidget(self.submit_button)
        dvlayout.addWidget(self.add_wid)
        dvlayout.addWidget(h_wid)
        
class rem_dialog(QDialog):
    def __init__(self, val_edit, parent=None):
        super().__init__(parent)
        self.setMinimumSize(350, 350)
        self.setWindowTitle("Remove Entry")
        
        self.cnd_hed = QComboBox()
        for i in val_edit[1:]:
            self.cnd_hed.addItem(i[0])
        self.cnd_wid = ConditionWidget(val_edit)
        dvlayout = QVBoxLayout()
        self.setLayout(dvlayout)
        
        self.submit_button = QPushButton("Submit")
        #self.submit_button.clicked.connect(self.delete_item)
        self.cnd_hed.currentIndexChanged.connect(self.on_comb_changed)
        
        dvlayout.addWidget(self.cnd_hed)
        dvlayout.addWidget(self.cnd_wid)
        dvlayout.addWidget(self.submit_button)
        
    def on_comb_changed(self, index):
        self.cnd_wid.setCmbo(index)
        
    def get_cnd_string(self):
        return self.cnd_wid.get_string()
    
class updateN_dialog(QDialog):
    def __init__(self, val_edit, parent=None):
        super().__init__(parent)
        self.setMinimumSize(350, 350)
        self.setWindowTitle("Update Name")
        
        self.val_edit = val_edit
        layout = QVBoxLayout()
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        hlayout3 = QHBoxLayout()
        hlayout4 = QHBoxLayout()
        
        labl1 = QLabel(val_edit[0])
        self.ln_edt1 = QLineEdit()
        l = val_edit[1].split("(")
        lim = str(l[1][:-1])
        validator = QRegularExpressionValidator(r"^\d{1," + lim + r"}$")
        self.ln_edt1.setValidator(validator)
        
        validator = QRegularExpressionValidator(r"^[a-zA-Z ]+$")
        labl2 = QLabel("Name: ")
        self.ln_edt2 = QLineEdit()
        self.ln_edt2.setValidator(validator)
        
        labl3 = QLabel("First Name: ")
        self.ln_edt3 = QLineEdit()
        self.ln_edt3.setValidator(validator)
        
        labl4 = QLabel("Last Name: ")
        self.ln_edt4 = QLineEdit()
        self.ln_edt4.setValidator(validator)
        
        self.submit_button = QPushButton("Submit")
        
        hlayout1.addWidget(labl1)
        hlayout2.addWidget(labl2)
        hlayout3.addWidget(labl3)
        hlayout4.addWidget(labl4)
        
        hlayout1.addWidget(self.ln_edt1)
        hlayout2.addWidget(self.ln_edt2)
        hlayout3.addWidget(self.ln_edt3)
        hlayout4.addWidget(self.ln_edt4)
        
        layout.addLayout(hlayout1)
        layout.addLayout(hlayout2)
        layout.addLayout(hlayout3)
        layout.addLayout(hlayout4)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)
        
    def get_string(self):
        if not self.ln_edt1.text() or not self.ln_edt2.text() or not self.ln_edt3.text() or not self.ln_edt4.text() or not self.ln_edt3.text() in self.ln_edt2.text() or not self.ln_edt4.text() in self.ln_edt2.text(): return
        cmd1 = f"UPDATE student_info SET NAME = '{self.ln_edt2.text()}' WHERE {self.val_edit[0]} = {self.ln_edt1.text()};"
        cmd2 = f"UPDATE students SET FIRST_NAME = '{self.ln_edt3.text()}', LAST_NAME = '{self.ln_edt4.text()}' WHERE {self.val_edit[0]} = {self.ln_edt1.text()};"
        return cmd1, cmd2, self.ln_edt1.text()
    
    
class updateA_dialog(QDialog):
    def __init__(self, val_edit, parent=None):
        super().__init__(parent)
        self.setMinimumSize(350, 350)
        self.setWindowTitle("Update Name")
        
        self.val_edit = val_edit
        layout = QVBoxLayout()
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        
        labl1 = QLabel(val_edit[0])
        self.ln_edt1 = QLineEdit()
        l = val_edit[1].split("(")
        lim = str(l[1][:-1])
        validator = QRegularExpressionValidator(r"^\d{1," + lim + r"}$")
        self.ln_edt1.setValidator(validator)
        
        #validator = QRegularExpressionValidator(r"^[a-zA-Z ]+$")
        labl2 = QLabel("Name: ")
        self.ln_edt2 = QLineEdit()
        
        self.submit_button = QPushButton("Submit")
        
        hlayout1.addWidget(labl1)
        hlayout2.addWidget(labl2)
        hlayout1.addWidget(self.ln_edt1)
        hlayout2.addWidget(self.ln_edt2)
        
        layout.addLayout(hlayout1)
        layout.addLayout(hlayout2)
        layout.addWidget(self.submit_button)
        
        self.setLayout(layout)
        
    def get_string(self):
        if not self.ln_edt1.text() or not self.ln_edt2.text(): return
        cmd = f"UPDATE student_info SET HOME_ADDRESS = '{self.ln_edt2.text()}' WHERE {self.val_edit[0]} = {self.ln_edt1.text()};"
        return cmd, self.ln_edt1.text()
        
        
class updateM_dialog(QDialog):
    def __init__(self, val_edit, parent=None):
        super().__init__(parent)
        self.setMinimumSize(350, 350)
        self.setWindowTitle("Update Columns")
        
        layout = QVBoxLayout()
        dvlayout = QVBoxLayout()
        
        tab_widget = QTabWidget(self)
        self.tab1 = QWidget()
        self.cnd_hed = QComboBox()
        for i in val_edit[1:]:
            self.cnd_hed.addItem(i[0])
        
        self.cmb_box = QComboBox()
        for i in val_edit[1][1]:
            self.cmb_box.addItem(i)
        self.upd_wid = UpdateItemWidget(val_edit)
        self.cnd_wid = ConditionWidget(val_edit)
        self.submit_button = QPushButton("Submit")
        
        tab_widget.addTab(self.tab1, "Updates")
        tab_widget.addTab(self.cnd_wid, "Condition")
        
        layout.addWidget(self.cmb_box)
        layout.addWidget(self.upd_wid)
        
        dvlayout.addWidget(self.cnd_hed)
        dvlayout.addWidget(tab_widget)
        dvlayout.addWidget(self.submit_button)
        
        self.tab1.setLayout(layout)
        self.setLayout(dvlayout)
        
        self.cnd_hed.currentIndexChanged.connect(self.on_hed_changed)
        self.cmb_box.currentIndexChanged.connect(self.on_cmb_changed)
        #self.upd_wid.add_new_widget(self.cmb_box.currentText())
        
    def on_hed_changed(self):
        
        self.cmb_box.clear()
        self.upd_wid.clear()
        for i in self.upd_wid.val_edit[self.cnd_hed.currentIndex()+1][1]:
            self.cmb_box.addItem(i)
        self.cnd_wid.setCmbo(self.cnd_hed.currentIndex())
        self.on_cmb_changed()
        
    def on_cmb_changed(self):
        
        for i in range(self.upd_wid.count()):
            if self.upd_wid.itemWidget(self.upd_wid.item(i)).form_edit.itemAt(0, QFormLayout.LabelRole) and self.cmb_box.currentText() in self.upd_wid.itemWidget(self.upd_wid.item(i)).form_edit.itemAt(0, QFormLayout.LabelRole).widget().text():
                return
        self.upd_wid.add_new_widget(self.cmb_box.currentText())
        
    def get_upd_string(self):
        return self.upd_wid.get_string()
    
    def get_cnd_string(self):
        return self.cnd_wid.get_string()
    
    def reset(self):
        
        self.cmb_box.clear()
        self.upd_wid.clear()
        self.cnd_wid.clear()
        for i in self.upd_wid.val_edit[self.cnd_hed.currentIndex()+1][1]:
            self.cmb_box.addItem(i)
        
class SelectView(QWidget):
    def __init__(self, val_edit, parent=None):
        super().__init__(parent)
        self.setMinimumSize(350, 350)
        self.setWindowTitle("Update Columns")
        
        dvlayout = QVBoxLayout()
        layout = QVBoxLayout()
        
        tab_widget = QTabWidget(self)
        self.tab1 = QWidget()
        
        ###############################
        self.cnd_hed = QComboBox()
        for i in val_edit[1:]:
            self.cnd_hed.addItem(i[0])
        self.tbl_hed = QComboBox()
        for i in val_edit[1][1]:
            self.tbl_hed.addItem(i)
            
        self.cnd_wid = ConditionWidget(val_edit)
        dvlayout = QVBoxLayout()
        self.setLayout(dvlayout)
        
        self.cnd_hed.currentIndexChanged.connect(self.on_comb_changed)
        self.tbl_hed.currentIndexChanged.connect(self.on_cmbo_changed)
        
        self.sel_wid = SelectViewWidget(val_edit[1][1])
        
        tab_widget.addTab(self.tab1, "Updates")
        tab_widget.addTab(self.cnd_wid, "Condition")
        
        layout.addWidget(self.tbl_hed)
        layout.addWidget(self.sel_wid)
        
        dvlayout.addWidget(self.cnd_hed)
        dvlayout.addWidget(tab_widget)
        #dvlayout.addWidget(self.view_button)
        self.tab1.setLayout(layout)
        self.setLayout(dvlayout)
        
        self.sel_wid.add_new_widget(self.tbl_hed.currentText())
        
        
    def on_comb_changed(self, index):
        self.tbl_hed.clear()
        for i in self.cnd_wid.val_edit[index+1][1]:
            self.tbl_hed.addItem(i)
        self.sel_wid.val_edit = self.cnd_wid.val_edit[index+1][1]
        self.cnd_wid.setCmbo(index)
        self.sel_wid.clear()
        
    def on_cmbo_changed(self):
        self.sel_wid.add_new_widget(self.tbl_hed.currentText())
        
    def get_sel_string(self):
        return self.sel_wid.get_string()
    
    def get_cnd_string(self):
        return self.cnd_wid.get_string()
    
    def reset(self):
        self.tbl_hed.clear()
        self.sel_wid.clear()
        self.cnd_wid.clear()
        #self.sel_wid.val_edit = val_edit
        #self.cnd_wid.val_edit = val_edit
        
        
ZOOM_MULTIPLIER = math.sqrt(2.0)

class pdf_edit(QPdfView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_document = QPdfDocument(self)
        self.setDocument(self.m_document)
        self.setMinimumSize(400, 400)
        
        sizePol = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePol.setHorizontalStretch(10)
        sizePol.setVerticalStretch(0)
        sizePol.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePol)
        self.setZoomFactor(0.4)
        
    def page_selected(self, page):
        nav = self.pageNavigator()
        nav.jump(page, QPoint(), nav.currentZoom())
    
    def open_file(self):
        self.m_document.load("output.pdf")
        #document_title = self.m_document.metaData(QPdfDocument.MetaDataField.Title)
        #self.setWindowTitle(document_title if document_title else "PDF Viewer")
        self.page_selected(0)
        #self.m_pageSelector.setMaximum(self.m_document.pageCount() - 1)
    
    def zmin_click(self):
        factor = self.zoomFactor() * ZOOM_MULTIPLIER
        self.setZoomFactor(factor)
    
    def zmout_click(self):
        factor = self.zoomFactor() / ZOOM_MULTIPLIER
        self.setZoomFactor(factor)
    
    def Cntnus_click(self, state):
        #cont_checked = self.ui.actionContinuous.isChecked()
        mode = QPdfView.PageMode.MultiPage if state == Qt.Checked else QPdfView.PageMode.SinglePage
        self.setPageMode(mode)
        
class pdfview_dialog(QDialog):
    def __init__(self, val_edit, parent=None):
        super().__init__(parent)
        self.setMinimumSize(750, 600)
        self.setWindowTitle("PDF View")
        
        wid1 = QWidget(self)
        wid2 = QWidget(self)
        layout = QHBoxLayout()
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        vlayout1 = QVBoxLayout()
        vlayout2 = QVBoxLayout()
        splitter1 = QSplitter(self)
        splitter1.setOrientation(Qt.Horizontal)
        splitter1.setHandleWidth(10)
        splitter2 = QSplitter(self)
        splitter2.setOrientation(Qt.Vertical)
        splitter2.setHandleWidth(10)
        splitter1.setStyleSheet("QSplitter::handle { background-color: #D3D3D3; }")
        splitter2.setStyleSheet("QSplitter::handle { background-color: #D3D3D3; }")
        layout.setContentsMargins(11, 11, 11, 11)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.pdfView = pdf_edit(self)
        self.sel_view = SelectView(val_edit)
        self.view_button = QPushButton("View")
        self.zmin_button = QPushButton("Zoom In")
        self.zmout_button = QPushButton("Zoom OUT")
        self.cntnus_button = QCheckBox("Continous Page")
        
        self.zmin_button.clicked.connect(self.pdfView.zmin_click)
        self.zmout_button.clicked.connect(self.pdfView.zmout_click)
        self.cntnus_button.stateChanged.connect(self.pdfView.Cntnus_click)
        #self.submit_button = QPushButton("Submit")
        
        splitter1.addWidget(wid1)
        splitter1.addWidget(splitter2)
        
        splitter2.addWidget(self.sel_view)
        splitter2.addWidget(wid2)
        
        f_lay1 = QFormLayout()
        self.col_widths = QLineEdit()
        validator = QRegularExpressionValidator(r"^(?!0\d)(\d{1},){0,9}$")
        self.col_widths.setValidator(validator)
        f_lay1.addRow("Column Width", self.col_widths)
        
        f_lay2 = QFormLayout()
        self.left_margin = QLineEdit()
        validator = QRegularExpressionValidator(r"^\d{1,2}$")
        self.left_margin.setValidator(validator)
        f_lay2.addRow("Left Margin", self.left_margin)
        
        f_lay3 = QFormLayout()
        self.right_margin = QLineEdit()
        self.right_margin.setValidator(validator)
        f_lay3.addRow("Right Margin", self.right_margin)
        
        hlayout1.addWidget(self.zmin_button)
        hlayout1.addWidget(self.zmout_button)
        hlayout1.addWidget(self.cntnus_button)
        vlayout1.addWidget(self.pdfView)
        vlayout1.addLayout(hlayout1)
        
        hlayout2.addLayout(f_lay2)
        hlayout2.addLayout(f_lay3)
        vlayout2.addLayout(f_lay1)
        vlayout2.addLayout(hlayout2)
        vlayout2.addWidget(self.view_button)
        #vlayout.addWidget(self.submit_button)
        layout.addWidget(splitter1)
        
        wid1.setLayout(vlayout1)
        wid2.setLayout(vlayout2)
        self.setLayout(layout)
        
    def get_string(self):
        return self.sel_view.get_sel_string(), self.sel_view.get_cnd_string()
    
    def reset(self):
        self.sel_view.reset()
    
    def view_to_pdf(self, clm, data):
        #self.col_widths = [200, 500, 350, 200, 200, 500, 350, 200]
        # Page size and margin
        page_width, page_height = letter
        
        if self.left_margin.text():
            left_margin = int(self.left_margin.text())
        else:
            left_margin = 0
        if self.right_margin.text():
            right_margin = int(self.right_margin.text())
        else:
            right_margin = 0
        
        # Calculate available width for table
        available_width = page_width - left_margin - right_margin
        
        # Check if total width of columns exceeds available width
        c = self.col_widths.text().split(",")
        wid_lst = []
        for width in self.col_widths.text().split(","):
            if width != "":
                wid_lst.append(int(width)*100)
        
        if self.sel_view.sel_wid.count() != 0:
            if len(wid_lst) == self.sel_view.sel_wid.count():
                total_width = sum(wid_lst)
            else:
                for i in range(self.sel_view.sel_wid.count() - len(wid_lst)):
                    wid_lst.append(100)
                total_width = sum(wid_lst)
        elif len(wid_lst) == len(clm):
            total_width = sum(wid_lst)
        else:
            for i in range(len(clm) - len(wid_lst)):
                wid_lst.append(100)
            total_width = sum(wid_lst)
        
        if total_width > available_width:
            # Calculate scaling factor for reducing column widths
            scale_factor = available_width / total_width
            col_widths = [int(width) * scale_factor for width in wid_lst]
        else:
            col_widths = wid_lst
        # Create PDF
        pdf = SimpleDocTemplate("output.pdf", pagesize=letter, leftMargin=left_margin, rightMargin=right_margin)
        elements = []
        
        row_data = []
        
        for item, width in zip(clm, col_widths):
            paragraph = Paragraph(item, getSampleStyleSheet()['BodyText'])
            row_data.append(paragraph)
        elements.append(row_data)
        # Add table data
        for row in data:
            row_data = []
            for item, width in zip(row, col_widths):
                paragraph = Paragraph(str(item), getSampleStyleSheet()['BodyText'])
                row_data.append(paragraph)
            elements.append(row_data)
        
        # Create table
        table = Table(elements, colWidths=col_widths)
        
        # Add style to table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
        
        table.setStyle(style)
        # Start a new page before each row if it doesn't fit entirely on the current page
        if table.split(0, 1):
            for row in table.split(0, 1):
                # Calculate the height of the row
                row_height = sum(row.heights)
                
                # Calculate the remaining space on the current page
                remaining_space = pdf.bottomMargin + pdf._frame._height - pdf._curPos[1]
                
                # Check if the row fits on the current page
                if remaining_space < row_height:
                    # Start a new page
                    pdf.add_page()
                
                # Add the row to the document
                pdf.build([row])
                # Add table to the PDF
        else:
            pdf.build([table])
        
        self.pdfView.open_file()
        
class SimpleDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle(message)

        # Set up the layout and label
        layout = QVBoxLayout()
        hlayout = QHBoxLayout()
        label = QLabel(message)
        layout.addWidget(label)
        label.setWordWrap(True)
        
        # Add a close button
        yes = QPushButton("Yes")
        no = QPushButton("No")
        yes.clicked.connect(self.yes_clicked)
        no.clicked.connect(self.no_clicked)
        hlayout.addWidget(no)
        hlayout.addWidget(yes)
        
        layout.addLayout(hlayout)
        self.setLayout(layout)
    
    def yes_clicked(self):
        self.click = True
        self.close()
        
    def no_clicked(self):
        self.click = False
        self.close()
        
        
import sqlite3

class mainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.table_name = 'student_info'
        self.resize(640, 480)
        self.setWindowTitle("Main Application")
        self.table_wid = QTableWidget(self)
        self.table_wid.insertRow(0)
        mainWidget = QWidget(self)
        
        #self.mydb = mysql.connector.connect(host="localhost", user="root", password="akshay", database="school")
        self.mydb = sqlite3.connect("example.db")
        self.create_bar()
        self.init_struct()
        self.init_addclm()
        #print(self.val_edit)
        self.add_dialog = add_dialog(self.newent_clm, self)
        self.rem_dialog = rem_dialog(self.val_edit, self)
        self.upd_name = updateN_dialog(self.val_edit[0], self)
        self.upd_adrs = updateA_dialog(self.val_edit[0], self)
        self.upd_mark = updateM_dialog(self.val_edit, self)
        self.pdf_view = pdfview_dialog(self.val_edit, self)
        
        self.add_dialog.import_button.clicked.connect(self.import_item)
        self.add_dialog.submit_button.clicked.connect(self.place_item)
        self.upd_name.submit_button.clicked.connect(self.update_name)
        self.upd_adrs.submit_button.clicked.connect(self.update_adrs)
        self.upd_mark.submit_button.clicked.connect(self.update_mark)
        #self.pdf_view.submit_button.clicked.connect(self.dwnld_pdf)
        self.pdf_view.view_button.clicked.connect(self.view_pdf)
        self.view_all()
        
        vLayout = QVBoxLayout()
        hLayout = QHBoxLayout()
        tool_wid = QWidget()
        
        mainWidget.setLayout(vLayout)
        tool_wid.setLayout(hLayout)
            
        self.table_wid.itemChanged.connect(self.item_cng)
        
        vLayout.addWidget(self.table_wid)
        vLayout.addWidget(tool_wid)
        
        self.setCentralWidget(mainWidget)
    
    def init_addclm(self):
        
        #for i in self.clm_Type:
        #    self.newent_clm.append(i)
        self.newent_clm = []
        mycursor = self.mydb.cursor()#buffered=True
        mycursor.execute('PRAGMA table_info(student_info);')
        for i, idx in enumerate(mycursor):
            #if idx[5] != 'auto_increment':
            if idx[2] == 'date':
                self.newent_clm.append([idx[1], idx[2], idx[4]])
            elif 'int' in idx[2]:
                self.newent_clm.append([idx[1], idx[2], idx[4]])
            elif 'varchar' in idx[2]:
                self.newent_clm.append([idx[1], idx[2], idx[4]])
            
        mycursor = self.mydb.cursor()#buffered=True
        mycursor.execute('PRAGMA table_info(students);')
        for i, idx in enumerate(mycursor):
            cpy = True
            for j in self.column:
                if j[1] == idx[1]:
                    cpy = False
                    break
            if cpy:# and idx[5] != 'auto_increment':
                if idx[2] == 'date':
                    self.newent_clm.append([idx[1], idx[2], idx[4]])
                elif 'int' in idx[2]:
                    self.newent_clm.append([idx[1], idx[2], idx[4]])
                elif 'varchar' in idx[2]:
                    self.newent_clm.append([idx[1], idx[2], idx[4]])
                    
        self.mydb.commit()
                    
    def init_struct(self):
        
        mycursor = self.mydb.cursor()#buffered=True
        self.val_edit = []
        self.val_edit.append(['ENROLL_UID', 1])
        
        for clm in ['class_i', 'class_ii', 'class_iii', 'class_iv', 'class_v']:
            mycursor.execute(f'PRAGMA table_info({clm});')#f'DESCRIBE {clm}')
            self.val_edit.append([clm, []])
            for i, idx in enumerate(mycursor):
                #print(idx)
                #if i != 0 and idx[5] != 'auto_increment':
                self.val_edit[-1][1].append(idx[1])
                    
        
        mycursor = self.mydb.cursor()#buffered=True
        mycursor.execute(f'PRAGMA table_info({self.table_name});')#f'DESCRIBE {self.table_name}')
        self.column_list, self.clm_Type, self.column = [], [], []
        for i, idx in enumerate(mycursor):
            self.table_wid.insertColumn(i)
            self.column.append(idx)
            self.column_list.append(idx[1])
        self.mydb.commit()
        self.table_wid.setHorizontalHeaderLabels(self.column_list)
        
        for i in range(len(self.column)):
            #if self.column[i][5] != 'auto_increment':
            if self.column[i][2] == 'date':
                self.clm_Type.append([self.column[i][1], self.column[i][2], self.column[i][4]])
            elif 'int' in self.column[i][2]:
                if self.column[i][1] == 'ENROLL_UID':
                    self.val_edit[0][1] = self.column[i][2]
                self.clm_Type.append([self.column[i][1], self.column[i][2], self.column[i][4]])
            elif 'varchar' in self.column[i][2]:
                self.clm_Type.append([self.column[i][1], self.column[i][2], self.column[i][4]])
        
    def create_bar(self):
        
        menuBar = self.menuBar()
        
        # Add a menu to the menu bar
        fileMenu = menuBar.addMenu("File")
        stdMenu = menuBar.addMenu("Student")
        updateMenu = menuBar.addMenu("Update")
        viewMenu = menuBar.addMenu("View")
        
        # Add an action to the menu
        addAction = QAction("New Student", self)
        addAction.triggered.connect(self.add_click)
        stdMenu.addAction(addAction)
        
        removeAction = QAction("Drop Student", self)
        removeAction.triggered.connect(self.rem_click)
        stdMenu.addAction(removeAction)
        
        prmAction = QAction("Promote Student", self)
        prmAction.triggered.connect(self.prm_click)
        stdMenu.addAction(prmAction)
        
        updAction = QAction("Name", self)
        updAction.triggered.connect(self.updnme_click)
        updateMenu.addAction(updAction)
        
        updAction = QAction("Address", self)
        updAction.triggered.connect(self.updadr_click)
        updateMenu.addAction(updAction)
        
        updAction = QAction("Marks", self)
        updAction.triggered.connect(self.updmrk_click)
        updateMenu.addAction(updAction)
        
        pdfAction = QAction("PDF View", self)
        pdfAction.triggered.connect(self.pdf_click)
        viewMenu.addAction(pdfAction)
        
        openMenu = QMenu("Open", self)
        mycursor = self.mydb.cursor()#buffered=True
        mycursor.execute("SELECT name FROM sqlite_master WHERE type='table';")#"SELECT table_name FROM information_schema.TABLES WHERE table_schema = 'school';")
        
        for x in mycursor:
            if x[0] == 'sqlite_sequence': continue
            action = QAction(x[0], self)
            action.triggered.connect(self.open_table)
            openMenu.addAction(action)
        
        fileMenu.addMenu(openMenu)
        
        exitAction = QAction("Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)
        
    def showContextMenu(self, pos):
        # Show the modified context menu at the given position
        selitm = self.widget_list.itemAt(pos)
        if selitm:
            self.selrow = self.widget_list.row(selitm)
        else:
            self.selrow = -1
        self.context_menu.exec(self.widget_list.mapToGlobal(pos))
        
    def add_click(self):
        
        self.add_dialog.add_wid.add_new_widget()
        self.add_dialog.exec()
        self.add_dialog.add_wid.clear()
        
    def rem_click(self):
        self.rem_dialog.setWindowTitle("Remove Student")
        self.rem_dialog.submit_button.clicked.connect(self.delete_item)
        self.rem_dialog.cnd_wid.add_new_widget()
        self.rem_dialog.exec()
        self.rem_dialog.cnd_wid.clear()
       
    def prm_click(self):
        self.rem_dialog.setWindowTitle("Promote Student")
        self.rem_dialog.submit_button.clicked.connect(self.promot_item)
        self.rem_dialog.cnd_wid.add_new_widget()
        self.rem_dialog.exec()
        self.rem_dialog.cnd_wid.clear()
        
    def updnme_click(self):
        self.upd_name.setWindowTitle("Update Name")
        self.upd_name.exec()
        #self.upd_clm.reset(self.column, self.clm_Type)
        
        #print("Update Clicked")
        
    def updadr_click(self):
        self.upd_adrs.setWindowTitle("Update Address")
        self.upd_adrs.exec()
        #self.upd_clm.reset(self.column, self.clm_Type)
        
        #print("Update Clicked")
        
    def updmrk_click(self):
        self.upd_mark.setWindowTitle("Update Marks")
        self.upd_mark.exec()
        self.upd_mark.reset()
        
        #print("Update Clicked")
        
    def pdf_click(self):
        self.pdf_view.exec()
        self.pdf_view.reset()
        
        #print("PDF View Clicked")
        
    def open_table(self):
        
        txt = self.sender().text().split(" ")
        self.table_name = txt[-1]
        #print(self.table_name)
        cmd = f"SELECT * FROM {txt[-1]} LIMIT 50 OFFSET 1;"
        if not self.run_cmd(cmd): return
        self.table_wid.clear()
        self.table_wid.setColumnCount(0)
        self.table_wid.setRowCount(0)
        self.init_struct()
        self.view_all()
        #print("open table", cmd)
        
    def view_pdf(self):
        
        cmd = "SELECT "
        sel_cnd = self.pdf_view.get_string()
        #print(sel_cnd)
        if sel_cnd[0]:
            cmd += f"{sel_cnd[0]} FROM {self.pdf_view.sel_view.cnd_hed.currentText()} "
            if sel_cnd[1]:
                cmd += f"WHERE {sel_cnd[1]};"
            elif self.pdf_view.sel_view.cnd_wid.count() == 0:
                cmd = cmd[:-1] + ";"
            else:
                return
        else:
            cmd += f"* FROM {self.pdf_view.sel_view.cnd_hed.currentText()} "
            if sel_cnd[1]:
                cmd += f"WHERE {sel_cnd[1]};"
            elif self.pdf_view.sel_view.cnd_wid.count() == 0:
                cmd = cmd[:-1] + ";"
            else:
                return
        
        #print(cmd)
        try:
            mycursor = self.mydb.cursor()#buffered = True
            mycursor.execute(cmd)
            self.mydb.commit()
            column_names = [column[0] for column in mycursor.description]
            self.pdf_view.view_to_pdf(column_names, mycursor.fetchall())
        except mysql.connector.Error as e:
            ee = str(e)
            print(ee)
            return
        
    def promot_item(self):
        cnd = self.rem_dialog.get_cnd_string()
        if not cnd: return
        cmd = f"SELECT ENROLL_UID FROM {self.rem_dialog.cnd_hed.currentText()} Where {cnd};"
        dialog = SimpleDialog(f"Are you sure you want to promote by the consition {cnd}?", self.rem_dialog)
        dialog.exec()
        if not dialog.click: return
        
        #print(cmd)
        try:
            mycursor = self.mydb.cursor()#buffered = True
            mycursor.execute(cmd)
            self.mydb.commit()
        except mysql.connector.Error as e:
            ee = str(e)
            print(ee)
            return
        for i, idx in enumerate(mycursor):
            cmd = f"DELETE FROM {self.rem_dialog.cnd_hed.currentText()} Where ENROLL_UID = {idx[0]};"
            #print(cmd)
            if not self.run_cmd(cmd): return
            j = self.rem_dialog.cnd_hed.currentIndex()
            
            if len(self.val_edit) == j+2:
                cmd = f"DELETE FROM students Where ENROLL_UID = {idx[0]};"
                print(cmd)
                if not self.run_cmd(cmd): return
                cmd = f"DELETE FROM student_info Where ENROLL_UID = {idx[0]};"
                #print(cmd)
                if not self.run_cmd(cmd): return
            else:
                txt = self.val_edit[j+2][0].split("_")
                cmd = f"UPDATE students SET CLASS_ID = '{txt[-1].upper()}' Where ENROLL_UID = {idx[0]};"
                #print(cmd)
                if not self.run_cmd(cmd): return
                cmd = f"INSERT INTO {self.val_edit[j+2][0]}(ENROLL_UID, GRADE) VALUES({idx[0]}, 'D');"
                #print(cmd)
                if not self.run_cmd(cmd): return
        
        self.rem_dialog.close()
        self.table_wid.setRowCount(0)
        self.view_all()
        
    def delete_item(self):
        cnd = self.rem_dialog.get_cnd_string()
        cmd = f"SELECT ENROLL_UID FROM {self.rem_dialog.cnd_hed.currentText()} Where {cnd};"
        
        dialog = SimpleDialog(f"Are you sure you want to delete by the consition {cnd}?", self.rem_dialog)
        dialog.exec()
        if not dialog.click: return
        
        #print(cmd)
        try:
            mycursor = self.mydb.cursor()#buffered = True
            mycursor.execute(cmd)
            self.mydb.commit()
        except mysql.connector.Error as e:
            ee = str(e)
            print(ee)
            return
        for i, idx in enumerate(mycursor):
            cmd = f"DELETE FROM {self.rem_dialog.cnd_hed.currentText()} Where ENROLL_UID = {idx[0]};"
            #print(cmd)
            if not self.run_cmd(cmd): return
            cmd = f"DELETE FROM students Where ENROLL_UID = {idx[0]};"# AND CLASS_ID = '{cls[-1].upper()}'
            #print(cmd)
            if not self.run_cmd(cmd): return
            cmd = f"DELETE FROM student_info Where ENROLL_UID = {idx[0]};"
            #print(cmd)
            if not self.run_cmd(cmd): return
            
            self.rem_dialog.close()
            self.mydb.commit()
        
        self.table_wid.setRowCount(0)
        self.view_all()
        
    def run_cmd(self, cmd):
        try:
            mycursor = self.mydb.cursor()#buffered = True
            mycursor.execute(cmd)
            self.mydb.commit()
            return True
        except mysql.connector.Error as e:
            ee = str(e)
            print(ee)
            return
        
    def import_item(self):
        
        my_list = []
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)", options=options)
        
        if not file_name:
            return
        #print(file_name)
        with open(file_name, mode ='r')as file:
            csvFile = csv.reader(file)
            for row in csvFile:
                my_list.append(row)
            cmd = self.add_dialog.add_wid.get_csv_string(my_list)
            
            if not self.run_cmd(cmd): return
            self.add_dialog.close()
            self.mydb.commit()
            self.view_all()
            
    def place_item(self):
        
        cmd = self.add_dialog.add_wid.get_string()
        if not cmd:
            return
        #print(cmd)
        dialog = SimpleDialog("Are you sure you want to insert the items?", self.add_dialog)
        dialog.exec()
        if not dialog.click: return
        #cmd = f"INSERT INTO student_info({key[:-1]}) VALUES({val[:-1]});"
        mycursor = self.mydb.cursor()
        try:
            mycursor.execute(cmd[0])
            self.mydb.commit()
            mycursor.execute(cmd[1])
            self.mydb.commit()
            mycursor.execute(cmd[2])
            self.add_dialog.close()
            self.view_all()
    
        except 'MySQLInterfaceError' as e:
            print(e)
        
    def update_name(self):
        cmd = self.upd_name.get_string()
        if not cmd: return
        #print(cmd)
        dialog = SimpleDialog(f"Are you sure you want to update the name of {cmd[2]}?", self.upd_name)
        dialog.exec()
        if not dialog.click: return
        
        if not self.run_cmd(cmd[0]): return
        if not self.run_cmd(cmd[1]): return
        self.upd_name.close()
        self.table_wid.setRowCount(0)
        self.view_all()
        
    def update_adrs(self):
        cmd = self.upd_adrs.get_string()
        if not cmd: return
        #print(cmd)
        dialog = SimpleDialog(f"Are you sure you want to update the address of {cmd[1]}?", self.upd_adrs)
        dialog.exec()
        if not dialog.click: return
        
        if not self.run_cmd(cmd[0]): return
        self.upd_adrs.close()
        self.table_wid.setRowCount(0)
        self.view_all()
        
    def update_mark(self):
        upd = self.upd_mark.get_upd_string()
        if upd:
            cmd = f"UPDATE {self.upd_mark.cnd_hed.currentText()} SET {upd} "
        else:
            return
        cnd = self.upd_mark.get_cnd_string()
        if cnd:
            cmd += f"WHERE {self.upd_mark.get_cnd_string()};"
        elif self.upd_mark.cnd_wid.count() ==0:
            cmd += ";"
        else:
            return
        #print(cmd)
        dialog = SimpleDialog(f"Are you sure you want to update the marks of {self.upd_mark.get_cnd_string()}?", self.upd_mark)
        dialog.exec()
        if not dialog.click: return
        
        if not self.run_cmd(cmd): return
        self.upd_mark.close()
        self.table_wid.setRowCount(0)
        self.view_all()
        
    #def dwnld_pdf(self):
    #    if self.pdf_view.file_loc:
    #        if self.pdf_view.cmd:
                #self.pdf_view.view_to_pdf()
    #            self.pdf_view.close()
    #    else:
    #        return#self.pdfView.file_loc
        
    def view_all(self):
        mycursor = self.mydb.cursor()#buffered=True
        mycursor.execute(f"SELECT * FROM {self.table_name}")
        
        self.table_wid.clearContents()
        for i, idx in enumerate(mycursor):
            #print(idx)
            if self.table_wid.rowCount() <= i:
                self.table_wid.insertRow(i)
            for j in range(len(idx)):
                if self.column[j][3] == 'PRI':
                    itm = QTableWidgetItem(str(idx[0]))
                    self.table_wid.setItem(i, j, itm)
                    itm.setFlags(itm.flags() & ~Qt.ItemIsEditable)
                else:
                    self.table_wid.setItem(i, j, QTableWidgetItem(str(idx[j])))
        self.mydb.commit()
        
    def item_cng(self, item):
        
        row = item.row()
        mycursor = self.mydb.cursor()#buffered=True
        edit_clm = self.table_wid.horizontalHeaderItem(item.column()).text()
        typ = self.column[item.column()][1]
        
        if 'date' == typ:
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", item.text()):
                mycursor.execute(f"SELECT {edit_clm} FROM {self.table_name} WHERE {self.table_wid.horizontalHeaderItem(0).text()}={self.table_wid.item(row, 0).text()};")
                for x in mycursor:
                    item.setText(str(x[0]))
                self.mydb.commit()
            else:
                cmd = f"UPDATE {self.table_name} SET {edit_clm}=date('{item.text()}') WHERE {self.table_wid.horizontalHeaderItem(0).text()}={self.table_wid.item(row, 0).text()};"
                mycursor.execute(cmd)
                mycursor.execute("SELECT * FROM student_info")
                #for x in mycursor:
                #    print(x)
                self.mydb.commit()
        elif 'varchar' in typ:
            cmd = f"UPDATE {self.table_name} SET {edit_clm}='{item.text()}' WHERE {self.table_wid.horizontalHeaderItem(0).text()}={self.table_wid.item(row, 0).text()};"
            mycursor.execute(cmd)
            mycursor.execute("SELECT * FROM student_info")
            #for x in mycursor:
            #    print(x)
            self.mydb.commit()
        
app = QApplication(sys.argv)
window = mainApp()
window.show()

sys.exit(app.exec())
#del app