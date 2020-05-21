from leatherman.dictionary import head_body
from leatherman.repr import __repr__
from leatherman.yaml import yaml_format

from refractr.url import URL
from refractr.utils import *

class BaseRefract:
    def __init__(self, dst=None, srcs=None, status=None, tests=None):
        self.dst = dst
        self.srcs = srcs
        self.status = status
        self.tests = tests

    def __str__(self):
        return yaml_format(self.json())

    __repr__ = __repr__

    @property
    def balance(self):
        '''
        generated tests will always match location redirects
        rewrites do no generate tests; so this is to help identify that
        '''
        dst_count = len(self.dst) if isinstance(self.dst, list) else 1
        test_count = len(self.tests)
        return test_count - dst_count

    def json(self):
        return dict(
            dst=self.dst,
            srcs=self.srcs,
            status=self.status,
            tests=self.tests
        )

    @property
    def server_name(self):
        return join([URL(src).netloc for src in self.srcs])

    def render(self):
        raise NotImplementedError
