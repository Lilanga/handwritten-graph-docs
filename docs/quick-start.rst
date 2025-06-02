Quick Start Guide
=================

Get up and running with the Handwritten Graph Library in just a few minutes!

Prerequisites
-------------

Make sure you have the library installed. If not, check the :doc:`installation` guide first.

Your First Chart
-----------------

Let's create a simple line chart to get started:

Installation
~~~~~~~~~~~~

.. code-block:: bash

   npm install handwritten-graph

Basic Usage
~~~~~~~~~~~

.. code-block:: typescript

   import { LineChart } from 'handwritten-graph';

   // Sample data
   const chartData = {
     labels: ["Q1", "Q2", "Q3", "Q4"],
     datasets: [{
       label: "Revenue",
       data: [65, 59, 80, 81],
       lineColor: "rgb(75, 192, 192)"
     }]
   };

   // Create line chart
   const lineChart = new LineChart("#chart-container", chartData, {
     showArea: true,
     useScribbleFill: true
   });

HTML Setup
~~~~~~~~~~~

.. code-block:: html

   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>My First Handwritten Chart</title>
   </head>
   <body>
       <h1>Sales Data</h1>
       <div id="chart-container"></div>
       
       <!-- Include D3.js -->
       <script src="https://d3js.org/d3.v7.min.js"></script>
       <!-- Include Handwritten Graph Library -->
       <script src="https://unpkg.com/handwritten-graph@latest/dist/handwritten-graph.js"></script>
       
       <script>
           // Your chart code goes here
           const chartData = {
             labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
             datasets: [{
               label: 'Monthly Sales',
               data: [65, 59, 80, 81, 56, 72],
               lineColor: '#ff6b6b'
             }]
           };

           const chart = new HandwrittenGraph.LineChart('#chart-container', chartData, {
             width: 800,
             height: 400,
             handDrawnEffect: true
           });
       </script>
   </body>
   </html>

Chart Types
-----------

Line Chart
~~~~~~~~~~

.. code-block:: javascript

   const lineChart = new HandwrittenGraph.LineChart('#line-chart', {
     labels: ['Q1', 'Q2', 'Q3', 'Q4'],
     datasets: [{
       label: 'Revenue',
       data: [100, 150, 200, 180],
       lineColor: '#4ecdc4'
     }]
   });

Bar Chart
~~~~~~~~~

.. code-block:: javascript

   const barChart = new HandwrittenGraph.BarChart('#bar-chart', {
     labels: ['Product A', 'Product B', 'Product C'],
     datasets: [{
       label: 'Sales',
       data: [45, 67, 23],
       barColor: '#45b7d1'
     }]
   });

Pie Chart
~~~~~~~~~

.. code-block:: javascript

   const pieData = [
     { label: 'Desktop', value: 45, color: '#ff6b6b' },
     { label: 'Mobile', value: 35, color: '#4ecdc4' },
     { label: 'Tablet', value: 20, color: '#45b7d1' }
   ];

   const pieChart = new HandwrittenGraph.PieChart('#pie-chart', pieData);

Configuration Options
---------------------

Basic Configuration
~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   const config = {
     width: 800,                    // Chart width in pixels
     height: 400,                   // Chart height in pixels
     handDrawnEffect: true,         // Enable hand-drawn styling
     lineColor: '#ff6b6b',         // Default line color
     fontFamily: 'Comic Sans MS'    // Font for text elements
   };

Hand-Drawn Effects
~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   const handDrawnConfig = {
     handDrawnEffect: true,         // Enable hand-drawn look
     handDrawnJitter: 3,           // Amount of "wobble" (default: 2)
     useScribbleFill: true,        // Artistic fill patterns
     fillStyle: 'directional'      // or 'oilpaint'
   };

Next Steps
----------

Now that you've created your first charts, explore these topics:

- :doc:`api/line-chart-api` - Complete Line Chart API reference
- :doc:`api/bar-chart-api` - Complete Bar Chart API reference  
- :doc:`api/pie-chart-api` - Complete Pie Chart API reference
- :doc:`advanced/styling` - Advanced styling techniques
- :doc:`api/configuration` - All configuration options