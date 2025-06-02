Advanced Styling
=================

Take your charts to the next level with advanced styling techniques, custom themes, and artistic effects.

Hand-Drawn Effects
------------------

The signature feature of the Handwritten Graph Library is its authentic hand-drawn aesthetic.

Basic Hand-Drawn Styling
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const chart = new LineChart('#chart', data, {
     handDrawnEffect: true,        // Enable hand-drawn look
     handDrawnJitter: 2,          // Amount of random variation (pixels)
     strokeLinecap: 'round',      // Rounded line endings
     strokeLinejoin: 'round'      // Rounded line joins
   });

Jitter Control
~~~~~~~~~~~~~~

The ``handDrawnJitter`` parameter controls how "wobbly" your lines appear:

.. code-block:: typescript

   // Subtle hand-drawn effect
   const subtleChart = new LineChart('#subtle', data, {
     handDrawnJitter: 1
   });

   // More pronounced wobble
   const wobbyChart = new LineChart('#wobbly', data, {
     handDrawnJitter: 4
   });

   // Extremely sketchy (use sparingly)
   const sketchyChart = new LineChart('#sketchy', data, {
     handDrawnJitter: 8
   });

.. note::
   Higher jitter values (>5) can make charts difficult to read. Use them only for artistic effect.

Line Quality Control
~~~~~~~~~~~~~~~~~~~~

For LineCharts, you can control the smoothness of hand-drawn lines:

.. code-block:: typescript

   const chart = new LineChart('#chart', data, {
     handDrawnPoints: 50,    // Fewer points = more angular
     handDrawnPoints: 200    // More points = smoother curves
   });

Fill Patterns and Textures
---------------------------

Create rich, artistic fill effects with scribble patterns and oil paint textures.

Directional Scribble Fills
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const chart = new BarChart('#chart', data, {
     useScribbleFill: true,
     fillStyle: 'directional'
   });

The directional fill style creates hatching patterns at various angles:

- Different datasets get different hatch directions
- Automatic color variation creates depth
- Paper-like texture overlay adds authenticity

Oil Paint Textures
~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   const chart = new PieChart('#chart', data, {
     useScribbleFill: true,
     fillStyle: 'oilpaint'
   });

Oil paint style creates watercolor-like organic textures:

- Multiple layers of color blobs
- Natural color variation within each area
- Soft, artistic appearance

Custom Color Schemes
--------------------

Professional Color Palettes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Corporate blue theme
   const corporateTheme = {
     lineColor: '#2c3e50',
     barColor: '#3498db',
     gridColor: '#ecf0f1',
     tooltipBgColor: '#34495e',
     tooltipTextColor: '#ffffff'
   };

   // Warm sunset theme
   const sunsetTheme = {
     lineColor: '#e74c3c',
     barColor: '#f39c12',
     gridColor: '#fdf2e9',
     tooltipBgColor: '#d35400',
     tooltipTextColor: '#ffffff'
   };

   // Modern minimal theme
   const minimalTheme = {
     lineColor: '#2d3436',
     barColor: '#636e72',
     gridColor: '#f8f9fa',
     tooltipBgColor: '#ffffff',
     tooltipTextColor: '#2d3436',
     handDrawnEffect: false  // Clean, precise lines
   };

Accessibility-First Colors
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // High contrast theme for accessibility
   const accessibleTheme = {
     lineColor: '#000000',
     barColor: '#0066cc',
     gridColor: '#666666',
     tooltipBgColor: '#ffffff',
     tooltipTextColor: '#000000',
     tooltipBorderColor: '#000000',
     tooltipBorderWidth: 3
   };

   // Colorblind-friendly palette
   const colorblindFriendly = [
     '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
     '#9467bd', '#8c564b', '#e377c2', '#7f7f7f'
   ];

Multi-Series Color Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Automatic color assignment
   const data = {
     labels: ['Q1', 'Q2', 'Q3', 'Q4'],
     datasets: [
       {
         label: 'Series 1',
         data: [10, 20, 30, 25],
         lineColor: '#e74c3c'  // Explicit color
       },
       {
         label: 'Series 2',
         data: [15, 25, 20, 30]
         // Color will be auto-assigned from D3's color scheme
       }
     ]
   };

Typography and Fonts
--------------------

