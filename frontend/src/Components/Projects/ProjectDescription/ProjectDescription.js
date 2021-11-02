import React from 'react';
import { TechnologiesList } from './TechnologiesList'

export const ProjectDescription = ({ project }) => {

    return <div className="project-item-description">
        <h4>{project.role}</h4>
        <div className="float-left">{project.company}</div>
        <div className="float-right">{project.date_start} - {project.date_end}</div> <br/>
        <h4>Main Responsibilities</h4>
        <dl>{project.description.split("\n").map((description, id) => {
            return <dd key={id}>{description}</dd>
        })}</dl>
        <h4>Technologies Used</h4>
        <TechnologiesList technologies={project.technologies} />
    </div>
}
