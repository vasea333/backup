import httplib
from pubapiutils import TestCaseClass


class TestClass(TestCaseClass):
    def test_merge_two_items_same_name(self):
        item = self.utils.random_name()
        source_folder = self.utils.random_name()
        target_folder = self.utils.random_name()
        source_folder_path = self.utils.form_standard_path(source_folder)
        target_folder_path = self.utils.form_standard_path(target_folder)
        self.calls.create_folder(source_folder)
        self.calls.create_folder(target_folder)
        self.calls.create_folder(item, source_folder_path)
        self.calls.create_folder(item, target_folder_path)
        resp = self.calls.move_item(name=item, destination=target_folder_path, parent_path=source_folder_path)
        assert resp.status_code == httplib.OK
        self.calls.delete_folder(name='', parent_path=self.config.testpath)
