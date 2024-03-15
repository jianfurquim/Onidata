import "../../app/globals.css"
import React, { useEffect } from 'react';
import CustomLink from '../../components/CustomLink.js';
import Navbar from '../../components/Navbar.js';
import List from '../../components/List.js';
import {useRouter} from "next/router";

const LoansListPage = () => {
    const headers = [
        { label: 'ID', field: 'pk', type: '' },
        { label: 'Client', field: 'client', type: '' },
        { label: 'Bank', field: 'bank', type: '' },
        { label: 'Value', field: 'value', type: 'currency' },
        { label: 'Installments', field: 'amount_of_payments', type: '' },
        { label: 'Interest Rate', field: 'interest_rate', type: 'percentage' },
        { label: 'Date', field: 'request_date', type: 'date' },
        { label: 'Delete', field: 'delete', type: 'button' },
    ];


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
                    <div className="flex justify-end mb-4 mr-4 mt-4 md-4">
                        <div>
                            <CustomLink href="/loan/create">
                                Add Loan
                            </CustomLink>
                        </div>
                    </div>
                    <div>
                        <List apiUrl={'http://localhost:8000/api/loan/'} headers={headers}/>
                    </div>
                </div>
            </main>
        </div>
    );
};

export default LoansListPage;
