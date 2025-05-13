

## <h2 style="color: #5697bf;"><u>Signal</u></h2>


**Inherits from: _object_**

Signal object.


### <h2 style="color: #5e5d84;">Signature</h2>

```python
__init__(self):
```

Class constructor.

  Signals an event:

   MyObj:
    obj_signal = Signal()

    


### <h2 style="color: #5e5d84;">Properties</h2>


#### _callback

```python
_callback(self) -> callable:
```


### <h2 style="color: #5e5d84;">Methods<h2>


#### value

```python
value(self, value: any) -> None:
```

Signal value.

   my_signal = self.obj_signal
   signal_value = my_signal.value
   self.my_signal.connect(lambda: print(signal_value))
  

#### disconnect

```python
disconnect(self, callback: callable = None) -> None:
```

Function to be disconnected.

   my_obj.obj_signal.disconnect(self.my_function)

  
**:param callback:** Function to be disconnect.
  

#### emit

```python
emit(self) -> None:
```

Send this signal.

  This method should be executed when you need to send the signal.
  
