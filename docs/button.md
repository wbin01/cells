#  

## <h2 style="color: #4d7c99;">class Button</h2>


**Inherits from: _Widget_**

Button Widget.


### Signature

```python
__init__(
            self,
            text: str = None,
            icon: str = None,
            orientation: Orientation = Orientation.HORIZONTAL,
            *args, **kwargs) -> None:
```

Class constructor.

  The icon is rendered from the path of a passed file, or from the name 
  of an icon in the current operating system, such as 


### Properties


#### selectable

```python selectable(self) -> bool:```

If it is selectable.

  Whether the widget is selectable as a toggle button.
  

#### selected

```python selected(self) -> bool:```

If Widget is selected.

  Only works if the 'selectable' property is True.
  Use True or False to select or deselect the widget.
  

#### text

```python text(self) -> str:```

Button text.
  
  Pass a new string to update the text.
  
