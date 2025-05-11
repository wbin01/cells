#  

## <h2 style="color: #4d7c99;">class CoreWidget</h2>


**Inherits from: _QtWidgets.QFrame_**

Core Widget.


### Signature

```python
__init__(self, *args, **kwargs):
```

Class constructor.


## <h2 style="color: #4d7c99;">class Widget</h2>


**Inherits from: _Widget_**

Widget.

 Tip: The base widget is an empty object, with no margins or spacing, and 
 is visually imperceptible, as it does not take up a single pixel. Adding 
 height, width or background color will help to make it noticeable.
 


### Signature

```python
__init__(
            self,
            main_parent = None,
            orientation: Orientation = Orientation.VERTICAL,
            *args, **kwargs) -> None:
```

Class constructor.

  :main_parent: MainFrame object
  
