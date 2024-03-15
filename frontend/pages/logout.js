import "../app/globals.css"
import { useEffect } from 'react';
import { useRouter } from 'next/router';

const LogoutPage = () => {
  const router = useRouter();

  useEffect(() => {
    localStorage.removeItem('token');
    router.push('/login');
  }, []);

  return (
    <div className="flex justify-center items-center h-screen">
        <div className="text-xl font-bold text-gray-700">Loading logout...</div>
    </div>
  );
};

export default LogoutPage;
