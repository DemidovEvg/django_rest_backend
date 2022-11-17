
from rest_framework.pagination import PageNumberPagination


class FactoryPagination:
    @staticmethod
    def get_pagination(**kwargs):
        kwargs_for_meta: dict = kwargs

        class Meta(type):
            def __new__(cls, name, bases, dct):
                for arg_name, arg_val in kwargs_for_meta.items():
                    dct[arg_name] = arg_val
                return super().__new__(cls, name, bases, dct)

        class InstancePagination(PageNumberPagination, metaclass=Meta):
            pass
        return InstancePagination
