from pyparser.oleparser import OleParser
from pyparser.hwp_parser import HwpParser
from scan.init_scan import init_scan
from scan.binData_scanner import scan_BinData
from scan.jscript_scanner import scan_JScript

if __name__ == '__main__':
    ole_parser = OleParser()
    ole_parser.read_ole_binary('./sample/sample.hwp')
    ole_parser.parse()

    #script_entry = ole_parser.get_dir_entry_by_name('JScriptVersion')

    hwp_parser = HwpParser(ole_parser)
    hwp_parser.parse()
    
    # print(hwp_parser.hwp_header.get_signature())

    if not init_scan(hwp_parser.hwp_header):
        exit(-1)
    
    #scan_BinData(hwp_parser)
    scan_JScript(hwp_parser)
    
    
    '''
    hwp_binData = hwp_parser.get_bindata()
    scan_bin_data(hwp_binData, True)
    '''