def scan_JScript(hwp_parser):
    for jscript_stream in hwp_parser.hwp_jscript.script_streams:
        print(
            jscript_stream.get_script()
        )