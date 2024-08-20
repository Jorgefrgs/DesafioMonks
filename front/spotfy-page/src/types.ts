export interface IArtist {
    name: string;
    followers: number;
    popularity: number;
    genres: string[];
    images: string[];
  }
  
  export interface IRankingResponse {
    pop_ranking: IArtist[];
    genre_ranking: string[];
  }
  