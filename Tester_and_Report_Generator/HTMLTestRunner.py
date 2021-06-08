
import logging
from can.interfaces.pcan import PcanBus
from udsoncan.connections import PythonIsoTpConnection
from udsoncan.services.RoutineControl import RoutineControl
from udsoncan.client import Client
#from datetime import datetime, timedelta
from udsoncan.Response import Response
from udsoncan.client import services
import udsoncan.configs
import isotp
import time
#import unittest
import struct
import sys,pytest

__version__ = "1.0.2"
from datetime import datetime, timedelta
from io import StringIO
from unittest import TestResult, TestProgram
from xml.sax import saxutils
import sys
from flask import Flask
from unittest import suite
import unittest
#import TestIO
from unittest import TestLoader, TestSuite
import webbrowser
import os 

app = Flask(__name__)


################### UDSONCAN CONFIG #####################
log_file = open(os.getcwd() + '\log.txt', 'a')
log_file2 = open(os.getcwd() + 'TestsNOK.txt', 'a')
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
conn = PythonIsoTpConnection(stack)  




def get_RDBI(vrb):
        
    config = dict(udsoncan.configs.default_client_config)
    config['data_identifiers'] = {
    
    vrb : udsoncan.AsciiCodec(64)  # Codec that read ASCII string. We must tell the length of the string
    }
    with Client(conn, request_timeout= 1, config = config ) as client:  
        
                                    
        response = client.read_data_by_identifier(vrb)
        return response.data.decode(encoding='windows-1252')

# ------------------------------------------------------------------------
# The redirectors below are used to capture output during testing. Output
# sent to stdout and stderr are automatically captured. However
# in some cases stdout is already cached before HTMLTestRunner is
# invoked (e.g. calling logging.basicConfig). In order to capture those
# output, use the redirectors for the cached stream.
#
# e.g.
#   >>> logging.basicConfig(stream=HTMLTestRunner.stdout_redirector)
#   >>>

def to_unicode(s):
    try:
        return str(s)
    except UnicodeDecodeError:
        # s is non ascii byte string
        return s.decode('unicode_escape')

