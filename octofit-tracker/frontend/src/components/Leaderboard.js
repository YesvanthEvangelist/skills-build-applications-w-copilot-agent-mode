import React, { useState, useEffect } from 'react';

function Leaderboard({ apiBaseUrl }) {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchLeaderboard();
  }, []);

  const fetchLeaderboard = async () => {
    try {
      setLoading(true);
      const url = `${apiBaseUrl}/leaderboard/`;
      console.log(`Fetching from: ${url}`);
      const response = await fetch(url);
      const data = await response.json();
      console.log('Leaderboard data:', data);
      const leaderboardData = Array.isArray(data) ? data : (data.results || []);
      setLeaderboard(leaderboardData.sort((a, b) => a.rank - b.rank));
      setError(null);
    } catch (err) {
      console.error('Error fetching leaderboard:', err);
      setError('Failed to load leaderboard');
    } finally {
      setLoading(false);
    }
  };

  const getRankBadgeClass = (rank) => {
    if (rank === 1) return 'ranking-badge gold';
    if (rank === 2) return 'ranking-badge silver';
    if (rank === 3) return 'ranking-badge bronze';
    return 'ranking-badge';
  };

  if (loading) return <div className="loading">Loading leaderboard...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div>
      <h2>Leaderboard</h2>
      {leaderboard.length === 0 ? (
        <p>No leaderboard data found</p>
      ) : (
        <div className="table-responsive">
          <table className="table table-hover">
            <thead>
              <tr>
                <th>Rank</th>
                <th>User</th>
                <th>Team</th>
                <th>Total Calories</th>
                <th>Workouts</th>
                <th>Total Minutes</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry) => (
                <tr key={entry._id || entry.id}>
                  <td><span className={getRankBadgeClass(entry.rank)}>{entry.rank}</span></td>
                  <td><strong>{entry.user?.username || 'Unknown'}</strong></td>
                  <td>{entry.team?.name || 'No Team'}</td>
                  <td><span className="badge badge-primary">{Math.round(entry.total_calories_burned)}</span></td>
                  <td>{entry.total_workouts}</td>
                  <td>{entry.total_minutes} min</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
