import axios from 'axios';
import React from 'react';
import { useState, useEffect } from 'react';
import { ProjectItem } from './ProjectItem/ProjectItem';
import { ProjectDescription } from './ProjectDescription/ProjectDescription';

export const Projects = () => {

    const [state, setState] = useState({})
    const [currentProject, setCurrentProject] = useState({})

    useEffect(() => {
        const interval = setInterval(()=>{
            axios.get("/api/me/1/projects").then(response => {
                if (currentProject.id) {
                    const project = response.data.find(x => x.id === currentProject.id)
                    setCurrentProject(project)
                }
                setState({ 'projects': response.data })
            }
            )
        }, 1000)
        return () => clearInterval(interval)
    }, [currentProject])

    return <div className="content">
        <div className="project-item-list">
            <h3>List</h3>
            {(typeof state.projects === 'undefined') ? (
                <p>Loading...</p>
            ) : (
                state.projects.map((project) => (
                    <ProjectItem key={project.id} project={project} updateCurrentProject={(project) => setCurrentProject(project)} />
                ))
            )}
        </div>
        <div className="item-description">
            <h3>Description</h3>
            {(typeof currentProject.id === 'undefined') ? (
                <p>Click on a project...</p>
            ) : (
                <ProjectDescription project={currentProject} />
            )}
        </div>
    </div>
}