class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """
    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(to_unicode(s))

    def writelines(self, lines):
        lines = map(to_unicode, lines)
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()

stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)



# ----------------------------------------------------------------------
# Template

class Template_mixin(object):
    """
    Define a HTML template for report customerization and generation.
    Overall structure of an HTML report
    HTML
    +------------------------+
    |<html>                  |
    |  <head>                |
    |                        |
    |   STYLESHEET           |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </head>               |
    |                        |
    |  <body>                |
    |                        |
    |   HEADING              |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   REPORT               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   ENDING               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </body>               |
    |</html>                 |
    +------------------------+
    """

    STATUS = {
    0: 'pass',
    1: 'fail',
    2: 'error',
    3: 'skip',
    }

    DEFAULT_TITLE = 'ActiMux'
    DEFAULT_DESCRIPTION = 'Software Validation - Tests Automator'

    # ------------------------------------------------------------------------
    # HTML Template

    HTML_TMPL = r"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body,h1,h2,h3,h4,h5,h6 {font-family: "Raleway", sans-serif}
</style>
<head>
    <title>%(title)s</title>
    <meta name="generator" content="%(generator)s"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    %(stylesheet)s
	
<script src="https://code.jquery.com/jquery-1.12.0.min.js"></script>
<script src="https://cdn.bootcss.com/echarts/3.8.5/echarts.common.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script type=text/javascript>
      $SCRIPT_ROOT = {{ request.script_root|tojson|safe }};
</script>
<script>
$(document).ready(function(){
  var seen = [];  
  var tableRows = document.getElementsByTagName('tr');
  for(i = 0; i < tableRows.length; i++){
    var tableData = tableRows[i].getElementsByTagName('td');
    var value = tableData[0].innerText;
    if(seen[value]){
      tableRows[i].style.display = "none"; 
    }else{
      seen[value] = true;
    }
  }
});
</script>

</head>
<body class="w3-light-grey w3-content" style="max-width:1600px; background-color: #f2f2f2;">
<script language="javascript" type="text/javascript"><!--
output_list = Array();
/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}

function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}
function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}

function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}
/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
--></script>
%(heading)s
%(report)s
%(ending)s
%(chart_script)s
</body>
</html>
"""
    # variables: (title, generator, stylesheet, heading, report, ending,chart_script)
    ECHARTS_SCRIPT = """
<script type="text/javascript">
//
var myChart = echarts.init(document.getElementById('chart'));

// 
var option = {
title : {
text: 'Graphic charter showing the status of tests',
x:'center'
},
tooltip : {
trigger: 'item',
formatter: "{a} <br/>{b} : {c} ({d}%%)"
},
color: ['#95b75d', 'grey', '#b64645'],
legend: {
orient: 'vertical',
left: 'left',
data: ['pass','fail','error']
},
series : [
{
name: 'chart',
type: 'pie',
radius : '60%%',
center: ['50%%', '60%%'],
data:[
{value:%(Pass)s, name:'pass'},
{value:%(fail)s, name:'fail'},
{value:%(error)s, name:'error'}
],
itemStyle: {
emphasis: {
shadowBlur: 10,
shadowOffsetX: 0,
shadowColor: 'rgba(0, 0, 0, 0.5)'
}
}
}
]
};

//
myChart.setOption(option);
</script>
""" # variables: (Pass, fail, error)
	
    # ------------------------------------------------------------------------
    # Stylesheet
    #
    # alternatively use a <link> for external style sheet, e.g.
    #   <link rel="stylesheet" href="$url" type="text/css">

    STYLESHEET_TMPL = """
<style type="text/css" media="screen">
body        {  font-size: 100%; }
table       { font-size: 100%; margin: auto;}
pre         { }
/* -- heading ---------------------------------------------------------------------- */
h1 {
  text-align: left;
  font-family: 'Oswald', Helvetica, sans-serif;
  font-size: 40px;
  transform: skewY(-0deg);
  letter-spacing: 4px;
  word-spacing: -8px;
  color: #004d4d;

}
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}
.heading .attribute {
    margin-top: 1ex;
    margin-bottom: 0;
}
.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}
/* -- css div popup ------------------------------------------------------------------------ */
a.popup_link {
}
a.popup_link:hover {
    color: red;
}
.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    padding: 10px;
    background-color: #E6E6D6;
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 8pt;
    width: 900px;
}


/* -- report ------------------------------------------------------------------------ */
#show_detail_line {
    margin-top: 3ex;
    margin-bottom: 1ex;

}

#result_table {
    width: 95%;
    border-collapse: collapse;

}

#header_row {
    font-weight: bold;
    color: #4b7467;
    background-color: #c8d8e4;
}

#total_row  { font-weight: bold; }
.passClass  { background-color: #6c6; }
.failClass  { background-color: #c60; }
.errorClass { background-color: #c00; }
.skipClass  { background-color: #ff0; }
.passCase   { color: #6c6; }
.failCase   { color: #c60; font-weight: bold; }
.skipCase   { color: #ff0; font-weight: bold; }
.errorCase  { color: #c00; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }
/* -- ending ---------------------------------------------------------------------- */
#ending {
}
</style>
"""

    ################################ WORK HERE TO MODIFY THE TEMPLATE - MAHDI ARFAOUI ########################

    # ------------------------------------------------------------------------
    # Heading
    #

    HEADING_TMPL = """<div class='heading w3-container'>              
                        <div class="w3-container w3-center">
            <img src="../../logo_transparent.png" alt="log"  class="w3-image w3-center" style= "width:90%%; max-width:300px;">
        </div>
                        <h4 class='description w3-center '><strong>%(description)s</strong></h4>
                            <div class="w3-row w3-border w3-round-large" style="background-color:  #2b6777;">
                                <div class="w3-half w3-container" style="text-align:left; background-color:c8d8e4; color : #f2f2f2;">
                                    %(parameters)s
                                </div>
                                <div class="w3-half w3-container w3-border w3-round-large" style="background-color: #c8d8e4 ;">
                                <div class ='w3-container w3-center' id="chart" style="width:100%%;height:400px; position: relative; margin:auto;"></div>
                                </div>

                            </div>
                    </div>

""" # variables: (title, parameters, description)

    HEADING_ATTRIBUTE_TMPL = """<p class='attribute w3-container'><strong>%(name)s :</strong> %(value)s</p>
""" # variables: (name, value)



    # ------------------------------------------------------------------------
    # Report
    #

    REPORT_TMPL = """

<div class ='w3-container w3-center' id='show_detail_line'>Show
<a href='javascript:showCase(0)'>Summary</a>
<a href='javascript:showCase(1)'>Failed</a>
<a href='javascript:showCase(2)'>All</a>
</div>

<table class='w3-table w3-striped w3-card-4 w3-border w3-round-large w3-hoverable ' id='result_table'>
<colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>
<tr id='header_row'>
    <td>Test Group/Test case</td>
    <td>Count</td>
    <td>Pass</td>
  <!--  <td>Skip</td> -->
    <td>Fail</td>
    <td>Error</td>
    <td>View</td>
</tr>
%(test_list)s
<tr id='total_row'>
    <td>Total</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
<!-- <td>%(skip)s</td> -->  
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td>&nbsp;</td>
</tr>
</table>
""" # variables: (test_list, count, Pass, fail, error)

    REPORT_CLASS_TMPL = r"""
<tr class='%(style)s'>
    <td>%(desc)s</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
   <td>%(error)s</td>
    <td><a href="javascript:showClassDetail('%(cid)s',%(count)s)">Detail</a></td>
</tr>
""" # variables: (style, desc, count, Pass, fail, error, cid)


    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td  class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>
    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_%(tid)s')" > View log</a>
    <div id='div_%(tid)s' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_%(tid)s').style.display = 'none' " >
           [x]</a>
        </div>
        <div class="w3-container" style="width:100%%;overflow:auto">
        <pre>
        %(script)s
        </pre>
        </div>
    </div>
    <!--css div popup end-->
    </td>
