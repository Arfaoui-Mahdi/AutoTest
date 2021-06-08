#from can.interfaces.vector import VectorBus

from can.interfaces.pcan import PcanBus
from udsoncan.connections import PythonIsoTpConnection
from udsoncan.services.RoutineControl import RoutineControl
from udsoncan.client import Client
from datetime import datetime, timedelta
from udsoncan.Response import Response
from udsoncan.client import services
import udsoncan.configs
import isotp
import time
import unittest
import struct
import sys,pytest



log_file = open(r'C:\Users\Mahdi\Desktop\Test_Python_Projectttttttt\VENTURA_Tests_Script\VENTURA_Tests_Script\log.txt', 'w')
log_file2 = open(r'C:\Users\Mahdi\Desktop\Test_Python_Projectttttttt\VENTURA_Tests_Script\VENTURA_Tests_Script\TestsNOK.txt', 'w')
BIG_ENDIAN = "big"
# Refer to isotp documentation for full details about parameters


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class MyCustomCodecThatShiftBy4(udsoncan.DidCodec):
   def encode(self, val):
      val = (val << 4) & 0xFFFFFFFF # Do some stuff
      return struct.pack('<L', val) # Little endian, 32 bit value

   def decode(self, payload):
      val = struct.unpack('<L', payload)[0]  # decode the 32 bits value
      return val >> 4                        # Do some stuff (reversed)

   def __len__(self):
      return 4    # encoded paylaod is 4 byte long.


isotp_params = {
   'stmin' : 32,                          # Will request the sender to wait 32ms between consecutive frame. 0-127ms or 100-900ns with values from 0xF1-0xF9
   'blocksize' : 8,                       # Request the sender to send 8 consecutives frames before sending a new flow control message
   'wftmax' : 0,                          # Number of wait frame allowed before triggering an error
   'll_data_length' : 8,                  # Link layer (CAN layer) works with 8 byte payload (CAN 2.0)
   'tx_padding' :255,                      # Will pad all transmitted CAN messages with byte 0x00. None means no padding
   'rx_flowcontrol_timeout' : 1000,       # Triggers a timeout if a flow control is awaited for more than 1000 milliseconds
   'rx_consecutive_frame_timeout' : 1000, # Triggers a timeout if a consecutive frame is awaited for more than 1000 milliseconds
   'squash_stmin_requirement' : False     # When sending, respect the stmin requirement of the receiver. If set to True, go as fast as possible.
}

bus = PcanBus(channel='PCAN_USBBUS1', bitrate=250000)                                      # Link Layer (CAN protocol)
tp_addr = isotp.Address(isotp.AddressingMode.Normal_29bits, txid=0x18DAFEF9, rxid=0x18DAF9FE)#Network layer addressing scheme
stack = isotp.CanStack(bus=bus, address=tp_addr, params=isotp_params)               # Network/Transport layer (IsoTP protocol)
conn = PythonIsoTpConnection(stack)                                               # interface between Application and Transport layer


class TestInit(unittest.TestCase):
    def test_InitAllIO(self):
        with Client(conn, request_timeout=1) as client:  
            parent_conn,child_conn = Pipe()
            p = Process(target=f, args=(child_conn,))
            p.start()
            data = parent_conn.recv()


            #vrr = "00000001000000"
            vrr = data[3]
            vrb = bytes.fromhex(vrr)                                   # Application layer (UDS protocol)
            req=services.RoutineControl.make_request(routine_id=0x0003, control_type=RoutineControl.ControlType.startRoutine, data=vrb)
            conn.send(req.get_payload()) #send the request
            payload =conn.wait_frame(timeout=1)
            response = Response.from_payload(payload)
            services.RoutineControl.interpret_response(response)
            print(response.data)
            print("Test1: initAllIO")
            print('Expected result: Return code 0')
            print('Obtained result: %s'%response.data[4])

            sys.stdout = sys.__stdout__
            sys.stdout = log_file
            print("Test1: initAllIO")
            print('Expected result: Return code 0')
            print('Obtained result: %s'%response.data[4])
            if response.data[4] ==0:
                print('Test result: OK','\n')
            else:
                print('Test result: init all IO NOK','\n')

            if response.data[4] != 0:
                sys.stdout = sys.__stdout__
                sys.stdout = log_file2
                print("Test1: initAllIO")
                print('\t','Expected result: return code 0')
                print( '\t','Obtained result: %s' % response.data[4])
                print('\t','Test result: init all IO NOK', '\n')
                raise self.fail('Test failed: Initialisation of the IO in same operation is failed')

