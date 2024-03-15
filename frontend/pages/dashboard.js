import { useRouter } from 'next/router';
import { useEffect } from 'react';

const DashboardPage = () => {
    const router = useRouter();

    useEffect(() => {
        router.push('/loan/list');
    }, []);

    return null;
};

export default DashboardPage;

