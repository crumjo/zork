from abc import ABCMeta, abstractmethod


class Observer(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args, **kwargs):
        print("Monster Updated.")
