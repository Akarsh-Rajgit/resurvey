import React from 'react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  LineChart,
  Line,
  CartesianGrid,
  Legend,
  ResponsiveContainer
} from 'recharts';
import Plot from 'react-plotly.js';

const Charts = ({ priceTrendData }) => {
  return (
    <div className="flex justify-center">
      <div className="grid gap-10 p-4 w-full max-w-5xl">
        {/* Line Chart: Price Trend */}
        <div>
          <h2 className="text-xl font-semibold mb-2 text-center">Price Trend (Top 20)</h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={priceTrendData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="index" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="price_per_sqft" stroke="#8884d8" />
            </LineChart>
          </ResponsiveContainer>
          <p>
  The line chart titled <strong>"Price Trend (Top 20)"</strong> visualizes the <strong>price per square foot</strong> for the top 20 properties with the <strong>lowest rates</strong> in the dataset. Each point on the X-axis represents the index of a property (from 0 to 19), while the Y-axis denotes its respective <code>price_per_sqft</code> value. The properties are sorted in ascending order of price per square foot to help users detect <strong>market underpricing, emerging low-cost areas</strong>, or sudden changes in affordability. The data used comes directly from the <code>price_per_sqft</code> field in the backend property records fetched via the Flask API.
</p>
        </div>

        {/* Plotly: BHK Distribution */}
        <div>
          <h2 className="text-xl font-semibold mb-2 text-center">BHK Distribution</h2>
          <Plot
            data={[
              {
                x: [1, 2, 3, 4],
                y: [350, 3400, 3100, 500],
                type: 'bar',
                marker: { color: 'steelblue' },
              },
            ]}
            layout={{
              title: 'Distribution of BHK',
              xaxis: { title: 'BHK' },
              yaxis: { title: 'Number of Properties' },
              autosize: true,
            }}
            style={{ width: '100%' }}
            useResizeHandler
          />
          <p>
  The bar chart titled <strong>"BHK Distribution"</strong> displays how many properties fall under each BHK category such as 1BHK, 2BHK, 3BHK, etc. The X-axis holds the BHK values (number of rooms), while the Y-axis indicates the <strong>count of listings</strong> for each type. These counts are aggregated based on the <code>size</code> field from the dataset, where string values like "2 BHK" are normalized to numerical values. This chart gives insight into <strong>preferred housing configurations</strong> and helps identify the balance between supply and demand for different property sizes.
</p>
        </div>

        {/* Plotly: Price Distribution */}
        <div>
          <h2 className="text-xl font-semibold mb-2 text-center">Price Distribution (in Lakh)</h2>
          <Plot
            data={[
              {
                x: [20, 40, 60, 80, 100, 120, 140, 160],
                y: [100, 400, 800, 600, 300, 200, 100, 50],
                type: 'bar',
                marker: { color: 'skyblue' },
              },
            ]}
            layout={{
              title: 'Price Distribution (in Lakh INR)',
              xaxis: { title: 'Price (Lakh)' },
              yaxis: { title: 'Frequency' },
              autosize: true,
            }}
            style={{ width: '100%' }}
            useResizeHandler
          />
          <p>
  The bar chart titled <strong>"Price Distribution (in Lakh)"</strong> segments the entire property dataset into predefined price ranges (or bins) like 0–20L, 20–40L, ..., up to 160L and beyond. The X-axis shows the midpoints of these bins (e.g., 20, 40, 60...), while the Y-axis represents how many properties fall within each price range. The price data comes from the <code>price_lakhs</code> field, which is derived from dividing the raw price by 1,00,000. This graph helps visualize the <strong>affordability spectrum</strong> of the real estate market in Bangalore and allows users to filter based on their budget.
</p>
        </div>

        {/* Plotly: Top 10 Locations */}
        <div>
          <h2 className="text-xl font-semibold mb-2 text-center">Top 10 Locations By Count</h2>
          <Plot
            data={[
              {
                x: ['Other', 'Whitefield', 'Sarjapur Road', 'Electronic City', 'Kanakapura Road', 'Thanisandra', 'Yelahanka', 'Hebbal', 'RR Nagar', 'Hennur Road'],
                y: [1300, 390, 300, 230, 210, 205, 160, 150, 135, 120],
                type: 'bar',
                marker: { color: 'mediumseagreen' },
              },
            ]}
            layout={{
              title: 'Top 10 Locations by Property Count',
              xaxis: { title: 'Location' },
              yaxis: { title: 'Number of Properties' },
              autosize: true,
            }}
            style={{ width: '100%' }}
            useResizeHandler
          />
         <p>
  The bar chart titled <strong>"Top 10 Locations By Count"</strong> illustrates the <strong>ten most frequently occurring locations</strong> in the dataset. On the X-axis are location names such as Whitefield, Sarjapur Road, etc., while the Y-axis shows how many listings exist for each location. The data is derived from the <code>location</code> field of the property dataset and aggregated using a frequency count. This chart is essential for identifying <strong>real estate hotspots, supply-heavy zones</strong>, and can assist investors or buyers in selecting regions with active markets.
</p>
        </div>
      </div>
    </div>
  );
};

export default Charts;
