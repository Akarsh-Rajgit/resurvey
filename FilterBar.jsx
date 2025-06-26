import React from 'react';

const FilterBar = ({ filters, onChange }) => {
  return (
    <div style={{ marginBottom: '20px', display: 'flex', gap: '10px' }}>
      <input name="location" placeholder="Search Location" value={filters.location} onChange={onChange} />
    </div>
  );
};

export default FilterBar;
