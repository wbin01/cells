

## <h2 style="color: #4d7c99;">Widget</h2>


**Inherits from: _object_**

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
  


### Properties


#### accent

```python
accent(self) -> str:
```

...

#### align

```python
align(self) -> Align:
```

Align enum.

  Sets the Box alignment.
  

#### enabled

```python
enabled(self) -> bool:
```

Enables the Widget.

  When False, the Widget is inactive both in appearance and in the 
  Event.MOUSE_PRESS and Event.MOUSE_RELEASE events.
  

#### height

```python
height(self) -> int:
```

Returns the height of the Widget.

  Pass a new integer value to update the height.
  

#### margin

```python
margin(self) -> tuple:
```

Utility to set widget margins using a simple int tuple.

  Will affect all widget states, such as pressed, hover and inactive.

  Note: The Box's 'spacing' property takes precedence over the widget's 
  margins, unless the widget is the only one isolated within a Box. If 
  the Box is vertical, then only the side margins of the widgets will be 
  respected. The Box does not activate the spacing with a single 
  isolated widget.
  

#### max_height

```python
max_height(self) -> int:
```

Returns the Widget maximum height.

  Pass a new integer value to update the maximum height the Widget can 
  have.
  

#### max_width

```python
max_width(self) -> int:
```

Returns the Widget maximum width.

  Pass a new integer value to update the maximum width the Widget can 
  have.
  

#### min_height

```python
min_height(self) -> int:
```

Returns the Widget minimum height.

  Pass a new integer value to update the minimum height the Widget can 
  have.
  

#### min_width

```python
min_width(self) -> int:
```

Returns the Widget minimum width.

  Pass a new integer value to update the minimum width the Widget can 
  have.
  

#### spacing

```python
spacing(self) -> int:
```


  The space between widgets inside the Widget box.

  This property takes precedence over the margins of the widgets that 
  are added (add_widgets), so if the Box is vertical, then only the side 
  margins of the widgets will be respected. The Box does not activate 
  the spacing with a single isolated widget.
  

#### state

```python
state(self) -> str:
```

...

#### style

```python
style(self) -> str:
```

Style as dict.

  The style is a 'dict' that goes back to the style INI file. The 
  contents of this file are something like:

   [Widget]
   background=rgba(200, 0, 0, 1.00)
   margin=5px 5px 5px 5px

  So the dictionary will be:

   {'[Widget]': {
    'background': 'rgba(200, 0, 0, 1.00)',
    'margin': '5px 5px 5px 5px',}
   }

  Simply changing the existing dictionary does not update the style, 
  the property actually needs to be updated with a new dictionary:

   new_style = my_widget.style
   new_style['[Widget]']['margin'] = '05px 05px 05px 05px'
   my_widget.style = new_style

  Shortened:

   my_widget.style['[Widget]']['margin'] = '05px 05px 05px 05px'
   my_widget.style = my_widget.style

  Note: The Box's 'spacing' property takes precedence over the widget's 
  margins, unless the widget is the only one isolated within a Box.
  

#### style_class

```python
style_class(self) -> str | None:
```

Changes the style to that of the desired class.
  
  Use appropriate generic classes, such as 'Success', 'Danger', 
  'Warning' and 'Accent'.
  
   my_button.style_class = 'Danger'
  
  Use None to reset.

  The style class will only be changed if the Widget already contains a 
  _main_parent (The 'add' method automatically sets the _main_parent).
  

#### style_id

```python
style_id(self) -> str:
```

Style ID.

  An ID allows you to define a unique style that does not distort 
  parent objects of the same type that inherit from the class.

  Send a string with a unique ID to set the style for this Widget only.
  

#### visible

```python
visible(self) -> bool:
```

Widget Visibility.

  Qt has minor issues when calculating pixels to render areas that are 
  repeatedly hidden and visible, so clearly define the sizes and spacing 
  to avoid minor visual discomforts.
  

#### width

```python
width(self) -> int:
```

Returns the Widget width.

  Pass a new integer value to update the width.
  

#### _main_parent

```python
_main_parent(self):
```

Main frame of the application.

  Use only to access properties and methods of the Main Frame, defining 
  a new frame will break the application.
  

#### _obj

```python
_obj(self):
```

Direct access to Qt classes.

  Warning: Direct access is discouraged and may break the project. 
  This access is considered a hacking for complex Qt implementations, 
  and should only be used for testing and analysis purposes.
  


### Methods


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
  
  :param item: It can be a Widget (Widget, Label, Button...) or a Box.
  :param index: Index number where the item should be added 
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

  :param item: A Widget (Widget, Label, Button...) or a Box.
  

#### move

```python
move(self, x: int, y: int) -> None:
```

Move the Widget.

  The X and Y positions are relative to the main parent.
  
  :param x: Horizontal position relative to the main parent.
  :param y: Vertical position relative to the main parent.
  

#### signal

```python
signal(self, event: Event) -> Signal:
```

Event Signals.

  Signals are connections to events. When an event such as a mouse 
  click (Event.MOUSE_PRESS) or other event occurs, a signal is sent. The 
  signal can be assigned a function to be executed when the signal is 
  sent.

  Use the 'events_available_for_signal()' method to see all available 
  events.

  :param event:
   Event enumeration (Enum) corresponding to the requested event, 
   such as Event.HOVER_ENTER. See: events_available_for_signal().
  
