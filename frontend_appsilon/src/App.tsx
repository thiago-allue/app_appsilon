import React, {useEffect, useState} from 'react';
import './App.scss';

// Define the API URL
const API_URL = 'http://localhost:5000';

// Interface for the movie data
interface Movie {
  id: number;
  movie_id: string;
  title: string;
  release_date: string;
}

// Interface for the IMDB data
interface IMDB {
  id: number;
  movie_id: string;
  imdb_id: string;
}

function App(): JSX.Element {
  // State variables
  const [loading, setLoading] = useState<boolean>(false);
  const [status, setStatus] = useState<string>('');
  const [movies, setMovies] = useState<Movie[]>([]);
  const [imdb, setIMDB] = useState<IMDB[]>([]);

  useEffect(() => {
  }, []);

  // Fetch movies and IMDB data
  const fetchTables = (): void => {
    setLoading(true);
    setStatus('Processing...');
    setMovies([]);
    setIMDB([]);

    Promise.all([
      fetch(`${API_URL}/load_movies`).then((response) => response.json()),
      fetch(`${API_URL}/load_imdbs`).then((response) => response.json())
    ])
      .then(([moviesData, imdbData]) => {
        setMovies(moviesData);
        setIMDB(imdbData);
        setStatus('');
        setLoading(false);
      })
      .catch((error) => {
        setStatus('Error fetching tables.');
        setLoading(false);
        console.error(error);
      });
  };

  // Handle retrieving data from Wikidata
  const handleRetrieveData = (): void => {
    setLoading(true);
    setStatus('Processing: ~3 minutes');

    fetch(`${API_URL}/retrieve`)
      .then(() => {
        setStatus('Data exported to data.json.');
        setLoading(false);
      })
      .catch((error) => {
        setStatus('Error retrieving data from Wikidata.');
        setLoading(false);
        console.error(error);
      });
  };

  // Handle ingesting data into PostgreSQL
  const handleIngestData = (): void => {
    setLoading(true);
    setStatus('Processing: ~10 seconds');

    fetch(`${API_URL}/ingest`)
      .then(() => {
        setStatus('Data ingested into PostgreSQL.');
        setLoading(false);
      })
      .catch((error) => {
        setStatus('Error ingesting data into PostgreSQL.');
        setLoading(false);
        console.error(error);
      });
  };

  // Handle deleting data from PostgreSQL
  const handleDeleteData = (): void => {
    setLoading(true);
    setStatus('Processing: ~30 seconds');

    fetch(`${API_URL}/delete`)
      .then(() => {
        setStatus('All data deleted from PostgreSQL.');
        setMovies([]);
        setIMDB([]);
        setLoading(false);
      })
      .catch((error) => {
        setStatus('Error deleting data from PostgreSQL.');
        setLoading(false);
        console.error(error);
      });
  };

  return (
    <div className="container">
      <h1 className="title">Movies</h1>

      <div className="buttons-container">
        {/* Button to retrieve data from Wikidata */}
        <button className="retrieve-button" onClick={handleRetrieveData} disabled={loading}>
          Retrieve Data from Wikidata
        </button>

        {/* Button to ingest data into PostgreSQL */}
        <button className="ingest-button" onClick={handleIngestData} disabled={loading}>
          Ingest Data into PostgreSQL
        </button>

        {/* Button to fetch tables from PostgreSQL */}
        <button className="fetch-button" onClick={fetchTables} disabled={loading}>
          Fetch Tables from PostgreSQL
        </button>

        {/* Button to delete tables from PostgreSQL */}
        <button className="delete-button" onClick={handleDeleteData} disabled={loading}>
          Delete Tables from PostgreSQL
        </button>
      </div>

      {/* Display the status */}
      <div className="status-container">{status}</div>

      <div className="data-container">
        <div className="table-container">
          <h2>Movies Table</h2>
          {movies.length > 0 ? (
            <table>
              <thead>
              <tr>
                <th style={{width: '30%'}}>Movie ID</th>
                <th>Title</th>
                <th style={{width: '30%'}}>Release Date</th>
                {/* Update width */}
              </tr>
              </thead>
              <tbody>
              {movies.slice(0, 50).map((movie) => (
                <tr key={movie.id}>
                  <td>{movie.movie_id}</td>
                  <td>{movie.title}</td>
                  <td>{movie.release_date}</td>
                </tr>
              ))}
              </tbody>
            </table>
          ) : (
            <div>
              <p className="warning-empty-tables">No movies data. </p>
              <p className="warning-empty-tables">Please fetch tables.</p>
            </div>
          )}
        </div>
        <div className="table-container">
          <h2>IMDB Table</h2>
          {imdb.length > 0 ? (
            <table>
              <thead>
              <tr>
                <th>Movie ID</th>
                <th>IMDB ID</th>
              </tr>
              </thead>
              <tbody>
              {imdb.slice(0, 50).map((item) => (
                <tr key={item.id}>
                  <td>{item.movie_id}</td>
                  <td>{item.imdb_id}</td>
                </tr>
              ))}
              </tbody>
            </table>
          ) : (
            <div>
              <p className="warning-empty-tables">No IMDB data. </p>
              <p className="warning-empty-tables">Please fetch tables.</p>
            </div>
          )}
        </div>
      </div>

      <p className="first_itens">*50 first items</p>
    </div>
  );
}

export default App;
