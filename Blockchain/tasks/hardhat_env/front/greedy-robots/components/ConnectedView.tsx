import {
  Button,
  Container,
  Image,
  Spacer,
  Text,
  useTheme,
} from "@nextui-org/react";
import { useState } from "react";
import { useAccount } from "wagmi";

export const ConnectedView = ({}) => {
  const { address } = useAccount();
  const [flagValue, setFlag] = useState("");

  const onClick = async () => {
    try {
      const resp = await fetch("/api/flag", {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ address }),
      });

      const responseBody = await resp.json();
      if (responseBody.canPass !== null) setFlag(responseBody.flag);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Container
      css={{ display: "flex", flexDirection: "column", alignItems: "center" }}
    >
      <Image
        src="https://sm.ign.com/t/ign_ap/news/h/humans-abu/humans-abusing-sad-robots-subject-of-new-study_559q.1200.jpg"
        css={{
          width: 400,
        }}
      />
      <Spacer />
      <Text h3 color="">
        Robot is sad because he has no money
      </Text>
      <Text h4 color="#9750DD">
        Would you send him 0.1 ethers to make him happy ?{" "}
      </Text>
      {flagValue !== "" ? (
        flagValue
      ) : (
        <Button color="gradient" onClick={onClick}>
          I did !, be happy please
        </Button>
      )}
    </Container>
  );
};

export default ConnectedView;
