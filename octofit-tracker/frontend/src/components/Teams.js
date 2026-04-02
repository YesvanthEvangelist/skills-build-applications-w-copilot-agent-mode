import React, { useState, useEffect } from 'react';

function Teams({ apiBaseUrl }) {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchTeams();
  }, []);

  const fetchTeams = async () => {
    try {
      setLoading(true);
      const url = `${apiBaseUrl}/teams/`;
      console.log(`Fetching from: ${url}`);
      const response = await fetch(url);
      const data = await response.json();
      console.log('Teams data:', data);
      setTeams(Array.isArray(data) ? data : (data.results || []));
      setError(null);
    } catch (err) {
      console.error('Error fetching teams:', err);
      setError('Failed to load teams');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div className="loading">Loading teams...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div>
      <h2>Teams</h2>
      {teams.length === 0 ? (
        <p>No teams found</p>
      ) : (
        <div className="table-responsive">
          <table className="table table-hover">
            <thead>
              <tr>
                <th>Team Name</th>
                <th>Description</th>
                <th>Created</th>
              </tr>
            </thead>
            <tbody>
              {teams.map((team) => (
                <tr key={team._id || team.id}>
                  <td><strong>{team.name}</strong></td>
                  <td>{team.description}</td>
                  <td>{new Date(team.created_at).toLocaleDateString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Teams;
