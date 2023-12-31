const env = process.env.REACT_APP_ENV;

let envApiUrl = '';

if (env === 'production') {
  envApiUrl = `https://${process.env.REACT_APP_API_PROD}`;
} else if (env === 'staging') {
  envApiUrl = `https://${process.env.REACT_APP_API_STAG}`;
} else {
  envApiUrl = `http://${process.env.REACT_APP_API_DEV}`;
}

export const apiUrl = envApiUrl;
export const appName = process.env.REACT_APP_NAME;
