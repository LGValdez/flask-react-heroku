import React from 'react';
import { TechnologiesList } from './TechnologiesList'

export const ProjectDescription = ({ project }) => {

    return <div className="project-item-description">
        <p>{project.description}</p>
        <h4>Technologies</h4>
        <TechnologiesList technologies={project.technologies} />
        <h4>Frameworks</h4>
        <TechnologiesList technologies={project.frameworks} />
    </div>
}
