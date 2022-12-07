import { Container, Text } from "@nextui-org/react";
import { useEffect } from "react";
import { useAccount, useConnect, useNetwork, useProvider } from "wagmi";
import { MetaMaskConnector } from "wagmi/connectors/metaMask";
import "./App.css";
import ConnectedView from "./components/ConnectedView";
import NotConnectedView from "./components/NotConnectedView";

function App() {
  const { address, isConnected, connector } = useAccount();
  const { connect } = useConnect({
    connector: new MetaMaskConnector(),
  });

  const { chain } = useNetwork();

  useEffect(() => {
    if (connector?.switchChain) connector?.switchChain(5);
  }, []);

  return (
    <div className="App" style={{ height: "100vh" }}>
      {address && isConnected ? (
        chain?.id !== 5 ? (
          <Container>
            <Text h4> Address: {address}</Text>
            <Text>Please switch to the Goerli Testnet </Text>
          </Container>
        ) : (
          <ConnectedView />
        )
      ) : (
        <NotConnectedView connect={connect} />
      )}
    </div>
  );
}

export default App;
