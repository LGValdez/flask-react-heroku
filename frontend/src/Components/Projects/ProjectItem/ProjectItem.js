import React from 'react';
import { useState, useEffect } from 'react';

export const ProjectItem = ({ project, updateCurrentProject }) => {

    const [state, setState] = useState({})

    useEffect(() => {
        setState({ 'project': project })
    }, [project])

    return <div className="project-item">
        <div onClick={() => updateCurrentProject(project)}>
            {(typeof state.project === 'undefined') ? (
                <p>Loading project data...</p>
            ) : (state.project.name)}
        </div>
    </div>
}
