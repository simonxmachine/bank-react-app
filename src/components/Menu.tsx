//Help me design the menu bar for a react app
//The menu bar should have a logo, a search bar, and a menu button
//The menu button should have a drop down menu with the following options: Home, About, Contact, and Login
//The menu should be responsive and should collapse into a hamburger menu on smaller screens
//The menu should be a reusable component that can be used in any react app
//The menu should be written in TypeScript
//How do i use link from react-router-dom in TypeScript?
//
//import { Link } from "react-router-dom";
//<Link to="/about">About</Link>

import { Link } from "react-router-dom";

interface Props {
  logo: string;
  menuItems: string[];
}

function Menu({ logo, menuItems }: Props) {
  return (
    <div className="menu">
      <div className="logo">
        <img src={logo} alt="logo" />
      </div>
      <div className="menu-items">
        {menuItems.map((item) => (
          <li>{item}</li>
        ))}
      </div>
    </div>
  );
}

export default Menu;