Custom Font Integration
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Using web fonts
   const chart = new LineChart('#chart', data, {
     fontFamily: '"Roboto", sans-serif'
   });

   // Using system fonts
   const systemFontChart = new BarChart('#chart', data, {
     fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
   });

   // Maintaining the hand-drawn aesthetic
   const handwrittenChart = new PieChart('#chart', data, {
     fontFamily: '"Kalam", "Comic Sans MS", cursive'
   });

.. note::
   The library includes the "xkcd" font (Humor Sans) by default. You can override this with any web-safe or custom font.

Font Size Control
~~~~~~~~~~~~~~~~~

While the library manages font sizes automatically, you can influence them through CSS:

.. code-block:: css

   /* Custom CSS for font sizing */
   .handwritten-graph-container {
     font-size: 14px; /* Base font size */
   }

   .handwritten-graph-container .legend text {
     font-size: 16px; /* Larger legend text */
   }

   .handwritten-graph-container .axis text {
     font-size: 12px; /* Smaller axis labels */
   }

Layout and Spacing
------------------

Custom Margins
~~~~~~~~~~~~~~

.. code-block:: typescript

   // Extra space for long labels
   const wideMarginChart = new BarChart('#chart', data, {
     margin: { top: 20, right: 200, bottom: 100, left: 100 }
   });

   // Compact layout
   const compactChart = new LineChart('#chart', data, {
     margin: { top: 10, right: 10, bottom: 30, left: 40 }
   });

Dynamic Sizing
~~~~~~~~~~~~~~

.. code-block:: typescript

   // Responsive chart sizing
   function createResponsiveChart(selector, data) {
     const container = document.querySelector(selector);
     const containerWidth = container.clientWidth;
     const containerHeight = container.clientHeight;

     return new LineChart(selector, data, {
       width: Math.min(800, containerWidth * 0.95),
       height: Math.min(400, containerHeight * 0.8),
       margin: {
         top: 20,
         right: containerWidth > 600 ? 150 : 50,
         bottom: 60,
         left: 60
       }
     });
   }

Advanced Visual Effects
-----------------------

Combining Effects
~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Maximum artistic effect
   const artisticChart = new PieChart('#chart', data, {
     handDrawnEffect: true,
     handDrawnJitter: 3,
     useScribbleFill: true,
     fillStyle: 'oilpaint',
     strokeLinecap: 'round',
     strokeLinejoin: 'round',
     cornerRadius: 8,
     padAngle: 0.05
   });

Performance vs. Quality
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // High quality for presentations
   const presentationChart = new LineChart('#chart', data, {
     handDrawnEffect: true,
     handDrawnPoints: 200,    // Very smooth
     handDrawnJitter: 2,
     useScribbleFill: true
   });

   // Optimized for performance
   const performanceChart = new LineChart('#chart', data, {
     handDrawnEffect: false,   // Fastest rendering
     useScribbleFill: false,
     handDrawnPoints: 50      // If hand-drawn is needed
   });

Custom CSS Integration
----------------------

