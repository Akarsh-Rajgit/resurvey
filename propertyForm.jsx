import React from 'react';

const PropertyForm = ({ formData, onChange, onSubmit }) => (
  <form onSubmit={onSubmit} style={{ margin: '20px 0' }}>
    <input name="location" placeholder="Location" value={formData.location} onChange={onChange} />
    <input name="size" placeholder="Size" value={formData.size} onChange={onChange} />
    <input name="total_sqft" placeholder="Total Sqft" value={formData.total_sqft} onChange={onChange} />
    <input name="bath" placeholder="Bath" value={formData.bath} onChange={onChange} />
    <input name="price_lakhs" placeholder="Price in Lakhs" value={formData.price_lakhs} onChange={onChange} />
    <input name="price_per_sqft" placeholder="Price per Sqft" value={formData.price_per_sqft} onChange={onChange} />
    <button type="submit">Add Property</button>
  </form>
);

export default PropertyForm;