class TestInputs(unittest.TestCase):
    def test_SetupAna1Resistor(self):
        with Client(conn, request_timeout=1) as client:
                req=services.RoutineControl.make_request(routine_id=0xFE17, control_type=RoutineControl.ControlType.startRoutine, data=b'\x01')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                print('Analogue inputs data: %s' %response.data)
                print('Test2.1: Setup ANA1 as resistor input')
                print('Expected result: return code 0')
                print('Obtained result: %s' % response.data[4])
                services.RoutineControl.interpret_response(response)
                sys.stdout = log_file
                print('Test2.1: Setup ANA1 as resistor input')
                print('Expected result: return code 0')
                print('Obtained result: %s' % response.data[4])
                if response.data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result: setup ANA1 as resistor NOK','\n')
                    #raise self.fail('Test failed')

                if response.data[4] != 0:
                    sys.stdout = sys.__stdout__
                    sys.stdout=log_file2
                    print('Test2.1: Setup ANA1 as resistor input')
                    print('\t','Expected result: return code 0')
                    print('\t','Obtained result: %s' % response.data[4])
                    print('\t','Test result: setup ANA1 as resistor NOK', '\n')
                    raise self.fail('Test failed')

    def test_SetupAna2Resistor(self):
        with Client(conn, request_timeout=1) as client:
                req=services.RoutineControl.make_request(routine_id=0xFE17, control_type=RoutineControl.ControlType.startRoutine, data=b'\x02')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                print('Analogue inputs data: %s' %response.data)
                print('Test2.2: Setup ANA2 as resistor input')
                print('Expected result: return code 0')
                print('Obtained result: %s' % response.data[4])
                services.RoutineControl.interpret_response(response)
                sys.stdout = log_file
                print('Test2.2: Setup ANA2 as resistor input')
                print('Expected result: return code 0')
                print('Obtained result: %s' % response.data[4])
                if response.data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result: setup ANA2 as resistor NOK','\n')

                if response.data[4] != 0:
                    sys.stdout = sys.__stdout__
                    sys.stdout=log_file2
                    print('Test2.2: Setup ANA2 as resistor input')
                    print('\t','Expected result: return code 0')
                    print('\t','Obtained result: %s' % response.data[4])
                    print('\t','Test result: setup ANA2 as resistor NOK', '\n')
                    raise self.fail('Test failed')

    def test_SetupAna1Voltage(self):
        with Client(conn, request_timeout=1) as client:
                req=services.RoutineControl.make_request(routine_id=0xFE17, control_type=RoutineControl.ControlType.startRoutine, data=b'\x03')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                print('Analogue inputs data: %s' %response.data)
                print('Test2.3: Setup ANA1 as voltage input')
                print('Expected result: return code 0')
                print('Obtained result: %s' % response.data[4])
                services.RoutineControl.interpret_response(response)
                #self.assertEqual(response.data[4], 0, 'test failed')
                sys.stdout = log_file
                print('Test2.3: Setup ANA1 as voltage input')
                print('Expected result: return code 0')
                print('Obtained result: %s' % response.data[4])
                if response.data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result: setup ANA1 as voltage NOK','\n')

                # log to lo2.txt
                if response.data[4] != 0:
                    sys.stdout = sys.__stdout__
                    sys.stdout=log_file2
                    print('Test2.3: Setup ANA1 as voltage input')
                    print('\t','Expected result: return code 0')
                    print('\t','Obtained result: %s' % response.data[4])
                    print('\t','Test result: setup ANA1 as voltage NOK', '\n')
                    raise self.fail('Test failed')


    def test_SetupAna2Voltage(self):
       with Client(conn, request_timeout=1) as client:
                req=services.RoutineControl.make_request(routine_id=0xFE17, control_type=RoutineControl.ControlType.startRoutine, data=b'\x03')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                print('Analogue inputs data: %s' %response.data)
                print('Test2.4: Setup ANA2 as voltage input')
                print('Expected result: return code 0')
                print('Obtained result: %s' % response.data[4])
                services.RoutineControl.interpret_response(response)
                #self.assertEqual(response.data[4], 0, 'test failed')
                sys.stdout = log_file
                print('Test2.4: Setup ANA2 as voltage input')
                print('Expected result: return code 0')
                print('Obtained result: %s' % response.data[4])
                if response.data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result: setup ANA2 as voltage NOK','\n')

                # log to lo2.txt
                if response.data[4] != 0:
                    sys.stdout = sys.__stdout__
                    sys.stdout=log_file2
                    print('Test2.4: Setup ANA2 as voltage input')
                    print('\t','Expected result: return code 0')
                    print('\t','Obtained result: %s' % response.data[4])
                    print('\t','Test result: setup ANA2 as voltage NOK', '\n')
                    raise self.fail('Test failed')

    def test_ReadAnalogInputs(self):
        with Client(conn, request_timeout=1) as client:
                data=[]
                req2 = services.RoutineControl.make_request(routine_id=0xFE17,control_type=RoutineControl.ControlType.startRoutine,data=b'\x05')
                conn.send(req2.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                print('Test2.5: Read analogInputs Values')
                print('Expected result: 0x7D0 ')
                for j in range(len(response.data)):
                    data.append(hex(response.data[j]))
                print('obtained result:%s' % '/'.join([str(a) for a in data]))
                print('ANA1 value  %s%s' % (data[6], data[5]))
                print('ANA2 value  %s%s' % (data[8], data[7]))

                sys.stdout = log_file
                print('Test2.5: Read analogInputs Values')
                print('Expected result: 0x7D0 ')
                print('obtained result:%s' % '/'.join([str(a) for a in data]))
                print('ANA1 value  %s%s' % (data[6], data[5]))
                print('ANA2 value  %s%s' % (data[8], data[7]))

                if response.data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result: NOK','\n')
                    raise self.fail('Test failed')

    def test_SetupUinVoltage(self):
        with Client(conn, request_timeout=1) as client:
                req = services.RoutineControl.make_request(routine_id=0xFE19,control_type=RoutineControl.ControlType.startRoutine, data=b'\x01')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                print('Universal inputs data: %s' % response.data)
                print('Test2.6:SetupUIN as voltage inputs')
                print('Expected result: return code 0')
                print('Obtained result: %s' % response.data[4])
                services.RoutineControl.interpret_response(response)

                sys.stdout =log_file
                print('Test2.6:SetupUIN as voltage inputs')
                print('Expected result: return code 0')
                print('Obtained result: %s' % response.data[4])
                if response.data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result: setup UIn as voltage NOK','\n')
            # log to lo2.txt
                if response.data[4] != 0:
                    sys.stdout = sys.__stdout__
                    sys.stdout=log_file2
                    print('Test2.6: SetupUIN as voltage input')
                    print('\t','Expected result: return code 0')
                    print('\t','Obtained result: %s' % response.data[4])
                    print('\t','Test result: setup UIN as voltage NOK', '\n')
                    raise self.fail('Test failed: Setup UIN as voltage input is failed')

    def test_ReadUniversalInputs(self):
        with Client(conn, request_timeout=1) as client:
                data=[]
                req = services.RoutineControl.make_request(routine_id=0xFE19,control_type=RoutineControl.ControlType.startRoutine, data=b'\x02')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                for j in range(len(response.data)):
                    data.append(hex(response.data[j]))
                print('Test2.7:read UIN values')
                print('Expected result: TBD')
                print('obtained result:%s' % '/'.join([str(a) for a in data]))

                services.RoutineControl.interpret_response(response)
                sys.stdout = log_file
                print('Test2.7:read UIN values')
                print('Expected result: TBD')
                print('obtained result:%s' % '/'.join([str(a) for a in data]))
                if response.data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result: raed UIN NOK','\n')
                    #raise self.fail('Test failed: Read UIN as voltage input is failed')

                if response.data[4] != 0:
                    sys.stdout = sys.__stdout__
                    sys.stdout=log_file2
                    print('Test2.7:read UIN values')
                    print('\t','Expected result: return code 0')
                    print('\t','Obtained result: %s' % response.data[4])
                    print('\t','Test result: read UIN NOK', '\n')
                    raise self.fail('Test failed: Read UIN as voltage input is failed')

    def test_ReadPulseNumber(self):
        with Client(conn, request_timeout=1) as client:
            data=[]
            req = services.RoutineControl.make_request(routine_id=0xFE16,control_type=RoutineControl.ControlType.startRoutine,data=b'\x01')
            conn.send(req.get_payload())
            payload = conn.wait_frame(timeout=1)
            response = Response.from_payload(payload)
            services.RoutineControl.interpret_response(response)
            for j in range(len(response.data)):
                data.append(hex(response.data[j]))
            print('Test2.8:read Pulse counter')
            print('Expected result: TBD')
            print('obtained result :%s' % '/'.join([str(a) for a in data]))
            print('number of pulse is: %s%s%s%s' % (data[7], data[6],data[5],data[4]))
            sys.stdout=log_file
            print('Test2.8:read pulse counter')
            print('Expected result: TBD')
            print('obtained result:%s' % '/'.join([str(a) for a in data]))
            print('number of pulse is: %s%s%s%s' % (data[7], data[6], data[5], data[4]))
            print('\n')

    def test_ReadFreqinputs(self):
        with Client(conn, request_timeout=1) as client:
            data=[]
            req = services.RoutineControl.make_request(routine_id=0xFE1E,control_type=RoutineControl.ControlType.startRoutine,data=b'\x01')
            conn.send(req.get_payload())
            payload = conn.wait_frame(timeout=1)
            response = Response.from_payload(payload)
            services.RoutineControl.interpret_response(response)
            for j in range(len(response.data)):
                data.append(hex(response.data[j]))
            print('Test2.9:read Freq inputs')
            print('Expected result: TBD')
            print('obtained result :%s' % '/'.join([str(a) for a in data]))
            print('FREQ1 period: %s%s' % (data[5],data[4]))
            print('FREQ1 TON: %s%s' % (data[7], data[6]))
            print('FREQ2 period: %s%s' % (data[9], data[8]))
            print('FREQ2 TON: %s%s' % (data[11], data[10]))
            sys.stdout=log_file
            print('Test2.9:read Freq inputs')
            print('Expected result: TBD')
            print('obtained result :%s' % '/'.join([str(a) for a in data]))
            print('FREQ1 period: %s%s' % (data[5],data[4]))
            print('FREQ1 TON: %s%s' % (data[7], data[6]))
            print('FREQ2 period: %s%s' % (data[9], data[8]))
            print('FREQ2 TON: %s%s' % (data[11], data[10]))
            print('\n')

class TestOutputsDutycyle0(unittest.TestCase):
    def test_DriveOutputsDutycycle0(self):
        time_execution = datetime.now() + timedelta(hours=0, seconds=2, microseconds=0, milliseconds=0, minutes=0)
        with Client(conn, request_timeout=1) as client:
            while datetime.now() < time_execution:
                req2=services.RoutineControl.make_request(routine_id=0xFE15, control_type=RoutineControl.ControlType.startRoutine,  data=b'\x01')
                conn.send(req2.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                print(response.data)
                print("Test3.1: drive the Outputs with duty cycle 0%")
                print('Expected result: Return code 0')
                print('Obtained result: %s' % response.data[4])

                sys.stdout = log_file
                print("Test3.1: drive the Outputs with duty cycle 0%")
                print('Expected result: Return code 0')
                print('Obtained result: %s' % response.data[4])
                if response.data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result: NOK','\n')
                if response.data[4]!=0:
                    sys.stdout = sys.__stdout__
                    sys.stdout = log_file2
                    print("Test3.1: drive the Outputs with duty cycle 0%")
                    print('\t','Expected result: return code 0')
                    print('\t','Obtained result: %s' % response.data[4])
                    print('\t','Test result: NOK', '\n')
                    raise self.fail('Test failed')

    def test_ReadHS9ACurrentDutycycle0(self):
        with Client(conn, request_timeout=1) as client:
                data=[]
                req = services.RoutineControl.make_request(routine_id=0xFE1D, control_type=RoutineControl.ControlType.startRoutine,data=b'\x02')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                for j in range(len(response.data)):
                    data.append(hex(response.data[j]))
                print('Test3.2: Read Current on HS9A outputs drived with 0% duty cycle')
                print('Expected result: 0x01F4')
                print('HS9A Current:%s' % '/'.join([str(a) for a in data]))
                print( 'Out5 Current  %s%s'%(data[5],data[4]))
                print('Out6 Current  %s%s' % (data[7], data[6]))
                print('Out7 Current  %s%s' % (data[9], data[8]))
                print('Out8 Current  %s%s' % (data[11], data[10]))
                sys.stdout = log_file
                print('Test3.2: Read Current on HS9A outputs drived with 0% duty cycle')
                print('Expected result: 0x01F4')
                print('Obtained result:%s' % '/'.join([str(a) for a in data]))
                print( 'Out5 Current  %s%s'%(data[5],data[4]))
                print('Out6 Current  %s%s' % (data[7], data[6]))
                print('Out7 Current  %s%s' % (data[9], data[8]))
                print('Out8 Current  %s%s' % (data[11], data[10]))
                print('\n')

    def test_ReadHS2ACurrentDutycycle0(self):
            with Client(conn, request_timeout=1) as client:
                data = []
                req = services.RoutineControl.make_request(routine_id=0xFE1D,control_type=RoutineControl.ControlType.startRoutine,data=b'\x03')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                for j in range(len(response.data)):
                    data.append(hex(response.data[j]))
                print('Test3.3: Read Current on HS2A outputs drived with 0% duty cycle')
                print('Expected result: 0x01F4')
                print('obtained result:%s' % '/'.join([str(a) for a in data]))

                print ('HS2A Current:%s' %'/'.join([str(a) for a in data]))
                print('Out9 Current  %s%s' % (data[5], data[4]))
                print('Out10 Current  %s%s' % (data[7], data[6]))
                print('Out11 Current  %s%s' % (data[9], data[8]))
                print('Out12 Current  %s%s' % (data[11], data[10]))
                print('Out13 Current  %s%s' % (data[13], data[12]))
                print('Out14 Current  %s%s' % (data[15], data[14]))
                print('Out15 Current  %s%s' % (data[17], data[16]))
                print('Out16 Current  %s%s' % (data[19], data[18]))
                print('Out17 Current  %s%s' % (data[21], data[20]))
                print('Out18 Current  %s%s' % (data[23], data[22]))
                sys.stdout = log_file
                print('Test3.3: Read Current on HS2A outputs drived with 50% duty cycle')
                print('Expected result: 0x01F4')
                print('obtained result:%s' % '/'.join([str(a) for a in data]))
                print('Out9 Current  %s%s' % (data[5], data[4]))
                print('Out10 Current  %s%s' % (data[7], data[6]))
                print('Out11 Current  %s%s' % (data[9], data[8]))
                print('Out12 Current  %s%s' % (data[11], data[10]))
                print('Out13 Current  %s%s' % (data[13], data[12]))
                print('Out14 Current  %s%s' % (data[15], data[14]))
                print('Out15 Current  %s%s' % (data[17], data[16]))
                print('Out16 Current  %s%s' % (data[19], data[18]))
                print('Out17 Current  %s%s' % (data[21], data[20]))
                print('Out18 Current  %s%s' % (data[23], data[22]))
                print('\n')

    def test_ReadHS12ACurrentDutycycle0(self):
        with Client(conn, request_timeout=1) as client:
            data = []
            req = services.RoutineControl.make_request(routine_id=0xFE1D,control_type=RoutineControl.ControlType.startRoutine, data=b'\x04')
            conn.send(req.get_payload())
            payload = conn.wait_frame(timeout=1)
            response = Response.from_payload(payload)
            services.RoutineControl.interpret_response(response)
            for j in range(len(response.data)):
                data.append(hex(response.data[j]))

            print('Test3.4: Read Current on HS12A outputs drived with 0% duty cycle')
            print('Expected result: 0x01F4')
            print('HS12A Current:%s' % '/'.join([str(a) for a in data]))
            print('Out19 Current  %s%s' % (data[5], data[4]))
            print('Out20 Current  %s%s' % (data[7], data[6]))
            sys.stdout = log_file
            print('Test3.4: Read Current on HS12A outputs drived with 0% duty cycle')
            print('Expected result: 0x01F4')
            print('obtained result:%s' % '/'.join([str(a) for a in data]))
            print('Out19 Current  %s%s' % (data[5], data[4]))
            print('Out20 Current  %s%s' % (data[7], data[6]))
            print('\n')


class TestOutputsDutycycle50(unittest.TestCase):
    def test_DriveOutputsDutycycle50(self):
        time_execution = datetime.now() + timedelta(hours=0, seconds=5, microseconds=0, milliseconds=0, minutes=0)
        with Client(conn, request_timeout=1) as client:
            while datetime.now() < time_execution:
                req2 = services.RoutineControl.make_request(routine_id=0xFE15,control_type=RoutineControl.ControlType.startRoutine, data=b'\x02')
                conn.send(req2.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                print(response.data)
                print("Test4.1: drive the Outputs with duty cycle 50%")
                print('Expected result: Return code 0')
                print('Obtained result: %s' % response.data[4])

                sys.stdout = log_file
                print("Test4.1: drive the Outputs with duty cycle 50%")
                print('Expected result: Return code 0')
                print('Obtained result: %s' % response.data[4])
                if response.data[4] == 0:
                    print('Test result: OK', '\n')
                else:
                    print('Test result: NOK', '\n')

                if response.data[4] != 0:
                    sys.stdout = sys.__stdout__
                    sys.stdout = log_file2
                    print("Test4.1: drive the Outputs with duty cycle 50%")
                    print('\t','Expected result: return code 0')
                    print('\t','Obtained result: %s' % response.data[4])
                    print('\t','Test result: NOK', '\n')
                    raise self.fail('Test failed')

    def test_ReadHS9ACurrentDutycycle50(self):
        with Client(conn, request_timeout=1) as client:
            data = []
            req = services.RoutineControl.make_request(routine_id=0xFE1D,control_type=RoutineControl.ControlType.startRoutine,data=b'\x02')
            conn.send(req.get_payload())
            payload = conn.wait_frame(timeout=1)
            response = Response.from_payload(payload)
            services.RoutineControl.interpret_response(response)
            for j in range(len(response.data)):
                data.append(hex(response.data[j]))
            print('Test4.2: Read Current on HS9A outputs drived with 50% duty cycle')
            print('Expected result: 0x01F4')
            print('HS9A Current:%s' % '/'.join([str(a) for a in data]))
            print('Out5 Current  %s%s' % (data[5], data[4]))
            print('Out6 Current  %s%s' % (data[7], data[6]))
            print('Out7 Current  %s%s' % (data[9], data[8]))
            print('Out8 Current  %s%s' % (data[11], data[10]))
            sys.stdout = log_file
            print('Test4.2: Read Current on HS9A outputs drived with 50% duty cycle')
            print('Expected result: 0x01F4')
            print('Obtained result:%s' % '/'.join([str(a) for a in data]))
            print('Out5 Current  %s%s' % (data[5], data[4]))
            print('Out6 Current  %s%s' % (data[7], data[6]))
            print('Out7 Current  %s%s' % (data[9], data[8]))
            print('Out8 Current  %s%s' % (data[11], data[10]))
            print('\n')

    def test_ReadHS2ACurrentDutycycle50(self):
        with Client(conn, request_timeout=1) as client:
            data = []
            req = services.RoutineControl.make_request(routine_id=0xFE1D,control_type=RoutineControl.ControlType.startRoutine,data=b'\x03')
            conn.send(req.get_payload())
            payload = conn.wait_frame(timeout=1)
            response = Response.from_payload(payload)
            services.RoutineControl.interpret_response(response)
            for j in range(len(response.data)):
                data.append(hex(response.data[j]))
            print('Test4.3: Read Current on HS2A outputs drived with 50% duty cycle')
            print('Expected result: 0x01F4')
            print('HS2A Current:%s' % '/'.join([str(a) for a in data]))
            print('Out9 Current  %s%s' % (data[5], data[4]))
            print('Out10 Current  %s%s' % (data[7], data[6]))
            print('Out11 Current  %s%s' % (data[9], data[8]))
            print('Out12 Current  %s%s' % (data[11], data[10]))
            print('Out13 Current  %s%s' % (data[13], data[12]))
            print('Out14 Current  %s%s' % (data[15], data[14]))
            print('Out15 Current  %s%s' % (data[17], data[16]))
            print('Out16 Current  %s%s' % (data[19], data[18]))
            print('Out17 Current  %s%s' % (data[21], data[20]))
            print('Out18 Current  %s%s' % (data[23], data[22]))
            sys.stdout = log_file
            print('Test4.3: Read Current on HS2A outputs drived with 50% duty cycle')
            print('Expected result: 0x01F4')
            print('obtained result:%s' % '/'.join([str(a) for a in data]))
            print('Out9 Current  %s%s' % (data[5], data[4]))
            print('Out10 Current  %s%s' % (data[7], data[6]))
            print('Out11 Current  %s%s' % (data[9], data[8]))
            print('Out12 Current  %s%s' % (data[11], data[10]))
            print('Out13 Current  %s%s' % (data[13], data[12]))
            print('Out14 Current  %s%s' % (data[15], data[14]))
            print('Out15 Current  %s%s' % (data[17], data[16]))
            print('Out16 Current  %s%s' % (data[19], data[18]))
            print('Out17 Current  %s%s' % (data[21], data[20]))
            print('Out18 Current  %s%s' % (data[23], data[22]))
            print('\n')

    def test_ReadHS12ACurrentDutycycle50(self):
        with Client(conn, request_timeout=1) as client:
            data = []
            req = services.RoutineControl.make_request(routine_id=0xFE1D,control_type=RoutineControl.ControlType.startRoutine,data=b'\x04')
            conn.send(req.get_payload())
            payload = conn.wait_frame(timeout=1)
            response = Response.from_payload(payload)
            services.RoutineControl.interpret_response(response)
            for j in range(len(response.data)):
                data.append(hex(response.data[j]))
            print('Test4.4: Read Current on HS12A outputs drived with 50% duty cycle')
            print('Expected result: 0x01F4')
            print('HS12A Current:%s' % '/'.join([str(a) for a in data]))
            print('Out19 Current  %s%s' % (data[5], data[4]))
            print('Out20 Current  %s%s' % (data[7], data[6]))
            sys.stdout = log_file
            print('Test4.4: Read Current on HS12A outputs drived with 50% duty cycle')
            print('Expected result: 0x01F4')
            print('obtained result:%s' % '/'.join([str(a) for a in data]))
            print('Out19 Current  %s%s' % (data[5], data[4]))
            print('Out20 Current  %s%s' % (data[7], data[6]))
            print('\n')


class TestOutputsDutycycle100(unittest.TestCase):
    def test_DriveOutputsDutycycle100(self):
        time_execution = datetime.now() + timedelta(hours=0, seconds=5, microseconds=0, milliseconds=0, minutes=0)
        with Client(conn, request_timeout=1) as client:
            while datetime.now() < time_execution:
                req2 = services.RoutineControl.make_request(routine_id=0xFE15, control_type=RoutineControl.ControlType.startRoutine, data=b'\x03')
                conn.send(req2.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                print(response.data)
                print("Test5.1: drive the Outputs with duty cycle 100%")
                print('Expected result: Return code 0')
                print('Obtained result: %s' % response.data[4])

                sys.stdout = log_file
                print("Test5.1: drive the Outputs with duty cycle 100%")
                print('Expected result: Return code 0')
                print('Obtained result: %s' % response.data[4])
                if response.data[4] == 0:
                    print('Test result: OK', '\n')
                else:
                    print('Test result: NOK', '\n')

                if response.data[4] != 0:
                    sys.stdout = sys.__stdout__
                    sys.stdout = log_file2
                    print("Test5.1: drive the Outputs with duty cycle 100%")
                    print('Expected result: return code 0')
                    print('Obtained result: %s' % response.data[4])
                    print('Test result: NOK', '\n')
                    raise self.fail('Test failed')

    def test_ReadHS9ACurrentDutycycle100(self):
        with Client(conn, request_timeout=1) as client:
                data=[]
                req = services.RoutineControl.make_request(routine_id=0xFE1D, control_type=RoutineControl.ControlType.startRoutine,data=b'\x02')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                for j in range(len(response.data)):
                    data.append(hex(response.data[j]))
                print('Test5.2: Read current on HS9A outputs drived with 100% duty cycle ')
                print('Expected result: 0x01F4')
                print('HS9A Current:%s' % '/'.join([str(a) for a in data]))
                print( 'Out5 Current  %s%s'%(data[5],data[4]))
                print('Out6 Current  %s%s' % (data[7], data[6]))
                print('Out7 Current  %s%s' % (data[9], data[8]))
                print('Out8 Current  %s%s' % (data[11], data[10]))
                sys.stdout = log_file
                print('Test5.2: Read current on HS9A outputs drived with 100% duty cycle')
                print('Expected result: 0x01F4')
                print('Obtained result:%s' % '/'.join([str(a) for a in data]))
                print( 'Out5 Current  %s%s'%(data[5],data[4]))
                print('Out6 Current  %s%s' % (data[7], data[6]))
                print('Out7 Current  %s%s' % (data[9], data[8]))
                print('Out8 Current  %s%s' % (data[11], data[10]))
                print('\n')

    def test_ReadHS2ACurrentDutycycle100(self):
            with Client(conn, request_timeout=1) as client:
                data = []
                req = services.RoutineControl.make_request(routine_id=0xFE1D,control_type=RoutineControl.ControlType.startRoutine,data=b'\x03')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                for j in range(len(response.data)):
                    data.append(hex(response.data[j]))
                print('Test5.3: Read current on HS2A outputs drived with 100% duty cycle')
                print('Expected result: 0x01F4')
                print ('HS2A Current:%s' %'/'.join([str(a) for a in data]))
                print('Out9 Current  %s%s' % (data[5], data[4]))
                print('Out10 Current  %s%s' % (data[7], data[6]))
                print('Out11 Current  %s%s' % (data[9], data[8]))
                print('Out12 Current  %s%s' % (data[11], data[10]))
                print('Out13 Current  %s%s' % (data[13], data[12]))
                print('Out14 Current  %s%s' % (data[15], data[14]))
                print('Out15 Current  %s%s' % (data[17], data[16]))
                print('Out16 Current  %s%s' % (data[19], data[18]))
                print('Out17 Current  %s%s' % (data[21], data[20]))
                print('Out18 Current  %s%s' % (data[23], data[22]))
                sys.stdout = log_file
                print('Test5.3: Read current on HS2A outputs drived with 100% duty cycle')
                print('Expected result: 0x01F4')
                print('obtained result:%s' % '/'.join([str(a) for a in data]))
                print('Out9 Current  %s%s' % (data[5], data[4]))
                print('Out10 Current  %s%s' % (data[7], data[6]))
                print('Out11 Current  %s%s' % (data[9], data[8]))
                print('Out12 Current  %s%s' % (data[11], data[10]))
                print('Out13 Current  %s%s' % (data[13], data[12]))
                print('Out14 Current  %s%s' % (data[15], data[14]))
                print('Out15 Current  %s%s' % (data[17], data[16]))
                print('Out16 Current  %s%s' % (data[19], data[18]))
                print('Out17 Current  %s%s' % (data[21], data[20]))
                print('Out18 Current  %s%s' % (data[23], data[22]))
                print('\n')

    def test_ReadHS12ACurrentDutycycle100(self):
        with Client(conn, request_timeout=1) as client:
            data = []
            req = services.RoutineControl.make_request(routine_id=0xFE1D,control_type=RoutineControl.ControlType.startRoutine, data=b'\x04')
            conn.send(req.get_payload())
            payload = conn.wait_frame(timeout=1)
            response = Response.from_payload(payload)
            services.RoutineControl.interpret_response(response)
            for j in range(len(response.data)):
                data.append(hex(response.data[j]))
            print('Test5.4: Read current on HS12A outputs drived with 100% duty cycle')
            print('Expected result: 0x01F4')
            print('HS12A Current:%s' % '/'.join([str(a) for a in data]))
            print('Out19 Current  %s%s' % (data[5], data[4]))
            print('Out20 Current  %s%s' % (data[7], data[6]))
            sys.stdout = log_file
            print('Test5.4: Read current on HS12A outputs drived with 100% duty cycle')
            print('Expected result: 0x01F4')
            print('obtained result:%s' % '/'.join([str(a) for a in data]))
            print('Out19 Current  %s%s' % (data[5], data[4]))
            print('Out20 Current  %s%s' % (data[7], data[6]))
            print('\n')

class TestOutputsDiag(unittest.TestCase):
    def test_CheckOutputsOC(self):
        with Client(conn, request_timeout=1) as client:
                retVal=0
                req2 = services.RoutineControl.make_request(routine_id=0xFE15,control_type=RoutineControl.ControlType.startRoutine,data=b'\x04')
                conn.send(req2.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                print('OutputsSC data %s:'%response.data)
                print('Test6.1: Detect OC on the outputs')
                print('Expected result: 0x03')
                print('Obtained result: %s' % response.data)
                if response.data[4] == 0:
                    for i in range(5, len(response.data) ):
                        print('Default detected on Out%s :%s' % (i , response.data[i]))
                        if response.data[i] != 3:
                            retVal=1
                    if retVal ==0:
                        print('Test result: OK','\n')
                    else:
                        print('Test result :NOK' ,'\n' )
                else:
                    print('Test result: NOk','\n')
                sys.stdout = log_file
                print('Test6.1: Detect OC on the outputs')
                print('Expected result: 0x03')
                print('Obtained result: %s' % response.data)
                if response.data[4] == 0:
                    for i in range(5, len(response.data) ):
                        print('Default detected on Out%s :%s' % (i , response.data[i]))
                        if response.data[i] != 3:
                            retVal=1
                    if retVal ==0:
                        print('Test result: OK','\n')
                    else:
                        print('Test result :NOK' ,'\n' )
                else:
                    print('Test result: NOk','\n')

                if response.data[4] != 0 or retVal !=0:
                    sys.stdout = sys.__stdout__
                    sys.stdout = log_file2
                    print('Test6.1: Detect OC on the outputs')
                    print('\t','Expected result: return code 0x03')
                    print('\t','Obtained result: %s' % response.data)
                    print('\t','Test result: NOK', '\n')
                    raise self.fail('Test failed')


    def test_CheckOutputsSC(self):
        with Client(conn, request_timeout=1) as client:
                req2 = services.RoutineControl.make_request(routine_id=0xFE15,control_type=RoutineControl.ControlType.startRoutine,data=b'\x04')
                conn.send(req2.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                print('Test6.2: Detect SC on the outputs from OUt5 to OUT20')
                print('Expected result: 0x01')
                print('Obtained result: %s' % response.data)
                if response.data[4] == 0:
                    for i in range(5, len(response.data)):
                        print('Default detected on Out%s :%s' % (i , response.data[i]))
                        if response.data[i] != 1:
                            retVal=1
                    if retVal ==0:
                        print('Test result: OK','\n')
                    else:
                        print('Test result :NOK' ,'\n' )
                else:
                    print('Test result: NOk','\n')
                sys.stdout = log_file
                print('Test6.2: Detect SC on the outputs from OUt5 to OUT20')
                print('Expected result: 0x01')
                print('Obtained result: %s' % response.data)
                if response.data[4] == 0:
                    for i in range(5, len(response.data) ):
                        print('Default detected on Out%s :%s' % (i, response.data[i]))
                        if response.data[i] != 1:
                            retVal=1
                    if retVal ==0:
                        print('Test result: OK','\n')
                    else:
                        print('Test result :NOK' ,'\n' )
                else:
                    print('Test result: NOk','\n')

                if response.data[4] != 0 or retVal != 0:
                    sys.stdout = sys.__stdout__
                    sys.stdout = log_file2
                    print('Test6.2: Detect SC on the outputs')
                    print('\t','Expected result: return code 0x01')
                    print('\t','Obtained result: %s' % response.data)
                    print('\t','Test result: NOK', '\n')
                    raise self.fail('Test failed')


class TestBridgesForward(unittest.TestCase):
    def test_DriveBridgesForward(self):
        with Client(conn, request_timeout=1) as client:
            time_execution = datetime.now() + timedelta(hours=0, seconds=5, microseconds=0, milliseconds=0, minutes=0)
            data=[]
            while datetime.now() < time_execution:
                req1 = services.RoutineControl.make_request(routine_id=0xFE14,control_type=RoutineControl.ControlType.startRoutine, data=b'\x01')
                conn.send(req1.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                print(response.data)
                for j in range(len(response.data)):
                    data.append(hex(response.data[j]))
                print('Drive the bridges to forward state:%s' % '/'.join([str(a) for a in data]) )
                print('Test7.1: drive The bridges to forward state')
                print('Expected result: return code 0 ')
                print('Obtained result: %s' % data[4])

                sys.stdout = log_file
                print('Test7.1: drive The bridges to forward state')
                print('Expected result: return code 0 ')
                print('Obtained result: %s' % data[4])
                if data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result: NOK','\n')
                    #raise self.fail('Test failed')

    def test_ReadFBForwardCurrent(self):
        with Client(conn, request_timeout=1) as client:
                data=[]
                req = services.RoutineControl.make_request(routine_id=0xFE1D, control_type=RoutineControl.ControlType.startRoutine,data=b'\x01')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                for j in range(len(response.data)):
                    data.append(hex(response.data[j]))

                print('Test7.2: Read current of the bridges in forward state')
                print('Expected result: 0x01F4')
                print('HB9ACurrent data:%s' % '/'.join([str(a) for a in data]) )
                print( 'FB1 Current  %s%s'%(data[5],data[4]))
                print('FB2 Current  %s%s' % (data[7], data[6]))
                sys.stdout = log_file
                print('Test7.2: Read current of the bridges in forward state')
                print('Expected result: 0x01F4')
                print('Obtained result: %s' % '/'.join([str(a) for a in data]))
                print( 'FB1 Current  %s%s'%(data[5],data[4]))
                print('FB2 Current  %s%s' % (data[7], data[6]))
                print('Test result:')
                print('\n')

class TestbridgesBrake(unittest.TestCase):
    def test_DriveBridgesBrake(self):
        with Client(conn, request_timeout=1) as client:
            time_execution = datetime.now() + timedelta(hours=0, seconds=5, microseconds=0, milliseconds=0, minutes=0)
            data=[]
            while datetime.now() < time_execution:
                req1 = services.RoutineControl.make_request(routine_id=0xFE14,control_type=RoutineControl.ControlType.startRoutine, data=b'\x02')
                conn.send(req1.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                print(response.data)
                for j in range(len(response.data)):
                    data.append(hex(response.data[j]))
                print('Drive the bridges to brake state:%s' % '/'.join([str(a) for a in data]) )
                print('Test8.1: drive The bridges to brake state')
                print('Expected result: return code 0 ')
                print('Obtained result: %s' % data[4])

                sys.stdout = log_file
                print('Test8.1: drive The bridges to brake state')
                print('Expected result: return code 0 ')
                print('Obtained result: %s' % data[4])
                if data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result: NOK','\n')
                    #raise self.fail('Test failed')


class TestBridgesReverse(unittest.TestCase):
    def test_DriveBridgesReverse(self):
            with Client(conn, request_timeout=1) as client:
                time_execution = datetime.now() + timedelta(hours=0, seconds=5, microseconds=0, milliseconds=0,minutes=0)
                data = []
                while datetime.now() < time_execution:
                    req1 = services.RoutineControl.make_request(routine_id=0xFE14,control_type=RoutineControl.ControlType.startRoutine,data=b'\x03')
                    conn.send(req1.get_payload())
                    payload = conn.wait_frame(timeout=1)
                    response = Response.from_payload(payload)
                    print(response.data)
                    for j in range(len(response.data)):
                        data.append(hex(response.data[j]))
                    print('Drive the bridges to reverse state:%s' % '/'.join([str(a) for a in data]))
                    print('Test9.1: drive The bridges to reverse state')
                    print('Expected result: return code 0 ')
                    print('Obtained result: %s' % data[4])

                    sys.stdout = log_file
                    print('Test9.1: drive The bridges to reverse state')
                    print('Expected result: return code 0 ')
                    print('Obtained result: %s' % data[4])
                    if data[4] == 0:
                        print('Test result: OK', '\n')
                    else:
                        print('Test result: NOK', '\n')
                        # raise self.fail('Test failed')

    def test_ReadFBRevsrseCurrent(self):
        with Client(conn, request_timeout=1) as client:
                data=[]
                req = services.RoutineControl.make_request(routine_id=0xFE1D, control_type=RoutineControl.ControlType.startRoutine,data=b'\x01')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                for j in range(len(response.data)):
                    data.append(hex(response.data[j]))
                print('Test9.2: Read current of the bridges in reverse state')
                print('Expected result: 0x01F4')
                print('HB9ACurrent data:%s' % '/'.join([str(a) for a in data]) )
                print( 'FB1 Current  %s%s'%(data[5],data[4]))
                print('FB2 Current  %s%s' % (data[7], data[6]))
                sys.stdout = log_file
                print('Test9.2: Read current of the bridges in reverse state')
                print('Expected result: 0x01F4')
                print('Obtained result: %s' % '/'.join([str(a) for a in data]))
                print( 'FB1 Current  %s%s'%(data[5],data[4]))
                print('FB2 Current  %s%s' % (data[7], data[6]))
                print('Test result:')
                print('\n')

class TestbridgesStop(unittest.TestCase):
    def test_DriveBridgesStop(self):
        time_execution = datetime.now() + timedelta(hours=0, seconds=5, microseconds=0, milliseconds=0, minutes=0)
        with Client(conn, request_timeout=1) as client:
            while datetime.now() < time_execution:
                data=[]
                req1 = services.RoutineControl.make_request(routine_id=0xFE14,control_type=RoutineControl.ControlType.startRoutine, data=b'\x04')
                conn.send(req1.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                print(response.data)
                for j in range(len(response.data)):
                    data.append(hex(response.data[j]))
                print('Drive the bridges to stop state:%s' % '/'.join([str(a) for a in data]) )
                print('Test10.1: drive The bridges to forward state')
                print('Expected result: return code 0 ')
                print('Obtained result: %s' % data[4])

                sys.stdout = log_file
                print('Test10.1: drive The bridges to stop state')
                print('Expected result: return code 0 ')
                print('Obtained result: %s' % data[4])
                if data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result: NOK','\n')

class TestSensorConfig(unittest.TestCase):
    def test_sensorSupplyConfig(self):
        with Client(conn, request_timeout=1) as client:
                req=services.RoutineControl.make_request(routine_id=0xFE18, control_type=RoutineControl.ControlType.startRoutine, data=b'\x01')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                print('sensorSupplyOutputs config: %s' % response.data)
                print('Test11.1:SensorSupplyConfig')
                print('Expected result: return code 0 ')
                print('Obtained result: %s' % response.data[4])
                sys.stdout = log_file
                print('Test11.1:SensorSupplyConfig')
                print('Expected result: return code 0 ')
                print('Obtained result: %s' % response.data[4])
                if response.data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result:sensor config  NOK','\n')

                if response.data[4] != 0:
                    sys.stdout = sys.__stdout__
                    sys.stdout = log_file2
                    print('Test11.1:SensorSupplyConfig')
                    print('\t','Expected result: return code 0')
                    print('\t','Obtained result: %s' % response.data[4])
                    print('\t','Test result: Sensor config NOK', '\n')
                    raise self.fail('Config of sensor supply as voltage outputs is failed')


class TestReadSensorValues(unittest.TestCase):
    def test_ReadSensorVoltage(self):
        with Client(conn, request_timeout=1) as client:
                SensorValue=[]
                req=services.RoutineControl.make_request(routine_id=0xFE18, control_type=RoutineControl.ControlType.startRoutine, data=b'\x03')
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                services.RoutineControl.interpret_response(response)
                for j in range(len(response.data)):
                    SensorValue.append(hex(response.data[j]))
                print('Test12.1: ReadSensorSupply')
                print('Expected result: 0x1770')
                print('obtained result: %s' % '/'.join(SensorValue))
                print( 'sensor1 value  %s%s'%(SensorValue[6],SensorValue[5]))
                print('sensor2 value  %s%s' % (SensorValue[8], SensorValue[7]))

                sys.stdout = log_file
                print('Test12.1: ReadSensorSupply')
                print('Expected result: 0x1770')
                print('Obtained result:%s' %'/'.join(SensorValue))
                print( 'sensor1 value  %s%s'%(SensorValue[6],SensorValue[5]))
                print('sensor2 value  %s%s' % (SensorValue[8], SensorValue[7]))
                if response.data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print('Test result: NOK','\n')
                    raise self.fail('Test failed')

class TestCAN(unittest.TestCase):
    def test_CheckReceivedFrame(self):
        with Client(conn, request_timeout=1) as client:
            req = services.RoutineControl.make_request(routine_id=0xFE1B, control_type=RoutineControl.ControlType.startRoutine,data=b'\x01')
            conn.send(req.get_payload())
            payload = conn.wait_frame(timeout=1)
            response = Response.from_payload(payload)
            print('CAN data :%s'%response.data)
            print('Test13.1: Check ReceivedFrame')
            print('Expected result: return code 0 ')
            print('Obtained result: %s' % response.data[4])
            services.RoutineControl.interpret_response(response)
            if response.data[4] ==1:
                print( 'RX failed')
            if response.data[4]== 2:
                print('CAN status NOK')
            sys.stdout = log_file
            print('Test13.1: Check ReceivedFrame')
            print('Expected result: return code 0 ')
            print('Obtained result: %s' % response.data[4])
            if response.data[4] == 0:
                    print('Test result: OK','\n')
            if response.data[4]==1:
                print('Test result: NOk : Rx NOK','\n')
                #raise self.fail('Test failed:Rx failed')
            if response.data[4]==2:
                print('Test result:  CAN status NOK','\n')
                #raise self.fail('Test failed: CAN status NOK')

            if response.data[4] == 1 or response.data[4]==2 :
                sys.stdout = sys.__stdout__
                sys.stdout = log_file2
                print('Test13.1: Check ReceivedFrame')
                print('\t','Expected result: return code 0')
                print('\t','Obtained result: %s' % response.data[4])
                if response.data[4] ==1:
                    print('\t','Test result: Rx failed', '\n')
                    raise self.fail('Test failed:Rx NOK')
                else:
                    print('\t','Test result: CAN status NOK', '\n')
                    raise self.fail('Test failed: CAN status NOK')


class TestEEPROM(unittest.TestCase):
    def test_CheckEEpromWrite(self):
        with Client(conn, request_timeout=1) as client:
                req = services.RoutineControl.make_request(routine_id=0xFE1A,control_type=RoutineControl.ControlType.startRoutine,data=b'\x01' )
                conn.send(req.get_payload())
                payload = conn.wait_frame(timeout=1)
                response = Response.from_payload(payload)
                print('EEPROM write data: %s' % response.data)
                print('Test14.1: CheckEepromWrite')
                print('Expected result: return code 0 ')
                print('Obtained result: %s' % response.data[4])
                services.RoutineControl.interpret_response(response)
                sys.stdout = log_file
                print('Test14.1: CheckEepromWrite')
                print('Expected result: return code 0 ')
                print('Obtained result: %s' % response.data[4])
                if response.data[4] == 0:
                    print('Test result: OK','\n')
                else:
                    print("test result: NOK",'\n')

                if response.data[4] != 0:
                    sys.stdout = sys.__stdout__
                    sys.stdout = log_file2
                    print('Test14.1: CheckEepromWrite')
                    print('\t','Expected result: return code 0')
                    print('\t','Obtained result: %s' % response.data[4])
                    print('\t','Test result: EEPROM write NOK', '\n')
                    raise self.fail('Test failed:writing in EEPROm is failed')

    def test_CheckEEpromRead(self):
        with Client(conn, request_timeout=2) as client:
            req = services.RoutineControl.make_request(routine_id=0xFE1A,control_type=RoutineControl.ControlType.startRoutine,data=b'\x02')
            conn.send(req.get_payload())
            payload = conn.wait_frame(timeout=1)
            response = Response.from_payload(payload)
            services.RoutineControl.interpret_response(response)
            print('EEPROM read data:%s'%response.data)
            print('Test14.2: CheckEepromRead')
            print('Expected result: return code 0 ')
            print('Obtained result: %s' % response.data[4])
            sys.stdout = log_file
            print('Test14.2: CheckEepromRead')
            print('Expected result: return code 0 ')
            print('Obtained result: %s' % response.data[4])
            if response.data[4] == 0:
                print('Test result: OK','\n')
            else:
                print("test result: NOK",'\n')

            # log to lo2.txt
            if  response.data[4] != 0:
                sys.stdout = sys.__stdout__
                sys.stdout=log_file2
                print('Test14.2: CheckEepromRead')
                print('\t','Expected result: return code 0')
                print('\t','Obtained result: %s' % response.data[4])
                print('\t','Test result: EEPROM read NOK', '\n')
                raise self.fail('Test failed: Read from EEPROM is failed')


def GetBspSwVersion():
    config = dict(udsoncan.configs.default_client_config)
    config['data_identifiers'] = {
        0x1234: MyCustomCodecThatShiftBy4,  # Uses own custom defined codec. Giving the class is ok
        0x1235: MyCustomCodecThatShiftBy4(),  # Same as 0x1234, giving an instance is good also
        0xFD05: udsoncan.AsciiCodec(64)  # Codec that read ASCII string. We must tell the length of the string
    }
    conn = PythonIsoTpConnection(stack)
    with Client(conn,  request_timeout=2, config=config) as client:
        response = client.read_data_by_identifier(0xFD05)
        return (response.service_data.values[0xFD05])


def GetBootSwVersion():
    config = dict(udsoncan.configs.default_client_config)
    config['data_identifiers'] = {
        0x1234: MyCustomCodecThatShiftBy4,  # Uses own custom defined codec. Giving the class is ok
        0x1235: MyCustomCodecThatShiftBy4(),  # Same as 0x1234, giving an instance is good also
        0xF180: udsoncan.AsciiCodec(64)  # Codec that read ASCII string. We must tell the length of the string
    }
    conn = PythonIsoTpConnection(stack)
    with Client(conn,  request_timeout=2, config=config) as client:
        response = client.read_data_by_identifier(0xF180)
        return (response.service_data.values[0xF180])


def GetPulseNumber(self):
        config = dict(udsoncan.configs.default_client_config)
        config['data_identifiers'] = {
            0x1234: MyCustomCodecThatShiftBy4,  # Uses own custom defined codec. Giving the class is ok
            0x1235: MyCustomCodecThatShiftBy4(),  # Same as 0x1234, giving an instance is good also
            0xFD0E: udsoncan.AsciiCodec(64)  # Codec that read ASCII string. We must tell the length of the string
        }
        conn = PythonIsoTpConnection(stack)
        with Client(conn, request_timeout=2, config=config) as client:
            response = client.read_data_by_identifier(0xFD0E)
            print (response.service_data.values[0xFD0E])

'''
if __name__ == '__main__':
    # Create the report file
    html_report = open('templates/test_report.html', 'w')
    # Create the runner and set the file as output and higher verbosity
    runner = HTMLTestRunner.HTMLTestRunner(stream=html_report)
    # Create a test list
    tests = []
    # Load test cases
    loader = unittest.TestLoader()
    # Create a SuiteCase
    test_list = []
    for test in tests:
        cases = loader.loadTestsFromTestCase(test)
        test_list.append(cases)
    suite = unittest.TestSuite(test_list)
    # Run the suite
    runner.run(suite)
    url = "C:/Users/nguesmi/PycharmProjects/VENTURA_Tests_Script/VENTURA_Tests_Script/templates/test_report.html"
    webbrowser.open(url)

'''
'''
if __name__ == '__main__':
        html_report = open('templates/test_report.html', 'w')
        # Create the runner and set the file as output and higher verbosity
        runner = HTMLTestRunner.HTMLTestRunner(stream=html_report, verbosity=2)
        # Create a test list
        tests1 = TestLoader().loadTestsFromTestCase(TestInit)
        tests2 = TestLoader().loadTestsFromTestCase(TestInputs)
        tests3 = TestLoader().loadTestsFromTestCase(TestOutputs)
        tests4 = TestLoader().loadTestsFromTestCase(TestCAN)
        tests5 = TestLoader().loadTestsFromTestCase(TestEEPROM)
        suite = TestSuite([tests1,tests2,tests3,tests4,tests5])
        runner.run(suite)
        url = "C:/Users/nguesmi/PycharmProjects/VENTURA_Tests_Script/VENTURA_Tests_Script/templates/test_report.html"
        webbrowser.open(url)
'''
