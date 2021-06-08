import string
from collections import Counter


class OurClass:

    def __init__(self, validate):
        self.validate = validate

    @property
    def validate(self):
        return self.validate

    @validate.setter
    def validate(self, validate):

        if '@' not in validate:
            raise SyntaxError('Incorrect e-mail')

        prefix, domain = validate.split('@')

        '''For prefix'''
        if prefix[0] in string.punctuation or prefix[-1] in string.punctuation \
                or ' ' in prefix:
            raise SyntaxError('Incorrect prefix')

        punct_prefix = [v for k, v in Counter(zip(prefix, prefix[1:])).items() if
                        k[0] in string.punctuation and k[1] in string.punctuation]
        for i in punct_prefix:
            if i > 0:
                raise SyntaxError('Incorrect prefix')

        '''For domain'''
        if domain[0] in string.punctuation or domain[-1] in string.punctuation \
                or ' ' in domain:
            raise SyntaxError('Incorrect prefix')

        punct_domain = [v for k, v in Counter(zip(prefix, prefix[1:])).items() if
                        k[0] in string.punctuation and k[1] in string.punctuation]
        for i in punct_domain:
            if i > 0:
                raise SyntaxError('Incorrect domain')

        if '.' not in domain:
            raise SyntaxError('Incorrect domain')

        domain_mail, domain_dom = domain.split('.')
        if string.punctuation in domain_mail or ' ' in domain_mail:
            raise SyntaxError('Incorrect domain')

        if string.punctuation in domain_dom or ' ' in domain_dom or len(domain_dom) < 2:
            raise SyntaxError('Incorrect domain')


a = OurClass('mashkinaa99@gmail.com')
