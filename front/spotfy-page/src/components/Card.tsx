import React, { useEffect, useState } from 'react';
import { getRankings } from '../services/api';
import { IArtist } from '../types';
import style from './card.module.css';

export const Card: React.FC = () => {
  const [value, setValue] = useState<{ pop_ranking: IArtist[]; genre_ranking: string[] } | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchRankings = async () => {
      try {
        const response = await getRankings();
        setValue(response.data);
      } catch (err) {
        setError('Failed to fetch data.');
        console.error(err);
      }
    };

    fetchRankings();
  }, []);

  if (error) return <div>{error}</div>;
  if (!value) return <div>Loading...</div>;

  return (
    <div className={style.container}>
      <div className={style.cardContainer}>
        {value.pop_ranking.map((artist: IArtist) => (
          <div key={artist.name} className={style.card}>
            <img src={artist.images[0]} alt={artist.name} className={style.artistImage} />
            <div className={style.artistDetails}>
              <p className={style.artistName}>{artist.name}</p>
              <p className={style.artistFollowers}>Followers: {artist.followers}</p>
              <p className={style.artistPopularity}>Popularity: {artist.popularity}</p>
              <p className={style.artistGenre}>Genres: {artist.genres.join('  ').toUpperCase()}</p>
            </div>
          </div>
        ))}
      </div>
      <div className={style.genreCard}>
        <h2>Top 5 Genres Among Top Pop Artists</h2>
        <div className={style.genreDetails}>
          <ul className={style.genreRankingContent}>
            {value.genre_ranking.map((genre, index) => (
              <li key={index}>{genre}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};
