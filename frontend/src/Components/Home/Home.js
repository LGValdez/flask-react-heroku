
import React from 'react';
import { useState, useEffect } from 'react';

export const Home = () => {

    const [state, setState] = useState({})

    useEffect(() => {
        fetch("/api/me/1").then(response => {
            if (response.status === 200) {
                return response.json()
            }
        }).then(data => setState(data))
            .then(error => error)
    }, [])

    return <div className="content">
        {(typeof state.about === 'undefined') ? (
            <div>
                <h2>About Me</h2>
                <p>Loading...</p>
            </div>
        ) : (
            <div>
                <h2>About Me - {state.name}</h2>
                <p>{state.about}</p>
            </div>
        )}
    </div>
}
