class HWPBinData:
    def __init__(self, ole_container) -> None:
        self.ole_container = ole_container
        self.bindata_storage = self.ole_container.get_dir_entry_by_name('BinData')
        self.bindata = []
        self.get_child(self.bindata_storage.ChildID)
        pass

    def get_child(self, child_id):
        child = self.ole_container.get_dir_entry(child_id)
        self.bindata.append(child)
        if child.LeftSiblingID != 0xFFFFFFFF:
            self.get_child(child.LeftSiblingID)
        if child.RightSiblingID != 0xFFFFFFFF:
            self.get_child(child.RightSiblingID)
        return