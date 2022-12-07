import { Container, Text, useTheme } from "@nextui-org/react";
import React, { useEffect, useState } from "react";
import { useAccount } from "wagmi";
import Web3 from "web3";
import InteractABI from "../ABI/Int3r4ct.json";

interface ConnectedViewProps {}

export const ConnectedView: React.FC<ConnectedViewProps> = ({}) => {
  const { theme } = useTheme();
  const [web3, setWeb3] = useState<any | null>(null);
  const { address } = useAccount();

  useEffect(() => {
    (async () => {
      console.log("window.ethereum", window.ethereum);
      const provider: any = window.ethereum;

      try {
        const web3 = new Web3(provider);
        setWeb3(web3);
        await (window as any).ethereum.request({
          method: `eth_requestAccounts`,
        });

        if (!web3) {
          return;
        }
        const InteractContract = new web3.eth.Contract(
          InteractABI as any,
          "0xf75A5d4375568357EfD069f690b96b47d69Ed1Cd"
        );

        (window as any).InteractContract = InteractContract;
      } catch (error) {
        console.error(error);
        console.error(`Refresh the page to approve/reject again`);
        (window as any).web3 = null;
      }
    })();
  }, []);
  return (
    <Container css={{height:'100%'}}>
      <Text h1 color="$cyan800">
        {" "}
        Have you ever interacted with a contract ?
      </Text>
      <Text
        h4
        color="$cyan500"
        css={{ display: "flex", justifyContent: "center" }}
      >
        {" "}
        Don't worry, today you will do ! {"  "}Open{" "}
        <span style={{ color: theme?.colors.purple700.toString() ,margin:"0 4px"}} >
          {" "}
          the developer's console{" "}
        </span>{" "}
        to start.{" "}
      </Text>
      <Text h5 color="$yellow800">
        {" "}
        address: {address}
      </Text>
    </Container>
  );
};

export default ConnectedView;
