Configuration API Reference
============================

All chart types in the Handwritten Graph Library share a common base configuration interface, with chart-specific extensions for specialized options.

Base Configuration
------------------

BaseChartConfig
~~~~~~~~~~~~~~~

The foundation configuration interface inherited by all chart types.

.. code-block:: typescript

   interface BaseChartConfig {
     width?: number;
     height?: number;
     margin?: Partial<ChartMargin>;
     fontFamily?: string;
     handDrawnEffect?: boolean;
     handDrawnJitter?: number;
     strokeLinecap?: 'butt' | 'round' | 'square';
     strokeLinejoin?: 'miter' | 'round' | 'bevel';
     tooltipBgColor?: string;
     tooltipTextColor?: string;
     tooltipBorderColor?: string;
     tooltipBorderWidth?: number;
     tooltipBorderRadius?: number;
     tooltipOpacity?: number;
     useScribbleFill?: boolean;
     fillStyle?: 'directional' | 'oilpaint';
   }

Dimensions
~~~~~~~~~~

width
    **Type**: ``number``
    
    **Default**: ``960`` (LineChart, BarChart), ``600`` (PieChart)
    
    Total width of the chart in pixels, including margins.

height
    **Type**: ``number``
    
    **Default**: ``500`` (LineChart, BarChart), ``400`` (PieChart)
    
    Total height of the chart in pixels, including margins.

margin
    **Type**: ``Partial<ChartMargin>``
    
    **Default**: Varies by chart type
    
    Margins around the chart area. See :ref:`ChartMargin <chart-margin>` interface.

Typography
~~~~~~~~~~

fontFamily
    **Type**: ``string``
    
    **Default**: ``'xkcd'``
    
    Font family for all text elements. The library includes 'xkcd' (Humor Sans) font.

Hand-Drawn Effects
~~~~~~~~~~~~~~~~~~

handDrawnEffect
    **Type**: ``boolean``
    
    **Default**: ``true``
    
    Whether to apply hand-drawn styling effects to chart elements.

handDrawnJitter
    **Type**: ``number``
    
    **Default**: ``2``
    
    Amount of random variation applied to create hand-drawn appearance (in pixels).

strokeLinecap
    **Type**: ``'butt' | 'round' | 'square'``
    
    **Default**: ``'round'``
    
    Style of line endings for strokes.

strokeLinejoin
    **Type**: ``'miter' | 'round' | 'bevel'``
    
    **Default**: ``'round'``
    
    Style of line joins for strokes.

Fill Patterns
~~~~~~~~~~~~~

useScribbleFill
    **Type**: ``boolean``
    
    **Default**: ``false`` (LineChart, BarChart), ``true`` (PieChart)
    
    Whether to use artistic scribble fill patterns instead of solid colors.

fillStyle
    **Type**: ``'directional' | 'oilpaint'``
    
    **Default**: ``'directional'``
    
    Type of fill pattern when ``useScribbleFill`` is enabled:
    
    - ``'directional'``: Directional scribble lines with varied angles
    - ``'oilpaint'``: Watercolor-like organic blob patterns

Tooltips
~~~~~~~~

tooltipBgColor
    **Type**: ``string``
    
    **Default**: ``'#fff'``
    
    Background color for tooltips.

tooltipTextColor
    **Type**: ``string``
    
    **Default**: ``'#333'``
    
    Text color for tooltips.

tooltipBorderColor
    **Type**: ``string``
    
    **Default**: ``'#333'``
    
    Border color for tooltips.

tooltipBorderWidth
    **Type**: ``number``
    
    **Default**: ``2``
    
    Border width for tooltips in pixels.

tooltipBorderRadius
    **Type**: ``number``
    
    **Default**: ``5``
    
    Border radius for tooltips in pixels.

tooltipOpacity
    **Type**: ``number``
    
    **Default**: ``0.9``
    
    Opacity for tooltip background (0-1).

Supporting Interfaces
---------------------

.. _chart-margin:

ChartMargin
~~~~~~~~~~~

.. code-block:: typescript

   interface ChartMargin {
     top: number;
     right: number;
     bottom: number;
     left: number;
   }

Defines the margins around the chart plotting area.

**Default values by chart type**:

LineChart
    ``{ top: 10, right: 10, bottom: 40, left: 50 }``

BarChart
    ``{ top: 20, right: 150, bottom: 60, left: 60 }``

PieChart
    ``{ top: 20, right: 150, bottom: 20, left: 20 }``

ChartPosition
~~~~~~~~~~~~~

.. code-block:: typescript

   interface ChartPosition {
     type: 'auto' | 'upLeft' | 'upRight' | 'downLeft' | 'downRight';
     x: number;
     y: number;
   }

Used internally for tooltip positioning.

Chart-Specific Configurations
------------------------------

LineChartConfig
~~~~~~~~~~~~~~~

Extends ``BaseChartConfig`` with line-specific options:

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

**Additional properties**:

lineColor
    **Default**: ``'steelblue'``

pointRadius
    **Default**: ``4``

gridColor
    **Default**: ``'#e0e0e0'``

handDrawnPoints
    **Default**: ``100``

legendBorder
    **Default**: ``false``

