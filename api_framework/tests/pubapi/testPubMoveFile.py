from pubapiutils import Calls
from pubapiutils import Config
from pubapiutils import Utils
import httplib
from unittest import TestCase


class TestClass(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.no_json = 'NoJSON'
        cls.calls = Calls()
        cls.config = Config()
        cls.utils = Utils()

    def setUp(self):
        self.utils.delete_all_except(['Documents'])

    def test_move_file_all_combinations(self):
            perms = {'None': 0, 'Viewer': 1, 'Editor': 2, 'Full': 3, 'Owner': 4}
            file1 = self.utils.gen_file()
            source_folder = self.utils.random_name()
            target_folder = self.utils.random_name()
            source_folder_path = self.utils.form_standard_path(source_folder)
            target_folder_path = self.utils.form_standard_path(target_folder)
            for perm1 in perms:
                for perm2 in perms:
                    self.calls.create_folder(source_folder)
                    self.calls.create_folder(target_folder)
                    self.calls.upload(file1, source_folder_path)
                    self.calls.set_perms(folder_path=source_folder_path, permission=perm1, users=self.config.puser)
                    self.calls.set_perms(folder_path=target_folder_path, permission=perm2, users=self.config.puser)
                    resp = self.calls.move_item(name=file1, destination=target_folder_path, parent_path=source_folder_path,
                                                username=self.config.puser)
                    if perms[perm1] > 2 and perms[perm2] > 1:
                        assert resp.status_code == httplib.OK
                        assert resp.json == self.no_json
                    else:
                        assert resp.status_code == httplib.FORBIDDEN
                        assert resp.json['errorMessage'] == 'You do not have permission to perform this action'
                    self.calls.delete_folder(name='', parent_path=self.config.testpath)