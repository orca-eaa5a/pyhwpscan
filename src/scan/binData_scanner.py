from utils.dumphex import dump_as_physical_file, print_hexdump
class SuspiciousTAG:
    OLE_DATA = 1
    NOT_MATCH_WITH_TAG = 2

def scan_hwptag_bindata(bindata_stream_names, hwptag_bindata_records, TAG_ID=18):
    ole_records = []
    find_flag = False
    bindata_records = hwptag_bindata_records
    '''
    First, check number of binData stream is same with hwptag_binData
    '''
    if len(bindata_stream_names) != len(hwptag_bindata_records):
        for bindata_stream_name in bindata_stream_names:
            s = bindata_stream_name[len("BIN"):]
            ext_offset = s.rfind(".")
            ext = s[ext_offset:]
            find_flag = False
            for bindata_record in bindata_records:
                if str(bindata_record.bin_id) in bindata_stream_name[len("BIN"):] and\
                    bindata_record.extension in bindata_stream_name[len("BIN"):]:
                    find_flag = True
                    break
            if not find_flag:
                s = (SuspiciousTAG.NOT_MATCH_WITH_TAG, -1, bindata_stream_name)
                ole_records.append(s)
    
    for bindata_record in bindata_records:
        if bindata_record.extension not in ["jpg", "bmp", "gif", "png"]:
            '''
            TODO: check the extension of png file is ole? << yes
            '''
            for bindata_stream_name in bindata_stream_names:
                if str(bindata_record.bin_id) in bindata_stream_name[len("BIN"):]:
                    s = (SuspiciousTAG.OLE_DATA, bindata_record.bin_id, bindata_stream_name)
                    if s not in ole_records:
                        ole_records.append(s)
                    break
    return ole_records


def scan_BinData(hwp_parser, isCompressed=True):
    '''
    First, scan binData recoreds
    '''
    bindata_stream_name = [stream.name() for stream in hwp_parser.hwp_bindata.bindata]
    suspicious_records = scan_hwptag_bindata(bindata_stream_name, hwp_parser.hwp_docinfo.hwptag_bindatas)
    if not suspicious_records:
        return True
    print("[info] <BinData> : Suspicious BinData Detected!")
    for record in suspicious_records:
        for stream in hwp_parser.hwp_bindata.bindata:
            if record[2] == stream.name():
                if record[0] == SuspiciousTAG.OLE_DATA:
                    print("*** Suspicious OLE Detected!")
                elif record[0] == SuspiciousTAG.NOT_MATCH_WITH_TAG:
                    print("*** Mismatch with HWPTAG_BINDATA Detected!")
                dump_as_physical_file(stream.get_decompressed_stream(), stream.name())
                #print_hexdump(stream.get_stream())
                break