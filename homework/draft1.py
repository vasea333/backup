def parameter(self, users=None, folder_name=None, folder_path=None, destination=None, path=None, domain=None,
                      method=None, content_type=None, accept=None, username=None, password=None,):
        par = []
        if domain is None:
            par.append(self.config.domain)
        else:
            par.append(domain)
        if destination is None:
            par.append(self.config.destination)
        else:
            par.append(destination)
        if method is None:
            par.append(self.config.metod)
        else:
            par.append(method)
        if content_type is None:
            par.append(self.config.content_type)
        else:
            par.append(content_type)
        if accept is None:
            par.append(self.config.accept)
        else:
            par.append(accept)
        if username is None:
            par.append(self.config.admin_login)
        else:
            par.append(username)
        if password is None:
            par.append(self.config.password)
        else:
            par.append(password)
        if path is None:
            par.append(self.config.testpath)
        else:
            par.append(path)
        if folder_name is None:
            par.append(1234)
        else:
            par.append(folder_name)
        return par
print(parameter(users='Alex', accept="da"))