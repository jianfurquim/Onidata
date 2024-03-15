import "../app/globals.css"
import React from 'react';
import { useRouter } from 'next/router';

const CustomLink = ({ href, children }) => {
    const router = useRouter();

    const handleClick = (e) => {
        e.preventDefault();
        router.push(href);
    };

    return (
        <a href={href} onClick={handleClick}>
            {children}
        </a>
    );
};

export default CustomLink;
