import ListGroup from "./components/ListGroup.tsx";
import Alert from "./components/Alert.tsx";
import Button from "./components/Button.tsx";
import { useState } from "react";
import Menu from "./components/Menu.tsx";

function App() {
  let items = ["New York", "San Francisco", "Tokyo", "London", "Paris"];
  let items2 = ["NY", "CA", "MA", "FL", "DE"];
  let logo = "Blah";
  let menu_items = ["Home", "About", "Contact", "Login"];

  const [alertVisible, setAlertVisibility] = useState(false);

  const handleSelectionItem = (item: string) => {
    console.log(item);
  };

  return (
    <div>
      {" "}
      <Menu logo={logo} menuItems={menu_items} />
      <ListGroup
        items={items}
        heading={"Cities"}
        onSelectItem={handleSelectionItem}
      />{" "}
      <ListGroup
        items={items2}
        heading={"States"}
        onSelectItem={handleSelectionItem}
      />{" "}
      {alertVisible && (
        <Alert onClose={() => setAlertVisibility(false)}>My Alert</Alert>
      )}
      <Button color="primary" onClick={() => setAlertVisibility(true)}>
        Hello Button
      </Button>
    </div>
  );
}

export default App;
