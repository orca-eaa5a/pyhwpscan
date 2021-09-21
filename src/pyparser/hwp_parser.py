from pyparser.oleparser import OleParser
from structure.hwp.hwp_header import HWPHeader
from structure.hwp.hwp_bindata import HWPBinData
from structure.hwp.hwp_docinfo import HWPDocInfo
from structure.hwp.hwp_script import HWPJScript

class HwpParser:
    def __init__(self, ole_container:OleParser) -> None:
        self.ole_container = ole_container
        self.hwp_header = HWPHeader()
        self.hwp_bindata = None
        self.hwp_docinfo = None
        self.hwp_jscript = None
        pass
    
    def get_bindata(self):
        return self.hwp_bindata

    def parse_file_header(self):
        file_header_entry = self.ole_container.get_dir_entry_by_name('FileHeader')
        buf = file_header_entry.get_stream()
        self.hwp_header.cast(buf)
    
    def parse_bin_data(self, ole_container):
        self.hwp_bindata = HWPBinData(ole_container)

    def parse_jscript(self, ole_container):
        self.hwp_jscript = HWPJScript(ole_container)
        self.hwp_jscript.parse()

    def parse_docinfo(self):
        self.hwp_docinfo = HWPDocInfo(self.ole_container)
        self.hwp_docinfo.parse()

    def parse(self):
        self.parse_file_header()
        self.parse_jscript(self.ole_container)
        '''
        self.parse_docinfo()
        self.parse_bin_data(self.ole_container)
        '''
        