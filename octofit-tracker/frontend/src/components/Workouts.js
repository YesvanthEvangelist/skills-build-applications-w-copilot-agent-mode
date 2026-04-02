import React, { useState, useEffect } from 'react';

function Workouts({ apiBaseUrl }) {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchWorkouts();
  }, []);

  const fetchWorkouts = async () => {
    try {
      setLoading(true);
      const url = `${apiBaseUrl}/workouts/`;
      console.log(`Fetching from: ${url}`);
      const response = await fetch(url);
      const data = await response.json();
      console.log('Workouts data:', data);
      setWorkouts(Array.isArray(data) ? data : (data.results || []));
      setError(null);
    } catch (err) {
      console.error('Error fetching workouts:', err);
      setError('Failed to load workouts');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="loading">Loading workouts...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div>
      <h2>Workouts</h2>
      {workouts.length === 0 ? (
        <p>No workouts found</p>
      ) : (
        <div className="table-responsive">
          <table className="table table-hover">
            <thead>
              <tr>
                <th>User</th>
                <th>Activity</th>
                <th>Duration (min)</th>
                <th>Calories Burned</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              {workouts.map((workout) => (
                <tr key={workout._id || workout.id}>
                  <td><strong>{workout.user?.username || 'Unknown'}</strong></td>
                  <td>{workout.activity?.name || 'Unknown'}</td>
                  <td>{workout.duration_minutes}</td>
                  <td><span className="badge badge-primary">{Math.round(workout.calories_burned)}</span></td>
                  <td>{new Date(workout.date).toLocaleDateString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Workouts;
