Bar Chart API Reference
========================

The ``BarChart`` class creates interactive bar charts with a hand-drawn aesthetic, supporting both vertical and horizontal orientations.

Constructor
-----------

.. code-block:: typescript

   new BarChart(selector: string, data: BarChartData, config?: Partial<BarChartConfig>)

Parameters
~~~~~~~~~~

selector
    **Type**: ``string``
    
    CSS selector for the container element where the chart will be rendered.

data
    **Type**: :ref:`BarChartData <bar-chart-data>`
    
    The data to be visualized in the bar chart.

config
    **Type**: ``Partial<BarChartConfig>`` *(optional)*
    
    Configuration options to customize the chart appearance and behavior.

Data Interface
--------------

.. _bar-chart-data:

BarChartData
~~~~~~~~~~~~

.. code-block:: typescript

   interface BarChartData {
     labels: string[];
     datasets: BarDataset[];
   }

**Properties**:

labels
    **Type**: ``string[]``
    
    Array of labels for the categories/groups.

datasets
    **Type**: :ref:`BarDataset[] <bar-dataset>`
    
    Array of datasets to be plotted as bar series.

.. _bar-dataset:

BarDataset
~~~~~~~~~~

.. code-block:: typescript

   interface BarDataset {
     label: string;
     data: number[];
     barColor?: string;
     borderColor?: string;
     borderWidth?: number;
   }

**Properties**:

label
    **Type**: ``string``
    
    Display name for the dataset (shown in legend and tooltips).

data
    **Type**: ``number[]``
    
    Array of numeric values corresponding to each label.

barColor
    **Type**: ``string`` *(optional)*
    
    Fill color for the bars. Defaults to the global ``barColor`` setting.

borderColor
    **Type**: ``string`` *(optional)*
    
    Border color for the bars. Defaults to the global ``borderColor`` setting.

borderWidth
    **Type**: ``number`` *(optional)*
    
    Border width for the bars. Defaults to the global ``borderWidth`` setting.

Configuration Interface
-----------------------

BarChartConfig
~~~~~~~~~~~~~~

.. code-block:: typescript

   interface BarChartConfig extends BaseChartConfig {
     barColor?: string;
     borderColor?: string;
     borderWidth?: number;
     gridColor?: string;
     legendBorder?: boolean;
     valueFormat?: (value: number) => string;
     barSpacing?: number;
     groupSpacing?: number;
     showValues?: boolean;
     orientation?: 'vertical' | 'horizontal';
   }

**Properties**:

barColor
    **Type**: ``string``
    
    **Default**: ``'steelblue'``
    
    Default fill color for bars.

borderColor
    **Type**: ``string``
    
    **Default**: ``'#333'``
    
    Default border color for bars.

borderWidth
    **Type**: ``number``
    
    **Default**: ``2``
    
    Default border width for bars in pixels.

gridColor
    **Type**: ``string``
    
    **Default**: ``'#e0e0e0'``
    
    Color of the background grid lines.

legendBorder
    **Type**: ``boolean``
    
    **Default**: ``false``
    
    Whether to show a border around the legend.

valueFormat
    **Type**: ``(value: number) => string``
    
    **Default**: ``d3.format('.1f')``
    
    Function to format values in tooltips and labels.

barSpacing
    **Type**: ``number``
    
    **Default**: ``0.1``
    
    Spacing between bars as a fraction of bar width (0-1).

groupSpacing
    **Type**: ``number``
    
    **Default**: ``0.2``
    
    Spacing between groups of bars as a fraction of group width (0-1).

showValues
    **Type**: ``boolean``
    
    **Default**: ``false``
    
    Whether to display value labels on bars.

orientation
    **Type**: ``'vertical' | 'horizontal'``
    
    **Default**: ``'vertical'``
    
    Chart orientation. Vertical bars grow upward, horizontal bars grow rightward.

Methods
-------

destroy()
~~~~~~~~~

.. code-block:: typescript

   destroy(): void

Removes the chart from the DOM and cleans up event listeners.

**Example**:

.. code-block:: typescript

   const chart = new BarChart('#container', data);
   // ... later
   chart.destroy();

Examples
--------

Basic Vertical Bar Chart
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   import { BarChart } from 'handwritten-graph';

   const data = {
     labels: ['Q1', 'Q2', 'Q3', 'Q4'],
     datasets: [{
       label: 'Sales',
       data: [65, 59, 80, 81],
       barColor: '#ff6b6b'
     }]
   };

   const chart = new BarChart('#chart', data);

Horizontal Bar Chart
~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const chart = new BarChart('#horizontal-chart', data, {
     orientation: 'horizontal',
     showValues: true
   });