Overriding Default Styles
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: css

   /* Custom chart container styling */
   .my-custom-chart .handwritten-graph-container {
     background: linear-gradient(45deg, #f0f8ff, #e6f3ff);
     border-radius: 15px;
     padding: 20px;
     box-shadow: 0 10px 30px rgba(0,0,0,0.1);
   }

   /* Custom tooltip styling */
   .my-custom-chart .xkcd-tooltip rect {
     fill: #2c3e50 !important;
     stroke: #3498db !important;
     stroke-width: 3px !important;
   }

   .my-custom-chart .xkcd-tooltip text {
     fill: #ecf0f1 !important;
     font-weight: bold !important;
   }

Animation and Transitions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: css

   /* Smooth entrance animation */
   .handwritten-graph-container {
     opacity: 0;
     transform: translateY(20px);
     animation: chartFadeIn 0.8s ease-out forwards;
   }

   @keyframes chartFadeIn {
     to {
       opacity: 1;
       transform: translateY(0);
     }
   }

   /* Hover effects on chart elements */
   .handwritten-graph-container .bar:hover {
     transform: scale(1.05);
     transition: transform 0.2s ease;
   }

Theme System
------------

Creating Reusable Themes
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Theme definition
   interface ChartTheme {
     colors: {
       primary: string;
       secondary: string;
       accent: string;
       background: string;
       text: string;
       grid: string;
     };
     effects: {
       handDrawn: boolean;
       scribbleFill: boolean;
       fillStyle: 'directional' | 'oilpaint';
       jitter: number;
     };
     typography: {
       fontFamily: string;
     };
   }

   // Light theme
   const lightTheme: ChartTheme = {
     colors: {
       primary: '#3498db',
       secondary: '#e74c3c',
       accent: '#f39c12',
       background: '#ffffff',
       text: '#2c3e50',
       grid: '#ecf0f1'
     },
     effects: {
       handDrawn: true,
       scribbleFill: true,
       fillStyle: 'directional',
       jitter: 2
     },
     typography: {
       fontFamily: 'xkcd'
     }
   };

   // Dark theme
   const darkTheme: ChartTheme = {
     colors: {
       primary: '#74b9ff',
       secondary: '#fd79a8',
       accent: '#fdcb6e',
       background: '#2d3436',
       text: '#ddd',
       grid: '#636e72'
     },
     effects: {
       handDrawn: true,
       scribbleFill: true,
       fillStyle: 'oilpaint',
       jitter: 3
     },
     typography: {
       fontFamily: 'xkcd'
     }
   };

Theme Application Function
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   function applyTheme(chartConfig: any, theme: ChartTheme): any {
     return {
       ...chartConfig,
       lineColor: theme.colors.primary,
       barColor: theme.colors.primary,
       gridColor: theme.colors.grid,
       tooltipBgColor: theme.colors.background,
       tooltipTextColor: theme.colors.text,
       tooltipBorderColor: theme.colors.primary,
       handDrawnEffect: theme.effects.handDrawn,
       useScribbleFill: theme.effects.scribbleFill,
       fillStyle: theme.effects.fillStyle,
       handDrawnJitter: theme.effects.jitter,
       fontFamily: theme.typography.fontFamily
     };
   }

   // Usage
   const themedChart = new LineChart('#chart', data, 
     applyTheme({ width: 800, height: 400 }, darkTheme)
   );

Seasonal and Contextual Styling
-------------------------------

Holiday Themes
~~~~~~~~~~~~~~

.. code-block:: typescript

   // Christmas theme
   const christmasTheme = {
     lineColor: '#c0392b',
     barColor: '#27ae60',
     gridColor: '#f8f9fa',
     useScribbleFill: true,
     fillStyle: 'directional' as const
   };

   // Halloween theme
   const halloweenTheme = {
     lineColor: '#f39c12',
     barColor: '#d35400',
     gridColor: '#2c2c2c',
     tooltipBgColor: '#000000',
     tooltipTextColor: '#f39c12'
   };

Business Context Themes
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   // Financial/corporate theme
   const financialTheme = {
     lineColor: '#2c3e50',
     barColor: '#34495e',
     gridColor: '#bdc3c7',
     handDrawnEffect: false,  // Professional, clean lines
     useScribbleFill: false,
     fontFamily: '"Roboto", sans-serif'
   };

   // Creative/agency theme
   const creativeTheme = {
     lineColor: '#e74c3c',
     barColor: '#9b59b6',
     handDrawnJitter: 4,      // Extra artistic
     useScribbleFill: true,
     fillStyle: 'oilpaint' as const,
     fontFamily: '"Kalam", cursive'
   };

Best Practices
---------------

1. **Consistency**: Use the same theme across all charts in a dashboard
2. **Accessibility**: Always test with high contrast modes and color blindness simulators
3. **Performance**: Balance visual appeal with rendering performance
4. **Context**: Choose styling that matches your content and audience
5. **Testing**: Verify styles work across different browsers and devices

.. code-block:: typescript

   // Good: Consistent theming across charts
   const sharedConfig = {
     lineColor: '#3498db',
     handDrawnEffect: true,
     fontFamily: 'xkcd'
   };

   const lineChart = new LineChart('#line', lineData, {
     ...sharedConfig,
     showArea: true
   });

   const barChart = new BarChart('#bar', barData, {
     ...sharedConfig,
     barColor: sharedConfig.lineColor
   });

See Also
--------

- :doc:`../api/configuration` - Complete configuration reference