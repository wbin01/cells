

## <h2 style="color: #5697bf;"><u>Button</u></h2>

<span style="color: #888;">Class</span>

**Inherits from: _Widget_**

Button Widget.

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

### <h2 style="color: #5e5d84;">Properties</h2>

#### selectable

**_bool_**

If it is selectable.

Whether the widget is selectable as a toggle button.


#### selected

**_bool_**

If Widget is selected.

Only works if the 'selectable' property is True.
Use True or False to select or deselect the widget.


#### text

**_str_**

Button text.

Pass a new string to update the text.


---