</tr>
""" # variables: (tid, Class, style, desc, status)


    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s '>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>View log</td>
</tr>
""" # variables: (tid, Class, style, desc, status)


    REPORT_TEST_OUTPUT_TMPL = r"""
%(id)s: %(output)s
""" # variables: (id, output)



    # ------------------------------------------------------------------------
    # ENDING
    #

    ENDING_TMPL = """<div class='w3-container' id='ending'>&nbsp;</div>"""

# -------------------- The end of the Template class -------------------


TestResult = unittest.TestResult
class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1):
        TestResult.__init__(self)
        self.outputBuffer = StringIO()
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.skip_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity

        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []


    def startTest(self, test):
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector


    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()


    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        self.complete_output()


    def addSuccess(self, test):
        self.success_count += 1
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')

    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        _exc_str = self.errors[-1][1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _exc_str = self.failures[-1][1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')

    def addSkip(self, test, err):
        self.skip_count += 1
        TestResult.addSkip(self, test, err)
        _exc_str = self.skipped[-1][1]
        output = self.complete_output()
        self.result.append((3, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('S  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('S')


class HTMLTestRunner(Template_mixin):
    """
    """
    def __init__(self, stream=sys.stdout, verbosity=1, title=None, description=None):
        self.stream = stream
        self.verbosity = verbosity
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description

        self.startTime = datetime.now().replace(microsecond=0)

    def run(self, test, count ,rep, flag ):
        "Run the given test case or test suite."
        result = _TestResult(self.verbosity)
        test(result)
        
        if flag and count == rep -1 :
            result.success_count +=TestPassed
            result.failure_count +=TestFailed
            result.error_count += TestError
            result.result += TestR
            self.generateReport(test,result)
        
        
        return result

    def sortResult(self, result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
        rmap = {}
        classes = []
        for n,t,o,e in result_list:
            cls = t.__class__
            if not cls in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n,t,o,e))
        r = [(cls, rmap[cls]) for cls in classes]
        return r


    def getReportAttributes(self, result):
        """
        Return report attributes as a list of (name, value).
        Override this to add custom attributes.
        """
        startTime = str(self.startTime)
        #duration = str(self.stopTime - self.startTime)
        status = []
        if result.success_count: status.append('Pass %s'    % (result.success_count ))
        #if result.skip_count:    status.append('Skip %s'    % result.skip_count   )
        if result.failure_count: status.append('Failure %s' % (result.failure_count ))
        if result.error_count:   status.append('Error %s'   % (result.error_count ))
        if status:
            status = ' '.join(status)
        else:
            status = 'none'
        BootLoaderVersion = str(get_RDBI(0xF180))
        BspVersion = str(get_RDBI(0xF186))
        PythonVersion= sys.version

        return [
            ('Start Time', startTime),
#            ('Duration', duration),
            ('Status', status),
            ('BootLoader Version', BootLoaderVersion),
            ('BSP Version', BspVersion),
            ('Python Version', PythonVersion),

        ]

    def generateReport(self,test, result):
        report_attrs = self.getReportAttributes(result)
        generator = 'HTMLTestRunner %s' % __version__
        stylesheet = self._generate_stylesheet()
        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)
        ending = self._generate_ending()
        chart = self._generate_chart(result)
        output = self.HTML_TMPL % dict(
            title = saxutils.escape(self.title),
            generator = generator,
            stylesheet = stylesheet,
            heading = heading,
            report = report,
            ending = ending,
            chart_script = chart,
        )
        self.stream.write(output)

    def _generate_stylesheet(self):
        return self.STYLESHEET_TMPL

    def _generate_heading(self, report_attrs):
        a_lines = []
        for name, value in report_attrs:
            line = self.HEADING_ATTRIBUTE_TMPL % dict(
                    name = saxutils.escape(name),
                    value = saxutils.escape(value),
                )
            a_lines.append(line)
        heading = self.HEADING_TMPL % dict(
            title = saxutils.escape(self.title),
            parameters = ''.join(a_lines),
            description = saxutils.escape(self.description),
        )
        return heading

    def _generate_report(self, result):
        rows = []
        sortedResult = self.sortResult(result.result)
        for cid, (cls, cls_results) in enumerate(sortedResult):
            # subtotal for a class
            np = ns = nf = ne = 0
            for n,t,o,e in cls_results:
                if n == 0: np += 1
                elif n == 1: nf += 1
                elif n == 2: ne += 1
                elif n == 3: ns += 1

            # format class description
            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
            desc = doc and '%s: %s' % (name, doc) or name

            row = self.REPORT_CLASS_TMPL % dict(
                style = ne > 0 and 'errorClass' or nf > 0 and 'failClass' or ns > 0 and 'skipClass' or 'passClass',
                desc = desc,
                count = (np+ns+nf+ne),
                Pass = np,
                fail = nf,
                error = ne,
                skip=ns,
                cid = 'c%s' % (cid+1),
            )
            rows.append(row)
            
            for tid, (n,t,o,e) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e,cls_results)


        report = self.REPORT_TMPL % dict(
            test_list = ''.join(rows),
            count = str((result.success_count+result.failure_count+result.error_count+result.skip_count)),
            Pass = str(result.success_count ),
            skip = str(result.skip_count),
            fail = str(result.failure_count ),
            error = str(result.error_count ),
        )
        return report

    def _generate_chart(self, result):
        chart = self.ECHARTS_SCRIPT % dict(Pass=str(result.success_count),fail=str(result.failure_count),error=str(result.error_count ))
        return chart

    def _generate_report_test(self, rows, cid, tid, n, t, o, e,cls_results):
        
        # e.g. 'pt1.1', 'ft1.1', etc
        has_output = bool(o or e)
        tid = (n == 0 and 'p' or 'f') + 't%s.%s' % (cid+1,tid+1)
        #name = t.id().split('.')[-1] #################################################!!!!!#################
        
        #ATTRIBUTE########
        # e = error
        # n = (probably) name
        # t = class name
        # n = numbers ==> to explore
        # tid = test ID (exp : ft1.1 ft1.2 ....)

        
       # with open(r"C:\Users\Mahdi\Desktop\GIT_HUB_Directory_PFE2021\resultREScls.txt" , "a") as f :
            
           # f.write(str(cls_results) + "\n")

        n1 = o.split("\n")

        

        
        if len(n1)>1:
            if n1[1] == "":
                w1 = n1[0]
            else:
                w1 = n1[1]
            w2 = w1.split(':')
            
            name = w2[1]
        else : 
            name = "TEST INVALID"

        

        doc = t.shortDescription() or ""
        desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL or self.REPORT_TEST_NO_OUTPUT_TMPL

        # o and e should be byte string because they are collected from stdout and stderr?
        if isinstance(o,str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # uo = unicode(o.encode('string_escape'))
            uo = bytes(o, 'utf-8').decode('latin-1')
        else:
            uo = o
        if isinstance(e,str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # ue = unicode(e.encode('string_escape'))
            ue = bytes(e, 'utf-8').decode('latin-1')
        else:
            ue = e
        '''
        logtest =""
        log=[]
        for t,o in enumerate(cls_results):
            Testresult = o
            testname=  t
            for t, o in enumerate(cls_results) :
                if testname == t:
                    log.extend(o)
            logtest= '\n'.join([str(elem) for elem in log])
        '''
        script = self.REPORT_TEST_OUTPUT_TMPL % dict(
            id = tid ,
            output = saxutils.escape(uo+ue),
        )
        row = tmpl % dict(
            tid = tid,
            Class = (n == 0 and 'hiddenRow' or 'none'),
            style = n == 2 and 'errorCase' or (n == 1 and 'failCase' or 'none'),
            desc = desc,
            script = script,
            status = self.STATUS[n],
        )
        rows.append(row)
        if not has_output:
            return

    def _generate_ending(self):
        return self.ENDING_TMPL


##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# parameters like test title, CSS, etc.

class _TestProgram(TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """
    def runTests(self):
        # Pick HTMLTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate HTMLTestRunner before we know self.verbosity.
        if self.testRunner is None:
            self.testRunner = HTMLTestRunner(verbosity=self.verbosity)
        TestProgram.runTests(self)


main = _TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################
'''
@app.route('/')
def index():
    return render_template('test_report.html')

@app.route('/process')
def process():
        # Create the report file
        html_report = open('templates/test_report.html', 'w')
        # Create the runner and set the file as output and higher verbosity
        runner = HTMLTestRunner(stream=html_report, verbosity=2)
        # Create a test list
        tests1 = TestLoader().loadTestsFromTestCase(TestIO.TestInit)
        tests2 = TestLoader().loadTestsFromTestCase(TestIO.TestOutputs)
        tests3 = TestLoader().loadTestsFromTestCase(TestIO.TestInputs)
        suite = TestSuite([tests1,tests2,tests3])
        runner.run(suite)
        return render_template('test_report.html')
        url = "http://127.0.0.1:5000/"
        webbrowser.open(url)


@app.route('/stop')
def stop():
    pytest.skip()
    TestIO.Connexion.stopConnexion()

if __name__ == '__main__':
    app.run()

'''
################ TESTCASE Class ################

     ######## Routine Control #######
class Test_Routine_Control(unittest.TestCase):
    def __init__(self, testName, extraArg):
        super(Test_Routine_Control, self).__init__(testName)  # calling the super class init varies for different python versions.  This works for 2.7
        self.myExtraArg = extraArg
        

    def test_RC(self):
        
        with Client(conn, request_timeout=1) as client:  
            data=[]
            idd = int(self.myExtraArg[1],16) #ID
            vrb = bytes.fromhex(self.myExtraArg[2])   # Data                              
            req=services.RoutineControl.make_request(routine_id=idd, control_type=RoutineControl.ControlType.startRoutine, data=vrb)
            conn.send(req.get_payload()) #send the request
            payload =conn.wait_frame(timeout=1)
            response = Response.from_payload(payload)
            services.RoutineControl.interpret_response(response)
            #print(response.data)
            for j in range(len(response.data)):
                data.append(hex(response.data[j]))
            print('obtained data:%s' % '/'.join([str(a) for a in data]))
            print("Test : "+ self.myExtraArg[0]) # Test Name
            print('Expected result: Return code 0')
            #print('Obtained result: %s'%str(response.data[4]))
            
            bb = str(data[5])
            dd = str(data[6])

            al = bb + dd[2:4]
            inti = int(al,16)
            print('Obtained result: %s'%str(inti))


            sys.stdout = sys.__stdout__
            sys.stdout = log_file
            print("Test : "+ self.myExtraArg[0])
            print('Expected result: Return code 0')
            print('Obtained result: %s'%response.data[4])
            if inti > 22750:
                print('Test result: OK','\n')
            else:
                print('Test result: RC NOK','\n')

            if inti < 22750:
                sys.stdout = sys.__stdout__
                sys.stdout = log_file2
                print("Test : "+ self.myExtraArg[0])
                print('\t','Expected result: return code 0')
                print( '\t','Obtained result: %s' % response.data[4])
                print('\t','Test result: RC NOK', '\n')
                raise self.fail('Test failed: RC not OK')

    

     ######## RDBI #######
class Test_RDBI(unittest.TestCase):

    
    def __init__(self, testName, extraArg):
        super(Test_RDBI, self).__init__(testName)  # calling the super class init varies for different python versions.  This works for 2.7
        self.myExtraArg = extraArg
        self.vrb = int(self.myExtraArg[1],16) #ID 
    
    
    def test_RDBI(self):
        
        config = dict(udsoncan.configs.default_client_config)
        config['data_identifiers'] = {
      
        self.vrb : udsoncan.AsciiCodec(64)  # Codec that read ASCII string. We must tell the length of the string
        }
        with Client(conn, request_timeout= 1, config = config ) as client:  
            
                                      
            response = client.read_data_by_identifier(self.vrb)
            #services.ReadDataByIdentifier.interpret_response(response)
            print(response.data)
            print("Test : "+ self.myExtraArg[0]) # Test Name
            print('Expected result: Return code 0')
            print('Obtained result: %s'%response.code)

            sys.stdout = sys.__stdout__
            sys.stdout = log_file
            print(response.data)
            print(response.code)
            print("Test : "+ self.myExtraArg[0])
            print('Expected result: Return code 0')
            print('Obtained result: %s'%response.code)
            if response.code == 0:
                print('Test result: OK','\n')
            else:
                print('Test result: init all IO NOK','\n')

            if response.code != 0:
                sys.stdout = sys.__stdout__
                sys.stdout = log_file2
                print("Test : "+ self.myExtraArg[0])
                print('\t','Expected result: return code 0')
                print( '\t','Obtained result: %s' % response.code)
                print('\t','Test result: RDBI NOK', '\n')
                raise self.fail('Test failed: RDBI not OK')



######## WDBI #######
class Test_WDBI(unittest.TestCase):

    
    def __init__(self, testName, extraArg):
        super(Test_WDBI, self).__init__(testName)  # calling the super class init varies for different python versions.  This works for 2.7
        self.myExtraArg = extraArg
        self.vrb = int(self.myExtraArg[1],16) #ID 
        self.dat = extraArg[2]
    
    
    def test_WDBI(self):
        
        config = dict(udsoncan.configs.default_client_config)
        config['data_identifiers'] = {
        self.vrb : udsoncan.AsciiCodec(len(self.dat))  # Codec that read ASCII string. We must tell the length of the string
        }

        with Client(conn, request_timeout= 1, config = config ) as client:  
            
                                      
            response = client.write_data_by_identifier(self.vrb, self.dat)
            #services.ReadDataByIdentifier.interpret_response(response)
            print(response.data)
            print("Test : "+ self.myExtraArg[0]) # Test Name
            print('Expected result: Return code 0')
            print('Obtained result: %s'%response.code)

            sys.stdout = sys.__stdout__
            sys.stdout = log_file
            print(response.data)
            print(response.code)
            print("Test : "+ self.myExtraArg[0])
            print('Expected result: Return code 0')
            print('Obtained result: %s'%response.code)
            if response.code ==0:
                print('Test result: OK','\n')
            else:
                print('Test result: init all IO NOK','\n')

            if response.code != 0:
                sys.stdout = sys.__stdout__
                sys.stdout = log_file2
                print("Test : "+ self.myExtraArg[0])
                print('\t','Expected result: return code 0')
                print( '\t','Obtained result: %s' % response.code)
                print('\t','Test result: WDBI NOK', '\n')
                raise self.fail('Test failed: WDBI not OK')

###############"" Modified Loader ###############
class TestLoaderWithKwargs(unittest.TestLoader):
    """A test loader which allows to parse keyword arguments to the
       test case class."""
    def loadTestsFromTestCase(self, testCaseClass, **kwargs):
        """Return a suite of all tests cases contained in 
           testCaseClass."""
        if issubclass(testCaseClass, suite.TestSuite):
            raise TypeError("Test cases should not be derived from TestSuite. Maybe you meant to derive from TestCase?")
        testCaseNames = self.getTestCaseNames(testCaseClass)
        if not testCaseNames and hasattr(testCaseClass, 'runTest'):
            testCaseNames = ['runTest']

        # Modification here: parse keyword arguments to testCaseClass.
        test_cases = []
        for test_case_name in testCaseNames:
            test_cases.append(testCaseClass(test_case_name, **kwargs))
        loaded_suite = self.suiteClass(test_cases)

        return loaded_suite 

if __name__ == '__main__':
        
        # Aquiring and processing received Data from GUI App
        global args
        argss = sys.argv
        
        
        NoS = int(argss[1])
        servicesNames = argss[2:2+NoS]
        numOfServicesTests = argss[2+NoS : 2 + 2 * NoS ]
        testName = []
        testID = []
        testData = []
        testRep = []
        testIndex = []
       

            

        
        
        countt = 0
        for i in range(2 + 2 * NoS ,len(argss) , 5):
            testName.append(argss[i])
            testID.append(argss[i+1])
            testData.append(argss[i+2])
            testRep.append(int(argss[i+3]))
            testIndex.append(argss[i+4])
            #with open(r'C:\Users\Mahdi\Desktop\GIT_HUB_Directory_PFE2021\result.txt', 'a') as f:
               # f.write(testName[countt] + " " + testID[countt] + " " + testData[countt] + " " + str(testRep[countt]) + " " + str(testIndex[countt]) + "\n") 
            countt+=1
            
        #logging.debug(chosenService)
        
        global count 
        count = 0
        global time_execution
        global counter_execution
        global TestPassed
        global TestFailed
        global TestError
        global TestR
        TestR= []
        TestError =0
        TestFailed =0
        TestPassed=0
        counter_execution =0
        time_execution= datetime.now() + timedelta(hours=0,seconds=1,microseconds=0,milliseconds=0,minutes=0)
        #print (time_execution)
        html_report = open(r'C:\Users\Mahdi\Desktop\FIN_Project\Tester_and_Report_Generator\templates\TEESSSSSEEEETOO_report.html', 'w')
        # Create the runner and set the file as output and higher verbosity
        runner = HTMLTestRunner(stream=html_report, verbosity=2)
        currService = 0
        currTest = 0
        holder = 0
        while currService < NoS :
            #with open(r'C:\Users\Mahdi\Desktop\GIT_HUB_Directory_PFE2021\result.txt', 'a') as f:
               # f.write("CurrService = "+ str(currService) + ", SERVICE NAME : " + servicesNames[currService] + "\n")
            
            if servicesNames[currService] == 'RC':   
                #currTest = 0   
                if currService == 0 :
                    holder = int(numOfServicesTests[currService])
                else:
                    holder = holder + int(numOfServicesTests[currService ])         
                while currTest < holder :
                    
                   # with open(r'C:\Users\Mahdi\Desktop\GIT_HUB_Directory_PFE2021\result.txt', 'a') as f:
                       # f.write("Holder : "+ str(holder) +" , CurrService = "+ str(currService) + ", CurrTest = " + str(currTest) + ",  TEST name : " + testName[currTest] + "\n" )                   
                    
                    if (currTest == holder - 1) and (currService == NoS - 1): # execute and generate report
                        count = 0
                        while count < testRep[currTest]:
                            argsRC = [testName[currTest], testID[currTest], testData[currTest]]
                            loader = TestLoaderWithKwargs()
                            tests = loader.loadTestsFromTestCase(Test_Routine_Control, extraArg = argsRC)
                            sss = TestSuite([tests])
                            counter_execution += 1
                            result=runner.run(sss, count ,testRep[currTest], True)
                            TestPassed += result.success_count
                            TestFailed += result.failure_count
                            TestError += result.error_count
                            TestR += result.result
                            count += 1  
                        currTest += 1

                    else : # Execute only cause there are more Tests
                        count = 0
                        while count < testRep[currTest]:
                            argsRC = [testName[currTest], testID[currTest], testData[currTest]]
                            loader = TestLoaderWithKwargs()
                            tests = loader.loadTestsFromTestCase(Test_Routine_Control, extraArg = argsRC)
                            sss = TestSuite([tests])
                            counter_execution += 1
                            result=runner.run(sss, count ,testRep[currTest], False)
                            TestPassed += result.success_count
                            TestFailed += result.failure_count
                            TestError += result.error_count
                            TestR += result.result
                            count += 1 
                        currTest += 1 
                
                currService += 1
                
                        
                        


            elif servicesNames[currService] == 'RDBI':
                #currTest = 0
                if currService == 0 :
                    holder = int(numOfServicesTests[currService])
                else:
                    holder = holder + int(numOfServicesTests[currService])

                while currTest < holder : #execute without generation
              
                   # with open(r'C:\Users\Mahdi\Desktop\GIT_HUB_Directory_PFE2021\result.txt', 'a') as f:
                       # f.write("Holder : "+ str(holder) +" , CurrService = "+ str(currService) + ", CurrTest = " + str(currTest) + ",  TEST name : " + testName[currTest] + "\n" )                   
                    
                    if currTest == holder - 1 and currService == NoS - 1: # execute and generate report
                        count = 0
                        while count < testRep[currTest]:
                            argsRDBI = [testName[currTest], testID[currTest]]
                            loader = TestLoaderWithKwargs()
                            tests = loader.loadTestsFromTestCase(Test_RDBI, extraArg = argsRDBI)
                            sss = TestSuite([tests])
                            counter_execution += 1
                            result=runner.run(sss, count ,testRep[currTest], True)
                            TestPassed += result.success_count
                            TestFailed += result.failure_count
                            TestError += result.error_count
                            TestR += result.result
                            count += 1  
                        currTest += 1
                    else :
                        count = 0
                        while count < testRep[currTest]:
                            argsRDBI = [testName[currTest], testID[currTest]]
                            loader = TestLoaderWithKwargs()
                            tests = loader.loadTestsFromTestCase(Test_RDBI, extraArg = argsRDBI)
                            sss = TestSuite([tests])
                            counter_execution += 1
                            result=runner.run(sss, count ,testRep[currTest], False)
                            TestPassed += result.success_count
                            TestFailed += result.failure_count
                            TestError += result.error_count
                            TestR += result.result
                            count += 1 
                        currTest += 1 

                currService += 1

            elif servicesNames[currService] == 'WDBI':
                #currTest = 0
                if currService == 0 :
                    holder = int(numOfServicesTests[currService])
                else:
                    holder = holder + int(numOfServicesTests[currService])

                while currTest < holder : #execute without generation
                   
                    
                   
                    
                   # with open(r'C:\Users\Mahdi\Desktop\GIT_HUB_Directory_PFE2021\result.txt', 'a') as f:
                       # f.write("Holder : "+ str(holder) +" , CurrService = "+ str(currService) + ", CurrTest = " + str(currTest) + ", TEST name : \n"  )

                    if currTest == holder - 1 and currService == NoS - 1:# execute and generate report
                        count = 0
                        while count < testRep[currTest]:
                            argsWDBI = [testName[currTest], testID[currTest], testData[currTest]]
                            loader = TestLoaderWithKwargs()
                            tests = loader.loadTestsFromTestCase(Test_WDBI, extraArg = argsWDBI)
                            sss = TestSuite([tests])
                            counter_execution += 1
                            result=runner.run(sss, count ,testRep[currTest], True)
                            TestPassed += result.success_count
                            TestFailed += result.failure_count
                            TestError += result.error_count
                            TestR += result.result
                            count += 1  
                        currTest += 1
                    else :
                        count = 0
                        while count < testRep[currTest]:
                            argsWDBI = [testName[currTest], testID[currTest], testData[currTest]]
                            loader = TestLoaderWithKwargs()
                            tests = loader.loadTestsFromTestCase(Test_WDBI, extraArg = argsWDBI)
                            sss = TestSuite([tests])
                            counter_execution += 1
                            result=runner.run(sss, count ,testRep[currTest], False)
                            TestPassed += result.success_count
                            TestFailed += result.failure_count
                            TestError += result.error_count
                            TestR += result.result
                            count += 1 
                        currTest += 1
                currService +=1
       # url = r"C:\Users\Mahdi\Desktop\GIT_HUB_Directory_PFE2021\ACTIMUX_Tests_Script\templates\TEESSSSSEEEETOO_report.html"
       # webbrowser.open(url)



