import { Container, Text, useSSR } from "@nextui-org/react";
import Head from 'next/head';
import { useEffect } from "react";
import { useAccount, useConnect, useNetwork } from "wagmi";
import { MetaMaskConnector } from "wagmi/connectors/metaMask";
import ConnectedView from "../components/ConnectedView";
import NotConnectedView from "../components/NotConnectedView";
import styles from '../styles/Home.module.css';


const CSRComponent = () => {
  const { chain } = useNetwork();
  const { address, isConnected, connector } = useAccount();
  const { connect } = useConnect({
    connector: new MetaMaskConnector(),
  });

  useEffect(() => {
    if (connector?.switchChain) connector?.switchChain(5);
  }, []);

  return (
    <div className={styles.container}>
      <Head>
        <title>Gr33dyR0b0t</title>
        <meta name="description" content="With <3 from @YBK_Firelights" />
        <link rel="icon" href="/favicon.ico" />
      </Head>


      <main className={styles.main}>
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
      </main>
    </div>
  )
}
export default function Home() {
  const { isBrowser } = useSSR()

  if (isBrowser) return <CSRComponent></CSRComponent>
  else return null;

}



