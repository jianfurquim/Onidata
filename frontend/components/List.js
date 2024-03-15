import "../app/globals.css"
import React, { useEffect, useState } from 'react';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import axios from 'axios';

const List = ({ apiUrl, headers }) => {
    const [items, setItems] = useState([]);

    const fetchItems = async () => {
        try {
          const token = localStorage.getItem('token');
          const userId = localStorage.getItem('user_id');
          axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
          const response = await axios.get(`${apiUrl}?user_id=${userId}`);
          setItems(response.data);
        } catch (error) {
            toast.error('Erro ao buscar itens.');
        }
      };
    
    const handleDelete = async (itemId) => {
        try {
            const token = localStorage.getItem('token');
            const userId = localStorage.getItem('user_id');
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
            await axios.delete(`${apiUrl}${itemId}/?user_id=${userId}`);
            setItems(prevItems => prevItems.filter(item => item.id !== itemId));
        } catch (error) {
            toast.error('Erro ao excluir item.');
        }
    };

    useEffect(() => {
        fetchItems();
    }, []);

    useEffect(() => {
        if (items.length === 0) return;
        fetchItems();
    }, [items]);
    

    const formatDate = (date) => {
        const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
        return new Date(date).toLocaleDateString('pt-BR', options);
    };

    const formatValue = (value, type) => {
        if (type === 'currency') {
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
                    </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                    {items.map((item, index) => (
                        <tr key={index}>
                            {headers.map((header, index) => (
                                <td key={index} className="px-6 py-4 whitespace-nowrap">
                                {header.field !== 'delete' ? (
                                        <div className="text-sm text-gray-500">{formatValue(item[header.field], header.type)}</div>
                                    ) : (
                                        <div>
                                            <button onClick={() => handleDelete(item.pk)} className="text-red-600 px-4 py-2 border border-red-600 rounded-md hover:bg-red-600 hover:text-white transition-colors duration-300">
                                                Delete
                                            </button>
                                            <ToastContainer />
                                        </div>
                                    )}
                                </td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default List;
