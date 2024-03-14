import "../app/globals.css"
import { useEffect } from 'react';
import { useRouter } from 'next/router';

const LogoutPage = () => {
  const router = useRouter();

  useEffect(() => {
    localStorage.removeItem('token');
    router.push('/login');
  }, []);

  return <div>Loading logout...</div>;
};

export default LogoutPage;
