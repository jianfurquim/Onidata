import "../../app/globals.css"
import React, { useEffect } from 'react';
import CustomLink from '../../components/CustomLink.js';
import Navbar from '../../components/Navbar.js';
import List from '../../components/List.js';
import {useRouter} from "next/router";

const PaymentListPage = () => {
    const headers = [
        { label: 'Loan ID', field: 'loan', type: '' },
        { label: 'Client', field: 'client', type: '' },
        { label: 'Bank', field: 'bank', type: '' },
        { label: 'Value', field: 'value', type: 'currency' },
        { label: 'Interest Value', field: 'interest_value', type: 'currency' },
        { label: 'Total Value', field: 'total_value', type: 'currency' },
        { label: 'Created', field: 'date', type: 'date' },
        { label: 'Due Date', field: 'due_date', type: 'date' },
        { label: 'Paid', field: 'effective_date', type: 'date' },
    ];

    const buttons = [
        { label: 'Make Payment', type: 'make_payment' },
    ]

    const router = useRouter();

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            router.push('/login');
        }
    }, []);

    const handleLogout = () => {
       localStorage.removeItem('token');
       router.push('/login');
    };

    return (
        <div>
            <Navbar onLogout={handleLogout} />
            <main className="content">
                <div>
                    <div>
                        <List apiUrl={'http://localhost:8000/api/payment/'} headers={headers} buttons={buttons} />
                    </div>
                </div>
            </main>
        </div>
    );
};

export default PaymentListPage;
