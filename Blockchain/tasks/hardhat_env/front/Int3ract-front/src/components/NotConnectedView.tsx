import { Button, Container, Link, Text } from "@nextui-org/react";
import React from "react";

interface NotConnectedViewProps {
  connect: () => void;
}

export const NotConnectedView: React.FC<NotConnectedViewProps> = ({
  connect,
}) => {
  return (
    <Container
      css={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        height: "100%",
      }}
    >
      <Text h1> To start your journey connect your wallet ! 💳 🦊</Text>
      <Button onClick={connect}>Connect</Button>
      <Text h4>
        If you feel lost, check this{" "}
        <Link href="https://metamask.io/">Metamask</Link>
      </Text>
    </Container>
  );
};

export default NotConnectedView;
