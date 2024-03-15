import "../app/globals.css"
import React from 'react';
import CustomLink from './CustomLink';

const Navbar = () => {
    return (
        <nav className="bg-gray-200 p-4 flex justify-between items-center">
            <div className="flex items-start">
                <div className="mr-4">
                    <CustomLink href="/loan/list" className="text-white hover:text-gray-300">Loans</CustomLink>
                </div>
                <div>
                    <CustomLink href="/payments" className="text-white hover:text-gray-300">Payments</CustomLink>
                </div>
            </div>
            <div>
                <CustomLink href="/logout" className="text-white hover:text-gray-300">Logout</CustomLink>
            </div>
        </nav>
    );
};

export default Navbar;