showArea
    **Default**: ``false``

See :doc:`line-chart-api` for detailed documentation.

BarChartConfig
~~~~~~~~~~~~~~

Extends ``BaseChartConfig`` with bar-specific options:

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

**Additional properties**:

barColor
    **Default**: ``'steelblue'``

borderColor
    **Default**: ``'#333'``

borderWidth
    **Default**: ``2``

orientation
    **Default**: ``'vertical'``

See :doc:`bar-chart-api` for detailed documentation.

PieChartConfig
~~~~~~~~~~~~~~

Extends ``BaseChartConfig`` with pie-specific options:

.. code-block:: typescript

   interface PieChartConfig extends BaseChartConfig {
     innerRadius?: number;
     padAngle?: number;
     cornerRadius?: number;
     legendBorder?: boolean;
     valueFormat?: (value: number) => string;
   }

**Additional properties**:

innerRadius
    **Default**: ``0``

padAngle
    **Default**: ``0.02``

cornerRadius
    **Default**: ``3``

legendBorder
    **Default**: ``true``

See :doc:`pie-chart-api` for detailed documentation.

Configuration Examples
-----------------------

Minimal Configuration
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Use mostly defaults
   const chart = new LineChart('#chart', data, {
     width: 800,
     height: 400
   });

Full Customization
~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const fullyCustomChart = new BarChart('#chart', data, {
     // Dimensions
     width: 1000,
     height: 600,
     margin: { top: 30, right: 200, bottom: 80, left: 80 },
     
     // Typography
     fontFamily: 'Arial, sans-serif',
     
     // Hand-drawn effects
     handDrawnEffect: true,
     handDrawnJitter: 3,
     strokeLinecap: 'round',
     strokeLinejoin: 'round',
     
     // Fill patterns
     useScribbleFill: true,
     fillStyle: 'oilpaint',
     
     // Colors
     barColor: '#ff6b6b',
     borderColor: '#d63031',
     borderWidth: 3,
     gridColor: '#ddd',
     
     // Tooltips
     tooltipBgColor: '#2d3436',
     tooltipTextColor: '#ffffff',
     tooltipBorderColor: '#00b894',
     tooltipBorderWidth: 2,
     tooltipBorderRadius: 8,
     tooltipOpacity: 0.95,
     
     // Chart-specific
     orientation: 'horizontal',
     showValues: true,
     barSpacing: 0.15,
     groupSpacing: 0.25,
     legendBorder: true,
     valueFormat: (d) => `$${d.toLocaleString()}`
   });

Performance-Optimized Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Optimized for large datasets
   const performanceChart = new LineChart('#chart', largeDataset, {
     handDrawnEffect: false,     // Disable for better performance
     useScribbleFill: false,     // Solid colors are faster
     handDrawnPoints: 50,        // Reduce detail if needed
     pointRadius: 2              // Smaller points render faster
   });

Accessibility-Focused Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const accessibleChart = new PieChart('#chart', data, {
     // High contrast colors
     tooltipBgColor: '#000000',
     tooltipTextColor: '#ffffff',
     tooltipBorderColor: '#ffffff',
     tooltipBorderWidth: 3,
     
     // Clear typography
     fontFamily: 'Arial, sans-serif',
     
     // Disable complex visual effects
     handDrawnEffect: false,
     useScribbleFill: false,
     
     // Clear value formatting
     valueFormat: (d) => `${d} units (${((d/total)*100).toFixed(1)}%)`
   });

Configuration Validation
-------------------------

The library performs automatic validation and provides fallbacks:

.. code-block:: typescript

   // Invalid values are replaced with defaults
   const chart = new LineChart('#chart', data, {
     width: -100,        // → Falls back to default 960
     pointRadius: 'big', // → Falls back to default 4
     margin: null        // → Falls back to default margin object
   });

Environment-Specific Configurations
------------------------------------

Development vs Production
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const isDevelopment = process.env.NODE_ENV === 'development';

   const config = {
     handDrawnEffect: !isDevelopment, // Disable in dev for faster rendering
     useScribbleFill: !isDevelopment,
     width: isDevelopment ? 400 : 800, // Smaller in dev
     ...otherOptions
   };

Mobile vs Desktop
~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const isMobile = window.innerWidth < 768;

   const responsiveConfig = {
     width: isMobile ? 350 : 800,
     height: isMobile ? 250 : 400,
     margin: isMobile 
       ? { top: 10, right: 10, bottom: 30, left: 30 }
       : { top: 20, right: 150, bottom: 60, left: 60 },
     handDrawnEffect: !isMobile, // Simpler on mobile
     pointRadius: isMobile ? 3 : 4
   };

Best Practices
--------------

1. **Start with defaults**: Only override what you need to change
2. **Consider performance**: Disable complex effects for large datasets
3. **Test responsiveness**: Verify configurations work on different screen sizes
4. **Maintain consistency**: Use the same configuration patterns across charts
5. **Document custom configs**: Keep track of why specific options were chosen

See Also
--------

- :doc:`line-chart-api` - Line Chart specific configuration
- :doc:`bar-chart-api` - Bar Chart specific configuration  
- :doc:`pie-chart-api` - Pie Chart specific configuration