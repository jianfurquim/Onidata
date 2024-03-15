import "../app/globals.css"
import React from 'react';
import Navbar from '../components/Navbar';
import {useRouter} from "next/router";

const PaymentListPage = () => {
    const router = useRouter();
    const handleLogout = () => {
       localStorage.removeItem('token');
       router.push('/login');
    };

    return (
        <div>
            <Navbar onLogout={handleLogout} />
            <main className="content">
                {/* Conteúdo do dashboard será exibido aqui */}
            </main>
        </div>
    );
};

export default PaymentListPage;
