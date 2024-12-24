#!/usr/bin/env python3
from .core.coresignal import CoreSignal


class Signal(object):
    """Signal object."""
    def __init__(self):
        """Class constructor.

        Signals an event:

            MyObj:
                obj_signal = Signal()

                def obj_call(self):
                    obj_signal.emit()


            my_obj = MyObj()
            my_obj.obj_signal.connect(lamba: print('Signal has been emitted'))

        When a signal is emitted, it performs the connected function.
        """
        self.__signal = CoreSignal()

    @property
    def value(self) -> any:
        """Signal value.

            my_signal = self.obj_signal
            signal_value = my_signal.value
            self.my_signal.connect(lambda: print(signal_value))
        """
        return self.__signal.value

    @value.setter
    def value(self, value: any) -> None:
        self.__signal.value = value

    def connect(self, callback: callable) -> None:
        """Function to be executed.

            my_obj.obj_signal.connect(self.my_function)

        :param callback: Function to be executed when the signal is sent.
        """
        self.__signal.callback(callback)

    def disconnect(self, callback: callable) -> None:
        """Function to be disconnected.

            my_obj.obj_signal.disconnect(self.my_function)

        :param callback: Function to be disconnect.
        """
        self.__signal.remove_callback(callback)

    def emit(self) -> None:
        """Send this signal.

        This method should be executed when you need to send the signal.
        """
        self.__signal.send()

    def __str__(self) -> str:
        return f'<Signal: {id(self)}>'
