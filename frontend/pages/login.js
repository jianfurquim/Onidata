import "../app/globals.css"
import { useState } from 'react';
import { useRouter } from 'next/router';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import axios from 'axios';

const LoginPage = () => {
  const router = useRouter();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const tokenUrl = `http://localhost:8000/token/`;

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(tokenUrl, { username, password });
      if (response.data.access && response.data.access !== '') {
        const token = response.data.access;
        const user_id = response.data.user_id;

        localStorage.setItem('token', token);
        localStorage.setItem('user_id', user_id);
        router.push('/loan/list');
      } else {
        setError('Unable to obtain authentication token.');
      }
    } catch (error) {
      setError('Failed to login. Please verify your credentials.');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">Login</h2>
        </div>
        <form onSubmit={handleSubmit} className="mt-8 space-y-6">
          <div className="rounded-md shadow-sm -space-y-px">
            <div>
              <label htmlFor="username" className="sr-only">Username</label>
              <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Username" />
            </div>
            <div>
              <label htmlFor="password" className="sr-only">Password</label>
              <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password" />
            </div>
          </div>

          {error && <p className="text-red-500 text-xs italic">{error}</p>}

          <div>
            <button type="submit" className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
              Sign in
            </button>
            <ToastContainer />
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
