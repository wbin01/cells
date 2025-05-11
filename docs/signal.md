#  

## <h2 style="color: #4d7c99;">class Signal</h2>


**Inherits from: _object_**

Signal object.


### Signature

```python
__init__(self):
```

Class constructor.

  Signals an event:

   MyObj:
    obj_signal = Signal()

    


### Properties


#### _callback

```python _callback(self) -> callable:```


### Methods


#### value

```python value(self, value: any) -> None:```

Signal value.

   my_signal = self.obj_signal
   signal_value = my_signal.value
   self.my_signal.connect(lambda: print(signal_value))
  

#### disconnect

```python disconnect(self, callback: callable = None) -> None:```

Function to be disconnected.

   my_obj.obj_signal.disconnect(self.my_function)

  :param callback: Function to be disconnect.
  

#### emit

```python emit(self) -> None:```

Send this signal.

  This method should be executed when you need to send the signal.
  
