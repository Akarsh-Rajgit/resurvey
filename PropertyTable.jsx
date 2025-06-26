import React from 'react';

const PropertyTable = ({ properties, onDelete }) => {
  return (
    <table style={{ width: '100%', backgroundColor: '#2a2a2a', borderCollapse: 'collapse', color: 'white' }}>
      <thead>
        <tr>
          <th>Location</th>
          <th>Size</th>
          <th>Total Sqft</th>
          <th>Bath</th>
          <th>Price (Lakhs)</th>
          <th>Price/Sqft</th>
        </tr>
      </thead>
      <tbody>
        {properties.map((p) => (
          <tr key={p.id}>
            <td>{p.location}</td>
            <td>{p.size}</td>
            <td>{p.total_sqft}</td>
            <td>{p.bath}</td>
            <td>{p.price_lakhs}</td>
            <td>{p.price_per_sqft}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default PropertyTable;
