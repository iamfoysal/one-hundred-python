
<h1 align="center"">
Analog Clock 
<hr>
</h1>

This is a simple analog clock application written in Python with `PyQt5`. It displays the current time and highlights `the 12, 6, and 9 o'clock` positions. The clock is updated every second.

The clock is drawn using QPainter. The clock outline is drawn using drawEllipse(). 
The numbers are drawn using drawText(). The minute markers are drawn using `drawText()` as well. The hour, minute, and second hands are drawn using drawLine().

The clock is updated every second using a QTimer. The `QTimer` is started in the constructor of the AnalogClock class. 
The QTimer is connected to the `update()` method of the AnalogClock class. 
The `update()` method is called every second and the clock is redrawn.

## Python Library: 

    pip install PyQt5


 ## [Click here for Source Code](/analog_clock.py)

#####  Output:

<p align="center">

  <img src="/collections/analog_clock.png" />

</p>
<hr>