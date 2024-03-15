import "../../app/globals.css"
import { useRouter } from 'next/router';
import React, { useState } from 'react';
import axios from 'axios';

const LoanForm = () => {
    const [formData, setFormData] = useState({
        user: 1,
        client: '',
        bank: '',
        value: '',
        amount_of_payments: '',
        interest_rate: '',
    });

    const apiUrl='http://localhost:8000/api/loan/'
    const router = useRouter();

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const token = localStorage.getItem('token');
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            await axios.post(apiUrl, formData);

            router.push('/loan/list');
        } catch (error) {
            console.error('Error on Add Loan:', error);
        }
    };
    
    return (
        <form onSubmit={handleSubmit} className="max-w-lg mx-auto mt-8 p-6 bg-white shadow-md rounded-lg">
            <h2 className="text-2xl font-semibold mb-4">Add Loan</h2>
            <div className="mb-4">
                <label htmlFor="client" className="block text-sm font-medium text-gray-700">Client</label>
                <input
                    type="text"
                    id="client"
                    name="client"
                    value={formData.client}
                    onChange={handleChange}
                    className="mt-1 p-2 border rounded-md w-full focus:outline-none focus:ring focus:border-blue-300"
                />
            </div>
            <div className="mb-4">
                <label htmlFor="bank" className="block text-sm font-medium text-gray-700">Bank</label>
                <input
                    type="text"
                    id="bank"
                    name="bank"
                    value={formData.bank}
                    onChange={handleChange}
                    className="mt-1 p-2 border rounded-md w-full focus:outline-none focus:ring focus:border-blue-300"
                />
            </div>
            <div className="mb-4">
                <label htmlFor="value" className="block text-sm font-medium text-gray-700">Value</label>
                <input
                    type="number"
                    id="value"
                    name="value"
                    value={formData.value}
                    onChange={handleChange}
                    className="mt-1 p-2 border rounded-md w-full focus:outline-none focus:ring focus:border-blue-300"
                />
            </div>
            <div className="mb-4">
                <label htmlFor="amount_of_payments" className="block text-sm font-medium text-gray-700">Amount of Payments</label>
                <input
                    type="number"
                    id="amount_of_payments"
                    name="amount_of_payments"
                    value={formData.amount_of_payments}
                    onChange={handleChange}
                    className="mt-1 p-2 border rounded-md w-full focus:outline-none focus:ring focus:border-blue-300"
                />
            </div>
            <div className="mb-4">
                <label htmlFor="interest_rate" className="block text-sm font-medium text-gray-700">Interest Rate</label>
                <input
                    type="number"
                    id="interest_rate"
                    name="interest_rate"
                    value={formData.interest_rate}
                    onChange={handleChange}
                    className="mt-1 p-2 border rounded-md w-full focus:outline-none focus:ring focus:border-blue-300"
                />
            </div>
            <button type="submit" className="bg-blue-500 text-white font-semibold py-2 px-4 rounded hover:bg-blue-600">
                Add Loan
            </button>
        </form>
    );
};

export default LoanForm;



