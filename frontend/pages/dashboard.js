import { useRouter } from 'next/router';
import { useEffect } from 'react';

const DashboardPage = () => {
    const router = useRouter();

    useEffect(() => {
        router.push('/loans');
    }, []);

    return null;
};

export default DashboardPage;

