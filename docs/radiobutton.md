

## <h2 style="color: #5697bf;"><u>RadioButton</u></h2>


**Inherits from: _Widget_**

Radio Button Widget.


### <h2 style="color: #5e5d84;">Signature</h2>

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
  
  
**:param text:** RadioButton text label.
  
**:param value:** Value of any type to capture as an identifier.
  
**:param selected:** True to start already selected.
  


### <h2 style="color: #5e5d84;">Properties</h2>


#### text

```python
text(self) -> str:
```

Button text.
  
  Pass a new string to update the text.
  

#### selected

```python
selected(self) -> bool:
```

If Widget is selected.

  Use True or False to select or deselect the widget.
  

#### value

```python
value(self) -> any:
```

Button value.
  
  Pass a new value to update.
  
