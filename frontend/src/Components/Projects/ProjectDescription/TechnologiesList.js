import React from 'react';

export const TechnologiesList = ({ technologies }) => {

    const getImage = (tech) => {
        if (tech === 'Python') { return <img src="/technologies/python.png" alt="" width="64" /> }
        if (tech === 'JavaScript') { return <img src="/technologies/javascript.png" alt="" width="64" /> }
        if (tech === 'PostgreSQL') { return <img src="/technologies/postgresql.png" alt="" width="64" /> }
        if (tech === 'Docker') { return <img src="/technologies/docker.png" alt="" width="64" /> }
        if (tech === 'Odoo') { return <img src="/technologies/odoo.png" alt="" width="64" /> }
        if (tech === 'jQuery') { return <img src="/technologies/jquery.png" alt="" width="64" /> }
        if (tech === 'PyCharm') { return <img src="/technologies/pycharm.png" alt="" width="64" /> }
        if (tech === 'PGAdmin') { return <img src="/technologies/pgadmin.png" alt="" width="64" /> }
        if (tech === 'Django') { return <img src="/technologies/django.png" alt="" width="64" /> }
        if (tech === 'ReactJS') { return <img src="/technologies/react.png" alt="" width="64" /> }
        if (tech === 'VSCode') { return <img src="/technologies/vscode.png" alt="" width="64" /> }
    }

    return <ul>
        {technologies.map((tech, id) => (
            <li key={id}>
                {getImage(tech)}
            </li>
        ))}
    </ul>
}
