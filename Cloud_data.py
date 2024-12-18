import sys
import nidaqmx
import openpyxl
from openpyxl import Workbook
import os
from nidaqmx.constants import TerminalConfiguration, AcquisitionType
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,QHeaderView,QSizePolicy
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont, QPalette, QColor, QLinearGradient, QBrush
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime
import math
pi=math.pi


class SecondWindow(QWidget):
    def __init__(self,second_window):
        super().__init__()
        self.setWindowTitle("Second Window")
        self.setGeometry(400, 100, 300, 200)
        # self.data_display = DataDisplay()
        # print(self.data_display.avg_discharge) 
        self.er=second_window
        
       # self.avg_discharge = avg_discharge
       
        self.pulse = []
        self.e1 = []
        self.current_data = []
        self.discharge_data = []
        self.normal_d=[]
         


        palette = QPalette()
        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0.0, QColor(0, 0, 0))
        gradient.setColorAt(1.0, QColor(0, 23, 0))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # Layout for displaying data
        main_layout = QVBoxLayout()

        

        self.fig = Figure(figsize=(8,6))
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Real-Time Data Plot",fontsize=20)
        self.ax.set_xlabel("Sample",fontsize=20)
        self.ax.set_ylabel("Normal Pulse",fontsize=20)
        
        main_layout.addWidget(self.canvas)

      

        # Set main layout
        self.setLayout(main_layout)

        self.update_graph()

    def update_graph(self):
        """Updates the graph with new data."""
        self.ax.clear()
        self.e1.append(self.er.avg_discharge)
        self.pulse.append(self.er.sum_pulse)
        self.normal_d.append(self.er.normal_d)

        # self.ax.plot(self.pulse, self.e1, label="Voltage (V)", color="blue")
        self.ax.plot(self.pulse, self.normal_d, label="Normal pulse", color="Green",linewidth = 7, linestyle=":")
        self.ax.plot(self.pulse, self.e1, label="Discharge Energy (μJ)", color="orange",linewidth = 7, linestyle=":")
        self.ax.legend(loc="upper right")
        self.ax.set_title("Real-Time Data Plot",fontsize=20)
        self.ax.set_xlabel("Sample",fontsize=20)
        self.ax.set_ylabel("Discharge Energy(μJ)",fontsize=20)
        self.canvas.draw()


        if len(self.pulse) == 200:
            # Create a timestamped filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"Normal pulse.png"
            
            # Save the figure
            self.fig.savefig(filename, dpi=600)  # dpi=300 for high quality
            print(f"Plot saved as {filename}")
       
        # print("Average Discharge")
        # print(self.e1)
        # print(self.pulse)
        
        
class ThirdWindow(QWidget):
    def __init__(self,third_window):
        super().__init__()
        self.setWindowTitle("Third Window")
        self.setGeometry(400, 100, 300, 200)
        # self.data_display = DataDisplay()
        # print(self.data_display.avg_discharge) 
        self.er=third_window
        
       # self.avg_discharge = avg_discharge
       
        self.pulse = []
        self.e1 = []
        self.current_data = []
        self.discharge_data = []
        self.arcing_d=[]
         


        palette = QPalette()
        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0.0, QColor(0, 0, 0))
        gradient.setColorAt(1.0, QColor(0, 23, 0))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # Layout for displaying data
        main_layout = QVBoxLayout()

        

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Real-Time Data Plot",fontsize=20)
        self.ax.set_xlabel("Sample",fontsize=20)
        self.ax.set_ylabel("Arcing Pulse (μJ)",fontsize=20)
        
        main_layout.addWidget(self.canvas)

      

        # Set main layout
        self.setLayout(main_layout)

        self.update_graph()

    def update_graph(self):
        """Updates the graph with new data."""
        self.ax.clear()
        self.e1.append(self.er.avg_discharge)
        self.pulse.append(self.er.sum_pulse)
        self.arcing_d.append(self.er.arcing_d)

        # self.ax.plot(self.pulse, self.e1, label="Voltage (V)", color="blue")
        self.ax.plot(self.pulse, self.arcing_d, label="Arcing pulse", color="purple",linewidth = 7, linestyle=":")
        self.ax.plot(self.pulse, self.e1, label="Discharge Energy (μJ)", color="orange",linewidth = 7, linestyle=":")
        self.ax.legend(loc="upper right")
        self.ax.set_title("Real-Time Data Plot",fontsize=20)
        self.ax.set_xlabel("Sample",fontsize=20)
        self.ax.set_ylabel("Arcing Pulse (μJ)",fontsize=20)
        self.canvas.draw()
        
        if len(self.pulse) == 200:
            # Create a timestamped filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"Arcing pulse.png"
            
            # Save the figure
            self.fig.savefig(filename, dpi=600)  # dpi=300 for high quality
            print(f"Plot saved as {filename}")
        # print("Average Discharge")
        # print(self.e1)
        # print(self.pulse)



