import "../app/globals.css"
import React, { useEffect, useState } from 'react';
import { ToastContainer, toast } from 'react-toastify';
import { FaTrash, FaMoneyBillWave, FaCheck, FaTimes } from 'react-icons/fa';
import 'react-toastify/dist/ReactToastify.css';
import axios from 'axios';

const List = ({ apiUrl, headers, buttons }) => {
    const [items, setItems] = useState([]);

    const fetchItems = async () => {
        try {
          const token = localStorage.getItem('token');
          const userId = localStorage.getItem('user_id');
          axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
          const response = await axios.get(`${apiUrl}?user_id=${userId}`);
          setItems(response.data);
        } catch (error) {
            toast.error('Error when searching for items.');
        }
      };
    
    const handleDelete = async (itemId) => {
        try {
            const token = localStorage.getItem('token');
            const userId = localStorage.getItem('user_id');
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            await axios.delete(`${apiUrl}${itemId}/?user_id=${userId}`);
            setItems(prevItems => prevItems.filter(item => item.id !== itemId));
            await fetchItems();
        } catch (error) {
            toast.error('Error deleting item.');
        }
    };

    const handleGeneratePayments = async (itemId) => {
        try {
            const token = localStorage.getItem('token');
            const userId = localStorage.getItem('user_id');
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            await axios.post(`${apiUrl}${itemId}/generate_payments/?user_id=${userId}`);
            await fetchItems();
        } catch (error) {
            toast.error('Error generating item payments.');
        }
    };

    const handleCancelGeneratePayments = async (itemId) => {
        try {
            const token = localStorage.getItem('token');
            const userId = localStorage.getItem('user_id');
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            await axios.post(`${apiUrl}${itemId}/cancel_payments/?user_id=${userId}`);
            await fetchItems();
        } catch (error) {
            toast.error('Error canceling item payments.');
        }
    };

    const handleMakePayment = async (itemId) => {
        try {
            const token = localStorage.getItem('token');
            const userId = localStorage.getItem('user_id');
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            await axios.post(`${apiUrl}${itemId}/make_payment/?user_id=${userId}`);
            await fetchItems();
        } catch (error) {
            toast.error('Error when paying for item.');
        }
    };

    const handleCancelMakePayment = async (itemId) => {
        try {
            const token = localStorage.getItem('token');
            const userId = localStorage.getItem('user_id');
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            await axios.post(`${apiUrl}${itemId}/cancel_make_payment/?user_id=${userId}`);
            await fetchItems();
        } catch (error) {
            toast.error('Error when canceling item payment.');
        }
    };

    useEffect(() => {
        fetchItems();
    }, []);
    

    const formatDate = (date) => {
        const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
        return new Date(date).toLocaleDateString('pt-BR', options);
    };

    const formatValue = (value, type) => {
        if (typeof value === 'boolean') {
            return value ? <FaCheck /> : <FaTimes />;
        } else if (value == null) {
            return ' ';
        } else if (type === 'currency') {
            return `R$ ${value}`;
        } else if (type === 'percentage') {
            return `${value} %`;
        } else if (type === 'date') {
            return formatDate(value);
        } else {
            return value;
        }
    };

    return (
        <div className="overflow-hidden border-b border-gray-200 sm:rounded-lg">
            <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                    <tr>
                        {headers.map((header, index) => (
                            <th key={index} className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                {header.label}
                            </th>
                        ))}
                        {buttons.length > 0 && <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>}
                    </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                    {items.map((item, index) => (
                        <tr key={index}>
                            {headers.map((header, index) => (
                                <td key={index} className="px-6 py-4 whitespace-nowrap">
                                    <div className="text-sm text-gray-500">{formatValue(item[header.field], header.type)}</div>
                                </td>
                            ))}
                            {buttons.length > 0 && (
                                <td key={headers.length + 1} className="px-6 py-4 whitespace-nowrap">
                                    <div className="flex">
                                        {buttons.map((button, index) => (
                                            <div key={`button_${index}`}>
                                                {button.type === "delete" && (
                                                    <button onClick={() => handleDelete(item.pk)} className="text-red-600 px-4 py-2 border border-red-600 rounded-md hover:bg-red-600 hover:text-white transition-colors duration-300 mr-2">
                                                        <FaTrash className="inline-block"/>
                                                    </button>
                                                )}
                                                {button.type === "generate_payments" && !item.payment_generated && (
                                                    <button onClick={() => handleGeneratePayments(item.pk)} className="text-green-600 px-4 py-2 border border-green-600 rounded-md hover:bg-green-600 hover:text-white transition-colors duration-300">
                                                        <FaMoneyBillWave className="inline-block"/>
                                                    </button>
                                                )}
                                                {button.type === "generate_payments" && item.payment_generated && (
                                                    <button onClick={() => handleCancelGeneratePayments(item.pk)} className="text-red-600 px-4 py-2 border border-red-600 rounded-md hover:bg-red-600 hover:text-white transition-colors duration-300 mr-2">
                                                        <FaMoneyBillWave className="inline-block"/>
                                                    </button>
                                                )}
                                                {button.type === "make_payment" && !item.is_paid && (
                                                    <button onClick={() => handleMakePayment(item.pk)} className="text-green-600 px-4 py-2 border border-green-600 rounded-md hover:bg-green-600 hover:text-white transition-colors duration-300">
                                                        <FaCheck className="inline-block"/>
                                                    </button>
                                                )}
                                                {button.type === "make_payment" && item.is_paid && (
                                                    <button onClick={() => handleCancelMakePayment(item.pk)} className="text-red-600 px-4 py-2 border border-red-600 rounded-md hover:bg-red-600 hover:text-white transition-colors duration-300 mr-2">
                                                        <FaTimes className="inline-block"/>
                                                    </button>
                                                )}
                                            <ToastContainer />
                                            </div>
                                        ))}
                                    </div>
                                </td>
                            )}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default List;
