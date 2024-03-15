import "../app/globals.css"
import React from 'react';
import CustomLink from '../components/CustomLink';
import Navbar from '../components/Navbar';
import LoanList from '../components/LoanList';
import {useRouter} from "next/router";

const LoansListPage = () => {
    const router = useRouter();
    const handleLogout = () => {
       localStorage.removeItem('token');
       router.push('/login');
    };

    return (
        <div>
            <Navbar onLogout={handleLogout} />
            <main className="content">
                <div>
                    <section>
                        <CustomLink href="/loans/create" className="btn btn-primary">Novo Empréstimo</CustomLink>
                    </section>
                    <div>
                        <LoanList/>
                    </div>
                </div>
            </main>
        </div>
    );
};

export default LoansListPage;
