Pie Chart API Reference
========================

The ``PieChart`` class creates interactive pie and donut charts with a hand-drawn aesthetic.

Constructor
-----------

.. code-block:: typescript

   new PieChart(selector: string, data: PieChartData, config?: Partial<PieChartConfig>)

Parameters
~~~~~~~~~~

selector
    **Type**: ``string``
    
    CSS selector for the container element where the chart will be rendered.

data
    **Type**: :ref:`PieChartData <pie-chart-data>`
    
    The data to be visualized in the pie chart.

config
    **Type**: ``Partial<PieChartConfig>`` *(optional)*
    
    Configuration options to customize the chart appearance and behavior.

Data Interface
--------------

.. _pie-chart-data:

PieChartData
~~~~~~~~~~~~

.. code-block:: typescript

   type PieChartData = PieChartDataItem[];

   interface PieChartDataItem {
     label: string;
     value: number;
     color?: string;
   }

**Array of PieChartDataItem objects**:

label
    **Type**: ``string``
    
    Display name for the slice (shown in legend and tooltips).

value
    **Type**: ``number``
    
    Numeric value for the slice. Must be positive.

color
    **Type**: ``string`` *(optional)*
    
    Color for the slice. If not provided, colors are auto-generated from D3's color scheme.

Configuration Interface
-----------------------

PieChartConfig
~~~~~~~~~~~~~~

.. code-block:: typescript

   interface PieChartConfig extends BaseChartConfig {
     innerRadius?: number;
     padAngle?: number;
     cornerRadius?: number;
     legendBorder?: boolean;
     valueFormat?: (value: number) => string;
   }

**Properties**:

innerRadius
    **Type**: ``number``
    
    **Default**: ``0``
    
    Inner radius for donut charts. Set to 0 for a full pie chart, or a positive value for a donut.

padAngle
    **Type**: ``number``
    
    **Default**: ``0.02``
    
    Angle padding between slices in radians.

cornerRadius
    **Type**: ``number``
    
    **Default**: ``3``
    
    Corner radius for slice edges in pixels.

legendBorder
    **Type**: ``boolean``
    
    **Default**: ``true``
    
    Whether to show a border around the legend.

valueFormat
    **Type**: ``(value: number) => string``
    
    **Default**: ``d3.format('.1f')``
    
    Function to format values in tooltips and legend.

Methods
-------

destroy()
~~~~~~~~~

.. code-block:: typescript

   destroy(): void

Removes the chart from the DOM and cleans up event listeners.

**Example**:

.. code-block:: typescript

   const chart = new PieChart('#container', data);
   // ... later
   chart.destroy();

Examples
--------

Basic Pie Chart
~~~~~~~~~~~~~~~

.. code-block:: typescript

   import { PieChart } from 'handwritten-graph';

   const data = [
     { label: 'Marketing', value: 30, color: '#FF6384' },
     { label: 'Development', value: 45, color: '#36A2EB' },
     { label: 'Research', value: 15, color: '#FFCE56' },
     { label: 'Administration', value: 10, color: '#4BC0C0' }
   ];

   const chart = new PieChart('#chart', data);

Donut Chart
~~~~~~~~~~~

.. code-block:: typescript

   const donutChart = new PieChart('#donut-chart', data, {
     innerRadius: 60,
     cornerRadius: 5
   });

Auto-Generated Colors
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Colors will be automatically assigned from D3's color scheme
   const autoColorData = [
     { label: 'Category A', value: 25 },
     { label: 'Category B', value: 35 },
     { label: 'Category C', value: 20 },
     { label: 'Category D', value: 20 }
   ];

   const chart = new PieChart('#auto-color-chart', autoColorData);

Styled Pie Chart with Scribble Fill
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const styledChart = new PieChart('#styled-chart', data, {
     width: 600,
     height: 400,
     useScribbleFill: true,
     fillStyle: 'directional',
     handDrawnEffect: true,
     legendBorder: true,
     valueFormat: (d) => `${d}%`
   });

Large Dataset with Percentage Display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const salesData = [
     { label: 'Product A', value: 1250 },
     { label: 'Product B', value: 850 },
     { label: 'Product C', value: 600 },
     { label: 'Product D', value: 400 },
     { label: 'Product E', value: 300 },
     { label: 'Others', value: 200 }
   ];

   const salesChart = new PieChart('#sales-chart', salesData, {
     valueFormat: (value) => {
       const total = salesData.reduce((sum, item) => sum + item.value, 0);
       const percentage = ((value / total) * 100).toFixed(1);
       return `${value} (${percentage}%)`;
     },
     legendBorder: true
   });

