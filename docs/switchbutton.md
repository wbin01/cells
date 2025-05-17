

## <h2 style="color: #5697bf;"><u>SwitchButton</u></h2>

<span style="color: #888;">Class</span>

**Inherits from: _Widget_**

Switch Button Widget.

```python
__init__(
            self,
            text: str = None,
            value: any = None,
            selected: bool = False,
            orientation: Orientation = Orientation.HORIZONTAL,
            *args, **kwargs) -> None:
```

Class constructor.



**:param text:** SwitchButton text label.


**:param selected:** True to start already selected.


**:param value:** Value of any type to capture as an identifier.


### <h2 style="color: #5e5d84;">Properties</h2>

#### text

**_  str_**

Button text.

Pass a new string to update the text.



#### selected

**_  bool_**

If Widget is selected.

Use True or False to select or deselect the widget.



#### value

**_  any_**

Button value.

Pass a new value to update.



---