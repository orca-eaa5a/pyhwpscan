
def init_scan(hwp_header):
    '''
    check input file was .hwp file by checking signuatre
    '''
    HWP_SIGNATURE = 'HWP Document File'
    HWP_VERSION = 0
    signature = hwp_header.get_signature()
    if signature != HWP_SIGNATURE:
        print("[error] File is not a HWP document")
        print("*** Please check input file")
        return False

    '''
    check input file has password
    this tool not support unlock password
    '''
    hwp_properties = hwp_header.get_properties()
    if hwp_properties == 'encrypted':
        print("[error] File has password")
        print("*** This tool not support unlock password...")
        print("*** Please unlock password first!")
        return False
        
    return True
