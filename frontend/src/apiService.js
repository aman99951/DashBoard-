import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/';

const fetchDataPoints = async () => {
  try {
    const response = await axios.get(`${BASE_URL}datapoints/`);
    return response.data;
  } catch (error) {
    console.error('Error fetching data points:', error);
    throw error;
  }
};

export { fetchDataPoints };
