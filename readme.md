WiqiCharts
==========

Presenting complex time-series data in a way that is self-explanatory is important. Doing so in static charts is essential for ease of use. Interactive or moving charts look nice but are slow to read and interpret. Overwrought charts are just confusing.

The purpose of this small range of charts is to present complex data in a simple way.

You will require Matplotlib to use the code. In addition, the code is also meant to be part of an http response in Django which may explain the slightly different approach taken in the Matplotlib show function.

Comets
------

Those familiar with [Gapminder][1] will know of the power of moving bubble-charts. You may also have experienced the tedium of waiting for the bubbles to finish moving so you can see the result. The comet chart is a simple way of presenting the data in a static format.

The chart below has GDP per capita and Inflation on the X and Y axes, and Unemployment as a % on the Z for the years 2013 to 2018 (taken from the IMF World Economic Outlook October 2013 update).

![][2]

Shadows
-------

Spaghetti charts are the sort of horrifying disaster that result when attempting to show far too many time-series data on a single chart.

An alternative is to create a range from comparative data and highlight the series you wish to show. Most often, a chart is used to demonstrate a comparison between different series. Given a known range it is simple to show how a highlighted / selected series looks relative to others.

Licenses
--------

The code is licensed under [GPL][3] and the chart designs themselves are [CC BY-SA 3.0][4].

Attribution: Gavin Chait, http://www.whythawk.com/

  [1]: http://www.gapminder.org/
  [2]: http://farm4.staticflickr.com/3691/10889219054_de8607c86a.jpg
  [3]: http://www.gnu.org/copyleft/gpl.html
  [4]: http://creativecommons.org/licenses/by-sa/3.0/deed.en_GB
