
import React from 'react';
import { useState, useEffect } from 'react';

export const Home = () => {

    const [state, setState] = useState({})

    useEffect(() => {
        fetch("/api/me").then(response => {
            if (response.status === 200) {
                return response.json()
            }
        }).then(data => setState(data))
            .then(error => console.log(error))
    }, [])

    return <div class="main">
        <h2>About Me</h2>
        {(typeof state.info === 'undefined') ? (
            <p>Loading...</p>
        ) : (
            state.info.map((info, i) => (
                <p key={i}>{info}</p>
            ))
        )}
    </div>
}
