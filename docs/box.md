

## <h2 style="color: #5697bf;"><u>Box</u></h2>

<span style="color: #888;">Class</span>

**Inherits from: _object_**

Box layout

```python
__init__(
            self,
            orientation: Orientation = Orientation.VERTICAL,
            *args, **kwargs) -> None:
```

Class constructor.

By default the Box orientation is vertical. Use the horizontal 
parameter to change it.



**:param orientation:** Changes the orientation of the Box to horizontal


### <h2 style="color: #5e5d84;">Properties</h2>

#### align

**_  Align_**

Align enum.

Sets the Box alignment.



#### margin

**_  tuple_**

Box Margins


#### spacing

**_  int_**


The space between widgets inside the box.

This property takes precedence over the margins of the widgets that 
are added (add_widgets), so if the Box is vertical, then only the side 
margins of the widgets will be respected. The Box does not activate 
the spacing with a single isolated widget.



#### _main_parent

**_  Widget | Box_**

Main frame of the application.

Use only to access properties and methods of the Main Frame, defining a 
new frame will break the application.



#### _obj

**_  QtWidgets_**

Direct access to Qt classes.

Warning: Direct access is discouraged and may break the project. 
This access is considered a hacking for complex Qt implementations, 
and should only be used for testing and analysis purposes.



### <h2 style="color: #5e5d84;">Methods<h2>


#### add

```python
add(self, item: Widget | Box, index: int = -1) -> Widget | Box:
```

Inserts a Widget or a Box.

  Returns the reference to the added item.
  
  
**:param item:** It can be a Widget (Widget, Label, Button...) or a Box.
  
**:param index:** Index number where the item should be added 
   (Default is -1)
  

#### items

```python
items(self) -> list:
```

List with added widgets.

#### remove

```python
remove(self, item: Widget | Box) -> None:
```

Removes a Widget or a Box.

  This only removes the widget, but does not delete it. The variable 
  referring to it still works and can be added again later. To 
  completely delete the widget from the variable, use the 'delete()' 
  method.

  
**:param item:** A Widget (Widget, Label, Button...) or a Box.
  

#### signal

```python
signal(self, event: Event) -> Signal:
```

Event Signals.

  Signals are connections to events. When an event such as a mouse 
  click (Event.MOUSE_BUTTON_PRESS) or other event occurs, a signal is 
  sent. The signal can be assigned a function to be executed when the 
  signal is sent.

  Use the 'events_available_for_signal()' method to see all available 
  events.

  
**:param event:**
   Event enumeration (Enum) corresponding to the requested event, 
   such as Event.HOVER_ENTER. See: events_available_for_signal().
  


---