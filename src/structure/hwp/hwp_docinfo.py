from structure.hwp.hwp_record import HWPRecord
from structure.hwp.hwptag_binData import HWPTAG_binData
from io import BytesIO
class HWPDocInfo:
    HWPTAG_BEGIN = 0x10
    HWPTAG_ID_BINDATA = HWPTAG_BEGIN + 2

    def __init__(self, ole_container) -> None:
        self.ole_container = ole_container
        self.hwptag_bindatas = []
        self.docinfo_stream = None
        self.docinfo_stream = None
        self.records = {}
        pass

    def get_docinfo_stream(self):
        '''
        get docinfo storage class
        '''
        docinfo_storage = self.ole_container.get_dir_entry_by_name('DocInfo')
        '''
        get docinfo stream from storage
        '''
        self.docinfo_stream = docinfo_storage.get_decompressed_stream()

    def parse(self):
        self.get_docinfo_stream()
        stream = BytesIO(self.docinfo_stream)
        while True:
            new_hwp_record = HWPRecord()
            res = new_hwp_record.parse(stream)
            if new_hwp_record.header.tag_id not in self.records:
                self.records[new_hwp_record.header.tag_id] = [new_hwp_record]
            else:
                self.records[new_hwp_record.header.tag_id].append(new_hwp_record)
            if not res:
                break
        self.parse_hwptag_bindata()

    def parse_hwptag_bindata(self):
        hwptag_bindatas = self.records[HWPDocInfo.HWPTAG_ID_BINDATA]
        for hwptag_bindata in hwptag_bindatas:
            hwptag_bindata_binary = HWPTAG_binData(hwptag_bindata.payload)
            self.hwptag_bindatas.append(hwptag_bindata_binary)

