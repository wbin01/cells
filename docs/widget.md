# CoreWidget
Inherits from: QtWidgets.QFrame
Core Widget.
## Constructor signature
```python
__init__(self, *args, **kwargs):
```
Class constructor.
# Widget
Inherits from: Widget
Widget.

 Tip: The base widget is an empty object, with no margins or spacing, and 
 is visually imperceptible, as it does not take up a single pixel. Adding 
 height, width or background color will help to make it noticeable.
 
## Constructor signature
```python
__init__(
            self,
            main_parent = None,
            orientation: Orientation = Orientation.VERTICAL,
            *args, **kwargs) -> None:
```
Class constructor.

  :main_parent: MainFrame object
  