Multi-Series Bar Chart
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const multiSeriesData = {
     labels: ['Jan', 'Feb', 'Mar', 'Apr'],
     datasets: [
       {
         label: 'Sales',
         data: [100, 150, 200, 250],
         barColor: '#4ecdc4'
       },
       {
         label: 'Profit',
         data: [20, 35, 55, 70],
         barColor: '#45b7d1'
       }
     ]
   };

   const chart = new BarChart('#multi-chart', multiSeriesData, {
     groupSpacing: 0.3,
     barSpacing: 0.1,
     legendBorder: true
   });

Styled Bar Chart with Scribble Fill
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const styledChart = new BarChart('#styled-chart', data, {
     width: 800,
     height: 400,
     barColor: '#ff6b6b',
     handDrawnEffect: true,
     useScribbleFill: true,
     fillStyle: 'oilpaint',
     showValues: true,
     valueFormat: (d) => `$${d}K`
   });

Bar Chart with Value Labels
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const labeledChart = new BarChart('#labeled-chart', data, {
     showValues: true,
     valueFormat: (value) => `${value}%`,
     barColor: '#45b7d1',
     borderColor: '#2980b9',
     borderWidth: 3
   });

Orientation Comparison
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Vertical bars (default)
   const verticalChart = new BarChart('#vertical', data, {
     orientation: 'vertical',
     showValues: true
   });

   // Horizontal bars
   const horizontalChart = new BarChart('#horizontal', data, {
     orientation: 'horizontal',
     showValues: true
   });

Events and Interactions
-----------------------

The BarChart automatically handles:

- **Hover effects**: Bars become semi-transparent and tooltips appear on hover
- **Multi-series tooltips**: Shows all dataset values for a category
- **Touch support**: Works on mobile devices
- **Responsive behavior**: Adapts to container size changes

Accessibility
-------------

The BarChart includes:

- Semantic SVG structure with proper grouping
- Text alternatives for screen readers
- Keyboard navigation support
- High contrast mode compatibility
- Value labels for improved accessibility (when ``showValues`` is enabled)

Performance Considerations
--------------------------

- Large datasets (>100 categories) may impact performance
- Multi-series charts with many datasets can be computationally intensive
- Hand-drawn effects and scribble fills add rendering overhead
- Consider simplifying visual effects for better performance with large datasets

Best Practices
--------------

Data Preparation
~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Ensure data arrays match labels length
   const data = {
     labels: ['A', 'B', 'C'],
     datasets: [{
       label: 'Series 1',
       data: [10, 20, 30] // Same length as labels
     }]
   };

Responsive Design
~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Set percentage-based dimensions
   const responsiveChart = new BarChart('#chart', data, {
     width: Math.min(800, window.innerWidth * 0.9),
     height: 400
   });

Color Management
~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Use consistent color palettes
   const colorPalette = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4'];
   
   const coloredData = {
     labels: ['Q1', 'Q2', 'Q3', 'Q4'],
     datasets: data.datasets.map((dataset, index) => ({
       ...dataset,
       barColor: colorPalette[index % colorPalette.length]
     }))
   };

Error Handling
--------------

The BarChart handles various error conditions gracefully:

.. code-block:: typescript

   // Empty data
   const emptyChart = new BarChart('#chart', { labels: [], datasets: [] });
   // Shows "No data to display" message

   // Invalid data
   const invalidData = {
     labels: ['A', 'B'],
     datasets: [{
       label: 'Test',
       data: [10, 'invalid', null, 30] // Mixed/invalid values filtered out
     }]
   };

Common Pitfalls
---------------

**Mismatched array lengths**:

.. code-block:: typescript

   // ❌ Incorrect - arrays don't match
   const badData = {
     labels: ['A', 'B', 'C'],
     datasets: [{
       data: [10, 20] // Missing value for 'C'
     }]
   };

   // ✅ Correct - arrays match
   const goodData = {
     labels: ['A', 'B', 'C'],
     datasets: [{
       data: [10, 20, 30] // All values present
     }]
   };

**Performance with large datasets**:

.. code-block:: typescript

   // ❌ May be slow with hand-drawn effects
   const largeDataChart = new BarChart('#chart', largeDataset, {
     handDrawnEffect: true,
     useScribbleFill: true
   });

   // ✅ Better performance for large datasets
   const optimizedChart = new BarChart('#chart', largeDataset, {
     handDrawnEffect: false,
     useScribbleFill: false
   });

See Also
--------

- :doc:`configuration` - Base configuration options
- :doc:`line-chart-api` - Line Chart API reference
- :doc:`pie-chart-api` - Pie Chart API reference