class FourthWindow(QWidget):
    def __init__(self,fourth_window):
        super().__init__()
        self.setWindowTitle("Fourth Window")
        self.setGeometry(400, 100, 300, 200)
        # self.data_display = DataDisplay()
        # print(self.data_display.avg_discharge) 
        self.er=fourth_window
        
       # self.avg_discharge = avg_discharge
       
        self.pulse = []
        self.e1 = []
        self.current_data = []
        self.discharge_data = []
        self.delay_d=[]
         


        palette = QPalette()
        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0.0, QColor(0, 0, 0))
        gradient.setColorAt(1.0, QColor(0, 23, 0))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # Layout for displaying data
        main_layout = QVBoxLayout()

        

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Real-Time Data Plot",fontsize=20)
        self.ax.set_xlabel("Sample",fontsize=20)
        self.ax.set_ylabel("Delay Pulse (μJ)",fontsize=20)
        
        main_layout.addWidget(self.canvas)

      

        # Set main layout
        self.setLayout(main_layout)

        self.update_graph()

    def update_graph(self):
        """Updates the graph with new data."""
        self.ax.clear()
        self.e1.append(self.er.avg_discharge)
        self.pulse.append(self.er.sum_pulse)
        self.delay_d.append(self.er.delay_d)

        # self.ax.plot(self.pulse, self.e1, label="Voltage (V)", color="blue")
        self.ax.plot(self.pulse, self.delay_d, label="Delay pulse", color="blue",linewidth = 7, linestyle=":")
        self.ax.plot(self.pulse, self.e1, label="Discharge Energy (μJ)", color="orange",linewidth = 7, linestyle=":")
        self.ax.legend(loc="upper right")
        self.ax.set_title("Real-Time Data Plot",fontsize=20)
        self.ax.set_xlabel("Sample",fontsize=20)
        self.ax.set_ylabel("Delay Pulse (μJ)",fontsize=20)
        self.canvas.draw()
        
        if len(self.pulse) == 200:
            # Create a timestamped filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"Delay pulse.png"
            
            # Save the figure
            self.fig.savefig(filename, dpi=600)  # dpi=300 for high quality
            print(f"Plot saved as {filename}")
        


class FifthWindow(QWidget):
    def __init__(self,fifth_window):
        super().__init__()
        self.setWindowTitle("Fifth Window")
        self.setGeometry(400, 100, 300, 200)
        # self.data_display = DataDisplay()
        # print(self.data_display.avg_discharge) 
        self.er=fifth_window
        
       # self.avg_discharge = avg_discharge
       
        self.pulse = []
        self.e1 = []
        self.current_data = []
        self.discharge_data = []
        self.short_d=[]
         


        palette = QPalette()
        gradient = QLinearGradient(0, 0, self.width(), 0)
        gradient.setColorAt(0.0, QColor(0, 0, 0))
        gradient.setColorAt(1.0, QColor(0, 23, 0))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # Layout for displaying data
        main_layout = QVBoxLayout()

        

        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Real-Time Data Plot",fontsize=20)
        self.ax.set_xlabel("Sample",fontsize=20)
        self.ax.set_ylabel("Short Circuit Pulse (μJ)",fontsize=20)
        
        main_layout.addWidget(self.canvas)

      

        # Set main layout
        self.setLayout(main_layout)

        self.update_graph()

    def update_graph(self):
        """Updates the graph with new data."""
        self.ax.clear()
        self.e1.append(self.er.avg_discharge)
        self.pulse.append(self.er.sum_pulse)
        self.short_d.append(self.er.short_d)

        # self.ax.plot(self.pulse, self.e1, label="Voltage (V)", color="blue")
        self.ax.plot(self.pulse, self.short_d, label="Short Circuit pulse", color="fuchsia",linewidth = 7, linestyle=":")
        self.ax.plot(self.pulse, self.e1, label="Discharge Energy (μJ)", color="orange",linewidth = 7, linestyle=":")
        self.ax.legend(loc="upper right")
        self.ax.set_title("Real-Time Data Plot",fontsize=20)
        self.ax.set_xlabel("Sample",fontsize=20)
        self.ax.set_ylabel("Short Circuit Pulse (μJ)",fontsize=20)
        self.canvas.draw()

        if len(self.pulse) == 200:
            # Create a timestamped filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"Short Circuit Pulse.png"
            
            # Save the figure
            self.fig.savefig(filename, dpi=600)  # dpi=300 for high quality
            print(f"Plot saved as {filename}")     

class DataDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.avg_discharge = 0.0
        self.Normal_pulse = 0.0
        self.Delay_pulse = 0.0
        self.Arcing_pulse = 0.0
        self.Shortcircuit_pulse = 0.0
        self.result = 0.0
        self.sum_pulse = 0.0
        self.Open_circuit_pulse = 0.0
        self.c = 0 
        self.normal_=0.0
        self.delay_=0.0
        self.p=0
        self.normal_d=0.0
        self.arcing_d=0.0
        self.delay_d=0.0
        self.short_d=0.0
    

    # Set up the DAQ tasks for myDAQ (Current) and cDAQ (Voltage)
        self.task_myDAQ = nidaqmx.Task()
        self.task_myDAQ.ai_channels.add_ai_voltage_chan(
            "myDAQ2/ai0", terminal_config=TerminalConfiguration.DIFF)  # Voltage signal

        self.task_cDAQ = nidaqmx.Task()
        self.task_cDAQ.ai_channels.add_ai_voltage_chan(
            "cDAQ1Mod1/ai2", terminal_config=TerminalConfiguration.DIFF)  # Current signal

        # Configure tasks for continuous acquisition with buffer size
        self.task_myDAQ.timing.cfg_samp_clk_timing(rate=2000, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=3000)
        self.task_myDAQ.in_stream.input_buf_size = 1110000  # Set buffer size for myDAQ

        self.task_cDAQ.timing.cfg_samp_clk_timing(rate=2000, sample_mode=AcquisitionType.CONTINUOUS, samps_per_chan=3000)
        self.task_cDAQ.in_stream.input_buf_size = 1110000  # Set buffer size for cDAQ

        # Timer to update data every 1000 ms (1 second)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)    

                 
         
    def open_second_window(self):
            # Create and show the second window
        self.second_window = SecondWindow(self)
        self.second_window.show()

    def open_third_window(self):
            # Create and show the second window
        self.third_window = ThirdWindow(self)
        self.third_window.show()    
   
    def open_fourth_window(self):
            # Create and show the second window
        self.fourth_window = FourthWindow(self)
        self.fourth_window.show()  

    def open_fifth_window(self):
            # Create and show the second window
        self.fifth_window = FifthWindow(self)
        self.fifth_window.show()      
    
    def initUI(self):
        self.setWindowTitle("Real-Time Data Display with Input")
        self.setGeometry(200, 200, 1200, 800)
        
        self.second_window = None
        self.third_window = None
        self.fourth_window = None
        self.fifth_window = None
        # Set gradient background
        palette = QPalette()
        gradient = QLinearGradient(0, 0, self.width(), 0)  # Horizontal gradient from left to right
        gradient.setColorAt(0.0, QColor(0, 0, 0))
        gradient.setColorAt(1.0, QColor(0, 23, 0))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        # Layout for displaying data
        main_layout = QVBoxLayout()

        # Labels for displaying real-time data
        self.label_current = self.create_label("Current (A): ")
        self.label_voltage = self.create_label("Voltage (V): ")
        self.label_Discharge_energy = self.create_label("Discharge Energy (μJ): ")

        # Labels for pulses
        self.Normal_pulse_label = self.create_label("Normal Pulse: 0.0")
        self.Delay_pulse_label = self.create_label("Delay Pulse: 0.0")
        self.Arcing_pulse_label = self.create_label("Arcing Pulse: 0.0")
        self.Shortcircuit_pulse_label = self.create_label("Short Circuit Pulse: 0.0")
        self.Open_pulse_label = self.create_label("Open Circuit Pulses : 0.0")
        self.sum_pulse_label = self.create_label("SUM OF PULSES : 0.0")
        self.kmr_label = self.create_label("Erosion Height:0.0")

        # Input boxes and labels arranged in a row
        input_layout = QHBoxLayout()

        # Styling for input fields
        self.voltage_input = self.create_styled_input("Enter Voltage (V)")
        self.current_input = self.create_styled_input("Enter Current (A)")
        self.time_input = self.create_styled_input("Enter Time (μs)")

        # Submit button
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setStyleSheet("background-color: #0056b3; color: white; border-radius: 10px; padding: 10px;")
        self.submit_button.clicked.connect(self.calculate_values)

        # Label for displaying the result
        self.result_label = self.create_label("Enter the input parameters")

        # Add input boxes to horizontal layout
        input_layout.addWidget(self.voltage_input)
        input_layout.addWidget(self.current_input)
        input_layout.addWidget(self.time_input)

        # Adding widgets to main layout
        main_layout.addWidget(self.label_current)
        main_layout.addWidget(self.label_voltage)
        main_layout.addWidget(self.label_Discharge_energy)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(self.submit_button, alignment=Qt.AlignCenter)
        main_layout.addWidget(self.Normal_pulse_label)
        main_layout.addWidget(self.Delay_pulse_label)
        main_layout.addWidget(self.Arcing_pulse_label)
        main_layout.addWidget(self.Shortcircuit_pulse_label)
        main_layout.addWidget(self.Open_pulse_label)
        main_layout.addWidget(self.sum_pulse_label)
        main_layout.addWidget(self.kmr_label)
       
        


        self.kmr_input = self.create_styled_input("Enter Kmr")
        self.hc_input = self.create_styled_input("Enter hc")
        self.dc_input = self.create_styled_input("Enter dc")
        self.re_input = self.create_styled_input("Enter re")
         
         # Submit button
        self.submit_button_erosion = QPushButton('Submit', self)
        self.submit_button_erosion.setStyleSheet("background-color: #0056b3; color: white; border-radius: 10px; padding: 10px;")
        self.submit_button_erosion.clicked.connect(self.calculate_values_erosionheight)

        
        
        self.button = QPushButton("Open Second Window", self)
        self.button.clicked.connect(self.open_second_window)
        
        self.button3 = QPushButton("Open Third Window", self)
        self.button3.clicked.connect(self.open_third_window)

        self.button4 = QPushButton("Open fourth Window", self)
        self.button4.clicked.connect(self.open_fourth_window)

        self.button5 = QPushButton("Open fifth Window", self)
        self.button5.clicked.connect(self.open_fifth_window)


        self.kmr_input.setFixedWidth(150)
        self.hc_input.setFixedWidth(150)
        self.dc_input.setFixedWidth(150)
        self.re_input.setFixedWidth(150)

        # Create a vertical layout for the new input fields
        additional_input_layout = QHBoxLayout()
        additional_input_layout.addWidget(self.kmr_input)
        additional_input_layout.addWidget(self.hc_input)
        additional_input_layout.addWidget(self.dc_input)
        additional_input_layout.addWidget(self.re_input)
        additional_input_layout.addWidget(self.submit_button_erosion)
        additional_input_layout.addWidget(self.button)
        additional_input_layout.addWidget(self.button3)
        additional_input_layout.addWidget(self.button4)
        additional_input_layout.addWidget(self.button5)


       # Add the additional input layout to the main layout
        main_layout.addLayout(additional_input_layout)

        main_layout.addWidget(self.kmr_input)
      

        # Adding a table to display the percentage of pulses
        self.table = QTableWidget(self)
        self.table.setRowCount(4)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Pulse Type", "Percentage"])
       # self.table.setStyleSheet("background-color: #e6f2ff; border-radius: 10px; padding: 5px; color: #003366;")

        # Remove extra padding and adjust size policy to fit content
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()


        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #f0f8ff;
                border-radius: 15px;
                border: 1px solid #0056b3;
                padding: 10px;
                color: #003366;
            }
            QHeaderView::section {
                background-color: #0056b3;
                color: white;
                font-weight: bold;
                border: 1px solid #0056b3;
                padding: 4px;
            }
            QTableWidget::item {
                border-bottom: 1px solid #0056b3;
            }
            QTableWidget::item:selected {
                background-color: #82caff;
            }
        """)
        
        # Set column widths
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 150)

        # Set table properties
        self.table.setAlternatingRowColors(True)  # Alternate row colors for better readability
        self.table.setShowGrid(True)  # Hide the grid for a cleaner look
        self.table.horizontalHeader().setStretchLastSection(True)  # Stretch last column
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)  # Hide row numbers

        # Set column widths
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)

        # Populate the table with pulse names
        self.table.setItem(0, 0, QTableWidgetItem("Normal Pulse"))
        self.table.setItem(1, 0, QTableWidgetItem("Delay Pulse"))
        self.table.setItem(2, 0, QTableWidgetItem("Arcing Pulse"))
        self.table.setItem(3, 0, QTableWidgetItem("Short Circuit Pulse"))

        main_layout.addWidget(self.table, alignment=Qt.AlignRight)

        self.setLayout(main_layout)
        

    def calculate_values_erosionheight(self):
        kmr=float(self.kmr_input.text())
        hc=float(self.hc_input.text())
        dc=float(self.dc_input.text())
        re=float(self.re_input.text())

        vc=pi * hc * ((dc**2)/8 + (hc**2)/6)

        he= (self.sum_pulse * self.normal_ * self.delay_ * kmr * vc)/(pi * (re**2) )

        self.p=1

        self.kmr_label.setText(f"Erosion Height: {he:.7f}")



    def create_label(self, text):
        label = QLabel(text, self)
        label.setFont(QFont('Arial', 16))
        label.setStyleSheet("color: white;")
        return label

    def create_styled_input(self, placeholder):
        input_field = QLineEdit(self)
        input_field.setPlaceholderText(placeholder)
        input_field.setFont(QFont('Arial', 14))
        input_field.setStyleSheet("""
            QLineEdit {
                border-radius: 15px;
                border: 2px solid #0056b3;
                padding: 10px;
                background-color: #e6f2ff;
                color: #003366;
            }
        """)
        return input_field

    def update_data(self):
        try:
            # Read 1000 samples from myDAQ and cDAQ
            data_myDAQ = self.task_myDAQ.read(number_of_samples_per_channel=1000)
            data_cDAQ = self.task_cDAQ.read(number_of_samples_per_channel=1000)
            #print(data_cDAQ)

            # Compute the average of the collected samples
            avg_current = sum(data_myDAQ) / len(data_myDAQ) * 10  # Convert and scale
            avg_voltage = sum(data_cDAQ) / len(data_cDAQ)
            self.avg_discharge = abs(avg_current * avg_voltage * 40)

            # Update the labels with the averaged data
            self.label_current.setText(f"Current (A): {avg_current:.7f}")
            self.label_voltage.setText(f"Voltage (V): {avg_voltage:.7f}")
            self.label_Discharge_energy.setText(f"Discharge Energy: {self.avg_discharge:.7f}")
            self.Pulse()
            self.log_to_excel(avg_current, avg_voltage, self.avg_discharge)
            if self.second_window:
             self.second_window.update_graph()

            if self.third_window:
                 self.third_window.update_graph() 

            if self.fourth_window:
                 self.fourth_window.update_graph()   

            if self.fifth_window:
                 self.fifth_window.update_graph()       
        except nidaqmx.DaqError as e:
            print(f"Error: {e}")
            self.timer.stop()


    def log_to_excel(self, avg_current, avg_voltage, avg_discharge):
        # Define the Excel file name
        file_name = "data/EDM_DATA.xlsx"

        # Check if the file already exists
        if not os.path.exists(file_name):
            # Create a new workbook and add headers if the file doesn't exist
            wb = Workbook()
            ws = wb.active
            ws.title = "EDM DATA"
            ws.append(["Timestamp", "Current (A)", "Voltage (V)", "Discharge Energy (μJ)"])
        else:
            # Load the existing workbook
            wb = openpyxl.load_workbook(file_name)
            ws = wb.active

        # Append the new data with a timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ws.append([timestamp, avg_current, avg_voltage, avg_discharge])

        # Save the workbook
        wb.save(file_name)
        print(f"Data logged to {file_name}")

    
               
            

    def calculate_values(self):
        try:
            # Get values from input fields
            voltage = float(self.voltage_input.text())
            current = float(self.current_input.text())
            time_microseconds = float(self.time_input.text())
            self.c=1 
            # Multiply the values
            self.result = voltage * current * time_microseconds
            self.Pulse()
           


            # Update the result label
            self.result_label.setText(f"Supplied Energy (V_s * I_s * T_on) = {self.result:.2f} μJ")

        except ValueError:
            # If inputs are invalid, show an error message
            self.result_label.setText("Please enter valid numerical values.")

    def Pulse(self):

        if 0.55 * self.result > self.avg_discharge >= 0.15 * self.result:
            self.Normal_pulse += 1
            self.normal_d = self.avg_discharge
            
            self.Normal_pulse_label.setText(f"Normal Pulse: {self.Normal_pulse:.7f}")
            self.delay_d = 0.0  
            self.arcing_d = 0.0  
            self.short_d = 0.0 
           # print("Normal pulse")
        elif 0.15 * self.result > self.avg_discharge >= 0.05 * self.result:
            self.Delay_pulse += 1
            self.delay_d = self.avg_discharge
            self.Delay_pulse_label.setText(f"Delay Pulse: {self.Delay_pulse:.7f}")
            self.arcing_d = 0.0  
            self.short_d = 0.0
            self.normal_d = 0.0
            #print("Delay pulse")
        elif 0.05 * self.result > self.avg_discharge >= 0.005 * self.result:
            self.Arcing_pulse += 1
            self.arcing_d = self.avg_discharge
            self.Arcing_pulse_label.setText(f"Arcing Pulse: {self.Arcing_pulse:.7f}")
            print(self.arcing_d)
            print(self.avg_discharge)
            self.normal_d = 0.0   
            self.delay_d = 0.0  
            self.short_d = 0.0
            
            print("Arcing pulse")
        elif self.avg_discharge < 0.005 * self.result:
            self.Shortcircuit_pulse += 1
            self.short_d = self.avg_discharge
            self.Shortcircuit_pulse_label.setText(f"Short Circuit Pulse: {self.Shortcircuit_pulse:.7f}")
            self.normal_d = 0.0   
            self.delay_d = 0.0  
            self.arcing_d = 0.0
          #  print("Short Circuit pulse")
        elif self.avg_discharge > 0.55 * self.result and self.c==1 :
            self.Open_circuit_pulse += 1
            self.Open_pulse_label.setText(f"Open Circuit Pulse: {self.Open_circuit_pulse:.7f}")
            self.normal_d = 0.0   
            self.delay_d = 0.0  
            self.arcing_d = 0.0  
            self.short_d = 0.0
           # print("Open Circuit pulse")  
        else:
            self.normal_d = 0.0   
            self.delay_d = 0.0  
            self.arcing_d = 0.0  
            self.short_d = 0.0  
        self.sum_pulse = self.Normal_pulse + self.Delay_pulse + self.Arcing_pulse + self.Shortcircuit_pulse
        self.sum_pulse_label.setText(f"SUM OF PULSES : {self.sum_pulse:.7f}")

        self.update_table()
        
    def update_table(self):
        # Calculate percentages for each pulse
        if self.sum_pulse > 0:
            normal_percent = (self.Normal_pulse / self.sum_pulse) * 100
            delay_percent = (self.Delay_pulse / self.sum_pulse) * 100
            arcing_percent = (self.Arcing_pulse / self.sum_pulse) * 100
            short_circuit_percent = (self.Shortcircuit_pulse / self.sum_pulse) * 100

            self.normal_ = (self.Normal_pulse / self.sum_pulse)
            self.delay_ = (self.Delay_pulse / self.sum_pulse) 
            self.arcing_ = (self.Arcing_pulse / self.sum_pulse) 
            self.short_circuit_ = (self.Shortcircuit_pulse / self.sum_pulse)
        else:
            normal_percent = delay_percent = arcing_percent = short_circuit_percent = 0.0

        if   self.p==1 :
             self.calculate_values_erosionheight()  

            

        # Update the table with percentages
        self.table.setItem(0, 1, QTableWidgetItem(f"{normal_percent:.2f}%"))
        self.table.setItem(1, 1, QTableWidgetItem(f"{delay_percent:.2f}%"))
        self.table.setItem(2, 1, QTableWidgetItem(f"{arcing_percent:.2f}%"))
        self.table.setItem(3, 1, QTableWidgetItem(f"{short_circuit_percent:.2f}%"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    data_display = DataDisplay()
 
    # ex = SecondWindow()
    data_display.show()
    #ex.show()
    sys.exit(app.exec_())
