

## <h2 style="color: #5697bf;"><u>Frame</u></h2>

<span style="color: #888;">Class</span>

**Inherits from: _object_**

Main frame.
 
 That is, the main application window.
 

```python
__init__(
        self,
        main_parent = None,
        orientation: Orientation = Orientation.VERTICAL,
        *args, **kwargs) -> None:
```

Class constructor.

### <h2 style="color: #5e5d84;">Properties</h2>

#### align

**_  Align_**

Align enum.

Sets the alignment of the Box.



#### flag

**_  list_**

Frame flags.

They are used to configure the native behavior of the Frame.
For example, the POPUP flag configures that the frame can appear on 
the indicated position on the X and Y axes, and also that the Frame 
closes by itself.



#### height

**_  int_**

Returns the height of the Frame.

Pass a new integer value to update the height.



#### icon

**_  Icon_**

Frame icon.

Application Icon.



#### max_height

**_  int_**

Returns the Frame maximum height.

Pass a new integer value to update the maximum height the Frame can 
have.



#### max_width

**_  int_**

Returns the Frame maximum width.

Pass a new integer value to update the maximum width the Frame can 
have.



#### min_height

**_  int_**

Returns the Frame minimum height.

Pass a new integer value to update the minimum height the Frame can 
have.



#### min_width

**_  int_**

Returns the Frame minimum width.

Pass a new integer value to update the minimum width the Frame can 
have.



#### spacing

**_  int_**


The space between widgets inside the Frame box.

This property takes precedence over the margins of the widgets that 
are added (add_widgets), so if the Box is vertical, then only the side 
margins of the widgets will be respected. The Box does not activate 
the spacing with a single isolated widget.



#### style

**_  dict_**

Style as dict.

Get the style as a dictionary or submit a new dictionary style to 
update it.



#### width

**_  int_**

Returns the Frame width.

Pass a new integer value to update the width.



#### _main_parent

**__**

Main frame of the application.

Use only to access properties and methods of the Main Frame, defining a 
new frame will break the application.



#### _obj

**__**

Direct access to Qt classes.

Warning: Direct access is discouraged and may break the project. 
This access is considered a hacking for complex Qt implementations, 
and should only be used for testing and analysis purposes.



### <h2 style="color: #5e5d84;">Methods<h2>


#### events_available_for_signal

```python
events_available_for_signal(self) -> str:
```

String with all available events.

#### add

```python
add(self, item: Widget | Box, index: int = -1) -> Widget | Box:
```

Inserts a Widget or a Box.

  Returns the reference to the added item.
  
  
**:param item:** It can be a Widget (Widget, Label, Button...) or a Box.
  
**:param index:** Index number where the item should be added 
   (Default is -1)
  

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
  

#### move

```python
move(self, x: int, y: int) -> None:
```

Move the Frame.

  The X and Y positions are relative to the main parent.
  
  
**:param x:** Horizontal position relative to the main parent.
  
**:param y:** Vertical position relative to the main parent.
  

#### show

```python
show(self) -> None:
```

Renders and displays the Frame.

#### signal

```python
signal(self, event: Event) -> Signal:
```

Event Signals.

  Signals are connections to events. When an event such as a mouse 
  click (Event.MOUSE_PRESS) or other event occurs, a signal is 
  sent. The signal can be assigned a function to be executed when the 
  signal is sent.

  Use the 'events_available_for_signal()' method to see all available 
  events.

  
**:param event:**
   Event enumeration (Enum) corresponding to the requested event, 
   such as Event.HOVER_ENTER. See: events_available_for_signal().
  

#### style_from_file

```python
style_from_file(self, path: str) -> dict:
```

Convert the contents of a file into a valid dictionary style.


---