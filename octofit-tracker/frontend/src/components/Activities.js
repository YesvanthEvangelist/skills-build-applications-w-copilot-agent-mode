import React, { useState, useEffect } from 'react';

function Activities({ apiBaseUrl }) {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchActivities();
  }, []);

  const fetchActivities = async () => {
    try {
      setLoading(true);
      const url = `${apiBaseUrl}/activities/`;
      console.log(`Fetching from: ${url}`);
      const response = await fetch(url);
      const data = await response.json();
      console.log('Activities data:', data);
      setActivities(Array.isArray(data) ? data : (data.results || []));
      setError(null);
    } catch (err) {
      console.error('Error fetching activities:', err);
      setError('Failed to load activities');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="loading">Loading activities...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div>
      <h2>Activities</h2>
      {activities.length === 0 ? (
        <p>No activities found</p>
      ) : (
        <div className="table-responsive">
          <table className="table table-hover">
            <thead>
              <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Calories/Min</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((activity) => (
                <tr key={activity._id || activity.id}>
                  <td><strong>{activity.name}</strong></td>
                  <td>{activity.description}</td>
                  <td><span className="badge badge-primary">{activity.calories_per_minute}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Activities;
