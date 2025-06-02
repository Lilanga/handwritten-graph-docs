Type Definitions Reference
===========================

This page contains all TypeScript type definitions used by the Handwritten Graph Library.

Core Interfaces
---------------

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

ChartPosition
~~~~~~~~~~~~~

.. code-block:: typescript

   interface ChartPosition {
     type: 'auto' | 'upLeft' | 'upRight' | 'downLeft' | 'downRight';
     x: number;
     y: number;
   }

Used for tooltip positioning.

TooltipItem
~~~~~~~~~~~

.. code-block:: typescript

   interface TooltipItem {
     color: string;
     text: string;
   }

Represents an item in a tooltip display.

Line Chart Types
----------------

LineDataset
~~~~~~~~~~~

.. code-block:: typescript

   interface LineDataset {
     label: string;
     data: number[];
     lineColor?: string;
     jitter?: number;
   }

LineChartData
~~~~~~~~~~~~~

.. code-block:: typescript

   interface LineChartData {
     labels: string[];
     datasets: LineDataset[];
   }

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

Bar Chart Types
---------------

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

BarChartData
~~~~~~~~~~~~

.. code-block:: typescript

   interface BarChartData {
     labels: string[];
     datasets: BarDataset[];
   }

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

Pie Chart Types
---------------

PieChartDataItem
~~~~~~~~~~~~~~~~

.. code-block:: typescript

   interface PieChartDataItem {
     label: string;
     value: number;
     color?: string;
   }

PieChartData
~~~~~~~~~~~~

.. code-block:: typescript

   type PieChartData = PieChartDataItem[];

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

Base Configuration
------------------

BaseChartConfig
~~~~~~~~~~~~~~~

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

Factory Function Types
----------------------

LineChartFactory
~~~~~~~~~~~~~~~~

.. code-block:: typescript

   type LineChartFactory = (
     selector: string,
     data: LineChartData,
     config?: Partial<LineChartConfig>
   ) => () => void;

BarChartFactory
~~~~~~~~~~~~~~~

.. code-block:: typescript

   type BarChartFactory = (
     selector: string,
     data: BarChartData,
     config?: Partial<BarChartConfig>
   ) => () => void;

PieChartFactory
~~~~~~~~~~~~~~~

.. code-block:: typescript

   type PieChartFactory = (
     selector: string,
     data: PieChartData,
     config?: Partial<PieChartConfig>
   ) => () => void;

Library Namespace
-----------------

HandwrittenGraphNamespace
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   interface HandwrittenGraphNamespace {
     LineChart: new (selector: string, data: LineChartData, config?: Partial<LineChartConfig>) => ILineChart;
     BarChart: new (selector: string, data: BarChartData, config?: Partial<BarChartConfig>) => IBarChart;
     PieChart: new (selector: string, data: PieChartData, config?: Partial<PieChartConfig>) => IPieChart;
     createGraph: LineChartFactory;
     createBarChart: BarChartFactory;
     createPieChart: PieChartFactory;
   }

Chart Interface Types
---------------------

ILineChart
~~~~~~~~~~

.. code-block:: typescript

   interface ILineChart {
     destroy(): void;
   }

IBarChart
~~~~~~~~~

.. code-block:: typescript

   interface IBarChart {
     destroy(): void;
   }

IPieChart
~~~~~~~~~

.. code-block:: typescript

   interface IPieChart {
     destroy(): void;
   }

Usage Examples
--------------

Basic Type Usage
~~~~~~~~~~~~~~~~

.. code-block:: typescript

   import { LineChart, LineChartData, LineChartConfig } from 'handwritten-graph';

   const data: LineChartData = {
     labels: ['A', 'B', 'C'],
     datasets: [{
       label: 'Series 1',
       data: [1, 2, 3],
       lineColor: '#ff0000'
     }]
   };

   const config: Partial<LineChartConfig> = {
     width: 800,
     height: 400,
     handDrawnEffect: true
   };

   const chart = new LineChart('#container', data, config);

Advanced Type Usage
~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   import { BarChartData, BarDataset } from 'handwritten-graph';

   const createDataset = (label: string, data: number[]): BarDataset => ({
     label,
     data,
     barColor: '#3498db'
   });

   const chartData: BarChartData = {
     labels: ['Q1', 'Q2', 'Q3', 'Q4'],
     datasets: [
       createDataset('Sales', [100, 150, 200, 180]),
       createDataset('Profit', [20, 35, 50, 45])
     ]
   };

See Also
--------

- :doc:`line-chart-api` - Line Chart API reference
- :doc:`bar-chart-api` - Bar Chart API reference
- :doc:`pie-chart-api` - Pie Chart API reference
- :doc:`configuration` - Configuration options