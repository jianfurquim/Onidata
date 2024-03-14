import { useEffect } from 'react';
import { useRouter } from 'next/router';

const isAuthenticated = () => {
  const token = localStorage.getItem('token');
  return !!token;
};

const IndexPage = () => {
  const router = useRouter();

  useEffect(() => {
    async function redirect() {
      const authenticated = await isAuthenticated();
      if (authenticated) {
        router.push('/dashboard');
      } else {
        router.push('/login');
      }
    }

    redirect();
  }, [router]);

  return null;
};

export default IndexPage;
