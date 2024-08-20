import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5051', 
});

export const getRankings = () => api.post('/rankings');
export const submitData = (data: any) => api.post('/submit', data);