Oil Paint Texture Effect
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const artisticChart = new PieChart('#artistic-chart', data, {
     useScribbleFill: true,
     fillStyle: 'oilpaint',
     handDrawnEffect: true,
     padAngle: 0.05,
     cornerRadius: 8
   });

Events and Interactions
-----------------------

The PieChart automatically handles:

- **Hover effects**: Slices expand outward and tooltips appear on hover
- **Touch support**: Works on mobile devices
- **Legend interactions**: Fully interactive legend with color coding
- **Smooth transitions**: Animated hover states

Accessibility
-------------

The PieChart includes:

- Semantic SVG structure with proper grouping
- Text alternatives for screen readers
- Keyboard navigation support
- High contrast mode compatibility
- Percentage information in tooltips and legend

Performance Considerations
--------------------------

- Large numbers of slices (>20) may impact readability
- Hand-drawn effects add computational overhead
- Scribble fills are more resource-intensive than solid colors
- Consider grouping small slices into "Others" category for better performance and readability

Best Practices
--------------

Data Preparation
~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Ensure positive values
   const cleanData = rawData
     .filter(item => item.value > 0)
     .map(item => ({
       label: item.label,
       value: Math.abs(item.value), // Ensure positive
       color: item.color
     }));

   // Group small slices
   const groupedData = groupSmallSlices(cleanData, 0.05); // Group slices < 5%

Color Management
~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Use accessibility-friendly color palettes
   const accessibleColors = [
     '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
     '#9467bd', '#8c564b', '#e377c2', '#7f7f7f'
   ];

   const coloredData = data.map((item, index) => ({
     ...item,
     color: item.color || accessibleColors[index % accessibleColors.length]
   }));

Responsive Design
~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Adjust size based on container
   const containerWidth = document.querySelector('#chart').clientWidth;
   const size = Math.min(600, containerWidth * 0.9);

   const responsiveChart = new PieChart('#chart', data, {
     width: size,
     height: size
   });

Error Handling
--------------

The PieChart handles various error conditions gracefully:

.. code-block:: typescript

   // Empty data
   const emptyChart = new PieChart('#chart', []);
   // Shows "No data to display" message

   // Invalid values filtered out automatically
   const mixedData = [
     { label: 'Valid', value: 10 },
     { label: 'Invalid', value: -5 }, // Filtered out (negative)
     { label: 'Another Invalid', value: 0 }, // Filtered out (zero)
     { label: 'Valid 2', value: 15 }
   ];

Common Pitfalls
---------------

**Too many small slices**:

.. code-block:: typescript

   // ❌ Hard to read with many tiny slices
   const tooManySlices = Array.from({length: 20}, (_, i) => ({
     label: `Item ${i}`,
     value: Math.random() * 5
   }));

   // ✅ Group small slices together
   const groupedSlices = groupSmallSlices(tooManySlices, 0.03);

**Missing or invalid data**:

.. code-block:: typescript

   // ❌ Invalid data structure
   const badData = [
     { name: 'A', amount: 10 }, // Wrong property names
     { label: 'B' }, // Missing value
     { label: 'C', value: 'ten' } // Non-numeric value
   ];

   // ✅ Correct data structure
   const goodData = [
     { label: 'A', value: 10 },
     { label: 'B', value: 20 },
     { label: 'C', value: 30 }
   ];

Advanced Usage
--------------

Custom Legend Positioning
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // The legend automatically positions itself, but you can influence it
   const wideChart = new PieChart('#wide-chart', data, {
     width: 800,  // Wide chart pushes legend to the right
     height: 400,
     margin: { top: 20, right: 200, bottom: 20, left: 20 }
   });

Dynamic Data Updates
~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // For dynamic updates, recreate the chart
   function updateChart(newData) {
     if (window.currentChart) {
       window.currentChart.destroy();
     }
     window.currentChart = new PieChart('#dynamic-chart', newData);
   }

Integration with Other Libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Use with animation libraries
   import { PieChart } from 'handwritten-graph';
   import anime from 'animejs';

   const chart = new PieChart('#animated-chart', data);
   
   // Add custom animations to the container
   anime({
     targets: '#animated-chart .handwritten-graph-container',
     opacity: [0, 1],
     scale: [0.8, 1],
     duration: 1000,
     easing: 'easeOutElastic'
   });

See Also
--------

- :doc:`configuration` - Base configuration options
- :doc:`line-chart-api` - Line Chart API reference
- :doc:`bar-chart-api` - Bar Chart API reference