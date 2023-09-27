import { useState } from "react";
//import { MouseEvent } from "react";

// { items: [], heading: string}
interface Props {
  items: string[];
  heading: string;
  onSelectItem: (item: string) => void;
}

function ListGroup({ items, heading, onSelectItem }: Props) {
  // Hook is function that taps into built-in  features in React
  const [selectedIndex, setSelectedIndex] = useState(-1);

  const message = items.length === 0 ? <p>No item found</p> : null;

  //Event handler
  //const handleClick = (event: MouseEvent) => console.log(event);

  return (
    //This is a fragment <> so can include multiple HTML elements in one component
    //When braces are used {}, so content is rendered dynamically
    <>
      <h1> {heading} </h1>

      {message}

      {items.length === 0 && <p>No item found</p>}

      <ul className="list-group">
        {items.map((item, index) => (
          <li
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            key={item}
            /* onClick={handleClick} */

            onClick={() => {
              setSelectedIndex(index);
              onSelectItem(item);
            }}
          >
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
