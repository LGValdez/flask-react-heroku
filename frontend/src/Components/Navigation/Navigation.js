import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from 'react-router-dom';
import { Home } from '../Home/Home';
import { Projects } from '../Projects/Projects';
import { Contact } from '../Contact/Contact';

function Navigation({ props }) {

  return (
    <Router>
      <div>
        <nav className="main-nav">
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/projects">Projects</Link></li>
            <li><Link to="/contact">Contact</Link></li>
          </ul>
        </nav>
      </div>
      <Switch>
        <Route exact path="/projects" render={() => <Projects />} />
        <Route exact path="/contact" render={() => <Contact />} />
        <Route exact path="/" render={() => <Home />} />
      </Switch>
    </Router>
  );
}

export default Navigation;
