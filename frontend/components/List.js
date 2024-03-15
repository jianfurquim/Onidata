import "../app/globals.css"
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const List = ({ apiUrl, headers }) => {
    const [items, setItens] = useState([]);

    useEffect(() => {
        const fetchItens = async () => {
            try {
                const token = localStorage.getItem('token');
                const userId = localStorage.getItem('user_id');
                axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
                axios.get(`${apiUrl}?user_id=${userId}`)
                .then(response => {
                    setItens(response.data);
                })
                .catch(error => {
                    console.error('Erro ao buscar empréstimos:', error);
                });
            } catch (error) {
                console.error('Erro ao buscar empréstimos:', error);
            }
        };

        fetchItens();
    }, []);

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
                                    <div className="text-sm text-gray-500">{formatValue(item[header.field], header.type)}</div>
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
