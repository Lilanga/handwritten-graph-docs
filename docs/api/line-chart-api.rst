Line Chart API Reference
=========================

The ``LineChart`` class creates interactive line charts with a hand-drawn aesthetic.

Constructor
-----------

.. code-block:: typescript

   new LineChart(selector: string, data: LineChartData, config?: Partial<LineChartConfig>)

Parameters
~~~~~~~~~~

selector
    **Type**: ``string``
    
    CSS selector for the container element where the chart will be rendered.

data
    **Type**: :ref:`LineChartData <line-chart-data>`
    
    The data to be visualized in the line chart.

config
    **Type**: ``Partial<LineChartConfig>`` *(optional)*
    
    Configuration options to customize the chart appearance and behavior.

Data Interface
--------------

.. _line-chart-data:

LineChartData
~~~~~~~~~~~~~

.. code-block:: typescript

   interface LineChartData {
     labels: string[];
     datasets: LineDataset[];
   }

**Properties**:

labels
    **Type**: ``string[]``
    
    Array of labels for the x-axis points.

datasets
    **Type**: :ref:`LineDataset[] <line-dataset>`
    
    Array of datasets to be plotted as lines.

.. _line-dataset:

LineDataset
~~~~~~~~~~~

.. code-block:: typescript

   interface LineDataset {
     label: string;
     data: number[];
     lineColor?: string;
     jitter?: number;
   }

**Properties**:

label
    **Type**: ``string``
    
    Display name for the dataset (shown in legend and tooltips).

data
    **Type**: ``number[]``
    
    Array of numeric values corresponding to each label.

lineColor
    **Type**: ``string`` *(optional)*
    
    Color for the line and points. Defaults to the global ``lineColor`` setting.

jitter
    **Type**: ``number`` *(optional)*
    
    Amount of random variation to apply to this dataset's line (for extra hand-drawn effect).

Configuration Interface
-----------------------

LineChartConfig
~~~~~~~~~~~~~~~

.. code-block:: typescript

   interface LineChartConfig extends BaseChartConfig {
     lineColor?: string;
     pointRadius?: number;
     gridColor?: string;
     handDrawnPoints?: number;
     legendBorder?: boolean;
     valueFormat?: (value: number) => string;
     showArea?: boolean;
   }

**Properties**:

lineColor
    **Type**: ``string``
    
    **Default**: ``'steelblue'``
    
    Default color for lines and points.

pointRadius
    **Type**: ``number``
    
    **Default**: ``4``
    
    Radius of data points in pixels.

gridColor
    **Type**: ``string``
    
    **Default**: ``'#e0e0e0'``
    
    Color of the background grid lines.

handDrawnPoints
    **Type**: ``number``
    
    **Default**: ``100``
    
    Number of points used when creating hand-drawn line effects.

legendBorder
    **Type**: ``boolean``
    
    **Default**: ``false``
    
    Whether to show a border around the legend.

valueFormat
    **Type**: ``(value: number) => string``
    
    **Default**: ``d3.format('.1f')``
    
    Function to format values in tooltips and labels.

showArea
    **Type**: ``boolean``
    
    **Default**: ``false``
    
    Whether to fill the area under the line(s).

Methods
-------

destroy()
~~~~~~~~~

.. code-block:: typescript

   destroy(): void

Removes the chart from the DOM and cleans up event listeners.

**Example**:

.. code-block:: typescript

   const chart = new LineChart('#container', data);
   // ... later
   chart.destroy();

Examples
--------

Basic Line Chart
~~~~~~~~~~~~~~~~

.. code-block:: typescript

   import { LineChart } from 'handwritten-graph';

   const data = {
     labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
     datasets: [{
       label: 'Sales',
       data: [65, 59, 80, 81, 56],
       lineColor: '#ff6b6b'
     }]
   };

   const chart = new LineChart('#chart', data);

Multi-Series Line Chart
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const multiSeriesData = {
     labels: ['Q1', 'Q2', 'Q3', 'Q4'],
     datasets: [
       {
         label: 'Revenue',
         data: [100, 150, 200, 250],
         lineColor: '#4ecdc4'
       },
       {
         label: 'Profit',
         data: [20, 35, 55, 70],
         lineColor: '#45b7d1'
       }
     ]
   };

   const chart = new LineChart('#multi-chart', multiSeriesData);

Area Chart
~~~~~~~~~~

.. code-block:: typescript

   const chart = new LineChart('#area-chart', data, {
     showArea: true,
     useScribbleFill: true,
     fillStyle: 'directional'
   });

Styled Line Chart
~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const styledChart = new LineChart('#styled-chart', data, {
     width: 800,
     height: 400,
     lineColor: '#ff6b6b',
     pointRadius: 6,
     handDrawnEffect: true,
     useScribbleFill: true,
     legendBorder: true,
     valueFormat: (d) => `$${d}K`
   });

Events and Interactions
-----------------------

The LineChart automatically handles:

- **Hover effects**: Points expand and tooltips appear on hover
- **Hover line**: Vertical line follows mouse movement
- **Touch support**: Works on mobile devices

Accessibility
-------------

The LineChart includes:

- Semantic SVG structure
- Text alternatives for screen readers
- Keyboard navigation support
- High contrast mode compatibility

Performance Considerations
--------------------------

- Large datasets (>1000 points) may impact performance
- Consider data sampling for very large datasets
- Hand-drawn effects add computational overhead
- Disable ``handDrawnEffect`` for better performance if needed

See Also
--------

- :doc:`configuration` - Base configuration options
- :doc:`bar-chart-api` - Bar Chart API reference
- :doc:`pie-chart-api` - Pie Chart API reference