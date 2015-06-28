



def update_parameters(self, parameters):
    def_parameters = {'domain': self.config.domain, 'path': self.config.path}
    def_parameters.update(parameters)
    return def_parameters

def create_url(self, **parameters):
    parameters = self.update_parameters(parameters)
    url = '%s/%s' % (parameters['domain'], parameters['path'])
    return url

def test_setup_url(self):
    self.create_url(domain='https://egnyte.com')







def foo(**args):
    print(args)
foo(a=1, b=2)
{'a': 1, 'b': 2}
