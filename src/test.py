
from pyparser.oleparser import OleParser
from pyparser.hwp_parser import HwpParser

if __name__ == '__main__':
    ole_parser = OleParser()
    ole_parser.read_ole_binary('./sample/sample_cpy.hwp')
    ole_parser.parse()
    ole_parser.print_dir_entry_all()