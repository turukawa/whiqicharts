WiqiCharts
==========

Presenting complex time-series data in a way that is self-explanatory is important. Doing so in static charts is essential for ease of use. Interactive or moving charts look nice but are slow to read and interpret. Overwrought charts are just confusing.

The purpose of this small range of charts is to present complex data in a simple way.

You will require Matplotlib to use the code. In addition, the code is also meant to be part of an http response in Django which may explain the slightly different approach taken in the Matplotlib show function.

Comets
------

Those familiar with [Gapminder][1] will know of the power of moving bubble-charts. You may also have experienced the tedium of waiting for the bubbles to finish moving so you can see the result. The comet chart is a simple way of presenting the data in a static format.

Shadows
-------

Spaghetti charts are the sort of horrifying disaster that result when attempting to show far too many time-series data on a single chart.

An alternative is to create a range from comparative data and highlight the series you wish to show. Most often, a chart is used to demonstrate a comparison between different series. Given a known range it is simple to show how a highlighted / selected series looks relative to others.

  [1]: http://www.gapminder.org/